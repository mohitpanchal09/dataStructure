
class Solution:
    def longest(self, names, n):
        # code here
        self.names=names
        l=[]
        for i in range(n):
            for j in names:
                x=len(j)
                l.append(x)
        large=l[0]
        for m in range(1,n):
            if l[m]>large:
                large=l[m]
        temp=large
        for k in self.names:
            if len(k)==temp:
                return k
           
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n=int(input())
        names = []
        for i in range(n):
            names.append(input())
        ob = Solution()
        print(ob.longest(names, n))
        
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
