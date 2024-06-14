from GPT_API import driver as gpt_driver 
from GPT_API import prompt
from GPT_API import PlatformBasedDriver

from flask import Flask, jsonify, request, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
PlatformBasedDriver.debuggingModeLauncher()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=chrome_options)


@app.route("/getSendPrompt", methods=['POST'])
def stealthGPT():
    json_prompt = request.get_json()
    if json_prompt:
        received_prompt = json.loads(json_prompt)
        #driver = gpt_driver.create_driver()
        #driver.get("https://chatgpt.com/")
        result = prompt.promptEnter(driver, received_prompt)
        if result:
            return jsonify({"message": result}), 200
        else:
            return jsonify({"error": "No result returned"}), 500
    else:
        return jsonify({"error": "No JSON data received"}), 400

if __name__ == '__main__':
    app.run(debug=True)
