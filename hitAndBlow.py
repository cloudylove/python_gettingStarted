# coding:utf-8
###############
# Hit & Blow
###############

#import
import random

#亂數
#rnd = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
#rnd[0] = random.randint(0,9)
#rnd[1] = random.randint(0,9)
#rnd[2] = random.randint(0,9)
#rnd[3] = random.randint(0,9)
#不重複的隨機四碼數字
rnd = random.sample([0,1,2,3,4,5,6,7,8,9], 4)
rndstr = str(rnd[0])+str(rnd[1])+str(rnd[2])+str(rnd[3])
print(rndstr)

#輸入
flag = False #旗標初始為False
while flag == False:
    #輸入指令
    ipt = input("請輸入數字>") 
    #檢查是否輸入四碼
    if len(ipt) != 4:
        print("非4位")
    else:
        #檢查是否為數字
        isNum = True
        for i in range(4):
            if (ipt[i] < "0" or ipt[i] > "9"):
                print("非數字")
                isNum = False
                break
        #確認為數字
        if isNum:
            #核對數值
            if rndstr != ipt:
                print("重猜一次")
                #計算AB數值
                a = 0
                b = 0
                for i in range(4):
                    for j in range(4):
                        if(i==j):
                            if(ipt[i] == rndstr[j]):
                                #print("A:ipt["+str(i)+"]="+ipt[i]+",rndstr["+str(j)+"]="+rndstr[j])
                                a+=1
                        else:
                            if(ipt[i] == rndstr[j]):
                                #print("B:ipt["+str(i)+"]="+ipt[i]+",rndstr["+str(j)+"]="+rndstr[j])
                                b+=1
                print(str(a)+"A"+str(b)+"B")
            else:
                print("猜對了")
                flag = True
