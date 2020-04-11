#Pythonによる西暦の和暦変換
#https://neguse-atama.hatenablog.com
# coding: utf-8

print("西暦年、月、日付をスペース区切りで、1行で入力してください。")

y, m, d = map(int, input().split())

new_m = m
new_d = d
if int(m) < 10:
    m = str(m)
    new_m = "0" + m
if int(d) < 10:
    d = str(d)
    new_d = "0" + d
    
date = str(y) + str(new_m) + str(new_d)
date = int(date)

if date >= 20190501:
    y = int(y) - 2018
    if y == 1:
        y = "元"
    print("令和{}年{}月{}日".format(y, m, d))
elif date >= 19890108:
    y = int(y) - 1988
    if y == 1:
        y = "元"
    print("平成{}年{}月{}日".format(y, m, d))
elif date >= 19261225:
    y = int(y) - 1925
    if y == 1:
        y = "元"
    print("昭和{}年{}月{}日".format(y, m, d))
elif date >= 19120730:
    y = int(y) - 1911
    if y == 1:
        y = "元"
    print("大正{}年{}月{}日".format(y, m, d))
elif date >= 18681023:
    print("明治{}年{}月{}日".format(y, m, d))
    y = int(y) - 1867
    if y == 1:
        y = "元"
else:
    print("1868年10月22日以前は改暦前であるため、旧暦については表示しません。")




