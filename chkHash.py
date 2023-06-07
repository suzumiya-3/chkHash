import hashlib

while True:
    files = input('Please select file: ')

    for file in files.split(','):
        with open(file, 'rb') as f:
            data = f.read()

            md5 = hashlib.md5(data).hexdigest()
            sha1 = hashlib.sha1(data).hexdigest()
            sha256 = hashlib.sha256(data).hexdigest()
            sha512 = hashlib.sha512(data).hexdigest()

            print(f'md5: {md5}\nsha1: {ha1}\nsha256: {sha256}\nsha512: {sha512}')
