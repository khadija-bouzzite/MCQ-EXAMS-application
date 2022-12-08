import string
from fpdf import FPDF
import PyPDF2
Liste = list(string.ascii_uppercase)


def create_QCM(id, pdf, nbr_qst, nbr_choix, nbrvariants, variant):
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)
    pdf.set_line_width(0.4)
    pdf.set_font('Times', 'B', 10)
    pdf.set_xy(0, 12)
    pdf.cell(3, 3, 'Code INE', ln=1, align='L')
    k = 20
    for i in range(0, 10):
        pdf.rect(k, 8, 10, 11, 'D')
        k = k + 10
    #pdf.rect(20, 7, 70, 12, 'D')

    pdf.set_xy(0, 28)
    pdf.cell(3, 3, 'Nom', ln=1, align='L')  # la chaine a comme coordonnes w=3,h=5
    k = 20
    # for i in range(0, 15):
    # pdf.rect(k, 20, 7, 7, 'D')
    # k = k + 7
    pdf.rect(20, 25, 105, 11, 'D')
    pdf.set_xy(0, 43)
    pdf.cell(3, 3, 'Prenom', ln=1, align='L')  # la chaine a comme coordonnes w=3,h=5
    k = 20
    # for i in range(0, 15):
    # pdf.rect(k, 30, 7, 7, 'D')
    # k = k + 7
    pdf.rect(20, 40, 105, 11, 'D')
    pdf.ln()
    pdf.ln()
    # set_remarque=[110,10]
    pdf.set_xy(130, 2)
    pdf.cell(2, 2, 'Remarques:', border=0, ln=1, align='L')
    txt = "Cette fiche doit être remplie avec un stylo au feutre noir.                                                                               " \
          "Ecrire le Nom et le Prenom en MAJUSCULE.           " \
          "Pour chaque question une seule réponse est juste." \
          "Vous devez cocher à l'intérieur des cases  sans les dépasser  de la maniere suivante:"
    pdf.set_xy(130, 10)
    pdf.multi_cell(80, 5, txt, border=0, align='L')
    pdf.rect(170, 43, 5, 5, 'D')
    pdf.line(170, 43, 175, 48)
    pdf.line(170, 48, 175, 43)
    pdf.rect(180, 43, 5, 5, 'DF')

    pdf.rect(129, 8, 80, 44)
    pdf.line(0, 55, 210, 55)

    # creer les cases des reponses

    start_c1 = [50, 105];
    coordinateChoixC1 = [50, 100];
    coordinateQstC1 = [35, 105]
    start_c2 = [130, 105];
    coordinateChoixC2 = [130, 100];
    coordinateQstC2 = [115, 105]


    if nbrvariants > 1:
        o = 90
        pdf.set_xy(50, 60)
        pdf.cell(10, 10, "VERSION  :", 0, 0, 'L')
        e = 90
        for i in range(nbrvariants):
            pdf.set_xy(e, 57)
            pdf.cell(1, 1, "{}".format(Liste[i]), 0, 0, )
            e = e + 10
        for i in range(nbrvariants):
            if (i == variant - 1):
                pdf.rect(o, 60, 6, 6, 'DF')
            else:
                pdf.rect(o, 60, 6, 6, 'D')
            o = o + 10
        #pdf.rect(90-2,60,nbrvariants*10-2,9)  #contourner la partie variants


    for k in range(nbr_choix):
        pdf.set_xy(coordinateChoixC1[0] + k * 5.9, coordinateChoixC1[1])
        pdf.cell(1, 1, "{}".format(Liste[k]), 0, 0, 'L')

    for i in range(0, nbr_qst):
        pdf.set_xy(coordinateQstC1[0], coordinateQstC1[1] + i * 5.9)
        if i < 9:
            pdf.cell(1, 1, "Q0{}".format(i + 1), 0, 0, 'L')
        if i >= 9:
            pdf.cell(1, 1, "Q{}".format(i + 1), 0, 0, 'L')
        for j in range(nbr_choix):
            pdf.rect(start_c1[0] + (j * 5.8), start_c1[1] + (i * 5.8), 4, 4)
        if (i == 19):
            break
    if nbr_qst <= 20:
        pdf.rect(start_c1[0] - 2, start_c1[1] - 2, nbr_choix * 3.8 + (nbr_choix + 1) * 2, nbr_qst * 3.8 + (nbr_qst + 1) * 2)
    else:
        pdf.rect(start_c1[0] - 2, start_c1[1] - 2, nbr_choix * 3.8 + (nbr_choix + 1) * 2, 20 * 3.8 + (20 + 1) * 2)

    nbr_qst = nbr_qst - 20

    if (nbr_qst > 0):
        for k in range(nbr_choix):
            pdf.set_xy(coordinateChoixC2[0] + k * 5.9, coordinateChoixC2[1])
            pdf.cell(1, 1, "{}".format(Liste[k]), 0, 0, 'L')
        for i in range(nbr_qst):
            pdf.set_xy(coordinateQstC2[0], coordinateQstC2[1] + i * 5.9)
            pdf.cell(1, 1, "Q{}".format(i + 20 + 1), 0, 0, 'L')
            for j in range(nbr_choix):
                pdf.rect(start_c2[0] + (j * 5.8), start_c2[1] + (i * 5.8), 4, 4)
            if (i == 19):
                break

        if nbr_qst <= 20:
            pdf.rect(start_c2[0] - 2, start_c2[1] - 2, nbr_choix * 3.8 + (nbr_choix + 1) * 2,
                     nbr_qst * 3.8 + (nbr_qst + 1) * 2)
        else:
            pdf.rect(start_c2[0] - 2, start_c2[1] - 2, nbr_choix * 3.8 + (nbr_choix + 1) * 2,
                     19 * 3.8 + (19 + 1) * 2)


    pdf.set_xy(60, 275)
    pdf.cell(1, 1, "Session | AU | Titre | Prof")
    idExam = 786904
    pdf.set_xy(170, 268)
    pdf.multi_cell(20, 7, str(idExam), border=0, align='C')
    #A = pdf.output(id+"Exam1.pdf",'S')
    #return A
    return pdf.output(id +"Exam2.pdf", 'F')

if __name__ == '__main__':
    nbrVariants=4
    nbr_qst=40
    nbr_choix=6
    id="titreid"
    pdf = FPDF('P', 'mm', 'A4')  # A4 equivalent au 210x297 mm
    #for i in range(nbrVariants):
        #pdf.setPage(i+1)
    create_QCM(id ,pdf, nbr_qst, nbr_choix, nbrVariants, 3) #i+1=Variant 1 2 3 ou 4
    A="titreidExam2.pdf"
    B="watermark.pdf"
    inputfile= open(A,'rb+')
    inputpdf= PyPDF2.PdfFileReader(inputfile)

    wmarkfile = open(B ,'rb')
    wmarkpdf = PyPDF2.PdfFileReader(wmarkfile)

    pdfpage= inputpdf.getPage(0)
    markpage=wmarkpdf.getPage(0)

    pdfpage.mergePage(markpage)
    output = PyPDF2.PdfFileWriter()
    output.addPage(pdfpage)

    #mergedfile="merge.pdf"
    #mergedfile=open(mergedfile, 'wb')
    output.write(inputfile)

    #mergedfile.close()
    inputfile.close()
    wmarkfile.close()




