import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Nombre del branch
branch = os.getenv('BRANCH_NAME', 'unknown')
print(f"La rama actual es: {branch}")

# Mensaje del commit
commit_message = os.getenv('COMMIT_MESSAGE', 'Sin mensaje')
print(f"Mensaje del commit: {commit_message}")

# Configuración de IONOS MX
smtp_server = "smtp.ionos.mx"
smtp_port = 587
username = "correoPractica2@icaaviation.com"
password = "correoPractica2."

# Crear mensaje
msg = MIMEMultipart()
msg["From"] = username
msg["To"] = "jpdelmuro@gmail.com"
msg["Subject"] = f"Cambios en la rama {branch}"
msg.attach(MIMEText(f"Hola\nSe hicieron los siguientes cambios en la rama {branch}\nMensaje del commit:\n{commit_message}", "plain"))

try:
    print("Conectando al servidor...")
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.set_debuglevel(1)  # 🐞 Imprime información del proceso SMTP
        server.starttls()  # ⚠️ IMPORTANTE: Esto activa TLS
        server.login(username, password)  # Aquí es donde suele fallar si hay error 535
        server.send_message(msg)
        print("✅ Correo enviado correctamente.")
except Exception as e:
    print(f"❌ Error al enviar el correo: {e}")
