class WavFileWarning(UserWarning):
    pass

WAVE_FORMAT_PCM = 0x0001
WAVE_FORMAT_IEEE_FLOAT = 0x0003
WAVE_FORMAT_EXTENSIBLE = 0xfffe
KNOWN_WAVE_FORMATS = (WAVE_FORMAT_PCM, WAVE_FORMAT_IEEE_FLOAT)

def _read_fmt_chunk(fid, is_big_endian):
    if is_big_endian:
        fmt = '>'
    else:
        fmt = '<'
    size = res = struct.unpack(fmt+'I', fid.read(4))[0]
    bytes_read = 0
    if size < 16:
        raise ValueError("Binary structure of wave file is not compliant")
    res = struct.unpack(fmt+'HHIIHH', fid.read(16))
    bytes_read += 16
    format_tag, channels, fs, bytes_per_second, block_align, bit_depth = res
    if format_tag == WAVE_FORMAT_EXTENSIBLE and size >= (16+2):
        ext_chunk_size = struct.unpack(fmt+'H', fid.read(2))[0]
        bytes_read += 2
        if ext_chunk_size >= 22:
            extensible_chunk_data = fid.read(22)
            bytes_read += 22
            raw_guid = extensible_chunk_data[2+4:2+4+16]
            if is_big_endian:
                tail = b'\x00\x00\x00\x10\x80\x00\x00\xAA\x00\x38\x9B\x71'
            else:
                tail = b'\x00\x00\x10\x00\x80\x00\x00\xAA\x00\x38\x9B\x71'
            if raw_guid.endswith(tail):
                format_tag = struct.unpack(fmt+'I', raw_guid[:4])[0]
        else:
            raise ValueError("Binary structure of wave file is not compliant")
    if format_tag not in KNOWN_WAVE_FORMATS:
        raise ValueError("Unknown wave file format")
    if size > (bytes_read):
        fid.read(size - bytes_read)
    return (size, format_tag, channels, fs, bytes_per_second, block_align,
            bit_depth)

def _read_data_chunk(fid, format_tag, channels, bit_depth, is_big_endian,mmap=False):
    if is_big_endian:
        fmt = '>I'
    else:
        fmt = '<I'
    size = struct.unpack(fmt, fid.read(4))[0]
    bytes_per_sample = bit_depth//8
    if bit_depth == 8:
        dtype = 'u1'
    else:
        if is_big_endian:
            dtype = '>'
        else:
            dtype = '<'
        if format_tag == WAVE_FORMAT_PCM:
            dtype += 'i%d' % bytes_per_sample
        else:
            dtype += 'f%d' % bytes_per_sample
    if not mmap:
        data = numpy.frombuffer(fid.read(size), dtype=dtype)
    else:
        start = fid.tell()
        data = numpy.memmap(fid, dtype=dtype, mode='c', offset=start,
                            shape=(size//bytes_per_sample,))
        fid.seek(start + size)
    if channels > 1:
        data = data.reshape(-1, channels)
    return data

def _skip_unknown_chunk(fid, is_big_endian):
    if is_big_endian:
        fmt = '>I'
    else:
        fmt = '<I'
    data = fid.read(4)
    if data:
        size = struct.unpack(fmt, data)[0]
        fid.seek(size, 1)
        
def _read_riff_chunk(fid):
    str1 = fid.read(4)
    if str1 == b'RIFF':
        is_big_endian = False
        fmt = '<I'
    elif str1 == b'RIFX':
        is_big_endian = True
        fmt = '>I'
    else:
        raise ValueError("File format {}... not "
                         "understood.".format(repr(str1)))
    file_size = struct.unpack(fmt, fid.read(4))[0] + 8
    str2 = fid.read(4)
    if str2 != b'WAVE':
        raise ValueError("Not a WAV file.")

    return file_size, is_big_endian

def read(filename, mmap=False):
    if hasattr(filename, 'read'):
        fid = filename
        mmap = False
    else:
        fid = open(filename, 'rb')
    try:
        file_size, is_big_endian = _read_riff_chunk(fid)
        fmt_chunk_received = False
        data_chunk_received = False
        channels = 1
        bit_depth = 8
        format_tag = WAVE_FORMAT_PCM
        while fid.tell() < file_size:
            chunk_id = fid.read(4)
            if not chunk_id:
                if data_chunk_received:
                    warnings.warn(
                        "Reached EOF prematurely; finished at {:d} bytes, "
                        "expected {:d} bytes from header."
                        .format(fid.tell(), file_size),
                        WavFileWarning, stacklevel=2)
                    break
                else:
                    raise ValueError("Unexpected end of file.")
            elif len(chunk_id) < 4:
                raise ValueError("Incomplete wav chunk.")
            if chunk_id == b'fmt ':
                fmt_chunk_received = True
                fmt_chunk = _read_fmt_chunk(fid, is_big_endian)
                format_tag, channels, fs = fmt_chunk[1:4]
                bit_depth = fmt_chunk[6]
                if bit_depth not in (8, 16, 32, 64, 96, 128):
                    raise ValueError("Unsupported bit depth: the wav file "
                                     "has {}-bit data.".format(bit_depth))
            elif chunk_id == b'fact':
                _skip_unknown_chunk(fid, is_big_endian)
            elif chunk_id == b'data':
                data_chunk_received = True
                if not fmt_chunk_received:
                    raise ValueError("No fmt chunk before data")
                data = _read_data_chunk(fid, format_tag, channels, bit_depth,
                                        is_big_endian, mmap)
            elif chunk_id == b'LIST':
                _skip_unknown_chunk(fid, is_big_endian)
            elif chunk_id in (b'JUNK', b'Fake'):
                _skip_unknown_chunk(fid, is_big_endian)
            else:
                warnings.warn("Chunk (non-data) not understood, skipping it.",
                              WavFileWarning, stacklevel=2)
                _skip_unknown_chunk(fid, is_big_endian)
    finally:
        if not hasattr(filename, 'read'):
            fid.close()
        else:
            fid.seek(0)
    return fs, data

def __load_modules__(**args):
    for name,module in args.items():
        globals()[name] = module
