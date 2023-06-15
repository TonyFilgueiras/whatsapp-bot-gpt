# pylint: disable-all
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config import REMOTE_DEBUGGING_PORT

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option("debuggerAddress", f'localhost:{REMOTE_DEBUGGING_PORT}')
driver = webdriver.Chrome(options=options)

driver.execute_script("window.open('https://web.whatsapp.com/');")
driver.execute_script("window.open('https://chat.openai.com/');")  

driver.close()

window_wpp = driver.window_handles[0]
window_chatgpt = driver.window_handles[1]

print("=-"*60)
print(f"windo_wpp = {window_wpp}")
print(f"windo_chatgpt = {window_chatgpt}")
print("=-"*60)

with open("tabs.txt", "w") as file:
    file.write(f"{window_wpp}" + "\n")
    file.write(f"{window_chatgpt}" + "\n")