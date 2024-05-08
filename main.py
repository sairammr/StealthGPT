from GPT_API import drii as gpt_driver 
from GPT_API import prompt

import time
driver = gpt_driver.create_driver()
driver.get("https://chatgpt.com/")
prompt.promptEnter(driver)
