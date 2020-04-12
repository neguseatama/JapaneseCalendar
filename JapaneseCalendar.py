# Pythonによる西暦の和暦変換
# https://neguse-atama.hatenablog.com
# coding: utf-8

print("西暦年、月、日付をスペース区切りで、1行で入力してください。")
# 西暦年、月、日付の入力
year, month, day = map(int, input().split())

new_m = month
new_d = day
# 月、日付を変数にする

if int(m) < 10:
    month = str(month)
    new_m = "0" + month
# 1桁の月に0を加えて2桁にする

if int(day) < 10:
    day = str(day)
    new_d = "0" + day
# 1桁の日に0を加えて2桁にする

date = str(year) + str(new_m) + str(new_d)
date = int(date)
# 西暦年、月、日付を8桁の数値にする

if date >= 20190501:
# 西暦年、月、日付を8桁の数値として大小関係を比較する
    year = int(y) - 2018
    if year == 1:
        year = "元"
# 和暦年が1であれば、元年と表示する
    print("令和{}年{}月{}日".format(year, month, day))
# 和暦変換の結果表示
  
elif date >= 19890108:
# 西暦年、月、日付を8桁の数値として大小関係を比較する
    year = int(year) - 1988
    if year == 1:
        year = "元"
# 和暦年が1であれば、元年と表示する
    print("平成{}年{}月{}日".format(year, month, day))
# 和暦変換の結果表示
    
elif date >= 19261225:
# 西暦年、月、日付を8桁の数値として大小関係を比較する
    year = int(year) - 1925
    if year == 1:
        year = "元"
# 和暦年が1であれば、元年と表示する
    print("昭和{}年{}月{}日".format(year, month, day))
# 和暦変換の結果表示

elif date >= 19120730:
# 西暦年、月、日付を8桁の数値として大小関係を比較する
    year = int(year) - 1911
    if year == 1:
        year = "元"
# 和暦年が1であれば、元年と表示する
    print("大正{}年{}月{}日".format(year, month, day))
# 和暦変換の結果表示

elif date >= 18681023:
# 西暦年、月、日付を8桁の数値として大小関係を比較する
    year = int(year) - 1867
    if year == 1:
        year = "元"
# 和暦年が1であれば、元年と表示する
    print("明治{}年{}月{}日".format(year, month, day))
# 和暦変換の結果表示

else:
    print("1868年10月22日以前は改暦前であるため、旧暦については表示しません。")
# 改暦前の入力について表示する
