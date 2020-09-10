def weather_condition(temperature):
    if temperature > 7:
        return "Hot"
    else:
        return "Cold"

user_input = float(input("Enter the temperature :"))
print(weather_condition(user_input))