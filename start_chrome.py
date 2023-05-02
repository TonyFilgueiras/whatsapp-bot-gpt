import os
from config import REMOTE_DEBUGGING_PORT

os.chdir('C:/Program Files/Google/Chrome/Application')
os.system(f'chrome.exe --remote-debugging-port={REMOTE_DEBUGGING_PORT} --user-data-dir="C:/Users/vaitc/OneDrive/Desktop/Tony/Chrome_Overrides"')
# os.system(r"cmd /c ")


# cd "C:\Program Files\Google\Chrome\Application"

# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\vaitc\OneDrive\Desktop\Tony\Chrome Overrides"