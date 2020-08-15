""" Program to check if two strings are anagrams or not"""

def anagram(s1, s2):
    l, ll = [], []
    for i in range(len(s1)):
        if s1[i] != ' ':
            l.append(s1[i].lower())
    for i in range(len(s2)):
        if s2[i] != ' ':
            ll.append(s2[i].lower())
    if len(l) != len(ll):
        return 'Strings are not Anagrams'
    for j in range(len(l)):
        if l[j] in ll and ll[j] in l:
            continue
        else:
            return 'Strings are not Anagrams'
    return 'Strings are Anagrams'
            
