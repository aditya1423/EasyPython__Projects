
#random password genrator
import random
import string 


# val = random.choice('a' ,'b' ,'c' ,'d')
# print(val)
# print(string.ascii_letters) #a to z A to Z 
# print(string.digits) # 0 to 9
# print(string.punctuation)   #special chracters @ ,# ,$ ,*


passlen= 8

char= string.ascii_letters + string.digits+ string.punctuation

password=" "

for i in range(passlen):
    password= password + random.choice(char)
    

print("your password is : " , password)






 
