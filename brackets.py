'''小括弧'()'と中括弧'{}'と大括弧'[]'のみで構成された文字列 s が与えられた時、s が下記のルールに従っているか判定するプログラムを作成せよ。'''
'''ルール1:開き括弧'({['は、同じ種類の閉じ括弧')}]'で閉じること'''
'''ルール2:括弧を開いた順に括弧を閉じること'''

def isValid(s: str) -> bool:
    """
それぞれの括弧が閉じられているかを計算し、Bool値を返します。

str:
    -> 閉じられている: 1
    閉じられていない: 0

例:
    s = "()"
    print(isValid(s)) #True
    
"""
    #処理部分
    decomp = list(s) #受け取った文を1文字ずつに分ける
    #各括弧が開かれているか
    parenFlag = False
    squaFlag = False
    curlyFlag = False
    #Matchは新しいからifで対応
    for i in decomp:
        #括弧はじめ
        if i == '(':
            if parenFlag:
                return 0
            else:
                parenFlag = True
        elif i == '[':
            if squaFlag:
                return 0
            else:
                squaFlag = True
        elif i == '(':
            if curlyFlag:
                return 0
            else:
                curlyFlag = True
        #括弧閉じる
        elif i == ')':
            if parenFlag:
                parenFlag = False
            else:
                return 0
        elif i == ']':
            if squaFlag:
                squaFlag = False
            else:
                return 0
        elif i == '}':
            if curlyFlag:
                curlyFlag = False
            else:
                return 0
    #最後にすべての括弧が開いたままでなければTrue
    if parenFlag == False and squaFlag == False and curlyFlag == False:
        return 1
    else:
        return 0
        

# デバッグ
s = "()"
print(isValid(s)) #True

s = "({)}"
print(isValid(s)) #False

s = "("
print(isValid(s)) # False