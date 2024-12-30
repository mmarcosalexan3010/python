import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox


def enviar_email():
    # Obtendo dados da interface
    remetente = entry_remetente.get()
    senha = entry_senha.get()
    destinatario = entry_destinatario.get()
    assunto = entry_assunto.get()
    mensagem = text_mensagem.get("1.0", tk.END).strip()

    if not remetente or not senha or not destinatario or not assunto or not mensagem:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    try:
        # Configurar o e-mail
        email = MIMEMultipart()
        email["From"] = remetente
        email["To"] = destinatario
        email["Subject"] = assunto
        email.attach(MIMEText(mensagem, "plain"))

        # Conectar ao servidor SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Ativar criptografia
            server.login(remetente, senha)  # Login no e-mail
            server.sendmail(remetente, destinatario, email.as_string())

        messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Erro de Autenticação", "Falha no login. Verifique e-mail e senha.")
    except smtplib.SMTPRecipientsRefused:
        messagebox.showerror("Erro", "O destinatário do e-mail é inválido.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar e-mail:\n{e}")


# Interface Gráfica com Tkinter
janela = tk.Tk()
janela.title("Envio de E-mails")

# Configuração dos campos
tk.Label(janela, text="E-mail do remetente:").grid(row=0, column=0, sticky="w")
entry_remetente = tk.Entry(janela, width=40)
entry_remetente.grid(row=0, column=1)

tk.Label(janela, text="Senha do remetente:").grid(row=1, column=0, sticky="w")
entry_senha = tk.Entry(janela, show="*", width=40)
entry_senha.grid(row=1, column=1)

tk.Label(janela, text="E-mail do destinatário:").grid(row=2, column=0, sticky="w")
entry_destinatario = tk.Entry(janela, width=40)
entry_destinatario.grid(row=2, column=1)

tk.Label(janela, text="Assunto:").grid(row=3, column=0, sticky="w")
entry_assunto = tk.Entry(janela, width=40)
entry_assunto.grid(row=3, column=1)

tk.Label(janela, text="Mensagem:").grid(row=4, column=0, sticky="nw")
text_mensagem = tk.Text(janela, width=50, height=10)
text_mensagem.grid(row=4, column=1)

# Botão para enviar o e-mail
btn_enviar = tk.Button(janela, text="Enviar", command=enviar_email)
btn_enviar.grid(row=5, column=1, sticky="e")

# Iniciar o loop da janela
janela.mainloop()
