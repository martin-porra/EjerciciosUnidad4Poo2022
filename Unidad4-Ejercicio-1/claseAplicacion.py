from tkinter import *
from tkinter import ttk, messagebox, font 

class Aplicacion():
    __ventana=None
    __altura=None
    __peso=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('401x181')
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.resizable(0,0)

        self.__altura=StringVar()
        self.__peso=StringVar()
        self.resultado=StringVar()
        self.composicion=StringVar()

        mainframe = Frame(self.__ventana,bg = 'white')
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=0)
        mainframe.rowconfigure(0,weight=0)
      

        fuente = font.Font(weight='bold')
        fuente2 = font.Font(weight='bold',size = 9)

        self.tituloLbl=Label(mainframe,text="Calculadora de IMC",font=fuente,bg ='#d8d8e0').grid(column=0,row=0,columnspan=5)
        self.alturaLbl=Label(mainframe,text='Altura:',fg='#696871',bg='white',font=fuente2).grid(column=0,row=1)
        self.pesoLbl=Label(mainframe,text='Peso:',fg='#696871',bg='white',font=fuente2).grid(column=0,row=2)
        self.cmLbl=Label(mainframe,text='cm',fg='#696871',bg='#d8d8e0').grid(column=2,row=1)
        self.kgLbl=Label(mainframe,text='kg',fg='#696871',bg ='#d8d8e0').grid(column=2,row=2)
        self.boton1=Button(mainframe,text='Calcular',width=17,fg='white',bg='#5ab359',command=self.calcular,borderwidth=0).grid(column=1,row=4,sticky=W)
        self.botonn2=Button(mainframe,text='Limpiar',width=17,fg='white',bg='#5ab359',command=self.limpiar,borderwidth=0).grid(column=1,row=4,sticky=E)       

        
        self.alturaEntry=Entry(mainframe,width=50,textvariable=self.__altura)
        self.pesoEntry=Entry(mainframe,width=50,textvariable=self.__peso)

        self.alturaEntry.grid(column=1,row=1)
        self.pesoEntry.grid(column=1,row=2)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5,pady=5)

        self.masaLbl=Label(mainframe,text='Tu índice de Masa Corporal (IMC) es ',bg='#c7e4ca',fg='#56865b').grid(column=1,row=5,sticky=SW,padx=0,pady=5)
        self.masaLbl2=Label(mainframe,textvariable=self.resultado,bg='#c7e4ca',fg='#56865b',font=fuente2).grid(column=1,row=5,sticky=SE,padx=0,pady=5)
        self.masaLbl3=Label(mainframe,textvariable=self.composicion,bg='#c7e4ca',fg='#56865b').grid(column=1,row=6)

        self.alturaEntry.focus() 
        self.__ventana.mainloop()

    def calcular(self):
        try:
            assert float(self.pesoEntry.get())>0 and float(self.alturaEntry.get())>0
            peso = float(self.pesoEntry.get())
            altura = float(self.alturaEntry.get())
            imc = peso / (altura / 100)**2
            self.resultado.set('%.2f Kg/m2' %(imc))
            if 0<=imc<18.5:
                self.composicion.set('Peso inferior al normal')
            elif 18.5<=imc<=24.9:
                self.composicion.set('Normal')
            elif 25.0<=imc<=29.9:
                self.composicion.set('Peso superior al normal')
            elif imc>30.0:
                self.composicion.set('Obesidad')             
            
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')

    def limpiar(self):
        self.__altura.set('')
        self.__peso.set('')
        self.resultado.set('')
        self.composicion.set('')
        self.alturaEntry.focus()