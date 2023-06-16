# 匯入類別
from reportlab.pdfgen import canvas #pdf描繪領域
from reportlab.pdfbase import pdfmetrics #pdf構造如字型註冊
from reportlab.pdfbase.cidfonts import UnicodeCIDFont #字型
from reportlab.pdfbase import ttfonts #字型
import reportlab.lib.units as unit #單位
import reportlab.lib.pagesizes as pagesizes #紙張大小

# 註冊字型
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))
pdfmetrics.registerFont(ttfonts.TTFont("kaiu", "C:\\Windows\\Fonts\\kaiu.ttf"))


# 製作PDF
pdf = canvas.Canvas("example.pdf", pagesize=pagesizes.A4) #指定pdf檔名跟紙張大小
content = "新年快樂！"
A4height = 290
A4width = 210
#fonSize = (A4width-5) #HeiseiKakuGo-W5
#tune = 25 #HeiseiKakuGo-W5
fonSize = (A4width)
tune = 42



for c in content:
    #pdf.setFont("HeiseiKakuGo-W5", fonSize * unit.mm) #字型&字體大小 
    pdf.setFont("kaiu", fonSize * unit.mm) #字型&字體大小
    #pdf.drawString(0 * unit.mm, 18 * unit.mm, c) #字串位置
    pdf.drawString(0 * unit.mm, ((A4height-fonSize)/2+tune) * unit.mm, c) #字串位置
    pdf.showPage() #換頁
pdf.save() #儲存
