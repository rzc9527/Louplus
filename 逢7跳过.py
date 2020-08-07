#逢7跳过
a=0
while a<100:
    a+=1
    if a%7!=0 and (a-7)%10!=0 and a//10!=7:
        print(a)
#另一种方法
    #if a%7==0 or (a-7)%10==0 or a//10==7:
    #    continue
    #else:
    #    print(a)
