# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ


def cipher(etc):
    etc_list = list(etc)
    print(etc_list)
    for x in range(len(etc)):
        box = etc_list(x)
        if box.isupper:
            box.encode(219)
        etc_list = box
    print(etc_list)


sample = 'hello world'
cipher(sample)
