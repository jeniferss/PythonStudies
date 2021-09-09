import zlib
from base64 import b64encode, b64decode


# Compressing
def compress(input_file, output_file):
    data = open(input_file, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = b64encode(zlib.compress(data_bytes, 9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(output_file, 'w')
    compressed_file.write(decoded_data)


compress('text.txt', 'compressed.txt')


# Decompressing
def decompress(input_file, output_file):
    file_content = open(input_file, 'r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8')
    file = open(output_file, 'w')
    file.write(decoded_data)
    file.close()


decompress('compressed.txt', 'decompressed.txt')
