import hashlib
import os
from random import randint


def create_large_file(path, size):
    with open(path, 'w') as f:
        char_count = 0
        while char_count < size:
            line = ''
            for _ in range(100):
                line += chr(randint(ord('a'), ord('z')))
            line += '\n'
            f.write(line)
            char_count += len(line)

p = 'large_file.txt'
size = 1000
create_large_file(p, size)


def get_file_sample(path, num_samples):
    lines = []
    size = os.path.getsize(path)
    offset = 0
    increment = size // num_samples
    read_size = 10
    print(f'{size=}, {offset=}, {increment=}, {read_size=}')
    with open(path, 'r') as f:
        while offset < size:
            f.seek(offset)
            lines.append(f.read(read_size))
            offset += increment

    return lines

print(get_file_sample('large_file.txt', num_samples=4))


def get_file_hash(path):
    lines = get_file_sample(path=path, num_samples=10)
    sample = ''.join(lines)
    import hashlib
    m = hashlib.sha256()
    m.update(sample.encode('utf-8'))
    return m.hexdigest()

def get_multi_hash(path):
    """
    Given a path to a file, returns multiple hashes based on chunk size.
    - Ensure that file is opened in binary mode = "rb"
    - Ensure file size is retrieved by os.path.getsize
    - Ensure if file chunk is not read, return
    """
    hashes = []
    fsize = os.path.getsize(path)
    chunk_size = 100
    with open(path, 'rb') as f:
        ptr = 0
        while ptr < fsize:
            f.seek(ptr)
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hashes.append(hashlib.sha256(chunk).hexdigest())
            ptr += chunk_size

    return hashes




h1 = get_file_hash('f1.txt')
h2 = get_file_hash('f2.txt')

print(h1 == h2)

h1 = get_multi_hash('f1.txt')
h2 = get_multi_hash('f2.txt')
print(h1)
print(h2)
print(h1 == h2)


def get_all_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(dirpath, dirnames, filenames)
        for filename in filenames:
            yield os.path.join(dirpath, filename)

file_map = {}
for e in get_all_files('/Users/nodofox/Documents/GitHub/interviews/src'):
    mh = tuple(get_multi_hash(e))
    if mh not in file_map:
        file_map[mh] = [e]
    else:
        file_map[mh].append(e)

for mh, files in file_map.items():
    if len(files) > 1:
        print(mh, files)
