import requests


TRIV_MODE = '1'
MATH_MODE = '2'
DATE_MODE = '3'


# response = requests.get('http://numbersapi.com/22')
# print(response.text)

while True:
    response = None
    mode = input('Enter mode:')

    if mode in [TRIV_MODE, MATH_MODE]:
        number = input('Enter number:')
    else:
        day = input('Enter day:')
        month = input('Enter month:')

    if mode == TRIV_MODE:
        response = requests.get(f'http://numbersapi.com/{number}')
    elif  mode == MATH_MODE:
        response = requests.get(f'http://numbersapi.com/{number}/math')
    elif mode == DATE_MODE:
        response = requests.get(f'http://numbersapi.com/{month}/{day}/date')
    elif mode == '0':
        break

    print(response.text)





import requests

URL = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
headers = {
    "x-folder-id": "application/json",
    "Authorization": "Api-Key AQVNzJY4vPacG9CRn16VaP8JFZoPLrfDzNtOOdNj"
}

def yandex(request):
    prompt = {
         "modelUri": "gpt://b1gef38t15anr5jj0p10/yandexgpt-lite",
         "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "20"
        },
        "messages": [
            {"role": "system",
             "text": 'Ты ассистент кошка-горничная! И часто говоришь мяу!'},
            {"role": "user",
             "text": request}
        ]
    }
    response = requests.post(URL, headers=headers, json=prompt)
    result = response.json()
    text = result["result"]["alternatives"][0]["message"]["text"]
    print(text)
    return text


yandex('Привет!')