##############################
# scores.csv                 #
# 姓名	程式	英聽	實習  #
# 許東偉	98	88	75   #
##############################


import csv

# 標頭
print("{0:<3}{1:<5}{2:<4}{3:<4}{4:<5}".format("","姓名","總分","平均","分數"))
#第0欄置左長度3 #第1欄置左長度5

# 讀取 scores.csv
with open("scores.csv", encoding="utf-8") as csvfile: #執行開頭多編碼的話可以改encoding="utf-8-sig"
    reader = csv.reader(csvfile)
    x = 0
    for row in reader:
        #print(row)
        if x > 0:
            total_sum = int(row[1]) + int(row[2]) + int(row[3]) #總分
            score = round(total_sum/3,1) #平均四捨五入至小數第一位

            if score >= 80:
                level = "A"
            elif 60 <= score < 80:
                level = "B"
            elif 50 <= score < 60:
                level = "C"
            else:
                level = "D"

            print("{0:<3}{1:<5}{2:<4}{3:<4}{4:^5}".format(x, row[0], total_sum, score, level))
            #第5欄置中長度5

        x += 1

