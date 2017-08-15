# coding=utf-8
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        print 'Getting value'
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print 'Setting value'
        self._temperature = value

    temperature = property(get_temperature,set_temperature)


c = Celsius()
c.temperature
# c._temperature = -300
# c.get_temperature()
# c.set_temperature(-90)
# print c.get_temperature()
# print c.set_temperature(-272)
# print c.to_fahrenheit()