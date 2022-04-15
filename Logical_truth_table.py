log = input().lower()
sym1 = [i for i in log if i.isalpha()]
sym=[]
for i in sym1:
    if not i in sym:
        sym.append(i)

def Count(sym):
    res=[]
    for i in range(len(sym)*len(sym)):
        s=str(bin(i))
        temp=""
        temp+=s[s.index("b")+1:]
        temp=(len(sym)-len(temp))*"0"+temp
        res.append(list(temp))
    return res
    
def calc(log,sym,Bin):
    res=[]
    for i in Bin:
        bin_d={}
        num=0
        for k in sym:
            bin_d[k]=i[num]
            num+=1 
        temp=""
        for j in log:
            if j.isalpha():
                temp+=bin_d[j]
            else:
                temp+=j
        result=eval(temp)
        res.append([bin_d,result])
    return res
    
res=calc(log,sym,Count(sym))

for j in res:
    temp=""
    for k in j[0].values():
        temp+=str(k)+" "
    temp+=str(j[1])
    print(temp)
