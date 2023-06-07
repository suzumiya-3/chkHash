import hashlib

def read_chk(type):
    for chunk in iter(lambda: f.read(2048 * type.block_size), b''):
            type.update(chunk)
    return type

while True:
    files = input('Please select file: ')
    if files == "":
        continue

    for file in files.split(','):
        with open(file, 'rb') as f:

            # md5
            md5 = hashlib.md5()
            hash_md5 = read_chk(md5).hexdigest()
            # sha1
            sha1 = hashlib.sha1()
            hash_sha1 = read_chk(sha1).hexdigest()
            # sha265
            sha256 = hashlib.sha256()
            hash_sha256 = read_chk(sha256).hexdigest()
            # sha512
            sha512 = hashlib.sha512()
            hash_sha512 = read_chk(sha512).hexdigest()

            print(f'md5: {hash_md5}\nsha1: {hash_sha1}\nsha256: {hash_sha256}\nsha512: {hash_sha512}\n')
