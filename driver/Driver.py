from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config import REMOTE_DEBUGGING_PORT
# from selenium.webdriver.common.keys import Keys

class WebDriverWrapper:
    def __init__(self):
        self.driver = webdriver.Chrome(service=self.service,options=self.options)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def __getattr__(self, attr):
        return getattr(self.driver, attr)
    
    def navigate(self, url):
        self.driver.get(url)
    
    @property
    def element(self):
        def find_element(*args, **kwargs):
            return self.driver.find_element(*args, **kwargs)
        return find_element()
    
    @property
    def options(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("start-maximized")
        opt.add_experimental_option("debuggerAddress", f"localhost:{REMOTE_DEBUGGING_PORT}")

        return opt

    @property
    def service(self):
        return ChromeService(ChromeDriverManager().install())

    @property
    def wpp_window(self):
        return self.driver.window_handles[0]

    @property
    def gpt_window(self):
        return self.driver.window_handles[1]

