import requests
import json


def get_weather(city_name):
    # Địa chỉ API với tên thành phố và khóa API
    api_key = "b13aa5f80dcd0061f8aabe996268fbbe"                # Get API key from website
    # &units=metric có tác dụng xác định đơn vị đo lường, yêu cầu trả về mét, Celsius,...
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công hay không
    if response.status_code == 200:
        data = response.json()
        print(data)

        # Lấy thông tin cần thiết từ phản hồi JSON
        weather = data['weather'][0]['description']          # Nghĩa là ban đầu truy xuất vào weather, sau đó vào phần tử đầu tiên, sau đó vào description
        # weather = data['weather'[0][main]]                 # Nếu tôi để code vậy thì output sẽ là  Mô tả: CloudsClouds

        temp = data['main']['temp']                          # Tại sao weather có [0] còn temp k có, vì weather là list, còn temp là dictdict
        # Độ ẩmẩm
        humidity = data['main']['humidity']     
        # Áp suấtsuất        
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        city = data['name']
        country = data['sys']['country']

        # In thông tin đã lấy được
        print(f"Thời tiết ở {city}, {country}:")
        print(f"  - Mô tả: {weather}")
        print(f"  - Nhiệt độ: {temp}°C")
        print(f"  - Độ ẩm: {humidity}%")
        print(f"  - Áp suất: {pressure} hPa")
        print(f"  - Tốc độ gió: {wind_speed} m/s")

    else:
        print("Không thể lấy dữ liệu thời tiết.")


if __name__ == "__main__":
    city_name = input("Nhập tên thành phố: ")
    get_weather(city_name)
