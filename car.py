class carshowroom:
    def __init__(self):
        self.cgst=0.18
        self.sgst=0.18
        self.incurance=100000
    def company(self):
        while True:
            print("Toyota","Tata","Suzuki")
            self.n=input("Enter the car company:")
            if self.n=="Toyota":
                print("Welcome to Toyota")
                self.model()
                break
            elif self.n=="Tata":
                print("Welcome to Tata")
                self.model()
                break
            elif self.n=="Suzuki":
                print("Welcome to Suzuki")
                self.model()
                break
            else:
                print("Enter valid company:")
    def model(self):
        if self.n=="Toyota":
            while True:
                print("Select from Fortuner and Innova")
                self.c=input("Enter the car model:")
                if self.c=="Fortuner":
                    self.price(self.c)
                    break
                elif self.c=="Innova":
                    self.price(self.c)
                    break
                else:
                    print("Enter a valid model;")
        elif self.n=="Tata":
            while True:
                print("Select from Tirog and Nexon")
                self.c=input("Enter the car model:")
                if self.c=="Tirog":
                    self.price(self.c)
                    break
                elif self.c=="Nexon":
                    self.price(self.c)
                    break
                else:
                    ("Enter a valid model")
        elif self.n=="Suzuki":
            while True:
                print("Select from Swift and Alto")
                self.c=input("Enter the car model:")
                if self.c=="Swift":
                    self.price(self.c) 
                    break
                elif self.c=="Alto":
                    self.price(self.c)
                    break
                else:
                    print("Enter a valid model")
    def price(self,c):
        if c=="Fortuner":
            self.p=7500000
        elif c=="Innova":
            self.p=5000000
        elif c=="Tirog":
            self.p=8000000
        elif c=="Nexon":
            self.p=8500000
        elif c=="Swift":
            self.p=300000
        elif c=="Alto":
            self.p=200000
        car_price=self.p+self.cgst+self.sgst+self.incurance
        print("Total car price:",car_price)                   
a=carshowroom()
a.company()




            
