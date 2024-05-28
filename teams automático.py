import win32com.client as win32                                
import time                                                    

#parte do envio de email

outlook = win32.Dispatch('outlook.application')                 

mail = outlook.CreateItem(0)                           

destinatario = input("digite o email do destinatario:")
mail.to = destinatario

mail.Subject = 'FEEDBACK GLPI'

mensagem = '''
<br>Olá caro colaborador!
<br>
<br>Verificamos aqui que você possui avaliações pendentes na nossa plataforma de chamados (id Chamado (#816) - Liberação de Sites - Jurídico - GLPI - Roberto), por favor, envie-nos um feedback.
<br>
<br>
Atenciosamente Equipe de T.I 
<br>
<br>
<br>[MENSAGEM AUTOMÁTICA]<br> '''

mail.HTMLBody = mensagem
mail.send()
time.sleep(3)

print('Email enviado com sucesso!')


#ENVIO DE EMAIL PARA DESTINATÁRIO DIFERENTE


outlook = win32.Dispatch('outlook.application')                          

mail = outlook.CreateItem(0)                                             

destinatario = input("digite o email do segundo destinatario:")          
mail.to = destinatario                                       
mail.Subject = 'FEEDBACK GLPI'                               

mensagem = '''
<br>Bom dia!
<br>
<br>Verificamos aqui que você possui avaliações pendentes na nossa plataforma de chamados (id Chamado (#816) - Liberação de Sites - Jurídico - GLPI - Roberto), por favor, envie-nos um feedback.
<br>
<br> 
<br>
<br>[MENSAGEM AUTOMÁTICA]<br> '''                               

mail.HTMLBody = mensagem                                        
mail.Send()                                                    
time.sleep(3)
print("Email enviado com sucesso!")                             
