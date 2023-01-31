item = ["やきそば", "パスタ", "うどん", "そば", "そうめん"]
price = [150, 200, 250, 250, 300]
getList = {"やきそば" : [0,0], "パスタ" : [0,0], "うどん" : [0,0], "そば" : [0,0], "そうめん" : [0,0]} #item name : [getCount , max price]
for i in range(0, 5):
    print(f"{i + 1} : {item[i]}")
total = 0
a, b = 0, 0
while b < 1:
    try:
        Num = input("メニュー番号　1～5を入力（9で注文内容確認、0で終了）: ")
        num = int(Num) - 1
        if 0 <= num <= 4:
            a = 0
            while a == 0:
                count = int(input(f'{item[num]}は何個要りますか？(キャンセルは0) : '))
                if count == 0:
                    print('キャンセルしました。')
                    a += 1
                elif 0 <= count:
                    print(f"{num+1}番 {item[num]} {count}個 : {price[num] * count}円")
                    a += 1
                getList[item[num]][0],getList[item[num]][1] = getList[item[num]][0] + count, getList[item[num]][1] + price[num] * count
                total += price[num] * count
        elif num == 8:
            print('これまでに入力した購入リストです。')
            for i in getList:
                if getList[i][0] == 0:
                    pass
                elif getList[i][0] >= 1:
                    print(f"{item.index(i) + 1}番 {i} {getList[i][0]}個 : {price[item.index(i)] * getList[i][0]}円")
            p = 0
            while p < 1:
                o = int(input('変更が必要ですか？ 必要であれば1、よろしければ0を入力してください。 : '))
                if o == 1:
                    f = 0
                    while f < 1:
                        d = int(input('変更が必要なメニュー番号を入力(0で終了) : ')) -1
                        if d == -1:
                            print('変更が保存されました。')
                            p = 1
                        elif 0 <= d <= 4:
                            if getList[item[d]][0] == 0:
                                print('購入履歴のない番号です。')
                            else:
                                h = 0
                                while h < 1:
                                    g = int(input('商品を取り消す場合は1、個数を減らすには2以上の数字を入力してください。(0で終了) : '))
                                    if g == 0:
                                        h = 1
                                    elif g == 1:
                                        j = input("本当に取り消しますか?(Y/N) : ")
                                        if j == 'y' or j == 'Y':
                                            getList[item[d]] = [0, 0]
                                            print('商品の取り消しに成功しました。')
                                        elif j == 'n' or j == 'N':
                                            print('取り消しをやめました。')
                                    elif g >= 2:
                                        if getList[item[d]][0] < g:
                                            print("入力された数字が大きすぎます。")
                                        else:
                                            l = input(f'本当にリストから{item[d]}を{g}個抜きますか？(Y/N) : ')
                                            if l == 'y' or j == 'Y':
                                                getList[item[d]] = [ getList[item[d]][0] - g   , getList[item[d]][1] - (g*price[d])   ]
                                                print('商品が成功的に{g}個抜けました。')
                                            elif j == 'n' or j == 'N':
                                                print('キャンセルしました。')
                        else:
                            print('正しい数字を入力してください。')
                elif o == 0:
                    p += 1
                else:
                    print('正しい数字を入力してください。')
        elif num == -1:
            r  = 0
            while r < 1:
                try:
                    print("今入力してもらった商品はこちらになります。\n間違いはないかご確認お願い致します。")
                    for i in getList:
                        if getList[i][0] == 0:
                            pass
                        elif getList[i][0] >= 1:
                            print(f"{item.index(i) + 1}番 {i} {getList[i][0]}個 : {price[item.index(i)] * getList[i][0]}円")
                    print(f"TOTAL : {total}円")
                    print("間違いがない場合は０を、ある場合は１を入力してください。")
                    t = 0
                    while t < 1:
                        res = int(input(""))
                        if res == 0:
                            print("*" * 20)
                            for i in getList:
                                if getList[i][0] == 0:
                                    pass
                                elif getList[i][0] >= 1:
                                    print(f"{item.index(i) + 1}番 {i} {getList[i][0]}個 : {price[item.index(i)] * getList[i][0]}円")
                            print(f"合計金額は {total}円です。")
                            r = 1
                            t = 1
                            b = 1
                            break
                        elif res == 1:
                            y = 0
                            while y < 1:
                                u = int(input("上にあるリストで修正または取り消しする番号を入力してください。(0で終了) : ")) - 1
                                if u == -1:
                                    print('変更が保存されました。')
                                    y = 1
                                elif 0 <= u <= 4:
                                    if getList[item[d]][0] == 0:
                                        print('購入履歴のない番号です。')
                                    else:
                                        h = 0
                                        while h < 1:
                                            g = int(input('商品を取り消す場合は0、個数を減らすには1 以上の数字を入力してください。: '))
                                            if g == 0:
                                                j = input("本当に取り消しますか?(Y/N) : ")
                                                if j == 'y' or j == 'Y':
                                                    getList[item[d]] = [0, 0]
                                                    print('商品の取り消しに成功しました。')
                                                elif j == 'n' or j == 'N':
                                                    print('取り消しをやめました。')
                                            elif g >= 1:
                                                if getList[item[d]][0] < g:
                                                    print("入力された数字が大きすぎます。")
                                                else:
                                                    l = input(f'本当にリストから{item[d]}を{g}個抜きますか？(Y/N) : ')
                                                    if l == 'y' or j == 'Y':
                                                        getList[item[d]] = [ getList[item[d]][0] - g   , getList[item[d]][1] - (g*price[d])   ]
                                                        print('商品が成功的に{g}個抜けました。')
                                                    elif j == 'n' or j == 'N':
                                                        print('キャンセルしました。')
                                print("this function is not developed.")###################################################
                                y = 1
                            t = 1
                        else:
                            print("正しい数字を入力してください。")
                except ValueError as e:
                    print("エラーが発生しました。数字だけ入力してください。")
                    print('error : ', e)
        else:
            print('数字は6未満で入力してください。')
    except ValueError as e:
        print("エラーが発生しました。数字だけ入力してください。")
        print('error : ', e)
    #except Exception as e:
        #print("エラーが発生しました。もう一度やり直してください。")
        #print('error : ', e)

