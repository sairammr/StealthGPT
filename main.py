from GPT_API import driver as gpt_driver 
from GPT_API import prompt
from GPT_API import PlatformBasedDriver

from flask import Flask, jsonify, request, json

app = Flask(__name__)
driver = None

def initialize_driver():
    PlatformBasedDriver.debuggingModeLauncher()
    global driver
    # Create the WebDriver instance if it's not already initialized
    if driver is None:
        driver = gpt_driver.create_driver()
        driver.get("https://chatgpt.com/")
@app.route("/getSendPrompt", methods=['POST'])
def stealthGPT():
    json_prompt = request.get_json()
    if json_prompt:
        received_prompt = json.loads(json_prompt)
        #driver = gpt_driver.create_driver()
        #driver.get("https://chatgpt.com/")
        initialize_driver()
        result = prompt.promptEnter(driver, received_prompt)
        if result:
            return jsonify({"message": result}), 200
        else:
            return jsonify({"error": "No result returned"}), 500
    else:
        return jsonify({"error": "No JSON data received"}), 400

if __name__ == '__main__':
    app.run(debug=True)
