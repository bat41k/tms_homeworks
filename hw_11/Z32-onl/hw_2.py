class Temperature:
    @staticmethod
    def get_from_celsius_to_kelvin(temperature: int | float) -> str:
        return f'Kelvin temperature = {round(temperature + 273.15, 1)} К'

    @staticmethod
    def get_from_celsius_to_fahrenheit(temperature: int | float) -> str:
        return f'Fahrenheit temperature = {round(temperature * (9 / 5) + 32, 1)}°F'

    @staticmethod
    def get_from_kelvin_to_celsius(temperature: int | float) -> str:
        return f'Celsius temperature = {round(temperature - 273.15, 1)}°C'

    @staticmethod
    def get_from_kelvin_to_fahrenheit(temperature: int | float) -> str:
        return f'Fahrenheit temperature = {round((temperature - 273.15) * (9 / 5) + 32, 1)}°F'

    @staticmethod
    def get_from_fahrenheit_celsius(temperature: int | float) -> str:
        return f'Celsius temperature = {round((temperature - 32) * (5 / 9), 1)}°C'

    @staticmethod
    def get_from_fahrenheit_kelvin(temperature: int | float) -> str:
        return f'Kelvin temperature = {round((temperature - 32) * (5 / 9) + 273.15, 1)} K'


if __name__ == '__main__':
    print(Temperature.get_from_celsius_to_kelvin(0))
    print(Temperature.get_from_celsius_to_fahrenheit(10))
    print(Temperature.get_from_kelvin_to_celsius(20))
    print(Temperature.get_from_kelvin_to_fahrenheit(30))
    print(Temperature.get_from_fahrenheit_celsius(40))
    print(Temperature.get_from_fahrenheit_kelvin(50))