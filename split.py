dec=11
bi=0
n=1
while dec!=0:
    rem=dec%2
    bi=n*rem+bi
    dec=dec//2
    n=n*10
print(bi)
c=0
for i in str(bi):
    if i=='1':
        c=c+1
print(c)
