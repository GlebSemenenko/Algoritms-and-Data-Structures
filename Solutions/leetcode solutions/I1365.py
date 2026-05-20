arr = [8,1,2,2,3] 
res = [] 
c = 0 
for i in arr: 
    res.append(0) 
    for item in arr: 
        if item < i: 
            res[c] +=1 
    c +=1
            
        

print(res)
