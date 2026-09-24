user_celsius_temperature = int(input("Enter temperature in Celsius: "))
fahrenheit_temperature = (user_celsius_temperature * 1.8) + 32
kelvin_temperature = user_celsius_temperature + 273.15


user_temperatures = {
	"Celsius" : user_celsius_temperature,
	"Fahrenheit" : fahrenheit_temperature ,
	"Kelvin" : kelvin_temperature 
}

for key, value in user_temperatures.items():
    print(f"{key}: {value}")