def lengthOfLongestSubstring( s):
    charset=set()
    l=0
    result=0
    for i in range(len(s)):
        while s[i] in charset:
            charset.remove(s[l])
            l+=1
        charset.add(s[i])
        result=max(result,len(charset))
    return result
s="abndjekkkmn"
print(lengthOfLongestSubstring(s))

       
