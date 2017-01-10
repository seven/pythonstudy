class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def test2():
    """
Data:
mobile,age,company,skill,salary
189xxx,16,ant,c++,10000
181xxx,36,ant,c++,90000
189xxx,46,alipay,java,80000
...
    """
    from itertools import groupby
    result = set()
    data = (x for x in sorted(data,key=x.skill) if x.age>18)
    for k,g in groupby(data,lambda x: x.company):
        if sum(y.salary for y in g)>100000:
            for z in g:
                result.add(z.mobile)
    return result


class Solution(object):
    def maximalRectangle(self, a):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #DP: f[i][j]= f[i-1][j-1]+1 if bottom[x:i]==1 and right[y:j]==1 else 0
        
    def maximalSquare(self, a):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #DP: f[i][j]= f[i-1][j-1]+1 if bottom[x:i]==1 and right[y:j]==1 else 0
        m,f=0,[]
        for i in xrange(len(a)):
            f.append([0]*len(a[i]))
        
        for i in xrange(len(a)):
            for j in xrange(len(a[i])):
                if a[i][j] =='1':
                    f[i][j]=1
                    if i>0 and j>0 and  f[i-1][j-1]>0:
                        for p in xrange(f[i-1][j-1],0,-1):
                            right = (a[x][j]=='1' for x in xrange(i-p,i)) 
                            bottom= (a[i][y]=='1' for y in xrange(j-p,j))
                            if all(right) and all(bottom): 
                                f[i][j]= p+1
                                break
                    m=max(m,f[i][j])
                else:
                    f[i][j]=0
        return m*m

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        n1,n2=head,head
        while n2 and n2.next: #1. seperate by half
            n1 = n1.next
            n2 = n2.next.next

        p = head
        while p:
            if p.next == n1:
                p.next = None
                break
            p = p.next

        p=None
        while n1: #2. reverse right, p/n1/t
            t=n1.next
            n1.next=p
            p = n1
            n1=t

        n1,n2 = head,p
        while n1 and n2: #3. merge two halves head/p
            t = n1.next
            n1.next = n2
            n1,n2 = n2,t

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.m={}
        k=(10**n)-1
        res=0
        t=[]
        for a in xrange(k,0,-1):
            for b in xrange(k,0,-1):
                if ispalindrome(a*b) and a*b>res:
                    #return a*b%1337
                    res=a*b
                    t=[a,b]
        print(t)
        return  res

    def ispalindrome(self,n):
        if n in self.m:
            return self.m[n]

        i,s= 0,str(n)
        while i<len(s)//2:
            if s[i]!= s[len(s)-1-i]: 
                slef.m[n]=False
                return False
            i+=1
        
        slef.m[n]=True
        return True
        
def test():
    s = Solution()
    return [s.largestPalindrome(n) for n in range(1,4)]
