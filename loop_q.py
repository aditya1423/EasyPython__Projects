

# Give list count how many are positive number 

number=[1,2,4,-5,7]

for i in number :
    if i > 0:
        count=0
        count=count+1
print(i)


#sum of even number 
 
n=10

num=0

# for i in range(1,n+1):
#     num = i + num
# print(num)

for i in range(1,n+1):
    if i%2==0:
      num = num + 1
print("Total sum of even number ...",num)


#print multiplication table 

s=10

for i in range(1,s+1):
    if i ==5 :
      print("Continue ...")
      continue
    print(f"{s} X {i} = {s*i}")
    
    
    
#reverse the string 

a= "Aditya"
rev=""
for i in a:
   rev= i+ rev #for reverse the string 
print(rev)

#find non repeated character

a="Adiii"

for i in a :
    print(i)
    if a.count(i) == 1:
        print("char is : " , i)
        
        
#factorial

b=5
fact=1

while b>0:
    fact= fact * b
    b= b-1
    
print(fact) 
    
    
#CHECK PRIME NUM OR NOT

num=10
is_prime=True
if num>0:
    for i in range(2, num):
        is_prime=False
        if (num %i)==0 :
            break
print(is_prime)    
         
         
         
#collect only unique item

x = ['a', 'c', 'b', 'f', 'x', 'z', 'f']

seen = set()
for i in x:
    if i in seen:
       print("Duplicate:",i)
       break
    seen.add(i)
    
    
import time

wait_time=1
max_try=3
attempt=0

while attempt< max_try:
    print("Attempt" , attempt+1 ,"- wait -time",wait_time)
    time.sleep(wait_time)
    wait_time=wait_time*2
    attempt=attempt+1
    
    
    