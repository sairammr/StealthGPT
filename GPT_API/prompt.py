from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

prompt_count = 0
def promptEnter(driver,prompt): 
    global prompt_count   
    try:
        print("entered")
        promptTextArea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#prompt-textarea")))
        promptTextArea.send_keys(prompt)
        sendButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='send-button']"))) 
        sendButton.click()
        prompt_count+=1
    except Exception as e:
        print("Error Occured")
        return 0
    #GET RESULT
    try :
        
        while True:
            try:
                completedGeneration =  WebDriverWait(driver, 1).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="mt-1 flex gap-3 empty:hidden juice:-ml-3"]')))
                try:
                    if len(completedGeneration)==prompt_count:
                        print("herrrrr")
                        break
                    else:
                        print("inga dha prechana")
                except Exception as e:
                    print(e)
                    print("inside")
            except:
                print("cannot find")
                pass
        while True:
            try:
                print("I am here")
                result = WebDriverWait(driver, 1).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".prose")))

                if len(result)==prompt_count:
                    print(result[len(result)-1].text)
                    return result[len(result)-1].text
            except :
                print("naan dha")
    except Exception as e:
        print("Cannot find element",e)
        return 0 
        
        



