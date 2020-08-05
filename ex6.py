
def lesser_of_two_evens(a,b):
    while True:
        if(a%2==0 and b%2==0 and a>b):
             return b
    else:
        return a
    if (a%2==0 or b%2!=0)and (a%2!=0 or b%2==2):
        print(a)
    else:
        print(b)
    
        
              
       
