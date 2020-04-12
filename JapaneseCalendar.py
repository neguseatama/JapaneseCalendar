# Pythonによる西暦の和暦変換
# https://neguse-atama.hatenablog.com
# coding: utf-8

print("西暦年、月、日付をスペース区切りで、1行で入力してください。")
year, month, day = map(int, input().split())

new_m = month
new_d = day

if int(month) < 10:
    month = str(month)
    new_m = "0" + month

if int(day) < 10:
    day = str(day)
    new_d = "0" + day

date = str(year) + str(new_m) + str(new_d)
date = int(date)

if date >= 20190501:
    year = int(y) - 2018
    if year == 1:
        year = "元"
    print("令和{}年{}月{}日".format(year, month, day))
  
elif date >= 19890108:
    year = int(year) - 1988
    if year == 1:
        year = "元"
    print("平成{}年{}月{}日".format(year, month, day))
    
elif date >= 19261225:
    year = int(year) - 1925
    if year == 1:
        year = "元"
    print("昭和{}年{}月{}日".format(year, month, day))

elif date >= 19120730:
    year = int(year) - 1911
    if year == 1:
        year = "元"
    print("大正{}年{}月{}日".format(year, month, day))

elif date >= 18681023:
    year = int(year) - 1867
    if year == 1:
        year = "元"
    print("明治{}年{}月{}日".format(year, month, day))

else:
    print("1868年10月22日以前は改暦前であるため、旧暦については表示しません。")
