class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("Ця "+self.model+" їде.")

    def stop(self):
        print("Ця "+self.model+" зупинилась.")
