from reportlab.pdfgen import canvas
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
import webbrowser,os
c=canvas.Canvas("Time_data_card.pdf")
c.drawImage('card.png',0,0,width=372,height=665,mask=None)
drawing=Drawing(372,665)
pc = Pie()
pc.x = 115
pc.y = 350
pc.width = 150
pc.height = 152
drawing.add(pc)
renderPDF.draw(drawing,c,0,0)
c.save()
webbrowser.open("file://"+os.path.realpath("Time_data_card.pdf"))
