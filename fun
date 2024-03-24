class carshowroom:
     def company(self,name):
         l=["toyota","mercedes","suzuki"]
         if name in l:
              print("welcome to ",name)
     def model(self,name):
         d={"Toyota":["fortuner","innova"],
           "Mercedes":["BMW"],
           "Suzuki":["Swift","Alto"]}
         if name in d:
              print(d[name])
     def price(self,m):
         print("you have selected",m)
         prices_list={"Fortuner":7500000,
                      "Innova":5000000,
                      "BMW":10000000,
                      "Swift":300000,
                      "Alto":100000}
         car_prices=prices_list
         print("the price of the car",car_prices)
         if m in prices_list:
              cgst=0.18
              gst1=cgst*2
              sgst=0.18
              gst2=sgst/2
              gst=(gst1+gst2)*car_prices
              insurance=100000
              final_price=car_prices+gst+insurance
              print("final price:",final_price)
n=input("enter the car company:")
c=carshowroom()
c.company(n)
c.model(n)
m=input("enter model of car:")
c.price(m) 
print(c)      
        
          