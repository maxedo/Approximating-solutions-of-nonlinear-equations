import numpy as np
from tkinter import *
from sympy import *
from scipy.optimize import minimize_scalar, fsolve
import metode as m
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt



def matplotCanvas(root,x,y):
    f=Figure(figsize=(5,5),dpi=50)
    a=f.add_subplot(111)
    a.plot(x,y)
    canvas=FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().place(x=600,y=300)


#Frame-ul
root=Tk()
root.geometry("900x600")
root.title("Solutii ecuatii neliniare")
root.config(background="#0459e0")

#input-uri
prim_var_lab=Label(root, text="A=", font=('Arial',20,'bold'),bg='#0459e0')
prim_var_lab.place(x=0,y=30)
sec_var_lab=Label(root, text="B=", font=('Arial',20,'bold'),bg='#0459e0')
sec_var_lab.place(x=0,y=70)
thr_var_lab=Label(root, text="f(x)=", font=('Arial',20,'bold'),bg='#0459e0')
thr_var_lab.place(x=0,y=110)

e1=Entry(root,width=20)
e1.place(x=70,y=40)
e2=Entry(root,width=20)
e2.place(x=70,y=80)
e3=Entry(root,width=20)
e3.place(x=70,y=120)

#radiobuttons
fr=LabelFrame(root,text='Alegeti optiunea dorita',padx=20,bg='#0459e0')
fr.place(x=250,y=20)
metode=["bisectie","coarda","tangenta","principiul contractiilor"]
x=IntVar()
for i in range(len(metode)):
    radb=Radiobutton(fr,text=metode[i],variable=x,value=i,padx=25,bg='#0459e0') 
    radb.pack(anchor=W)
    
#input-uri2
fth_var_lab=Label(root,text='Criterii de oprire',font=('Arial',20,'bold','underline'),bg='#0459e0')
fth_var_lab.place(x=10,y=230)
fif_var_lab=Label(root,text='Numarul de iteratii=',font=('Arial',18,'bold'),bg='#0459e0')
fif_var_lab.place(x=10,y=280)
six_var_lab=Label(root,text='E(n)=',font=('Arial',18,'bold'),bg='#0459e0')
six_var_lab.place(x=10,y=320)
e4=Entry(root,width=20)
e4.place(x=240,y=290)
e5=Entry(root,width=20)
e5.place(x=80,y=330)



#Rezultate
svt_var_lab=Label(root,text='Valoarea aproximativa:',font=('Arial',13,'bold'),bg='#0459e0')
svt_var_lab.place(x=500,y=25)
eig_var_lab=Label(root,text='Valoare eroare:',font=('Arial',13,'bold'),bg='#0459e0')
eig_var_lab.place(x=500,y=60)
e6=Entry(root,width=20)     #rezultat valoare
e6.place(x=700,y=30)
e7=Entry(root,width=20)     #rezultat eroare
e7.place(x=700,y=65)



warning=Label(root,text='',bg='#0459e0')
warning.place(x=10,y=580)

#buton
def click():
    warning.config(text="")
    e6.delete(0,"end")
    e7.delete(0,"end")
    try:
        a=int(e1.get())
        a2=a
        b=int(e2.get())
        b2=b
        f=e3.get()
        n=int(e4.get())
        err=float(e5.get())
        o=f
        q=Symbol('x')
        o=lambdify(q,o)
        x_val =np.linspace(a,b,n)
        
        if a<b:
            if (x.get()==0):
                r=m.bisectie_it(f,a,b,n)
                print(str(r))
                e6.insert(0,str(r))
                r2=m.bisectie_er(f,a2,b2,err)
                print(str(r2))
                e7.insert(0,str(r2))
                matplotCanvas(root,x_val,o(x_val))

                
            if(x.get()==1):
                rc=m.coarda_err(f,a2,b2,err)
                print(str(rc))
                e7.insert(0,str(rc))
                rc2=m.coarda_itr(f,a,b,n)
                print(str(rc2))
                e6.insert(0,str(rc2))
                matplotCanvas(root,x_val,o(x_val))
                
            if(x.get()==2):
                rt=m.tangenta_iter(f, a, b, n)
                print(str(rt))
                e6.insert(0,str(rt))
                rt2=m.tangenta_eroare(f, a2, b2, err)
                print(str(rt2))
                e7.insert(0,str(rt2))
                matplotCanvas(root,x_val,o(x_val))
                
            if(x.get()==3):
                rcon=m.contractii_itr(f,a,b,1.5,n)
                print(str(rcon))
                e6.insert(0,str(rcon))
                rcon2=m.contractii_err(f,a2,b2,1.5,err)
                print(str(rcon2))
                e7.insert(0,str(rcon2))
                matplotCanvas(root,x_val,o(x_val))
            
        else:
            warning.config(text="A trebuie sa fie mai mare decat B.Introduceti alte numere.")
            
    except ValueError:
        warning.config(text="Nu ati introdus numere!Incercati din nou.")

button=Button(root, text='Calculeaza',font=('Comic sans',30),command=click)
button.place(x=20,y=500)









root.mainloop()