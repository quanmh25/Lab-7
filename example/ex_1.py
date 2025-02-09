import requests


while True:
    fact = input("1 - факты из жизни, 2 - математические факты, 0 - выход: ")
    match fact:
        case "1":
            number = input("Введите число: ")
            response = requests.get(f"http://numbersapi.com/{number}/trivia")
            text = response.text
            print(text)
        case "2":
            number = input("Введите число: ")
            response = requests.get(f"http://numbersapi.com/{number}/math")
            text = response.text
            print(text)
        case "0":
            break
        case _:
            print("Я жду 0, 1 или 2, человек!")


