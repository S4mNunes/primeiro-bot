from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")

# Login no LinkedIn
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("samnunes@outlook.com.br")
password.send_keys("Murimel100319@!")
password.send_keys(Keys.RETURN)

time.sleep(5)

# Vai pra página de busca de empregos
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4204057070&keywords=Desenvolvedor%20python&origin=BLENDED_SEARCH_RESULT_NAVIGATION_SEE_ALL&originToLandingJobPostings=4204057070%2C4204936264%2C4206625622")

time.sleep(5)

# Encontra todas as vagas da página
job_listings = driver.find_elements(By.CLASS_NAME, "job-card-container")

for job in job_listings:
    try:
        job.click()
        time.sleep(2)

        if "Candidatura simplificada" in driver.page_source:
            print("Tem candidatura simplificada")

        # Troço importante: verifica se tem "Candidatura Simplificada"
        try:
            easy_apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Candidatura Simplificada') or contains(text(), 'Easy Apply')]")
            easy_apply_button.click()
            time.sleep(2)

            # Aqui tu pode preencher os campos e clicar em Enviar (dependendo da complexidade)
            print("👉 Candidatando na vaga simplificada...")
            # driver.find_element(By.XPATH, "//button[@aria-label='Enviar candidatura']").click()

            time.sleep(2)
        except Exception as e:
            print("Nao encontrei candidatura simplificada ", e)

        else:
            print("Nao tem candidatura simplificada ")

        time.sleep(1)

    except Exception as e:
        print("Erro ao processar a vaga: ", e)
