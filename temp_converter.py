# temp_converter.py

calcDic = {
    "cf": lambda x: x * 9/5 + 32,          # Celsius to Fahrenheit
    "ck": lambda x: x + 273.15,            # Celsius to Kelvin
    "fc": lambda x: (x - 32) * 5/9,        # Fahrenheit to Celsius
    "fk": lambda x: (x - 32) * 5/9 + 273.15,  # Fahrenheit to Kelvin
    "kc": lambda x: x - 273.15,            # Kelvin to Celsius
    "kf": lambda x: (x - 273.15) * 9/5 + 32 # Kelvin to Fahrenheit
}

def convert_temperature(value, from_unit, to_unit):
    key = f"{from_unit[0].lower()}{to_unit[0].lower()}"
    if key in calcDic:
        return calcDic[key](value)
    else:
        raise ValueError("Invalid conversion units")
