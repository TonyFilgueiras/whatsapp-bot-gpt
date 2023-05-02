from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config import REMOTE_DEBUGGING_PORT, CONTACT, SEARCH_NUMBER
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class WebDriverWrapper:
    def __init__(self):
        self._driver = webdriver.Chrome(service=self.service,options=self.options)
        with open("tabs.txt", "r") as file:
            self._window_chatgpt = str(file.readline().strip())
            self._window_wpp = str(file.readline().strip())
        self._reading = True
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def __getattr__(self, attr):
        return getattr(self.driver, attr)
    
    def navigate(self, url):
        self.driver.get(url)

    def verify_for_contact(self):
        self.driver.switch_to.window(self.wpp)
        try:
            active_chat = self.driver.find_element("xpath", '//*[@id="main"]/header/div[2]/div[1]/div/span')
            if active_chat.text == self.CONTACT:
                return True
            else:
                return False
        except NoSuchElementException:
            print(NoSuchElementException.msg)
            self.kill()
    def go_for_contact(self):
        self.driver.switch_to.window(self.wpp)

        try:
            self.clear_search_bar()

        except NoSuchElementException:
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
            self.kill()

    def kill(self):
        try:
            self.send_message("Ops!!! \u1FAE2 \nParece que deu algo errado!! \u1F614  \nPara eu voltar a funcionar, o meu mestre vai ter que verificar o que houve e me reiniciar.\n\t", "Luma")
        except:
            raise
        finally:
            self.driver.quit()

    def send_message(self, text : str, sender:str, send : bool = True):
        self.driver.switch_to.window(self.wpp)
        if self.verify_for_contact():
            try:
                self.driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(text)
                if send:
                    self.driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(f"\n\t - {sender}" + Keys.RETURN)
            except NoSuchElementException:
                print(NoSuchElementException.msg)
                self.kill()
        else:
            self.go_for_contact()
            try:
                self.driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(text)
                if send:
                    self.driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(f"\n\t - {sender}" + Keys.RETURN)
            except NoSuchElementException:
                print(NoSuchElementException.msg)
                self.kill()

    def verify_for_command(self, text : str):
        text = text.lower().strip()
        for commands in self.commands:
            if text not in commands.get("command"):
                pass
            else:
                if text == "!stop":
                    self.set_reading(False)
                elif text == "!start":
                    self.set_reading(True)
                elif text == "!help":
                    self.send_message(self.help_message, "Luma", send=False)
                    self.send_message("\n\tComandos:", "Luma", send=False)
                    for i in range (len(self.commands)):
                        self.send_message(f"\n\t\t{self.commands[i].get('command')}:", "Luma", send=False)
                        self.send_message(f"\nPara saber mais sobre o que cada comando faz, digite '!commands'\n\n \u1F970", "Luma", send=True)
                elif text == "!kill":
                    self.kill()
                elif text == "!introduction":
                    self.send_message(self.introduce_luma(), sender="Luma")
                elif text == "!commands":
                    self.send_message("Comandos:", "Luma", send=False)
                    for i in range (len(self.commands)):
                        self.send_message(f"\n\t{self.commands[i].get('command')}: \n\t\t{self.commands[i].get('definition')}", "Luma", send=False)
                        self.send_message(f"\n\n \u1F970", "Luma", send=True)
                elif text == "!ignore":
                    self.send_message("Irei ignorar qualquer forma de audio, foto, stickers, videos e textos com menos de 3 caractéres diferentes\n\nMeu mestre talvez no fúturo trabalhe para providenciar uma maneira de eu escutar os seus aúdios \u1F509, ja que ele mesmo não goste deles. \u1F611	", "Luma")

    def introduce_luma():
        return f"Olá {CONTACT}, eu sou a Luma!! \u1F970\u1F970\u1F970 \nMeu mestre me criou para te ajudar com o que for necessário. Tanto como dúvidas útis, ou até o simples fato de poder ter alguém para convesar.\n\nDigite '!help' para mais informações!"
    
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
        return f"Olá {CONTACT}!! \u1F970 \n\n aqui está a lista de comandos para auxiliar para você \u1F609	"
