class Car(object):
    def __init__(self):
        self.speed = 0
    
    def speed(self):
        return self.speed

    def start(self):
        self.speed = 25

    def stop(self):
        self.speed = 0
    
c = Car()
c.start()
print(c.speed == 25)
c.stop()
print(c.speed == 0)