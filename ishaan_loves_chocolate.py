
def chocolates (arr, n) : 
    #Complete the function
    small=arr[0]
    for i in range(1,n):
       
        
        if arr[i]<small:
            small= arr[i]
    
    return small
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = chocolates(arr, n)
    print(ans)
    





# } Driver Code Ends
