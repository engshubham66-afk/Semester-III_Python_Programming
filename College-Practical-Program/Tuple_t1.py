t1 = (1,2,5,7,9,2,4,6,8,10)

''' part (a) :  To break a tuple values in seperate two lines
such that half come on one line and other next line  '''

line1 = t1[0:5]
line2 = t1[5:]
print(line1)
print(line2)

"' part(b) : To print all even values of t1 as another tuple t2 '"
def even_num() : 
    t1 = (1,2,5,7,9,2,4,6,8,10)
    t2 = ()             

    for num in t1:
        if num % 2 == 0 :
            t2 += (num,)

    print("Another tuple t2: ", t2)        

even_num()    
    
''' part(c) : To concatenate a new tuple t2 with t1 '''
t1 = (1,2,5,7,9,2,4,6,8,10)
t2 = (11,13,15)     

t = t1 + t2
print(t)

# part(d) : To find minimum and maximum value from t1
t1 = (1,2,5,7,9,2,4,6,8,10)

print("Maximum value from tuple t1: ", max(t1))  
print("Minimum value from tuple t1: ", min(t1))
