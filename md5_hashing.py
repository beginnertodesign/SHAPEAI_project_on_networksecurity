#This is md5-hashing algorithm
import hashlib

username1 = input()
store1 = bytes(username1,'utf-8')
username2 = input()
store2 = bytes(username2,'utf-8')

md5_ref_1 = hashlib.md5(store1)
md5_ref_2 = hashlib.md5(store2)

print(md5_ref_1.hexdigest())
print(md5_ref_2.hexdigest())





#salting to the data and doing final hashing with sha512
import hashlib, uuid

userinput = input()
password = bytes(userinput,'utf-8')
salt = uuid.uuid4().bytes
hashed_password = hashlib.sha512(password + salt).hexdigest()
print(hashed_password)
