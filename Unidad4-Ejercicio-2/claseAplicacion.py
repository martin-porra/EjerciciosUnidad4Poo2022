from tkinter import *
from tkinter import ttk, font, messagebox

class Aplicacion():
    __ventana = None
    __precioBase = None
    __valor =  None

    def calcular(self):
        try:
            IVA = float(self.__valor.get())
            precio_base = float(self.precioEntry.get())
            if precio_base > 0:
                self.precioIVA.set(precio_base + (precio_base * (IVA/100)))
                self.IVA.set(precio_base * (IVA/100))
            else:
                messagebox.showerror(title = 'Error de valor', message = 'Debe ingresar un pecio superio a 0 pesos')    
            
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')
            self.precioEntry.set('')
            self.precioEntry.focus()

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('341x300')
        self.__ventana.title('Cálculo de IVA')
        self.__ventana.resizable(0,0)
        self.__precioBase = StringVar()
        self.IVA = StringVar()
        self.precioIVA = StringVar()
        self.__valor = StringVar()
        mainframe = Frame(self.__ventana)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=2)
        mainframe.rowconfigure(0, weight=2)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.tituloLbl = Label(mainframe, text = "Cálculo de IVA", font = 'bold')
        self.tituloLbl.grid(row = 1, column = 3, sticky = S)
        self.precioLbl = Label(mainframe, text="Precio sin IVA:",font='bold').grid(row = 2, column = 2,sticky = W)
        self.boton1 = ttk.Radiobutton(mainframe,text = 'IVA 21%', variable = self.__valor, value = 21)
        self.boton1.grid(row = 3, column =2, sticky =W)
        self.boton2 = ttk.Radiobutton(mainframe,text = 'IVA 10.5%', variable =self.__valor, value = 10.5)
        self.boton2.grid(row = 4, column =2, sticky =W)
        self.ivalbl = Label(mainframe, text="IVA:",font='bold').grid(row = 5, column = 2,sticky = W)
        self.precioIVAlbl = Label(mainframe, text="Precio con IVA:",font='bold').grid(row = 6, column = 2,sticky = W)
        self.precioEntry = Entry(mainframe, width= 7, textvariable = self.__precioBase)
        self.precioEntry.grid(column=4, row=2, sticky=(W, E))
        self.IVAEntry = Entry(mainframe, width= 7, textvariable = self.IVA)
        self.IVAEntry.grid(column=4, row=5, sticky=(W, E))
        self.precioIVAEntry = Entry(mainframe, width= 7, textvariable = self.precioIVA)
        self.precioIVAEntry.grid(column=4, row=6, sticky=(W, E))
        self.boton3 = Button(mainframe, text="Calcular", command = self.calcular).grid(column=2, row=7, sticky=W)
        self.boton4 = Button(mainframe, text='Salir', command=self.__ventana.destroy, fg='black', bg = '#F85939').grid(column=4, row=7,sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=10, pady=10)

        self.precioEntry.focus()
        self.__ventana.mainloop()
