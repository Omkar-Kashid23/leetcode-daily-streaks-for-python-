class Solution:
    def sortVowels(self, s: str) -> str:
        vowels='AEIOUaeiou'
        s1=list(s)
        new_array=[]
        for i in s1:
            if i not in vowels:
                pass
            else:
                new_array.append(i)
        new_array.sort()
        pointer=0
        for i in range(len(s1)):
            if s1[i] in vowels:
                s1[i]=new_array[pointer]
                pointer+=1
        return (''.join(s1))
