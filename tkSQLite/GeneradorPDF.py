from fpdf import FPDF #se importa libreria para generar el archivo 
from Controlador import * # se importa la clase controlador 

objControl2= Controlador() #se crea el segundo objeto controlador 

class GeneradorPDF(FPDF):
    
    def header(self): #Metodo para fijar el encabezado del PFD 
        self.set_font("Times","BU",14) #parametros de tipologia para el titulo del encabezado 
        self.cell(0,10,"Reporte de Usuarios",0,1,"C")
        
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial","I",8)
        self.cell(0,10,"Pagina %s"%self.page_no(),0,0,'C')
        
    def chapter_body(self):
        self.set_font("Arial","I",10)
        self.set_fill_color(255,159,51)
        listaUsuarios= objControl2.listaUsuariosBD()
        self.multi_cell(100,10,"ID:  "+"Usuario:  "+"Correo:  ",1,'C',1)
        
        for i in listaUsuarios:
            self.multi_cell(100,10, str(i[0])+" "+str([1])+" "+str([2]),1,'C',1)