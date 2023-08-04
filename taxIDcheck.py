######################
# 核對統編及公司名稱    #
# index.csv 打包檔    #
# input.csv 待核對    #
# id統編, name公司名稱 #
######################

import csv

# 讀取待查csv
with open("input.csv", encoding="big5") as csvInput:
    csvReader = csv.DictReader(csvInput) # 讀取csv轉成dict
    inputData = [row for row in csvReader] 
            
indexData = {}
# 讀取打包檔存成字典當索引
with open("index.csv", encoding="utf-8") as csvIndex:
    csvReader = csv.DictReader(csvIndex)
    for row in csvReader:
        indexData[row['#id']] = row['name'] 

# 匯出核對結果
with open("output.csv", "w", newline="", encoding="big5") as csvOutput:
    # 標頭
    fieldnames = list(inputData[0].keys()) 
    fieldnames.append("核對結果")
    writer = csv.DictWriter(csvOutput, fieldnames=fieldnames) #寫入csv
    writer.writeheader() #寫入第一列

    # 逐列核對並寫入結果
    for row in inputData:
        if row["#id"] in indexData:
            if row["name"] == indexData[row["#id"]]:
                row["核對結果"] = "ok"
            else:
                row["核對結果"] = indexData[row["#id"]]
        else:
            row["核對結果"] = "查無此統編"
        writer.writerow(row)
