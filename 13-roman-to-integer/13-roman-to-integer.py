class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        total=0
        dic ={"I":1,"V":5,"X":10,
              "L":50,
              "C":100,"D":500,
              "M":1000,"IV":4,
              "IX":9,"XL":40,"XC":90,
              "CD":400,"CM":900}
        while(i<len(s)):
            val = s[i:i+2]
            if(val=='IV' 
               or val== 'IX' 
               or val == 'XL' 
               or val=='XC' 
               or val=='CD' 
               or val=='CM'):
                total+=dic[val]
                i+=2
            else:
                total+=dic[s[i]]
                i+=1
        return total
        