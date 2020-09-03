import hashlib
hashed_word = input('Enter the hashed word: ')
pass_file = input('Enter the password file: ')
try:
    passfile = open(pass_file, "r")
except:
    print("No file found, please check again")
for word in passfile:
    enc_word = word.encode()
    passfile_hashes = hashlib.md5(enc_word.strip()).hexdigest()
    if passfile_hashes == hashed_word:
        print('Password found. Password is ' + word)
        break
    else:
        print("No password found")
        break
