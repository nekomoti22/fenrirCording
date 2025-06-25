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
    #フラグが早いけど要素が少ないので配列を用いたstackで実装
    bra = []
    match = {")":"(", "]":"[", "}":"{"}
    for i in decomp:
        if i == "(" or i == "[" or i == "{":
            if i in bra:
                return False
            else:
                bra.append(i)
        else:
            if match[i] == bra[-1]:
                bra.pop(-1)
            else:
                return False
    if len(bra) == 0:
        return True
    else:
        return False

        
        

# デバッグ
s = "()"
print(isValid(s)) #True

s = "({)}"
print(isValid(s)) #False

s = "("
print(isValid(s)) # False