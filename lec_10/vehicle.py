class Vehicle:
    def __init__(self, speed, make):
        self.speed = speed;
        self.make = make;

    def move(self):
        print(f"{self.make} vehicle is moving with speed {self.speed} km/h.")

    def stop(self):
        print(f"{self.make} vehicle stopped.")
