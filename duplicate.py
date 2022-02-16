list=[1,2,3,1,2,2]
dup=[]
i=0
while i<len(list):
    if list[i]not in dup:
        dup.append(list[i])
    i=i+1
print(dup)