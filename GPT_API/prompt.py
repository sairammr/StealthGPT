from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def promptEnter(driver,prompt):    
    try:
        print("entered")
        promptTextArea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#prompt-textarea")))
        promptTextArea.send_keys(prompt)
        sendButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='send-button']"))) 
        sendButton.click()
    except Exception as e:
        print("Error Occured")
        return 0
    #GET RESULT
    try :
        while True:
            try:
                completedGeneration =  WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="-ml-1 mt-0 flex h-7 items-center justify-center gap-[2px] self-end text-gray-400 lg:justify-start lg:self-center visible"]')))
                break
            except:
                pass
        result = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".prose")))
        print(result.text)
        return result.text
    except Exception as e:
        print("Cannot find element",e)
        return 0 
        
        



