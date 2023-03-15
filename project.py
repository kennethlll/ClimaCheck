from bs4 import BeautifulSoup
import requests
import sys
import datetime

# create a weather object. easy for storing each day weather information
class weather:
    def __init__(self, city, type_w, temp, tempfeel, temp_min, temp_max, vis, wind, cloud, date = datetime.datetime.now().date()):
        self.city = city
        self.type_w = type_w
        self.temp = temp
        self.tempfeel = tempfeel
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.vis = vis
        self.wind = wind
        self.cloud = cloud
        self.date = date

    # to print out the weather object argument data
    def print_info(self):
        print(f"Date: {self.date}")
        print(f"City: {self.city}")
        print(f"Weather type: {self.type_w}")
        print(f"Current temperature: {self.temp}°C")
        print(f"Feels like: {self.tempfeel}°C")
        print(f"Temperature range: {self.temp_min}°C to {self.temp_max}°C")
        print(f"Visiibilty: {self.vis}")
        print(f"Wind spped: {self.wind}km/h")
        print(f"Cloud: {self.cloud}")
        print()


def main():
    global api_key
    global city
    api_key = input("what is your api key? ")
    city = input("where are you? ")
    #checkCurrentAlert()
    data = weather_info()
    data.print_info()
    forecast()

def weather_info(api_key, city):
    """
    this function will get weather information from openweathermap
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"



    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()

    x = weather(
        data['name'],
        f"{data['weather'][0]['main']}, {data['weather'][0]['description']}",
        data['main']['temp'],
        data['main']['feels_like'],
        data['main']['temp_min'],
        data['main']['temp_max'],
        data['visibility'],
        data['wind']['speed'],
        data['clouds']['all']
    )
    return x


def forecast(api_key, city):
    """
    This function is designed for scraping the weather infromation from enviromental canada website
    Technically, ENV canada always provide more accurate weather alert than others.
    """
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    #response.raise_for_status()
    datas = response.json()
    forecasts = []
    for i in range(0, 40, 8):
        data = datas["list"][i]
        x = weather(
            datas["city"]['name'],
            f"{data['weather'][0]['main']}, {data['weather'][0]['description']}",
            data["main"]["temp"],
            data['main']['feels_like'],
            data['main']['temp_min'],
            data['main']['temp_max'],
            data['visibility'],
            data['wind']['speed'],
            data['clouds']['all'],
            data["dt_txt"].split()[0]
        )
        forecasts.append(x)
    return forecasts

def checkCurrentAlert():
    """
    This function is used for checking alert status in the York region
    This function will scrape the environmental canada webstie information
    In general, enviromental canada has a better forcasting model for canada region
    """

    page = requests.get('https://weather.gc.ca/warnings/report_e.html?on11')
    if page.status_code != 200:
        sys.exit("Cannot reach the website now, please try later")
    soup = BeautifulSoup(page.content,"html.parser")
    division = soup.find("div", {"class", 'col-xs-12'})
    if division.find_all("p")[0].get_text().find("No Alerts in effect") != -1:
        return None
    else:
        div = soup.find('div', class_='col-xs-12')

        return div

def split_message(message):
    """
    this function is used for splitting sms messages
    """
    message_parts = []
    max_len = 100
    while len(message) > 0:
        if len(message) <= max_len:
            message_parts.append(message)
            break
        else:
            message_parts.append(message[:max_len])
            message = message[max_len:]
    return message_parts



if __name__ == "__main__":
    main()