i = input()
vowel = 'aeiouAEIOU'
cname = ''.join(s for s in i if s not in vowel)
print(cname)