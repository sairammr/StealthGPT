# ChatGPT Selenium API

The ChatGPT Selenium API is a free and open-source tool that facilitates seamless access to OpenAI's ChatGPT in headless mode using Selenium. With this API, developers can integrate ChatGPT into their projects, automating interactions with the AI model without requiring a graphical user interface.

## Features

- **Headless Mode**: Interact with ChatGPT without the need for a graphical user interface.
- **Selenium Integration**: Utilize the powerful Selenium framework for web automation.
- **Chrome Auto-launch**: The API includes a feature to automatically launch Google Chrome for seamless integration.

## Installation

To install the ChatGPT Selenium API, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Philotheephilix/StealthGPT.git
   ```

2. Navigate to the project directory:
   ```bash
   cd StealthGPT
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Example

Here's an example of how you can use the ChatGPT Selenium API in your project:

```python
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
```

## Contributing

Contributions to the ChatGPT Selenium API are welcome! If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

The ChatGPT Selenium API is developed and maintained by [Philotheephilix](https://github.com/Philotheephilix). We would like to thank the OpenAI team for providing access to the ChatGPT model and the Selenium community for their excellent web automation framework.

Feel free to customize this README according to your project's specific needs and details.