import bcrypt

password = b'thisismypassword'
hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

input_password = input('Enter your password: ')
input_password = bytes(input_password, 'utf-8')

match = bcrypt.checkpw(input_password, hash_password)

print('Yay, your password is valid!') if match else print('Ops, your password is not valid!')
