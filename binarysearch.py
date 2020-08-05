def binsearch(arr,l,n,x):
    if n>=l:
        mid=l+(n-1)//2

        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binsearch(arr,l,mid-1,x)
        else:
            return binsearch(arr,mid+1,n,x)

    else:
        return -1

arr=list(map(int,input().split()))
x=int(input())
l=0
n=len(arr)-1
result=binsearch(arr,l,n,x)
print('The index where the value found',result)
