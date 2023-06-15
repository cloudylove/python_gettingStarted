# coding:utf-8
###############
# Hit & Blow with GUI
###############

# import
import random
import tkinter as tk
import tkinter.messagebox as tmsg

# function
def ButtonClick():
    # 取得輸入值
    ipt = editbox1.get()
    #tmsg.showinfo("輸入的數字", ipt)
    
    #flag = False #旗標初始為False
    #檢查是否輸入四碼
    if len(ipt) != 4:
        tmsg.showinfo("錯誤", "請輸入4位數字")
    else:
        #檢查是否為數字
        isNum = True
        for i in range(4):
            if (ipt[i] < "0" or ipt[i] > "9"):
                tmsg.showinfo("錯誤", "非數字")
                isNum = False
                break
    #確認為數字
    if isNum:
        #flag = True
        #核對數值
        if rndstr != ipt:
            #計算AB數值
            a = 0
            b = 0
            for i in range(4):
                for j in range(4):
                    if(i==j):
                        if(ipt[i] == rndstr[j]):
                            a+=1
                    else:
                        if(ipt[i] == rndstr[j]):
                            b+=1
            #tmsg.showinfo(ipt, str(a)+"A"+str(b)+"B")
            rirekibox.insert(tk.END, ipt+" / "+str(a)+"A"+str(b)+"B \n")
        else:
            tmsg.showinfo(ipt, "猜對了")
            #flag = True
            root.destroy()

# 不重複的隨機四碼數字
rnd = random.sample([0,1,2,3,4,5,6,7,8,9], 4)
rndstr = str(rnd[0])+str(rnd[1])+str(rnd[2])+str(rnd[3])
#print(rndstr)

root = tk.Tk() #產生視窗
root.geometry("300x400") #調整視窗大小
root.title("猜數字-0A0B") #視窗標題

label1 = tk.Label(root, text = "請輸入數字", font = ("微軟正黑體", 14))
label1.place(x = 20, y = 20)
editbox1 = tk.Entry(width = 4, font = ("微軟正黑體", 14))
editbox1.place(x = 120+5, y = 20)
button1 = tk.Button(root, text = "確認", font = ("微軟正黑體", 14), command = ButtonClick)
button1.place(x = 220, y = 20-5)

# 記錄
rirekibox = tk.Text(root, font = ("微軟正黑體", 14))
rirekibox.place(x = 20, y = 90, width = 200, height = 250)

root.mainloop() #顯示視窗

