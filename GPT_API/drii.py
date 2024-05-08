from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    print("Enter : ")
    debug = int(input())
    if debug:
        options = webdriver.ChromeOptions()
        options.debugger_address = "localhost:4444"
        return webdriver.Chrome(options=options)
    else: 
        return webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

