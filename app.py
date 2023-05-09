from driver import WebDriverWrapper
from time import sleep
from config import CONTACT
from chatgpt import ChatGpt

driver = WebDriverWrapper()
gpt = ChatGpt()

old_len = driver.execute_script('return document.querySelector("#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs").children.length;')
his_old_message = driver.get_his_last_message()
my_old_message = driver.get_my_last_message()

while True:
    new_len = driver.execute_script('return document.querySelector("#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs").children.length;')
    

    if new_len != old_len:
        his_last_message = driver.get_his_last_message()
        if his_last_message != his_old_message:
            if driver.verify_for_command(text=his_last_message):
                driver.execute_command(his_last_message)
            else:
                if driver.reading:
                    driver.send_message("Asking ChatGPT...", "Luma")
                    answer = gpt.ask_gpt(message=his_last_message)
                    driver.send_message(answer, "ChatGPT")
            his_old_message = driver.get_his_last_message()
            my_old_message = driver.get_my_last_message()

        my_last_message = driver.get_my_last_message()
        if my_last_message != my_old_message:
            if driver.verify_for_command(text=my_last_message):
                driver.execute_command(my_last_message)
            else:
                pass
            my_old_message = driver.get_my_last_message()


    print(f"Lendo: {driver.reading}")


    sleep(1)