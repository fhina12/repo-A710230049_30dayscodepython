class Car: 
2.     def __init__(self, make, model, year): 
3.         self.__make = make  
4.         self.__model = model  
5.         self.__year = year  
6.  
7.     def get_make(self):  
8.         return self.__make 
9.  
10.     def get_model(self):  
11.         return self.__model 
12.  
13.     def get_year(self):  
14.         return self.__year 
15.  
16. car = Car("Honda", "Civic", 2022) 
9 
 
17. print(car.get_make())  
18. print(car.get_model())  
19. print(car.get_year())