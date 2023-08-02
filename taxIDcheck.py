######################
# index.csv 打包檔    #
# input.csv 待核對    #
# id統編, name公司名稱 #
######################

import csv

with open('input.csv', encoding="big5") as csvFileInput:
    csvReaderInput = csv.reader(csvFileInput)
    listReportInput = list(csvReaderInput)

with open('index.csv', encoding="utf-8") as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)

# 標頭
print("{0:^5}{1:^8}{2:^30}{3:^30}{4:^10}".format("n","待核對統編","待核對公司","核對結果","第二層迴圈次數"))
n = 0
# 待核對檔
for rowInput in listReportInput: 
    x = 0
    iptCpy = rowInput[1] #待核對公司名
    check = "" #核對結果
    # 打包檔
    for row in listReport:
        x += 1
        if row[0] == rowInput[0]: #打包檔統編==待核對統編
            if row[2] != rowInput[1]: #打包檔公司名!=待核對公司名
                check = row[2] #公司名核對不同
            else:
                check = "ok" #公司名核對ok
        if check != "": #有核對結果中止迴圈
            break
        
    if check == "": #查無此統編
        check = "null"
    
    n += 1
    print("{0:^5}{1:<8}{2:^30}{3:^30}{4:^10}".format(n, rowInput[0], iptCpy, check, x))
    #<置左/^置中+長度
