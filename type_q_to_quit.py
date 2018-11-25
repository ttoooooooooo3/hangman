#ユーザー が q を 入力 する まで ループ を 繰り返す プログラム 

qs = ['what is your name?', # qs[0]
    'what is your favorite color?'  # qs[1]
    'what is your quest?']  # qs[2]

n = 0   # 最初の処理で0が入る
while True:
    print('type Q to quit') # 'type Q to quit'と表示する
    a = input(qs[n]) # qs[n]を表示し、ユーザにインプットを求める。インプットがaに代入される。
    if a == 'Q':    # ユーザのインプットがQであれば処理を終了
        break
    n = (n + 1) % 3 # Qでなかった場合、nの値を変更し、while文を継続する。