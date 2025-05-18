# iss program main temperature class banai or usmain eik static method banaya hai jo celcius say fahrenhiet main
# temperature convert krkay return krraha.

class TemperatureConverter:


    @staticmethod  # staticmethod
    def celsius_to_fahrenheit(c):
        celcius = c
        fahrenhiet = (celcius * 5/9) + 32
        return fahrenhiet


temp = TemperatureConverter()
print('42.5°C in Fahrenheit', temp.celsius_to_fahrenheit(42.5), 'F')