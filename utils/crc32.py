import os
import zlib


def crc32(filename: str, chunksize: int = 65536) -> str:
    """Compute the CRC-32 checksum of the contents of the given filename"""
    crc = 0
    with open(filename, "rb", chunksize) as ins:
        for x in range(int((os.stat(filename).st_size / chunksize)) + 1):
            crc = zlib.crc32(ins.read(chunksize), crc)
    return "%08X" % (crc & 0xFFFFFFFF)
