

#存入歌詞
x = '''It's been a long day without you, my friend.
And I'll tell you all about it when I see you again.
We've come a long way from where we began.
Oh, I'll tell you all about it when I see you again.
When I see you again.
'''


#將句子轉為小寫
x = x.lower()

#處理標點符號
x_punc = x.replace(',',' , ')
x_punc = x_punc.replace('.',' . ')

#分割並存入list
x_list = x_punc.split()

x_list_copy = x_list.copy()

#處理重複的部分
s = set(x_list)

'''for i in x_list:
    if i not in x_list_2:
        x_list_2.append(i)'''


'''for i in x_list.copy():
    n = x_list.count(i)
    if n > 1:
        x_list.remove(i)'''

#存回list
x_list = list(s)

#定義字典
cn_list = ["我們","長","告訴","我","方式","它","一直","來","朋友",
                     "當","它","從",'。',"我們","再次",'，',"關於","哪裡","哦","沒有","我",
                     "開始","和","日","所有","見","你","我","一個"]
x_Dict = {}
for i in range(len(x_list)):
    x_Dict[x_list[i]] = cn_list[i]



#翻譯字串
x_punc = x_punc.split('\n')


for i in range(len(x_punc)):
    x_punc[i] = x_punc[i].split()
    for a in range(len(x_punc[i])):
        x_punc[i][a] = x_Dict[x_punc[i][a]]
        print(x_punc[i][a],end='')
    print()

    