#定義詩詞
s0 = "<spring morning>"
s1 = "spring morning arrives unnoticed in my slumber, till I hear birds twittering everywhere.";
s2 = "It springs to mind a storm raged through overnight, Off it blew how many flowers I wonder?"

#將標題開頭轉為大寫
s0 = s0.title()

#讓詩詞內容格式符和大小寫規則
s1 = s1.capitalize()
s2 = s2.capitalize()

#將三個字串合併並換行
s = s0 + '\n' + s1 + '\n' + s2

#在逗號後換行
EZs = s.replace(', ',',\n')

#分割句子並存入清單
EZsList = EZs.split('\n')

lenlist = [0,0,0,0,0]

lenlist[0] = len(EZsList[0])
lenlist[1] = len(EZsList[1])
lenlist[2] = len(EZsList[2])
lenlist[3] = len(EZsList[3])
lenlist[4] = len(EZsList[4])


EZsListMax = max(lenlist)

print(EZsListMax)

centerEZsList = [0,0,0,0,0]


centerEZsList[0] = EZsList[0].center(EZsListMax)
centerEZsList[1] = EZsList[1].center(EZsListMax)
centerEZsList[2] = EZsList[2].center(EZsListMax)
centerEZsList[3] = EZsList[3].center(EZsListMax)
centerEZsList[4] = EZsList[4].center(EZsListMax)

#將詩詞重新組裝為一個字串
fancierS = '\n'.join(centerEZsList)

#顯示結果
print(fancierS)