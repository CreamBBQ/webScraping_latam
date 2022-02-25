from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.add_argument("-private")
driver = webdriver.Firefox(executable_path="./geckodriver", options=options)

URL = 'https://www.latamairlines.com/ar/es/ofertas-vuelos?dataFlight=%7B%22tripTypeSelected%22%3A%7B%22label%22%3A%22Solo+ida%22%2C%22value%22%3A%22OW%22%7D%2C%22cabinSelected%22%3A%7B%22label%22%3A%22Economy%22%2C%22value%22%3A%22Economy%22%7D%2C%22passengerSelected%22%3A%7B%22adultQuantity%22%3A1%2C%22childrenQuantity%22%3A0%2C%22infantQuantity%22%3A0%7D%2C%22originSelected%22%3A%7B%22id%22%3A%22BUE_AR_CITY%22%2C%22name%22%3A%22null%22%2C%22city%22%3A%22Buenos+Aires%22%2C%22cityIsoCode%22%3A%22BUE%22%2C%22country%22%3A%22Argentina%22%2C%22iata%22%3A%22BUE%22%2C%22latitude%22%3A-34.603684%2C%22longitude%22%3A-58.381559%2C%22timezone%22%3A-3%2C%22tz%22%3A%22America%2FMendoza%22%2C%22type%22%3A%22CITY%22%2C%22countryAlpha2%22%3A%22AR%22%2C%22allAirportsText%22%3A%22xp_sales_web_searchbox_od_allAirports%22%2C%22airportIataCode%22%3A%22BUE%22%7D%2C%22destinationSelected%22%3A%7B%22id%22%3A%22BOG_CO_AIRPORT%22%2C%22name%22%3A%22El+Dorado+Intl.%22%2C%22city%22%3A%22Bogot%C3%A1%22%2C%22cityIsoCode%22%3A%22BOG%22%2C%22country%22%3A%22Colombia%22%2C%22iata%22%3A%22BOG%22%2C%22latitude%22%3A4.70159%2C%22longitude%22%3A-74.1469%2C%22timezone%22%3A-5%2C%22tz%22%3A%22America%2FBogota%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22CO%22%2C%22allAirportsText%22%3Anull%2C%22airportIataCode%22%3A%22BOG%22%7D%2C%22dateGoSelected%22%3A%222022-03-25T15%3A00%3A00.000Z%22%2C%22dateReturnSelected%22%3Anull%2C%22redemption%22%3Afalse%7D'


def get_flight_info(url): 
    flights_info_list = []
    driver.get(url)
    flights = driver.find_elements(By.XPATH,'//ol[@aria-label="Vuelos disponibles."]/li[@class="sc-cxZfpC gDSZdh"]')
    for flight in flights: 
        schedule = flight.find_elements(By.XPATH, './/span[@class="sc-eCXBzT eiNgyV"]')
        duration = flight.find_element(By.XPATH, './/span[@class="sc-lmrgJh hhrBNA"]').text
        departure_time = schedule[0].text
        arrival_time = schedule[1].text
        departure_city = flight.find_element(By.XPATH, './/span[@class="sc-hfLElm glYDrI"]').text
        arrival_city = flight.find_element(By.XPATH, './/div[@class="sc-fguZLD dluWTb flight-information"][last()]/span[last()]').text
        duration = flight.find_element(By.XPATH, './/span[@class="sc-lmrgJh hhrBNA"]').text
        price = flight.find_elements(By.XPATH, './/span[@class="sc-buGlAa iJeoEg displayAmount"]')[1].text
        temp_dict = {'departure_city':departure_city,
        'arrival_city': arrival_city,
        'price':price,
        'duration':duration,
        'departure_time':departure_time,
        'arrival_time':arrival_time,
        }
        flights_info_list.append(temp_dict)
    driver.close()
    return flights_info_list


test = get_flight_info(URL)
print(test)