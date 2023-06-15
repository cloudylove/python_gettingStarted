# coding:utf-8
###############
# Canvas - 點擊畫圓+反彈
###############

# import
import tkinter as tk

# 圓形座標
x = 0
y = 0
# 移動量
dx = 1
dy = 1

# 點擊事件
def click(event):
    # 描繪圓形
    canvas.create_oval(event.x-20, event.y-20, event.x+20, event.y+20, fill = "red", width = 0)

    # 點擊處畫圓，消除舊圓
    global x, y #全域變數
    canvas.create_oval(x-20, y-20, x+20, y+20, fill = "white", width = 0)
    x = event.x
    y = event.y
    canvas.create_oval(x-20, y-20, x+20, y+20, fill = "red", width = 0)

# 移動事件
def move():
    global x, y, dx, dy
    canvas.create_oval(x-20, y-20, x+20, y+20, fill = "white", width = 0) #舊圓
    x = x+dx
    y = y+dy
    canvas.create_oval(x-20, y-20, x+20, y+20, fill = "red", width = 0) #新圓
    # 邊界反彈
    if x >= canvas.winfo_width():
        dx = -1
    if x <= 0:
        dx = +1
    if y >= canvas.winfo_height():
        dy = -1
    if y <= 0:
        dy = +1
    # 重啟計時器
    root.after(10, move)


# 描繪視窗
root = tk.Tk()
root.geometry("600x400")

# Canvas
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

# 設定事件
canvas.bind("<Button-1>", click) #點擊左鍵

# 設定計時器
root.after(10, move)

root.mainloop()
