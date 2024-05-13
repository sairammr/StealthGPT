from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    
 
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--remote-debugging-port=9222")
        return webdriver.Chrome(options=chrome_options)
    except:
        print("Cannot create")
        

