class Device:
    count=0
    def __init__(self, ip, mac, name):
        Device.count += 1
        self.ip = ip
        self.mac_adress = mac
        self.name = name
        # result = ping the devie
        # if result:
        #     self.status = 'active'
        # else:
        #     self.status = 'unknown'

class TV(Device):
    def turn_on(self):
        # connect to self.ip and turn on
        pass
    def turn_off(self):
        # connect to self.ip and turn off
        pass
    

class SmartTV(TV):
    def turn_on(self):
        # turn on the smart tv 
        pass
class Thermo(Device):
    # connect to self.ip and read degree and return result
    pass