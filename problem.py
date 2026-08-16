n = int(input())
words = input().split()
anagram = {}

for i in words:
    key = ''.join(sorted(i))
    
    if key not in anagram:
        anagram[key] = []
    
    anagram[key].append(i)
    
for j in anagram.values():
    print('  '. join(j))