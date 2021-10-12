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
        self.documentTitle = 'WhatsAppChatReport'
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
        '''The Title'''
        self.pdf.setFont("Helvetica", 36)
        self.pdf.drawCentredString(300, 770, self.title)
        
        '''The Subtitle'''
        self.pdf.setFillColorRGB(0, 0, 255)
        self.pdf.setFont("Courier-Bold", 24)
        self.pdf.drawCentredString(290,720, self.subTitle)
        
        textLines = [
        f'You and your friend exchanged a total of {self.totalMessages} text messages.',
        f'Over a span of {self.totalDays} days.',
        f'On an average, you guys exchanged {self.averageTextPerDay} texts per day.',
        'Your shared record for most number of texts sent in one days lies,',
        f'at {self.maxTextOneDay}.',
        f'{self.maxTextDate} was the day you achieved a record high of text messages',
        f'exchanged per day.'
        ]

        '''The numbers'''
        text = self.pdf.beginText(40, 680)
        text.setFont("Courier", 13)
        text.setFillColor(colors.red)

        for line in textLines:
            text.textLine(line)
        self.pdf.drawText(text)

        '''The Line Graph'''
        self.pdf.drawInlineImage(self.image, -1, 50)
        self.pdf.save()






# drawMyRuler(pdf)










