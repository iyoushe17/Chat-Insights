def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')    


from reportlab.pdfgen import canvas 

'''Font Setup'''
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

class WhatsAppReport():

    def __init__(self, data):
        self.fileName = f'WhatsApp-Chat-Report.pdf'
        self.documentTitle = 'WhatsApp Chat Report'
        self.title = 'Chat-Insights'
        self.subTitle = f'Your WhatsApp Chat Report'
        self.image = 'message-graph.png'
        
        '''Chat Stats'''
        self.totalMessages = data['totalMessages']
        self.totalDays = data['totalDays']
        self.averageTextPerDay = data['averageTextPerDay']
        self.maxTextOneDay = data['maxTextOneDay']
        self.maxTextDate = data['maxTextDate']
        
        self.pdf = canvas.Canvas(self.fileName)
        self.pdf.setTitle(self.documentTitle)

    def generate(self):
        '''Draw some lines'''
        self.pdf.line(30, 750, 550, 750)
        self.pdf.line(130, 690, 450, 690)
        self.pdf.line(130, 540, 450, 540)

        '''The Title'''
        self.pdf.setFont("Helvetica", 36)
        self.pdf.drawCentredString(300, 770, self.title)
        
        '''The Subtitle'''
        self.pdf.setFillColorRGB(0, 0, 255)
        self.pdf.setFont("Courier-Bold", 24)
        self.pdf.drawCentredString(290,710, self.subTitle)
        
        textLines = [
        f'You and your friend have been talking on WhatsApp for {self.totalDays} days.',
        f'You guys have exchanged a total of {self.totalMessages} text messages till date!',
        f'On an average, {self.averageTextPerDay} text messages have been exchanged per day.',
        f'{self.maxTextDate} was the day you achieved a record high of text messages',
        f'exchanged in one single day.',
        f'Your shared record for most number of text messages sent in one day ',
        f'lies at {self.maxTextOneDay}. Keep up the good work!',
]

        '''The numbers'''
        text = self.pdf.beginText(40, 660)
        text.setFont("Courier", 13)
        text.setFillColor(colors.black)

        for line in textLines:
            text.textLine(line)
        self.pdf.drawText(text)

        '''The Graph'''
        self.pdf.drawInlineImage(self.image, -1, 50)
        self.pdf.save()






# drawMyRuler(pdf)










