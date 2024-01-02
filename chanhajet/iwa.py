#!/bin/python3

from fpdf import FPDF


pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')

pdf.set_auto_page_break(False)

pdf.add_page()

pdf.rect(5,5,200,287)

pdf.line(105,98.5,105,198.5)

pdf.line(55,148.5,155,148.5)

for i in range(56,155):
    pdf.line(i,147.5,i,149.5)

for i in range(99,198):
    pdf.line(104,i+0.5,106,i+0.5)


pdf.add_page()

pdf.rect(2,5,200,287)

pdf.line(102,98.5,102,198.5)

pdf.line(52,148.5,152,148.5)

for i in range(53,152):
    pdf.line(i,147.5,i,149.5)

for i in range(99,198):
    pdf.line(101,i+0.5,103,i+0.5)
    
    
pdf.output('cadre.pdf')
