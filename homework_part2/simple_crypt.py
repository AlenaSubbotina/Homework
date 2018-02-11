from simplecrypt import decrypt, DecryptionException

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

passwords = open("passwords.txt", "r")
for line in passwords:
    try:
        l = line.strip()
        d = decrypt(l, encrypted)
        print(d, l)
    except DecryptionException:
        print("Error")






