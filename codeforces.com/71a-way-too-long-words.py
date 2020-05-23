i=input

for _ in [0]*int(i()):

    s = i(); l=len(s)-2;print([s,s[0]+str(l)+s[-1]][l>8])

for _ in range(i(), 0, -1):
    word = i()

    if word.length > 10:
        word = word[0] + str(word.length - 2) + word[word.length - 1]

    print(word)