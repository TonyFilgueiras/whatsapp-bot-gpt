from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config import REMOTE_DEBUGGING_PORT, CONTACT, SEARCH_NUMBER
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from time import sleep

class WebDriverWrapper:
    def __init__(self):
        self._driver = webdriver.Chrome(options=self.options)
        with open("tabs.txt", "r") as file:
            self._window_chatgpt = str(file.readline().strip())
            self._window_wpp = str(file.readline().strip())
        self.send_message(self.introduce_luma(), "Luma")
        self._reading = True
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def __getattr__(self, attr):
        return getattr(self.driver, attr)
    
    def navigate(self, url):
        self.driver.get(url)


    def get_chatgpt_reply(self, chats : WebElement)->str:
        self.driver.switch_to.window(self.gpt)
        childs = chats.find_elements("xpath", "./*")

        try:    
            gpt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[{len(childs)-1}]/div/div[2]/div[1]/div/div')))
            # gpt = self.driver.find_element("xpath", f'//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[16]/div/div[2]/div[1]/div/div')

            answer = gpt.text

            return answer
        except NoSuchElementException:
            self.kill()
            raise (NoSuchElementException.msg)


    def ask_chatgpt(self, text:str)-> WebElement:
        self.driver.switch_to.window(self.gpt)
        try:
            self.driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea').send_keys("Responder ao Bernardo " +text + Keys.RETURN)

            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[1]/div/button')))
            WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[1]/div/button/div'), "Regenerate response"))

            chats = self.driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div')

            return chats
        except NoSuchElementException:
            self.kill()
            raise (NoSuchElementException.msg)

    def verify_for_contact(self) -> bool:
        self.driver.switch_to.window(self.wpp)
        try:
            active_chat = self.driver.find_element("xpath", '//*[@id="main"]/header/div[2]/div[1]/div/span')
            if active_chat.text == self.CONTACT:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def go_for_contact(self):
        self.driver.switch_to.window(self.wpp)

        try:
            self.clear_search_bar()

        except:
            search_bar = self.driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
            search_bar.send_keys(SEARCH_NUMBER)

            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element(By.CSS_SELECTOR, f'span[title="{self.CONTACT}"]')))
            sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, f'span[title="{self.CONTACT}"]').click()

            self.clear_search_bar()

    def clear_search_bar(self):
        self.driver.switch_to.window(self.wpp)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/span/button/span')))
            sleep(1)
            self.driver.find_element("xpath", '//*[@id="side"]/div[1]/div/div/span/button/span').click()
        except:
            raise
            
    def get_his_last_message(self)-> str:
        self.driver.switch_to.window(self.wpp)
        def getting_last_message():
            try:
                his_messages =  self.driver.find_elements(By.CSS_SELECTOR, "div[data-id*='false']")
                his_last_message = his_messages[-1]
                
                message_content =  his_last_message.find_element(By.CLASS_NAME, '_11JPr.selectable-text.copyable-text')        

                return message_content.text
            except IndexError:
                return ""
            except NoSuchElementException:
                try:
                    message_content = his_last_message.find_element(By.TAG_NAME, "canvas")

                    self.send_message("Foi mal amigão... Mas eu não aprendi a escutar áudio ainda", "Luma")
                    self.execute_command("!stop")

                    return message_content.text
                except NoSuchElementException:
                    try:
                        message_content = his_last_message.find_element(By.CLASS_NAME, "jciay5ix tvf2evcx oq44ahr5 lb5m6g5c")

                        self.send_message("Belíssima imagem amiguinho, mas não consigo fazer nada a respeito disso...", "Luma")
                        self.execute_command("!stop")
                        return message_content.text
                    except NoSuchElementException:
                        message_content = his_last_message.find_element(By.CLASS_NAME, "K1vBa _1aShU ZRhsD")

                        self.send_message("Belíssimo sticker amiguinho, mas não consigo fazer nada a respeito disso...", "Luma")
                        self.execute_command("!stop")
                        return message_content.text
        if self.verify_for_contact():
            print("to no ctt certo")
            return getting_last_message()

        else:
            self.go_for_contact()
            return getting_last_message()

        
    def get_my_last_message(self)->str:
        self.driver.switch_to.window(self.wpp)
        def getting_last_self_message():
            try:
                my_messages =  self.driver.find_elements(By.CSS_SELECTOR, "div[data-id*='true']")
                my_last_message = my_messages[-1]
                
                message_content =  my_last_message.find_element(By.CLASS_NAME, '_11JPr.selectable-text.copyable-text')  

                return message_content.text   
            except:
                return ""
        if self.verify_for_contact():
            print("to no ctt certo")
            return getting_last_self_message()

        else:
            self.go_for_contact()
            return getting_last_self_message()


    def kill(self):
        print("matando")
        try:
            self.send_message("Ops!!!", "Luma", send=False)
            self.next_line()
            self.send_message("Parece que deu algo errado!!", "Luma", send=False)
            self.next_line()
            self.send_message("Para eu voltar a funcionar, o meu mestre vai ter que verificar o que houve e me reiniciar.", "Luma", send=True)                         
        except:
            raise
        finally:
            self.driver.quit()

    def send_message(self, text : str, sender:str, send : bool = True):
        def sending_message():
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
                self.driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(text)
                if send:
                    self.driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(f"\n - {sender}" + Keys.RETURN)
            except NoSuchElementException:
                self.kill()
            except ElementNotInteractableException:
                self.kill()
        self.driver.switch_to.window(self.wpp)
        if self.verify_for_contact():
            sending_message()
        else:
            self.go_for_contact()
            sending_message()

    def execute_command(self, command:str):
        command = command.lower().strip()
        if command == "!stop":
            self.send_message("Lendo = False", "Luma")
            self.set_reading(False)
        elif command == "!start":
            self.send_message("Lendo = True", "Luma")
            self.set_reading(True)
        elif command == "!help":
            self.send_message(self.help_message, "Luma", send=False)
            self.next_line(times=2)
            self.tab()
            self.send_message("Comandos:", "Luma", send=False)
            for i in range (len(self.commands)):
                self.next_line()
                self.tab(8)
                self.send_message(f"{self.commands[i].get('command')}:", "Luma", send=False)
            self.send_message(f"\nPara saber mais sobre o que cada comando faz, digite '!commands'", "Luma", send=True)
        elif command == "!kill":
            self.kill()
        elif command == "!introduction":
            self.send_message(self.introduce_luma(), sender="Luma")
        elif command == "!commands":
            self.send_message("Comandos:", "Luma", send=False)
            for i in range (len(self.commands)):
                self.next_line()
                self.tab()
                self.send_message(f"{self.commands[i].get('command')}: ", "Luma", send=False)
                self.next_line()
                self.tab(8)
                self.send_message(f"{self.commands[i].get('definition')}", "Luma", send=False)
            self.send_message(f"", "Luma")
        elif command == "!ignore":
            self.send_message("Irei ignorar qualquer forma de audio, foto, stickers, videos e textos com menos de 3 caractéres diferentes", "Luma", send=False)
            self.next_line()
            self.send_message("Meu mestre talvez no fúturo trabalhe para providenciar uma maneira de eu escutar os seus aúdios, ja que ele mesmo não goste deles.", "Luma")
        elif command == "!status":
            self.send_message(f"Status Lendo: '{self.reading}'", "Luma")

    def verify_for_command(self, text : str) -> bool:
        text = text.lower().strip()
        for i in self.commands:
            if text in i.get("command"):
                return True
        else:
            return False

    def introduce_luma(self):
        return f"Olá {CONTACT}, eu sou a Luma!!\n\n Meu mestre me criou para te ajudar com o que for necessário. Tanto como dúvidas útis, ou até o simples fato de poder ter alguém para convesar.\nDigite '!help' para mais informações!"

    
    @property
    def driver(self):
        return self._driver
    
    @property
    def options(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("debuggerAddress", f"localhost:{REMOTE_DEBUGGING_PORT}")

        return opt

    @property
    def commands(self):
        possible_commands = [
    {
        'command': "!stop",
        "definition": "Faz o bot parar de responder as suas mensagens"
    },
    {
        'command': "!start",
        "definition": "Faz o bot responder as suas mensagens"
    },
    {
        'command': "!help",
        "definition": "Mostra uma breve explicação sobre o bot"
    },
    {
        'command': "!kill",
        "definition": "Fecha o script rodando e as abas do Whatsapp e ChatGPT"
    },
    {
        'command': "!introduction",
        "definition": "Introduz o usuário a Luma"
    },
    {
        'command': "!commands",
        "definition": "Mostra os comandos disponiveis"
    },
    {
        'command': "!ignore",
        "definition": "Mostra o tipo de conteúdo que a Luma irá ignorar"
    },
    {
        'command': "!status",
        "definition": "Retorna o estado 'Lendo' ativo da Luma"
    }
    ]
        return possible_commands
    @property
    def service(self):
        return ChromeService(ChromeDriverManager().install())

    @property
    def CONTACT(self):
        return str(CONTACT.strip())

    @property
    def wpp(self):
        return self._window_wpp

    @property
    def gpt(self):
        return self._window_chatgpt

    @property
    def reading(self):
        return self._reading

    @reading.setter
    def reading(self, value: bool):
        self._reading = value

    def set_reading(self, value:bool):
        self.reading = value

    @property
    def help_message(self):
        return f"Olá {CONTACT}!!\n Aqui está uma lista de comandos para auxiliar para você"

    @property
    def actions(self):
        return ActionChains(self.driver)
    
    def next_line(self, times : int = 1):
        self.actions.key_down(Keys.SHIFT).send_keys(Keys.RETURN * times).key_up(Keys.SHIFT).perform()

    def tab(self, times: int = 4):
        self.actions.send_keys(Keys.SPACE * times).perform()

    

