from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def vote(driver, url, personal_data, candidate_name, interval):
    while True:
        try:
            driver.get(url)
            
            # Preencha o formulário com dados pessoais
            for field_name, value in personal_data.items():
                field = driver.find_element(By.NAME, field_name)
                field.send_keys(value)
            
            # Enviar o formulário de dados pessoais
            submit_button = driver.find_element(By.NAME, "submit_personal_data")
            submit_button.click()
            
            time.sleep(2)  # Aguarde a página de confirmação carregar
            
            # Clique no botão de confirmação
            confirm_button = driver.find_element(By.NAME, "confirm")
            confirm_button.click()
            
            time.sleep(2)  # Aguarde a página de votação carregar
            
            # Insira o nome do candidato no campo de texto
            candidate_field = driver.find_element(By.NAME, "candidate_name")
            candidate_field.send_keys(candidate_name)
            
            # Confirmar o voto
            vote_button = driver.find_element(By.NAME, "submit_vote")
            vote_button.click()
            
            print("Voto realizado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
        time.sleep(interval)

# Configurações do bot
vote_url = "http://example.com/vote"  # URL da página de votação
personal_data = {
    "first_name": "Lucas",
    "last_name": "Carneiro",
    "email": "seuemail@example.com",
    "phone": "75999944660"
}
candidate_name = "Mercante Distribuidora"  # Nome do candidato a ser votado
vote_interval = 10  # Intervalo de tempo entre cada voto (em segundos)
gecko_driver_path = 'C:\Temp\geckodriver.exe'


driver = webdriver.Firefox(executable_path=gecko_driver_path)  # ou webdriver.Firefox() se estiver usando o Firefox

try:
    vote(driver, vote_url, personal_data, candidate_name, vote_interval)
finally:
    driver.quit()
