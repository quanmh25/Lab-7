import json
import requests


RED = "\x1b[48;5;196m"  
END = "\033[0m" 


def taskFirst():
    
    city_name = "Moscow"
    key_api = "b13aa5f80dcd0061f8aabe996268fbbe"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key_api}&units=metric"

    req = requests.post(url)
    res = json.loads(req.text)

    if req.status_code == 200:
        # print(res)

        weather = res['weather'][0]['description']
        humidity = res['main']['humidity']
        pressure = res['main']['pressure']
        country = res['sys']['country']
        print(f" - Results of weather in {city_name}, {country}")
        print(f" - Description: {weather}")
        print(f" - Humidity: {humidity}%")
        print(f" - Pressure: {pressure}hPa")

    else:
        print("Unable to retrieve data")


def taskSecond(n):

    url = "https://api.covidtracking.com/v1/us/daily.json"
    res = requests.get(url)
    data = res.json()
    # print(data)

    date = data[n]['date']
    states = data[n]['states']
    positive = data[n]['positive']
    negative = data[n]['negative']
    death = data[n]['death']
    test_result = data[n]['totalTestResultsIncrease']

    print(f" ***DATA OF COVID-19 IN USA")
    print(f" - Date of result: {date}")
    print(f" - Quantity of States: {states}")
    print(f" - Total positive: {positive}")
    print(f" - Total negative: {negative}")
    print(f" - Total deaths {death}")
    print(f" - Total number of tests {test_result}")

    # print(f"Length of Dictionary: {len(data)}")


if __name__ == '__main__':

    print(RED + "Task 1:" + END)
    taskFirst()
    
    print("----------")
    print(RED + "Task 2:" + END)
    print("Number 0 - March 07, 2021")
    print("Number 1 - March 06, 2021")
    print("...")
    print("Number 419 - January 13, 2020")
    n = int(input("Enter day: "))

    taskSecond(n)