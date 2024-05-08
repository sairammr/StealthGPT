from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def promptEnter(driver):
    try:
        time.sleep(5)
        promptTextArea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#prompt-textarea"))) 
        
        promptTextArea.send_keys("tell me a joke")
        sendButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='send-button']"))) 
        sendButton.click()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")




