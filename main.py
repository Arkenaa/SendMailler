#Telegram : t.me/tokyohq
#Discord : discord.gg/jCfVXtyS7J

import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import platform
    
def print_ascii_art():
    print("""                        
          ██████  ██▓███   ▄▄▄      ███▄ ▄███▓ ▄▄▄       ██▓ ██▓    ▓█████  ██▀███  
        ▒██    ▒ ▓██░  ██▒▒████▄   ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒    ▓█   ▀ ▓██ ▒ ██▒
        ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄ ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░    ▒███   ▓██ ░▄█ ▒
          ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░    ▒▓█  ▄ ▒██▀▀█▄  
        ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒░▒████▒░██▓ ▒██▒
        ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
        ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
        ░  ░  ░  ░░         ░   ▒  ░      ░     ░   ▒    ▒ ░  ░ ░      ░     ░░   ░ 
    """)

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def send_emails(smtp_server, port, email, password, sender_name, subject, html_path, email_list_path, emails_per_second):
    try:
        try:
            with open(html_path, 'r', encoding='utf-8') as html_file:
                html_content = html_file.read()
        except FileNotFoundError:
            print(f"Erreur : Le fichier HTML '{html_path}' est introuvable.")
            return
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier HTML : {str(e)}")
            return
        try:
            with open(email_list_path, 'r', encoding='utf-8') as email_file:
                emails = [line.strip() for line in email_file if line.strip()]
        except FileNotFoundError:
            print(f"Erreur : Le fichier contenant les emails '{email_list_path}' est introuvable.")
            return
        except Exception as e:
            print(f"Erreur lors de la lecture de la liste d'emails : {str(e)}")
            return

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(email, password)
        print(f"{os.getlogin()}@root - Connexion établie\n ⤷  Début du spam...")

        for recipient in emails:
            try:
                msg = MIMEMultipart()
                msg['From'] = sender_name
                msg['To'] = recipient
                msg['Subject'] = subject
                msg.attach(MIMEText(html_content, 'html'))
                server.sendmail(email, recipient, msg.as_string())

                print(f"{time.strftime('%H:%M:%S')} - Envoyé à {recipient}")

                time.sleep(1 / emails_per_second)

            except Exception as e:
                print(f"{time.strftime('%H:%M:%S')} - Erreur d'envoi à {recipient}: {str(e)}")

        server.quit()
        print("Spam terminé avec succès.")
    except Exception as e:
        print(f"Erreur générale : {str(e)}")

def main():
    while True:
        clear_console()
        print_ascii_art()
        print("   ┌─                                                                                  ─┐")
        print("   ├─ 1 - Launch Spam                           ┌─ By ArkenaDev                         │")
        print("   ├─ 2 - Quit                                  ├─ https://discord.gg/UtyK46J           │")
        print("   └────────────────────────────────────────────┴───────────────────────────────────────┘\n")

        choice = input(f"{os.getlogin()}@root - Entre ton choix  \n ⤷ ")

        if choice == "1":
            smtp_server = input(f"{os.getlogin()}@root - Entre le serveur SMTP  \n ⤷ ")
            port = input(f"{os.getlogin()}@root - Entre le port  \n ⤷ ")
            email = input(f"{os.getlogin()}@root - Entre l'email  \n ⤷ ")
            password = input(f"{os.getlogin()}@root - Entre le password  \n ⤷ ")
            sender_name = input(f"{os.getlogin()}@root - Entre le nom d'expéditeur  \n ⤷ ")
            subject = input(f"{os.getlogin()}@root - Entre l'objet du message  \n ⤷ ")
            html_path = input(f"{os.getlogin()}@root - Entre le chemin du fichier HTML  \n ⤷ ")
            email_list_path = input(f"{os.getlogin()}@root - Entre le chemin du fichier contenant les emails  \n ⤷ ")
            emails_per_second = float(input(f"{os.getlogin()}@root - Entre le nombre d'envois par seconde  \n ⤷ "))
            send_emails(smtp_server, port, email, password, sender_name, subject, html_path, email_list_path, emails_per_second)

        elif choice == "2":
            print("Bye !")
            break

        else:
            print("Choix invalide, choisi une option valide.")

if __name__ == "__main__":
    main()
