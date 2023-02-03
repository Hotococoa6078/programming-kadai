item = ["やきそば", "パスタ", "うどん", "そば", "そうめん"]
price = [150, 200, 250, 250, 300]
getList = {"やきそば" : [0,0], "パスタ" : [0,0], "うどん" : [0,0], "そば" : [0,0], "そうめん" : [0,0]} #item_name : [getCount , max_price]
for i in range(0, 5): #item info
    print(f"{i + 1} : {item[i]}")
total = 0
a, b = 0, 0
while b < 1: #start
    try:
        Num = input("メニュー番号1～5を入力（9で注文内容確認、0で終了）: ")
        num = int(Num) - 1
        if 0 <= num <= 4: #1~5
            a = 0
            while a == 0: #setting buy info
                try:
                    count = int(input(f'{item[num]}は何個要りますか？(キャンセルは0) : '))
                    if count == 0:
                        print('キャンセルしました。')
                        a += 1
                    elif 0 <= count: #print buy item info
                        print('=' * 15)
                        print(f"{num+1}番 {item[num]} {count}個 : {price[num] * count}円")
                        print('=' * 15)
                        a += 1
                    getList[item[num]][0],getList[item[num]][1] = getList[item[num]][0] + count, getList[item[num]][1] + price[num] * count
                    total += price[num] * count
                except ValueError as e:
                    print("エラーが発生しました。数字だけ入力してください。")
                    print('error : ', e)
        elif num == 8: #9,  buyList info
            print('これまでに入力した購入リストです。\n', '='*15)
            for i in getList: #print buyList info
                if getList[i][0] == 0:
                    pass
                elif getList[i][0] >= 1:
                    print(f"{item.index(i) + 1}番 {i} {getList[i][0]}個 : {price[item.index(i)] * getList[i][0]}円")
            print('=' * 15)
            p = 0
            while p < 1: #check change buyList
                try:
                    o = int(input('変更が必要ですか？ 必要であれば1、よろしければ0を入力してください。 : '))
                    if o == 1: #break
                        f = 0
                        while f < 1: #to change
                            try:
                                d = int(input('変更が必要なメニュー番号を入力(0で終了) : ')) -1
                                if d == -1: #save change
                                    print('変更が保存されました。')
                                    p, f = 1, 1 #break
                                elif 0 <= d <= 4: #check number
                                    if getList[item[d]][0] == 0: #if didn't buy that item
                                        print('購入履歴のない番号です。')
                                    else:
                                        h = 0
                                        while h < 1: #check all reset or change value
                                            try:
                                                g = int(input('商品を取り消す場合は1、個数を減らすには2以上の数字を入力してください。(0で終了) : '))
                                                if g == 0: #cancel
                                                    h = 1
                                                elif g == 1: #reset
                                                    m = 0
                                                    while m < 1:
                                                        j = input("本当に取り消しますか?(Y/N) : ")
                                                        if j == 'y' or j == 'Y': #all reset
                                                            getList[item[d]] = [0, 0]
                                                            print('商品の取り消しに成功しました。')
                                                            m = 1
                                                        elif j == 'n' or j == 'N': #cancel
                                                            print('取り消しをやめました。')
                                                            m = 1
                                                        else:
                                                            print("Y(Yes)またはN(No)を入力してください。")
                                                elif g >= 2:
                                                    if getList[item[d]][0] < g:
                                                        print("商品がないか、または入力された数字が大きすぎます。")
                                                    else:
                                                        n = 0
                                                        while n < 1:
                                                            l = input(f'本当にリストから{item[d]}を{g}個抜きますか？(Y/N) : ')
                                                            if l == 'y' or l == 'Y':
                                                                getList[item[d]] = [ getList[item[d]][0] - g   , getList[item[d]][1] - (g*price[d])   ]
                                                                print(f'商品が成功的に{g}個抜けました。')
                                                                n = 1
                                                            elif l == 'n' or l == 'N':
                                                                print('キャンセルしました。')
                                                                n = 1
                                                            else:
                                                                print("Y(Yes)またはN(No)を入力してください。")
                                            except ValueError as e:
                                                print("エラーが発生しました。数字だけ入力してください。")
                                                print('error : ', e)
                                else:
                                    print('正しい数字を入力してください。')
                            except ValueError as e:
                                print("エラーが発生しました。数字だけ入力してください。")
                                print('error : ', e)
                    elif o == 0:
                        p += 1
                    else:
                        print('正しい数字を入力してください。')
                except ValueError as e:
                    print("エラーが発生しました。数字だけ入力してください。")
                    print('error : ', e)
        elif num == -1: #0
            r  = 0
            while r < 1:
                try:
                    print("入力してもらった商品はこちらになります。\n間違いはないかご確認お願い致します。")
                    for i in getList:
                        if getList[i][0] == 0:
                            pass
                        elif getList[i][0] >= 1:
                            print(f"{item.index(i) + 1}番 {i} {getList[i][0]}個 : {price[item.index(i)] * getList[i][0]}円")
                    print(f"TOTAL : {total}円")
                    print("間違いがない場合は0を、ある場合は1を入力してください。")
                    t = 0
                    while t < 1:
                        try:
                            res = int(input(""))
                            if res == 0:
                                print("=" * 20)
                                for i in getList:
                                    if getList[i][0] == 0:
                                        pass
                                    elif getList[i][0] >= 1:
                                        print(f"{item.index(i) + 1}番 {i} {getList[i][0]}個 : {price[item.index(i)] * getList[i][0]}円")
                                print("=" * 20)
                                print(f"合計金額は {total}円です。")
                                r, t, b = 1, 1, 1
                                break
                            elif res == 1:
                                y = 0
                                while y < 1:
                                    try:
                                        u = int(input("上にあるリストで修正または取り消しする番号を入力してください。(0で終了) : ")) - 1
                                        if u == -1:
                                            print('変更が保存されました。')
                                            y = 1
                                        elif 0 <= u <= 4:
                                            if getList[item[u]][0] == 0:
                                                print('購入履歴のない番号です。')
                                            else:
                                                h = 0
                                                while h < 1:
                                                    try:
                                                        g = int(input('商品を取り消す場合は1、個数を減らすには2以上の数字を入力してください。(0で終了) : '))
                                                        if g == 0:
                                                            print('変更が保存されました。')
                                                            h, u = 1, 1
                                                        elif g == 1:
                                                            v = 0
                                                            while v < 1:
                                                                j = input("本当に取り消しますか?(Y/N) : ")
                                                                if j == 'y' or j == 'Y':
                                                                    getList[item[u]] = [0, 0]
                                                                    print('商品の取り消しに成功しました。')
                                                                    v = 1
                                                                elif j == 'n' or j == 'N':
                                                                    print('取り消しをやめました。')
                                                                    v = 1
                                                                else:
                                                                    print("Y(Yes)またはN(No)を入力してください。")
                                                        elif g >= 2:
                                                            if getList[item[u]][0] < g:
                                                                print("商品がないか、または入力された数字が大きすぎます。")
                                                            else:
                                                                c = 0
                                                                while c < 1:
                                                                    l = input(f'本当にリストから{item[u]}を{g}個抜きますか？(Y/N) : ')
                                                                    if l == 'y' or j == 'Y':
                                                                        getList[item[u]] = [ getList[item[u]][0] - g   , getList[item[u]][1] - (g*price[u])]
                                                                        print(f'商品が成功的に{g}個抜けました。')
                                                                        c = 1
                                                                    elif j == 'n' or j == 'N':
                                                                        print('キャンセルしました。')
                                                                        c = 1
                                                                    else:
                                                                        print("Y(Yes)またはN(No)を入力してください。")
                                                    except ValueError as e:
                                                        print("エラーが発生しました。数字だけ入力してください。")
                                                        print('error : ', e)
                                    except ValueError as e:
                                        print("エラーが発生しました。数字だけ入力してください。")
                                        print('error : ', e)
                                t = 1
                            else:
                                print("正しい数字を入力してください。")
                        except ValueError as e:
                            print("エラーが発生しました。数字だけ入力してください。")
                            print('error : ', e)
                except ValueError as e:
                    print("エラーが発生しました。数字だけ入力してください。")
                    print('error : ', e)
        else:
            print('数字は6未満で入力してください。')
    except ValueError as e:
        print("エラーが発生しました。数字だけ入力してください。")
        print('error : ', e)
    except Exception as e:
        print("エラーが発生しました。もう一度やり直してください。")
        print('error : ', e)
print('program is end')