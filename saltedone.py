#salting to the data and doing final hashing with sha512
import hashlib, uuid

userinput = input()
password = bytes(userinput,'utf-8')
salt = uuid.uuid4().bytes
hashed_password = hashlib.sha512(password + salt).hexdigest()
print(hashed_password)
