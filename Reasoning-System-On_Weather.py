from time import strftime
import random
print("\t\t\t\t\t\tREASONING SYSTEM ON WEATHER FORECAST\n")

y = strftime('\t\t\t%d-%A-%Y                               %H:%M:%S %p\n')
print(y)
print("Enter the weater details as asked below:\n")
city = input("CITY YOU LIVE IN: ")
city = city.upper()
# _*_YESTERDAY_*_
y_temp = float(input(f"What was the avg temp in {city} last day: "))
rain = input(f"Is was raining yesterday in {city} [Y/N]: " )
if rain == "Y" or rain == "y":
    y_rain = True
else:
    y_rain = False

#  _*_TODAY_*_
t_temp = float(input(f"What was the avg temp in {city} today: "))
rain = input(f"Is it raining today in {city} [Y/N]:" )
if rain == "Y" or rain == "y":
    t_rain = True
else:
    t_rain = False

# _*_TOMORROW_*_
print("\n########______________TOMORROW'S WEATHER PREDICTION______________########\n")

print("\n\t\t\t\t ::::::Weather in {city} will be::::::\n")      
avg_tm_temp = random.uniform(20,36)

wind = ["E","W","N","S","NE","NW","SE","SW"]

print(u"\t\t\tTemperature(in \N{DEGREE SIGN}C )\t\t\tWind\t\t\t\tHumidity\n")
m_tm_temp = random.randrange(18,25,2)
a_tm_temp = random.randrange(25,40,2)
n_tm_temp = random.randrange(20,30,2)

m_w_speed = random.randrange(0,20,2)
a_w_speed = random.randrange(0,20,2)
n_w_speed = random.randrange(0,20,2)

if a_tm_temp <30:
    humidity = random.randrange(20,30,2)
elif a_tm_temp > 30:
    humidity = random.randrange(30,40,2)
 

print("Morning:\t\t",m_tm_temp, u"\N{DEGREE SIGN}C","\t\t\t\t",random.choice(wind)," (",m_w_speed,"Km/h)","\t\t\t",humidity,"%")
print("Day    :\t\t",a_tm_temp, u"\N{DEGREE SIGN}C","\t\t\t\t",random.choice(wind)," (",a_w_speed,"Km/h)")
print("Night  :\t\t",n_tm_temp, u"\N{DEGREE SIGN}C","\t\t\t\t",random.choice(wind)," (",n_w_speed,"Km/h)")

if y_rain and t_rain:
    tm_rain = random.uniform(30,45)
    print("\nRain  :", round(tm_rain,2), "%")
elif y_rain and not t_rain:
    tm_rain = random.uniform(15,25)
    print("\nRain  :", round(tm_rain,2), "%")
elif not y_rain and t_rain:
    tm_rain = random.uniform(20,35)
    print("\nRain  :", round(tm_rain,2), "%")
elif not y_rain and not t_rain and avg_tm_temp <= 25:
    tm_rain = random.uniform(10,15)
    print("\nRain  :", round(tm_rain,2), "%")
elif not y_rain and not t_rain and avg_tm_temp > 25:
    tm_rain = random.uniform(0,5)
    print("\nRain  :", round(tm_rain,2), "%")
    
if humidity > 30 and 25 < tm_rain < 35:
    print("\nWeather : Haze\t\t\tAverage Temperature will be:", round((m_tm_temp+a_tm_temp+n_tm_temp)/3,2),u"\N{DEGREE SIGN}C\n")
elif tm_rain >= 35:
    print("\nWeather : Cloudy\t\t\tAverage Temperature will be:", round((m_tm_temp+a_tm_temp+n_tm_temp)/3,2),u"\N{DEGREE SIGN}C\n")
elif  a_tm_temp >=35 and tm_rain <20:
    print("\nWeather : Sunny\t\t\tAverage Temperature will be:", round((m_tm_temp+a_tm_temp+n_tm_temp)/3,2),u"\N{DEGREE SIGN}C\n")
else: 
    print("\nWeather : Clear\t\t\tAverage Temperature will be:", round((m_tm_temp+a_tm_temp+n_tm_temp)/3,2),u"\N{DEGREE SIGN}C\n")
 
if y_temp > 30  and t_temp >30 and a_tm_temp >30:
    print(f"There is chances of DROUGHT in your city {city}")
elif y_rain and t_rain and tm_rain > 30:
    print(f"There is chances of FLOOD in your city {city}")




