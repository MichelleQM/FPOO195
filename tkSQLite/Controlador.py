from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    def conexion(self):
        try:
            conex=sqlite3.connect("C:/Users/DEll Gamer G3/Desktop/FPOO195/tkSQLite/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    
    def encriptapass(self,cont):
        passPlana=cont
        passPlana= passPlana.encode() #Se convierte la contrasena a boolean 
        sal= bcrypt.gensalt()#Se genera la contrasena generada en bits 
        passHash= bcrypt.hashpw(passPlana,sal)#encripta la contrasena 
        return passHash
    
    def insertUsuario(self,nom,corr,cont):
        conexion= self.conexion() #Se declara la variable a la cual se le vincula el metodo que conecta a la base de datos 
        if (nom=="" or corr=="" or cont==""):
            messagebox.showwarning("Cuidado","Inputs vacios")
            conexion.close()
            
        else:
            cursor = conexion.cursor()
            conH= self.encriptapass(cont)
            datos=(nom,corr,conH)
            sqlInsert="insert into tbUsuarios(nombre,correo,contra) values(?,?,?)"
            
            cursor.execute(sqlInsert,datos) #se insertan los datos y con el cursor se crea la conexion 
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito","Eso tilin!!!")
            
            
    #Metodo para la busqueda de un usuario en BD mediante su ID
    def buscarUsuario(self,id):
        conex=self.conexion()
        
        if(id==''):
            messagebox.showwarning("Cuidado","Inputs vacios")
            conex.close()
        else:
            try:
                cursor=conex.cursor()
                sqlSelect="select * from tbUsuarios where id="+id
                cursor.execute(sqlSelect)
                usuario=cursor.fetchall()
                conex.close()
                return usuario
            except sqlite3.OperationalError:
                print('No se pudo ejecutar la busqueda')