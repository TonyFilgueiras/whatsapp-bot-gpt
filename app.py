# selenium 4
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
# from .tabs import driver

options = webdriver.ChromeOptions()
options.add_experimental_option('debuggerAddress', 'localhost:9222')
driver = webdriver.Chrome(options=options)

print(driver.window_handles)

# Use the driver object to interact with the existing Chrome window.
window_wpp = '5BE67292DAB86F3C0632055BB3854F66'
# window_wpp = driver.window_handles[1]
# window_chatgpt = driver.window_handles[0]
window_chatgpt = 'E88690F94E4BFF93135332382960BC63'

driver.switch_to.window(window_wpp)

search_bar = driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
search_bar.send_keys("21 98790-9909")
sleep(2)
driver.find_element("xpath", '//*[@id="pane-side"]/div[1]/div/div/div[3]/div/div').click()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located(driver.find_element("xpath", '//*[@id="pane-side"]/div[1]/div/div/div[3]/div/div').click()))
# WebDriverWait(driver, 10).until(EC.presence_of_element_located(driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/span/button/span').click()))
sleep(2)
driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/span/button/span').click()

# """//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div/div/p"""

# """//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div"""

# """//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/p"""

"""//*[@id="main"]/div[2]/div/div[2]/div[3]/div[26]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/div/div/canvas"""

# """document.querySelector("#__next > div.overflow-hidden.w-full.h-full.relative.flex > div.flex.h-full.max-w-full.flex-1.flex-col > main > div.flex-1.overflow-hidden > div > div > div > div:nth-child(4) > div > div.relative.flex.w-\\[calc\\(100\\%-50px\\)\\].flex-col.gap-1.md\\:gap-3.lg\\:w-\\[calc\\(100\\%-115px\\)\\] > div.flex.flex-grow.flex-col.gap-3 > div > div > p")"""

# """document.querySelector("#__next > div.overflow-hidden.w-full.h-full.relative.flex > div.flex.h-full.max-w-full.flex-1.flex-col > main > div.flex-1.overflow-hidden > div > div > div > div:nth-child(3) > div > div.relative.flex.w-\\[calc\\(100\\%-50px\\)\\].flex-col.gap-1.md\\:gap-3.lg\\:w-\\[calc\\(100\\%-115px\\)\\] > div.flex.flex-grow.flex-col.gap-3 > div")"""

# """document.querySelector("#__next > div.overflow-hidden.w-full.h-full.relative.flex > div.flex.h-full.max-w-full.flex-1.flex-col > main > div.flex-1.overflow-hidden > div > div > div > div:nth-child(2) > div > div.relative.flex.w-\\[calc\\(100\\%-50px\\)\\].flex-col.gap-1.md\\:gap-3.lg\\:w-\\[calc\\(100\\%-115px\\)\\] > div.flex.flex-grow.flex-col.gap-3 > div > div > p")"""

# audio 
"""document.querySelector("#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs > div:nth-child(26) > div > div > div > div.ItfyB._3nbHh > div._35VV1._1kgzQ > div._3QeR3 > div._9JCTX > div > div.h8id8 > div.p357zi0d.bmot90v7 > div > div > div > canvas")"""


text = "failed"


elements = driver.find_element("xpath", '//*[@id="main"]/div[2]/div/div[2]/div[3]')
child_elements = elements.find_elements("xpath", "./*")

elements2 = driver.execute_script(f"return document.querySelector('#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs > div:nth-child({len(child_elements)}) > div > div > div > div.ItfyB._3nbHh > div.cm280p3y.to2l77zo.n1yiu2zv.c6f98ldp.ooty25bp.oq31bsqd > div.copyable-text > div > span._11JPr.selectable-text.copyable-text > span');")

text=elements2.text

# print(elements)
print(elements2.text)
# print(elements3.text)
# print(elements4.text)
# print(last_element)

answer = "didnt work bro..."


driver.switch_to.window(window_chatgpt)
driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea').send_keys("Responder ao Bernardo " +text + Keys.RETURN)
sleep(20)

chats = driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div')
childs = chats.find_elements("xpath", "./*")
print(len(childs))
print(childs)

gpt = driver.find_element("xpath", f'//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[{len(childs)-1}]/div/div[2]/div[1]/div/div')
                                    #  //*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div
answer = gpt.text

print(answer)

# driver.switch_to.window(window_wpp)

# driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(answer + Keys.RETURN)

driver.close()