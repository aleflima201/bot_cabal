import customtkinter as ctk
import pyodbc

ctk.set_appearance_mode('dark')

#função de validação de usuario
def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    #driver - driver
    #Server - Servidor
    #Database - Nome do banco de dados
    conexao = pyodbc.connect("drivers={SQLite3 ODBC Driver}, Server=localhost, Database=Tabela_Usuario.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Clients WHERE Usuario = ? AND Senha = ?", (usuario, senha))
    conectado = cursor.fetchone()
    if conectado:
        app.destroy()
    else:
        label_valid.configure(text="Usuário ou Senha incorreto!", text_color='red')
    


#tela de login
app = ctk.CTk()
app.title('Sistema de login')
app.geometry('300x300')

#label texto do usuario
label_usuario = ctk.CTkLabel(app, text="Digite o Usuario")
label_usuario.pack(pady=10)

#Entry texto do usuario
entry_usuario = ctk.CTkEntry(app, placeholder_text="Digite o Usuario")
entry_usuario.pack(pady=1)

#label texto da senha
label_senha = ctk.CTkLabel(app, text="Digite a Senha")
label_senha.pack(pady=10)

#Entry texto do usuario
entry_senha = ctk.CTkEntry(app, placeholder_text="Digite a Senha", show='*')
entry_senha.pack(pady=1)

checkbox = ctk.CTkCheckBox(app, text="Lembrar Login")

#botão de conferir login
botao = ctk.CTkButton(app, text="Login", command=validar_login)
botao.pack(pady=10)

#label texto de validação do login
label_valid = ctk.CTkLabel(app, text="")
label_valid.pack(pady=10)


app.mainloop()