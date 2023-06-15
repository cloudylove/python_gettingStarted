# coding:utf-8
###############
# Canvas - 三顆球
###############

# import
import tkinter as tk

# 三顆球
# 串列包字典 # 圓型座標&移動量&顏色
balls = [
    {"x":0, "y":0, "dx":1, "dy":1, "color":"red"},
    {"x":120, "y":0, "dx":1, "dy":1, "color":"blue"},
    {"x":0, "y":350, "dx":1, "dy":1, "color":"green"},
]

# 移動事件
def move():
    # 三顆球用串列包字典
    global balls
    for i in balls:
        # 清除舊圓
        canvas.create_oval(i["x"]-20, i["y"]-20, i["x"]+20, i["y"]+20, fill = "white", width = 0) 
        # 移動座標
        i["x"] = i["x"]+i["dx"]
        i["y"] = i["y"]+i["dy"]
        # 新圓
        canvas.create_oval(i["x"]-20, i["y"]-20, i["x"]+20, i["y"]+20, fill = i["color"], width = 0) #新圓
        # 邊界反彈
        if i["x"] >= canvas.winfo_width():
            i["dx"] = -1
        if i["x"] <= 0:
            i["dx"] = +1
        if i["y"] >= canvas.winfo_height():
            i["dy"] = -1
        if i["y"] <= 0:
            i["dy"] = +1
    root.after(10, move)

# 描繪視窗
root = tk.Tk()
root.geometry("600x400")

# Canvas
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

# 設定計時器
root.after(10, loop)


root.mainloop()
