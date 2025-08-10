# reordered power of two
class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
    #create a arr with all digits in n and sort it
        string=str(n)
        arr=[i for i in string]
        arr.sort()

        length=len(string)
        two_powers=[]
        power=1

    #generate powers of 2
        while(1):
            two_powers.append(str(power))
            power*=2
        #break while bigger digit number encounters
            if len(str(power))>length:
                break

    #check digit arr with all powers of 2
        for i in two_powers:
            temp=[j for j in i]
            temp.sort()
            if arr==temp:
                return True
        return False
        
