class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bucket = [0]*10
        bull=0
        for i in range(len(secret)):
            s=secret[i]
            g=guess[i]
            if int(s) == int(g):
                bull+=1
            else:
                bucket[int(s)]+=1
                bucket[int(g)]-=1
        sum=0
        for b in bucket:
            if b>0:
                sum+=b
        return str(bull)+"A"+str(len(secret)-bull-sum)+"B"