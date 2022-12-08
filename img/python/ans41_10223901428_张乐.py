#John,1,2 Lucy,3,6 Nancy,3,6,9
#豆豆,5 小胖,2,7,9 八戒,0

uList=input('请在下方输入空格隔开的多人记录花销（逗号隔开的每人姓名和花销）：\n').split(' ') #每个人一个字符串组成的列表
ss=0
d={}
for i in uList:
    p=i.split","
    s=0
    for x in range(1,len(p)+1):
        s+=x
    d[p[0]]=s
    ss+=s
    print(f"人均消费：{}[}".format(\t.ss/len(uList)))
    #好难，来不及了，完全不会，没有信心学python了
