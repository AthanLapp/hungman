word = input('gimme me word')
print('now find me me word')
#word = word.split()
print(word)
knownword=''
for k in range(len(word)):
    knownword=knownword+'*'
word=list(word)
knownword = list(knownword)
tries = int(input('how manny errors m8'))+1
letters=''
for i in range(tries+len(word)):
    print(knownword)
    print('try no', 1+i)
    letter=input('guess a lettar')
    letters=letters+letter
    f = False
    for j in range(len(word)):
        if letter == str(word[j]):
            f = True
            knownword[j]=letter
            print('Gjob')
    if f==False:
        tries=tries-1
        print('ERRATA!!! errors allowed yet:', tries-1)
        if tries == 0 :
            print('you L0os')
            break
    if word == knownword:
        print('YOHOOO')
        print('you found me me word', word)
        break
    print('guesses:', letters)
