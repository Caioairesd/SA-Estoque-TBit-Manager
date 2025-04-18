import tkinter as tk
from tkinter import messagebox
from tkinter import *
from database_geral import tbit_db
from menu_adm import menu_admin
from menu_user import menu_usuario
from database_geral import __init__

class login_menu:
    def __init__(self,root):
        tbit_db.__init__(self)
        

        self.root = root
        self.root.title("TBit Manager by TerraBytes") 
        self.create_widget()
        self.root.geometry("600x300")
        self.root.resizable( width = False, height = False)
        pass

    def create_widget(self):
        self.left_frame = Frame(root, width=200, height=300, bg="#003366", relief="raise") # Cria um frame à esquerda
        self.left_frame.pack(side=LEFT) # Posiciona o frame à esquerda

        self.right_frame = Frame(root, width=400, height=300, bg="#003366", relief="raise") # Cria um frame à esquerda
        self.right_frame.pack(side=RIGHT) # Posiciona o frame à esquerda

        #logo = PhotoImage(file='icon/tbit_logo_64x.png')
        #self.logo_label = Label(self.left_frame, image=logo) # Cria uma label que carrega a logo
        #self.logo_label.place(x=50, y=100) # Posiciona o label no frame esquerdo

        self.usuario_label = Label(self.right_frame, text="Usuario:", font=("Times New Roman", 20), bg="#00284d", fg='white') # Cria um label para o usuario
        self.usuario_label.place(x=10, y=105) # Posiciona o label o frame direito

        self.usuario_entry = tk.Entry(self.right_frame, width=30) # Cria um campo de entrada para o usuario
        self.usuario_entry.place(x=120, y=115) # Posiciona o campo de entrada

        self.senha_label = Label(self.right_frame, text="Senha:", font=("", 20), bg="#00284d", fg="White") # Cria um label para a senha
        self.senha_label.place(x=10, y=150) # Posiciona o label no frame direito

        self.senha_entry = tk.Entry(self.right_frame, width=30, show="*") # Cria um campo de entrada para a senha
        self.senha_entry.place(x=120, y=165)       
        
        self.login_button = tk.Button(self.right_frame, text="LOGIN", width=15, command=self.login_user) # Cria um botao de login
        self.login_button.place(x=80, y=225)

    def login_user(self):
        

        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        
        if usuario == 'ADM' and senha == '2025':
                
            self.root.destroy()  
            self.abrir_menu_admin()
            return
        else:
            try:
                database = tbit_db()
                cursor = database.cursor
                cursor.execute('SELECT * FROM funcionario WHERE usuario_funcionario = %s AND senha_funcionario = %s' ,(usuario, senha,))
            

                verify_login = cursor.fetchone()

            
                if verify_login:
                    
                    messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado. Bem Vindo!")

                    self.root.destroy()
                    self.abrir_menu_user()

                else:
                    messagebox.showinfo(title="INFO LOGIN", message="Acesso Negado. Verifique se está cadastrado no Sistema!")
                
            except Exception as e:
                messagebox.showerror(title="Erro", message=f"Ocorreu um erro: {str(e)}")
    
    def abrir_menu_admin(self):
        janela_admin = tk.Tk()  
        app = menu_admin(janela_admin) 

    def abrir_menu_user(self):
        janela_user = tk.Tk()
        app = menu_usuario(janela_user)
        
    
if __name__ == '__main__':
    root = tk.Tk()
    app = login_menu(root)
    root.mainloop()