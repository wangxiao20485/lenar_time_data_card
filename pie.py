from reportlab.pdfgen import canvas
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
import webbrowser,os
c=canvas.Canvas("Time_data_card.pdf")
plan = ["睡觉","上课","写作业","兴趣课","娱乐","吃饭"]
data = [9,8,2,2,2,1]
c.drawImage('card.png',0,0,width=372,height=665,mask=None)
drawing=Drawing(372,665)
pc = Pie()
pc.x = 115
pc.y = 350
pc.width = 150
pc.height = 152
pc.data = data
pc.sideLabels = 1
pc.labels = [str(1) for i in data]
drawing.add(pc)
renderPDF.draw(drawing,c,0,0)
c.save()
webbrowser.open("file://"+os.path.realpath("Time_data_card.pdf"))
