# from driver import WebDriverWrapper
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

def get_chatgpt_reply(childs : list):
    try:    
        gpt = driver.find_element("xpath", f'//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[{len(childs)-1}]/div/div[2]/div[1]/div/div')
                                        #  //*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div
        answer = gpt.text

        return answer
    except:
        raise ("Couldnt find the element") 

text= "me explica soma"

driver.switch_to.window(window_chatgpt)
driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea').send_keys("Responder ao Bernardo " +text + Keys.RETURN)

# element = driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[1]/div/button')
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[1]/div/button')))
WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element(("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[1]/div/button/div'), "Regenerate response"))

chats = driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div')
childs = chats.find_elements("xpath", "./*")
print(len(childs))

answer = get_chatgpt_reply(childs)

print(answer)
