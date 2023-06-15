# coding:utf-8
###############
# Canvas - 繼承類別畫球、矩形、三角形
###############

# import
import tkinter as tk

# 類別
class Ball:
    # 建構子(constructor)
    def __init__(self, x, y, dx, dy, color): #self指向該物件
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
    # method
    def test(self):
        print(self.x)
        print(self.y)
    def move(self, canvas):
        self.erase(canvas) #清除
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.draw(canvas) #畫圓
        if self.x >= canvas.winfo_width():
            self.dx = -1
        if self.x <= 0:
            self.dx = +1
        if self.y >= canvas.winfo_height():
            self.dy = -1
        if self.y <= 0:
            self.dy = +1
    # 清除舊圓
    def erase(self, canvas):
            canvas.create_oval(self.x-20, self.y-20, self.x+20, self.y+20, fill = "white", width = 0)
    # 畫新圓
    def draw(self, canvas):
            canvas.create_oval(self.x-20, self.y-20, self.x+20, self.y+20, fill = self.color, width = 0)
# 矩形 # 繼承 class Ball
class Rectangle(Ball):
    def erase(self, canvas):
            canvas.create_rectangle(self.x-20, self.y-20, self.x+20, self.y+20, fill = "white", width = 0)
    def draw(self, canvas):
            canvas.create_rectangle(self.x-20, self.y-20, self.x+20, self.y+20, fill = self.color, width = 0)
# 三角形 # 繼承 class Ball
class Triangle(Ball):
    def erase(self, canvas):
            canvas.create_polygon(self.x, self.y-20, self.x+20, self.y+20, self.x-20, self.y+20, fill = "white", width = 0)
    def draw(self, canvas):
            canvas.create_polygon(self.x, self.y-20, self.x+20, self.y+20, self.x-20, self.y+20, fill = self.color, width = 0)

# 串列包字典 # 圓型座標&移動量&顏色
balls = [
    Ball(0, 0, 1, 1, "red"),
    Rectangle(120, 0, 1, 1, "blue"),
    Triangle(0, 350, 1, 1, "green")
]

def loop():
    for i in balls:
        i.move(canvas)
    #r.move(canvas)
    #t.move(canvas)
    root.after(10,loop) #0.01秒後重新執行

#r = Rectangle(400, 300, 1, 1, "red")
#t = Triangle(400, 300, 1, -1, "green")

# 描繪視窗
root = tk.Tk()
root.geometry("600x400")

# Canvas
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

# 設定計時器
root.after(10, loop)


root.mainloop()
