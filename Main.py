import pyautogui
import time

def vote(personal_data_list, interval):
    #Abrindo o navegador
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Fire') #Pesquisa navegador de preferencia
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    
    #Abrindo pagina de votação    
    pyautogui.write('Pagina de interesse')#Substituir de acordo com a pagia de interesse
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    
    while True:
        for personal_data in personal_data_list:
            try:
                #Altere o preenchimento de formulario conforme o que informar na pagina
                #Substituir as coordenadas dos clicks conforme a pagina, utilize o codigo encontrarCursor.py
                print(f"Preenchendo o formulário para {personal_data['pessoa']}")
                
                #Preenchimento email
                pyautogui.click(x=866, y=331) 
                pyautogui.write(personal_data["email"])
                time.sleep(1)
                
                #Preenchimento nome da empresa
                pyautogui.click(x=868, y=408)  
                pyautogui.write(personal_data["nome"])
                time.sleep(1)
                
                #Preenchimento da pessoa
                pyautogui.click(x=891, y=476)  
                pyautogui.write(personal_data["pessoa"])
                time.sleep(1)
                
                #Preenchimento da UF
                pyautogui.click(x=927, y=544)  
                pyautogui.write(personal_data["uf"])
                pyautogui.press('enter')
                time.sleep(1)
                
                #Botão de confirma
                pyautogui.click(x=950, y=605)  
                
                #Tempo para carregamento
                print("Esperando a página de confirmação carregar")
                time.sleep(5)  
                
                #Confirmação dos dados e indentificação de logista
                pyautogui.click(x=300, y=526)
                time.sleep(1)
                pyautogui.click(x=293, y=679)
                time.sleep(1)
                pyautogui.click(x=435, y=656)
                time.sleep(1)
                
                #Primeiro voto(esquema diferente da pagina)
                pyautogui.click(x=341, y=394)
                pyautogui.write('Teste')
                time.sleep(1)
                pyautogui.click(x=304, y=484)
                time.sleep(1)
                
                #Votação direta 4x
                for i in range(3):
                    time.sleep(2)
                    pyautogui.click(x=341, y=394)
                    pyautogui.write('Nome do candidato')
                    time.sleep(1)
                    pyautogui.click(x=445, y=481)

                #Finalizando voto
                print("Esperando a página de votação carregar")
                time.sleep(5) 
                pyautogui.click(x=810, y=581) 
                time.sleep(5)
                
                print(f"Voto realizado com sucesso para {personal_data['pessoa']}!")
                pyautogui.click(x=694, y=73)
                pyautogui.write('https://www.revenda.com.br/pesquisas/pead/1/identifique-se')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(3)
                
            except Exception as e:
                print(f"Ocorreu um erro para {personal_data['pessoa']}: {e}") 
            
            print(f"Aguardando {interval} segundos antes de continuar")
            time.sleep(interval) 

#Lista com dados para serem utilizados como cadastro de voto.
personal_data_list = [
    {"email": "pessoa1@example.com", "nome": "Estabelecimento1", "pessoa": "Pessoa1", "uf": "Bahia"},
    {"email": "pessoa2@example.com", "nome": "Estabelecimento2", "pessoa": "Pessoa2", "uf": "Bahia"},
    {"email": "pessoa3@example.com", "nome": "Estabelecimento3", "pessoa": "Pessoa3", "uf": "Bahia"},
    {"email": "pessoa4@example.com", "nome": "Estabelecimento4", "pessoa": "Pessoa4", "uf": "Bahia"},
    {"email": "pessoa5@example.com", "nome": "Estabelecimento5", "pessoa": "Pessoa5", "uf": "Bahia"},
    {"email": "pessoa6@example.com", "nome": "Estabelecimento6", "pessoa": "Pessoa6", "uf": "Bahia"},
    {"email": "pessoa7@example.com", "nome": "Estabelecimento7", "pessoa": "Pessoa7", "uf": "Bahia"},
    {"email": "pessoa8@example.com", "nome": "Estabelecimento8", "pessoa": "Pessoa8", "uf": "Bahia"},
    {"email": "pessoa9@example.com", "nome": "Estabelecimento9", "pessoa": "Pessoa9", "uf": "Bahia"},
    {"email": "pessoa10@example.com", "nome": "Estabelecimento10", "pessoa": "Pessoa10", "uf": "Bahia"},
    {"email": "pessoa11@example.com", "nome": "Estabelecimento11", "pessoa": "Pessoa11", "uf": "Bahia"},
    {"email": "pessoa12@example.com", "nome": "Estabelecimento12", "pessoa": "Pessoa12", "uf": "Bahia"},
    {"email": "pessoa13@example.com", "nome": "Estabelecimento13", "pessoa": "Pessoa13", "uf": "Bahia"},
    {"email": "pessoa14@example.com", "nome": "Estabelecimento14", "pessoa": "Pessoa14", "uf": "Bahia"},
    {"email": "pessoa15@example.com", "nome": "Estabelecimento15", "pessoa": "Pessoa15", "uf": "Bahia"},
    {"email": "pessoa16@example.com", "nome": "Estabelecimento16", "pessoa": "Pessoa16", "uf": "Bahia"},
    {"email": "pessoa17@example.com", "nome": "Estabelecimento17", "pessoa": "Pessoa17", "uf": "Bahia"},
    {"email": "pessoa18@example.com", "nome": "Estabelecimento18", "pessoa": "Pessoa18", "uf": "Bahia"},
    {"email": "pessoa19@example.com", "nome": "Estabelecimento19", "pessoa": "Pessoa19", "uf": "Bahia"},
    {"email": "pessoa20@example.com", "nome": "Estabelecimento20", "pessoa": "Pessoa20", "uf": "Bahia"},
]
vote_interval = 20  

vote(personal_data_list, vote_interval)
