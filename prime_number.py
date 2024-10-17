#prime programming
num=11
count=0
for fa in range(1,num+1):
    if num%fa==0:
        count=count+1
if count==2:
    print('prime number')
else:
    print('not prime number')
    
