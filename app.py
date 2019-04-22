#python 3.7.0
#sqlite3
#tkinter8.6


from tkinter import *
import sqlite3
from tkinter import messagebox
v=Tk()
v.title("Pildoras App")
v.iconbitmap('unnamed-copia.ico')#---eliminate this line if you haven't the icon image-------
v.geometry("300x420+500+100")
v.resizable(width=False,height=False)

idvar=StringVar()
nombrevar=StringVar()
apellidovar=StringVar()
passwordvar=StringVar()
direccionvar=StringVar()

def crear_bbdd():
    try:
        con=sqlite3.connect('usuarios.db')
        cur=con.cursor()
        cur.execute('''CREATE TABLE DATOUSUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(30),
                   PASSWORD VARCHAR(15),APELLIDO VACHAR(30),DIRECCION VARCHAR(40),COMENTARIO VARCHAR(120))''')
        messagebox.showinfo("Mensaje","Base de datos creada con exito.")
    except:
        messagebox.showinfo("Error","La Base de datos ya existe")
    cur.close()
    con.close()
def read():
    num=idvar.get()
    try:
        read_bbdd(num)
    except:
        messagebox.showwarning("Error","Numero de Id incorrecto.")
def read_bbdd(id_num):
        
    con=sqlite3.connect('usuarios.db')
    cur=con.cursor()
    cur.execute('''SELECT * FROM DATOUSUARIOS WHERE ID= ?''',(id_num,))
    salida=cur.fetchall()
    cur.close()
    con.close()
    desplegar_datos(salida)
    return salida

def update_usuario():
    id_=idvar.get()
    nom=nombrevar.get()
    passw=passwordvar.get()
    ape=apellidovar.get()
    dire=direccionvar.get()
    comen=come.get("1.0",END)
    info=(nom,passw,ape,dire,comen,id_)    
    con=sqlite3.connect('usuarios.db')
    cur=con.cursor()
    cur.execute('''UPDATE DATOUSUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIO=? WHERE ID=?''',(info))
    con.commit()
    cur.close()
    con.close()
    messagebox.showinfo("Mensaje","Registro Actualizado con exito.")
    borrar_campos()
               
def pre_crear_usuario():    
    nom=nombrevar.get()
    passw=passwordvar.get()
    ape=apellidovar.get()
    dire=direccionvar.get()
    comen=come.get("1.0",END)
    info=(nom,passw,ape,dire,comen)
    crear_usuario(info)
    
def crear_usuario(info):
    con=sqlite3.connect('usuarios.db')
    cur=con.cursor()
    cur.execute('''INSERT INTO DATOUSUARIOS (NOMBRE,PASSWORD,APELLIDO,DIRECCION,COMENTARIO)VALUES(?,?,?,?,?)''',(info))
    con.commit()
    cur.close()
    con.close()
    messagebox.showinfo("Mensaje","Registro Guardado con exito.")
    borrar_campos()
    
def desplegar_datos(dato):
    lista=list(dato[0])
    come.delete('1.0',END)
    idvar.set(lista[0])
    nombrevar.set(lista[1])
    passwordvar.set(lista[2])
    apellidovar.set(lista[3])
    direccionvar.set(lista[4])
    come.insert(INSERT,lista[5])
    
def borrar_campos():
    idvar.set('')
    nombrevar.set('')
    passwordvar.set('')
    apellidovar.set('')
    direccionvar.set('')
    come.delete('1.0',END)
def pre_delete_usuario():
    dato=idvar.get()
    delete_usuario(dato)
       
def delete_usuario(id_num):
    con=sqlite3.connect('usuarios.db')
    cur=con.cursor()
    cur.execute('''DELETE FROM DATOUSUARIOS  WHERE ID= ?''',(id_num,))
    con.commit()
    cur.close()
    con.close()
    borrar_campos()
    messagebox.showinfo("Mensaje","Registro Eliminado con exito.")
    
def salir():
    if messagebox.askquestion('Salir','Desea salir de la aplicacion?')== 'yes':
        v.destroy()
    
def licencia():
    messagebox.showinfo("Licencia","Trabajo practico del curso de python de PILDORAS INFORMATICAS.")
    
#----barra de manu------
barra=Menu(v)
v.config(menu=barra,bg="#ccffff")

bd_menu=Menu(barra,tearoff=0)
bd_menu.add_command(label="Crear BBDD",command=crear_bbdd)
bd_menu.add_command(label="Salir",command=salir)

borrar_menu=Menu(barra, tearoff=0)
borrar_menu.add_command(label='Borrar campos',command=borrar_campos)

crud_menu=Menu(barra, tearoff=0)
crud_menu.add_command(label='Crear',command=pre_crear_usuario)
crud_menu.add_command(label='Leer',command=read)
crud_menu.add_command(label='Actualizar',command=update_usuario)
crud_menu.add_command(label='Borrar',command=pre_delete_usuario)

ayuda_menu=Menu(barra, tearoff=0)
ayuda_menu.add_command(label='Licencia',command=licencia)
ayuda_menu.add_command(label='Ayuda')

barra.add_cascade(label="BBDD", menu=bd_menu)
barra.add_cascade(label="Borrar", menu=borrar_menu)
barra.add_cascade(label="CRUD", menu=crud_menu)
barra.add_cascade(label="Ayuda", menu=ayuda_menu)

#cuestionario-----------
#------------labels-----------
id_lbl=Label(v,text="Id:",bg="#ccffff").place(x=85, y=20)
nombre_lbl=Label(v,text='Nombre:',bg="#ccffff").place(x=52, y=60)
password_lbl=Label(v,text='Password:',bg="#ccffff").place(x=45, y=100)
apellido_lbl=Label(v,text='Apellido:',bg="#ccffff").place(x=52, y=140)
direccion_lbl=Label(v,text='Direccion:',bg="#ccffff").place(x=49, y=180)
comentario_lbl=Label(v,text='Comentario:',bg="#ccffff").place(x=40, y=265)
#-----------entrys----------------
id_en=Entry(v,textvariable=idvar).place(x=140, y=20)
nombre_en=Entry(v,fg="red",justify=RIGHT,textvariable=nombrevar).place(x=140, y=60)
password_en=Entry(v,show="*",textvariable=passwordvar).place(x=140, y=100)
apellido_en=Entry(v,textvariable=apellidovar).place(x=140, y=140)
direccion_en=Entry(v,textvariable=direccionvar).place(x=140, y=180)
mf=Frame(v,bg="blue")
#-----area de texto----------
mf.place(x=140,y=220)
come=Text(mf ,width=15, height=7)
come.grid(row=1,column=1)
scroll=Scrollbar(mf,command=come.yview)
scroll.grid(row=1,column=2,sticky="nsew")

#-------------butons---------------
    
create_bt=Button(v,text='Create',command=pre_crear_usuario).place(x=20, y=365)
read_bt=Button(v,text=' Read ',command=read).place(x=92, y=365)
update_bt=Button(v,text='Update',command=update_usuario).place(x=164, y=365)
delete_bt=Button(v,text="Delete",command=pre_delete_usuario).place(x=236, y=365)

v.mainloop()
