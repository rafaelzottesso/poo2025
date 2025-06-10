import os

email = "rafael.zottesso@ifpr.edu.br"

msg_commit = ""
while(len(msg_commit)<10):
    msg_commit = input("Mensagem do commit (maior que 10 caracateres): ")

comando = f"git config user.email \"{email}\""
os.system(comando)

comando = "git add *"
os.system(comando)

comando = "git commit -m \"{msg_commit}\""
os.system(comando)

comando = "git push"
os.system(comando)
