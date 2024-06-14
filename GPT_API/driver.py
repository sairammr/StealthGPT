from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    try:
        chrome_options = Options()
        
        chrome_options.add_argument("--remote-debugging-port=9222")
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print("Cannot create WebDriver:", e)
        return None
        

