def Solution(n):
    
    bin = "{0:b}".format(n)
    max_gap = 0
    accum = 0
    for i in bin:
        if i=='0':
            accum+=1
        elif i =='1':
            if accum > max_gap:
                max_gap = accum
            accum = 0
    return(max_gap)

def numloop():
    for i in range(1,100):
         print(Solution(i))
         i+=i
   
print(numloop())
    
 