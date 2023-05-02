# pylint: disable-all

# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from config import REMOTE_DEBUGGING_PORT
# from .tabs import driver

options = webdriver.ChromeOptions()
options.add_experimental_option('debuggerAddress', f'localhost:{REMOTE_DEBUGGING_PORT}')
driver = webdriver.Chrome(options=options)

print(driver.window_handles)

with open("tabs.txt", "r") as file:
    window_chatgpt = str(file.readline().strip())
    window_wpp = str(file.readline().strip())

print("=-"*60)
print(f"windo_wpp = {window_wpp}")
print(f"windo_chatgpt = {window_chatgpt}")
print("=-"*60)


driver.switch_to.window(window_wpp)



camila = "21 98838-7774"
bernardo = "21 98790-9909"
teste = "Teste_bot"

search_bar = driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
search_bar.clear()
search_bar.send_keys(teste)
# sleep(2)

# driver.find_element(By.CSS_SELECTOR, 'span[title="Teste_bot"]').click()

# calma = driver.find_element(By.CSS_SELECTOR, 'span[title="Teste_bot"]')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, 'span[title="Teste_bot"]')))
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'span[title="Teste_bot"]').click()

# WebDriverWait(driver, 10).until(EC.presence_of_element_located(driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/span/button/span').click()))

# botao = driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/span/button/span')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/span/button/span')))
sleep(1)
driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/span/button/span').click()

def get_last_message():
    try:
        messages =  driver.find_elements(By.CSS_SELECTOR, "div[data-id*='true']")
        last_message = messages[-1]
        
        message_content =  last_message.find_element(By.CLASS_NAME, '_11JPr.selectable-text.copyable-text')        

        return message_content.text
    except NoSuchElementException:
        try:
            message_content = last_message.find_element(By.TAG_NAME, "canvas")

            return "É audio"
        except NoSuchElementException:
            try:
                message_content = last_message.find_element(By.CLASS_NAME, "jciay5ix tvf2evcx oq44ahr5 lb5m6g5c")

                return "Belíssima imagem amiguinho, mas n consigo fazer nada a respeito disso..."
            except NoSuchElementException:
                message_content = last_message.find_element(By.CLASS_NAME, "K1vBa _1aShU ZRhsD")

                return "Belíssimo sticker amiguinho, mas n consigo fazer nada a respeito disso..."


    except:
        raise ("Couldnt find the element")
    

old_len = driver.execute_script('return document.querySelector("#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs").children.length;')

while True:
    new_len = driver.execute_script('return document.querySelector("#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs").children.length;')

    if new_len != old_len:
        text= get_last_message()
        print(text)

        if text == "!stop":
            break
        old_len = new_len
    sleep(1)
