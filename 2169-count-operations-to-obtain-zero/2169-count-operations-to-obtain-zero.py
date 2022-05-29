class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1==0 or num2==0:
            return 0
        if num1==num2:
            return 1
        steps = 0
        if num1<num2:
            b,s=num2,num1
        else:
            b,s=num1,num2
        print(b,s)
        bflag = True
        while(bflag):
            if b-s > s :
                b,s = b-s,s
            else:
                b,s = s,b-s
                
            print(b,s)
            if (b-s==0 or s==0 or b==0):
                bflag=False
            steps = steps+1
        return steps+1
                
            
        