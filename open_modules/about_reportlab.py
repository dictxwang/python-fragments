# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
reportlab用于生成pdf文件
pip install reportlab
'''

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def test01():
    c = canvas.Canvas("data/test01.pdf")
    c.drawString(100, 100, "Hello, World")
    c.showPage()
    # 开启第二页
    c.drawString(100, 100, "Second Page")
    c.showPage()
    c.save()


def test02():
    # 调用模板，创建指定名称的PDF文档
    doc = SimpleDocTemplate("data/test02.pdf")
    # 获得模板表格
    styles = getSampleStyleSheet()
    # 指定模板(Normal,Italic,Title,Headline1-6,BodyText,Bullet,Definition,Code,UnorderedList,OrderedList)
    style = styles["Title"]
    # 将段落添加到内容中
    story = [Paragraph("This is the first Paragraph!", style),
             Paragraph("This is the second Paragraph!", style)]
    doc.build(story)


def test03():
    '''
    测试表格的使用
    :return:
    '''
    doc = SimpleDocTemplate("data/test03.pdf")
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    story = []
    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    t = Table(data)
    story.append(t)
    doc.build(story)


def test04():
    '''
    表格样式的使用，内嵌的方式
    :return:
    '''
    doc = SimpleDocTemplate("data/test04.pdf")
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    story = []
    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    t = Table(data, style=[
        ('GRID', (0, 0), (-1, -1), 1, colors.gray),
        ('GRID', (1, 1,), (-2, -2), 1, colors.green),
        ('BOX', (0, 1), (1, -1), 2, colors.red),
        ('BACKGROUND', (0, 0), (0, 1), colors.pink),
        ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
        ('BACKGROUND', (2, 2), (2, 3), colors.orange)
    ])
    story.append(t)
    doc.build(story)


def test05():
    '''
    表格样式的使用：外挂方式
    :return:
    '''
    doc = SimpleDocTemplate("data/test05.pdf")
    styles = getSampleStyleSheet()
    style = styles['Normal']
    story = []
    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    t = Table(data)
    t.setStyle(TableStyle(
        [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
         ('BOX', (0, 0), (-1, -1), 2, colors.black),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.yellow),
         ('LINEAFTER', (0, 0), (0, -1), 2, colors.blue),
         ('ALIGN', (1, 1), (-1, -1), 'RIGHT')]
    ))
    story.append(t)
    doc.build(story)


def test06():
    '''
    图片的使用
    :return:
    '''
    doc = SimpleDocTemplate("data/test06.pdf")
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    story = []

    img = Image("data/reportlab_test.jpg", width=300, height=200)
    story.append(img)
    doc.build(story)


def test07():
    '''
    字体的使用
    :return:
    '''
    # 可以同时注册多个字体
    pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttf"))
    pdfmetrics.registerFont(TTFont("SimHei", "SimHei.ttf"))
    c = canvas.Canvas("data/test07.pdf")
    # 选择使用宋体
    c.setFont("SimSun", 14)
    c.drawString(200, 500, "我爱北京天安门，天安门上太阳升")
    # 选择使用黑体
    c.setFont("SimHei", 16)
    c.drawString(300, 400, "伟大领袖毛主席，带领我们向前进")
    c.save()


def test08():
    '''
    在段落中使用字体
    :return:
    '''
    # 字体需要先注册才能使用
    pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttf"))
    pdfmetrics.registerFont(TTFont("SimHei", "SimHei.ttf"))
    doc = SimpleDocTemplate("data/test08.pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=60)
    styles = getSampleStyleSheet()
    # leading 设置行距
    styles.add(ParagraphStyle(name="ps1", fontName="SimHei", fontSize=14, backColor=colors.black,
                              textColor=colors.white, leading=30, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name="ps2", fontName="SimSun", fontSize=12, backColor=colors.red,
                              textColor=colors.black, leading=30, alignment=TA_JUSTIFY))
    styleN = styles["BodyText"]
    report = []
    report.append(Paragraph("一条大河波浪宽", styles["ps1"]))
    report.append(Spacer(1, 24))
    report.append(Paragraph("风吹稻花香两岸", styles["ps2"]))
    report.append(Spacer(1, 24))
    report.append(Paragraph("我家就在岸上住", styles["ps2"]))
    report.append(Spacer(1, 48))
    doc.build(report)


if __name__ == "__main__":
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    # test06()
    # test07()
    test08()
