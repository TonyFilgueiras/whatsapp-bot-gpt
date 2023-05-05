# pylint: disable-all
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config import REMOTE_DEBUGGING_PORT

# service = ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
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



# <img class="K1vBa _1aShU ZRhsD" draggable="false" src="blob:https://web.whatsapp.com/bd011c1f-70d0-4754-9f86-e22d9704830e" alt="Figurinha com: 😀">
# <img class="K1vBa _1aShU ZRhsD" draggable="false" src="blob:https://web.whatsapp.com/2141ae04-1e5f-4e69-b486-c954c8c9cea2" alt="Figurinha sem etiqueta">
# <img alt="Figurinha sem etiqueta" class="K1vBa _1aShU ZRhsD" draggable="false" src="blob:https://web.whatsapp.com/bf50d5b0-2cb5-40f2-be95-897825e8fbda" style="display: none;">

# <img src="blob:https://web.whatsapp.com/d3d5e3f9-0678-4cad-9d76-0e3853dc4b1f" class="jciay5ix tvf2evcx oq44ahr5 lb5m6g5c" style="width: 100%;">
# <img src="blob:https://web.whatsapp.com/f449432d-1773-4eb3-b34d-b22b13fd3c1f" class="jciay5ix tvf2evcx oq44ahr5 lb5m6g5c" style="width: 100%;">
# <img alt="Venha por favor" src="blob:https://web.whatsapp.com/fb707d9e-34cf-44b3-a953-09debb622b73" class="jciay5ix tvf2evcx oq44ahr5 lb5m6g5c" style="width: 100%;">