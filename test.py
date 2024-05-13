import requests,json
prompt = input("Enter Prompt : ")
prompt_json = json.dumps(prompt)
url = "http://127.0.0.1:5000/getSendPrompt"
try:
    response = requests.post(url,json=prompt_json)
    if response.status_code ==200:
        
        result = response.json()
        finalAnswer = result["message"]
        print(finalAnswer)
    else:
        pass
except Exception as e:
    print(e)