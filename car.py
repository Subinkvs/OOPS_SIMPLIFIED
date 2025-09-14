class Car:
    

    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
        
    def drive(self):
        print(f"The car {self.model} is driving and its price is {self.price} lakh rupees")
        
    def stop(self):
        print(f"The car {self.model} is stopped {self.price} lakh rupees")
        

