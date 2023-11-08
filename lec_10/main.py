from vehicle import Vehicle;

class Car(Vehicle):
    def __init__(self, speed, make, color):
        super().__init__(speed, make);
        self.color = color;

    def park(self):
        print(f"{self.color} car is parking.")

class Plane(Vehicle):
    def __init__(self, speed, make, currentSpeed):
        super().__init__(speed, make);
        self.currentSpeed = min(speed, currentSpeed);

    def checkSpeed(self):
        print(f"{self.make} plane is flying with speedn{self.currentSpeed}.")

class Boat(Vehicle):
    def __init__(self, speed, make, hasHelistop):
        super().__init__(speed, make);
        self.hasHelistop = hasHelistop;

    def parkHelicopter(self):
        if(self.hasHelistop):
            print(f"You can park your helicopter on '{self.make}'.");
        else:
            print(f"You can't park your helicopter on '{self.make}'.");

class RaceCar(Car):
    def __init__(self, speed, make, color, stageLevel):
        super().__init__(speed, make, color);
        self.stageLevel = stageLevel;
        self.speed += stageLevel * 0.1 * speed;

    def checkStage(self):
        print(f"{self.make} race car after stage {self.stageLevel} has speed {self.speed} km/h.")


car = Car(120, "Toyota", "Silver");
car.move();
car.park();
car.stop();

plane = Plane(900, "Boeing", 870);
plane.move();
plane.checkSpeed();
plane.stop();

boat = Boat(30, "Yamaha", True);
boat.move();
boat.parkHelicopter();
boat.stop();

raceCar = RaceCar(360, "Mercedes AMG Petronas", "Purple", 3)
raceCar.move()
raceCar.checkStage()
raceCar.stop();