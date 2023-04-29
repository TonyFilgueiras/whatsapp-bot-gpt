# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(service=service, options=options)

driver.execute_script("window.open('https://www.google.com');")
driver.execute_script("window.open('https://www.google.com');")

window_wpp = driver.window_handles[0]
window_chatgpt = driver.window_handles[1]

print("=-"*60)
print(f"windo_wpp = {window_wpp}")
print(f"windo_chatgpt = {window_chatgpt}")
print("=-"*60)

driver.close()