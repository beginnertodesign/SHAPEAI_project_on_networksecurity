#This is a sha1 hashing algorithm
import hashlib

username1 = input()
store1 = bytes(username1,'utf-8')
username2 = input()
store2 = bytes(username2,'utf-8')

md5_ref_1 = hashlib.sha1(store1)
md5_ref_2 = hashlib.sha1(store2)

print(md5_ref_1.hexdigest())
print(md5_ref_2.hexdigest())

#sha224 hashing technique
import hashlib

username1 = input()
store1 = bytes(username1,'utf-8')
username2 = input()
store2 = bytes(username2,'utf-8')

md5_ref_1 = hashlib.sha224(store1)
md5_ref_2 = hashlib.sha224(store2)

print(md5_ref_1.hexdigest())
print(md5_ref_2.hexdigest())


#blake2s hashing algorithm
import hashlib

username1 = input()
store1 = bytes(username1,'utf-8')
username2 = input()
store2 = bytes(username2,'utf-8')

md5_ref_1 = hashlib.blake2s(store1)
md5_ref_2 = hashlib.blake2s(store2)

print(md5_ref_1.hexdigest())
print(md5_ref_2.hexdigest())
