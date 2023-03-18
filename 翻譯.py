
#將句字存入變數
x = input()


#定義字典
book = {'I':'我','can':'會','play':'玩','but':'但是','cannot':'不會',
        'basketball':'籃球','baseball':'棒球','foodball':'足球','volleyball':'排球',
        'tennis':'網球','tabletennis':'桌球','badminton':'羽球',
        '.':'。',',':'，'}



#處理標點符號
y = x.replace(',',' , ')
y = y.replace('.',' . ')


#處理table tennis
y = y.replace('table tennis','tabletennis')

#分割句字為list
x1 = y.split()

#翻譯句子
for i in range(len(x1)):
    x1[i] = book[x1[i]]

print(''.join(x1))


'''for i in range(len(x1)):
    if x1[i] == 'I':
        x1[i] = '我'
        print(x1[i],end='')
    elif x1[i] == 'play':
        x1[i] = '打'
        print(x1[i],end='')
    elif x1[i] == 'basketball':
        x1[i] = '籃球'
        print(x1[i],end='')
    elif x1[i] == 'baseball':
        x1[i] = '棒球'
        print(x1[i],end='')
    elif x1[i] == 'football':
        x1[i] = '足球'
        print(x1[i],end='')
    elif x1[i] == 'volleyball':
        x1[i] = '排球'
        print(x1[i],end='')
    elif x1[i] == 'can':
        x1[i] = '會'
        print(x1[i],end='')
    elif x1[i] == 'cannot':
        x1[i] = '不會'
        print(x1[i],end='')
    elif x1[i] == 'but':
        x1[i] = '但是'
        print(x1[i],end='')
    elif x1[i] == 'but':
        x1[i] = '但是'
        print(x1[i],end='')'''

    