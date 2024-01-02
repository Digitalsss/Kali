#!/bin/python3

import time 

from fpdf import FPDF


def Recto(pdf,liste,first):

    if not first:
        pdf.add_page()
    pdf.set_auto_page_break(False)

    for x in range(2):
    
        for y in range(5):

            if x:
                smallliste = liste[5+y].split(',')
            else:
                smallliste = liste[y].split(',')

            pdf.set_font('Courier',style='B',size=14)
            pdf.set_text_color(0,0,255)
            pdf.set_xy(55+(x*90),12+(y*55))
            pdf.cell(10,10,txt=smallliste[0],ln=1,align='C')
            
            
            pdf.set_font('Courier',size=12)
            pdf.set_text_color(255,0,0)
            pdf.set_xy(25+(x*90),35+(y*55))
            pdf.cell(10,10,txt=smallliste[1],ln=1,align='L')
            
            pdf.set_font('Courier',size=12)
            pdf.set_text_color(51,153,102)
            pdf.set_xy(25+(x*90),45+(y*55))
            pdf.cell(10,10,txt=smallliste[2],ln=1,align='L')



def Verso(pdfv,liste,first):
    
    if not first:
        pdfv.add_page()
    pdfv.set_auto_page_break(False)
    pdfv.set_font('Courier')

    #pdfv.set_font_size(8)

    farben=[[255,0,0],[51,153,102],[0,0,255],[255,0,255],[255,102,0]]



    for x in range(2):

        for y in range(5):

            if x:
                Strukturn = liste[5+y]
            else:
                Strukturn = liste[y]


            pdfv.set_xy(13 + 90 - (90 * x ), 16 + ( 55 * y ))
            if Strukturn.count('\n') >= 6 :
                pdfv.set_font_size(8)
                cellw = 3
            else:
                pdfv.set_font_size(12)
                cellw = 5
            pdfv.set_text_color(farben[y][0],farben[y][1],farben[y][2])
            pdfv.multi_cell(90,cellw,Strukturn, border = 0,align='L')
            



def main():

    pdf = FPDF(orientation ='P', unit='mm', format='A4')
    pdfv = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
    cadre = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
    cadre.add_page()

    pdf.add_page()
    pdf.rect(15,11,180,275,'D')
    pdf.line(105,11,105,286)
    
    pdfv.add_page()
    pdfv.rect(12,11,178,275,'D')
    pdfv.line(102,11,102,286)

    cadre.rect(15,11,180,275,'D')
    cadre.line(105,11,105,286)
    
    pdf.line(0,11,210,11)
    pdf.line(0,286,210,286)
    pdf.line(15,0,15,297)
    pdf.line(195,0,195,297)
    
    pdfv.line(0,11,210,11)
    pdfv.line(0,286,210,286)
    pdfv.line(12,0,12,297)
    pdfv.line(192,0,192,297)


    for i in range(1,5):
        cadre.line(15,11+(55*i),195,11+(55*i))
        pdfv.line(12,11+(55*i),192,11+(55*i))
        pdf.line(15,11+(55*i),195,11+(55*i))
   

    common = open('out','r').readlines()
    liste = open('liste','r').readlines()
    noneexist = open('noneexist','w')
    
    for i in range(len(common)):
        common[i] = common[i].replace('\n','')
    for i in range(len(liste)):
        liste[i] = liste[i].replace('\n','')

    while '' in liste:
        liste.remove('')

    counter = 0 
    bufferR = []
    bufferV = []
    prebuffer = ''
    first = True
    for item in common:
        if counter == 10:
            if first:
                Recto(pdf,bufferR,True)
                Verso(pdfv,bufferV,True)
                first = False
            else:
                Recto(pdf,bufferR,False)
                Verso(pdfv,bufferV,False)
        
       
            counter = 0
            bufferR = []
            bufferV = []
            prebuffer = ''

        try:
            search = liste.index(item)
        
        except:
            noneexist.write(item+'\n')
            pass

        verb = liste[search]
        perf = '- '+liste[search+1]
        pret = '- '+liste[search+2]
        bufferR.append(verb+','+perf+','+pret)
        
        i = search + 3

       

        while not liste[i] == '!SEPARATOR!':
            
            if liste[i] == '' or liste[i] == '\n':
                pass

            nummer = 0

            try:
                while liste[i][nummer] == ' ':
                    nummer = nummer + 1
            except:
                pass

            liste[i] = liste[i][nummer:]
            


            if liste[i+1] == '!SEPARATOR!' :
                prebuffer = str(prebuffer) + str(liste[i])
            else:
                prebuffer = str(prebuffer) + str(liste[i]) + str('\n')
          
            i = i + 1

        counter = counter + 1
              
        bufferV.append(prebuffer)
        prebuffer = ''
     


   
    cadre.output('Cadre.pdf')
    pdf.output('Recto.pdf')
    pdfv.output('Verso.pdf')
    noneexist.close()
  
 





if __name__ == "__main__":
    main()



