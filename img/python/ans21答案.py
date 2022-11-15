#ans21答案.py
a=int(input("输入一个正整数(1~10)："))
p=1
while a>=1:
    p=p*a
    a=a-1
print("阶乘是:"+str(p))
