class Temperature:
    @staticmethod
    def get_from_celsius(temperature: int | float) -> str:
        return (f'Celsius temperature = {round(temperature, 1)}°C'
                f'\nKelvin temperature = {round(temperature + 273.15, 1)} К'
                f'\nFahrenheit temperature = {round(temperature * (9 / 5) + 32, 1)}°F')

    @staticmethod
    def get_from_kelvin(temperature: int | float) -> str:
        return (f'Kelvin temperature = {round(temperature, 1)} К'
                f'\nCelsius temperature = {round(temperature - 273.15, 1)}°C'
                f'\nFahrenheit temperature = {round((temperature - 273.15) * (9 / 5) + 32, 1)}°F')

    @staticmethod
    def get_from_fahrenheit(temperature: int | float) -> str:
        return (f'Fahrenheit temperature = {round(temperature, 1)}°F'
                f'\nCelsius temperature = {round((temperature - 32) * (5 / 9), 1)}°C'
                f'\nKelvin temperature = {round((temperature - 32) * (5 / 9) + 273.15, 1)} K')


if __name__ == '__main__':
    print(Temperature.get_from_celsius(0))
    print(Temperature.get_from_kelvin(10))
    print(Temperature.get_from_fahrenheit(20))