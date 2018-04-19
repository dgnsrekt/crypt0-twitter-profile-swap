from lifxlan import LifxLAN, RED, GREEN
from time import sleep
from settings import Configuration

CONFIG = Configuration()


class LifxProfile:

    def __init__(self, number_of_lifx):
        self.config = CONFIG.lifx
        print(self.config)
        self.lifx = LifxLAN(number_of_lifx)

        # get devices
        self.devices = self.lifx.get_power_all_lights()
        print("\nFound {} light(s):\n".format(len(self.devices)))

    def setProfileColor(self, color):
        print('Setting Lights {}'.format(color))
        for d in self.devices:
            try:
                d.set_color(color)
            except Exception as e:
                print(e)

    def setBullishLights(self):
        self.setProfileColor(GREEN)

    def setBearishLights(self):
        self.setProfileColor(RED)


def test():
    print('Testing Lights')
    profile = LifxProfile(4)
    profile.setBullishLights()
    print('Sleep for 10 seconds.')
    sleep(10)
    profile.setBearishLights()
    print('Test Complete')


if __name__ == '__main__':
    test()
