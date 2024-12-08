class Attraction:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
        self._status = "Closed"
       
    def get_details(self):
        return f"Ride name: {self._name}, Capacity: {self._capacity}"
        
    def start(self):
        return "The attraction is starting"
        
    def open_attraction(self):
        self._status = "Open"
    
    def close_attraction(self):
        self._status = "Closed"
        
class Thrillride(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self._min_height= min_height
        
    def start(self):
        if self._status == "Open":
            return f"Thrill ride {self.__name} is now starting. Hold on tight"
        else:
            return f"Thrill ride {self.__name} is closed."
        
    def is_elegible(self, visitor):
        if visitor.height >= self._min_height:
            return True    
        else:
            return False
 
class FamilyRide(Attraction):
     def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._min_age = min_age
        
     def start(self):
        if self._status == "Open":
            return f"Family Ride {self._name} is now starting. Enjoy the fun"
        else:
            return f"Family Ride {self._name} is closed."
        
     def is_elegible(self, visitor):
        if visitor.age >= self._min_age:
            return True
        else:
            return False
            
class Staff:
    def __init__(self, name, role):
        self._name = name
        self._role = role
        
    def work(self):
        return (f"Staff {self._name} is performing their role {self._role}")
        
class Visitor:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height
        self._ride_history = []
        
    def ride(self, attraction):
        if type(attraction) is FamilyRide:
            if attraction.is_elegible(self._age):
                print(attraction.start())
                self.__ride_history.append(attraction._name)
        if type(attraction) is Thrillride:
            if attraction.is_elegible(self._height):
                print(attraction.start())
                self.__ride_history.append(attraction._name)
        else:
            print(f"{self._name} cannot ride {attraction._name}")
            
    def view_history(self):
        return self._ride_history
        
class Manager(Staff):
    def __init__(self, name, role):
        super().__init__(name, role)
        self._team = []
        
    def add_staff(self, staff):
        (self._team).append(staff._name)
        
    def get_team_summary(self):
        team = []
        for staff in self._team:
            team.append(f"{staff._name} ({staff._role})")


Slippery_Slopes = Thrillride("Slippery Slopes", 8, 150)
Spinning_Teacups = FamilyRide("Spinning Teacups", 12, 130)
Robert = Visitor("Robert", 23, 184)
Emily = Staff("Emily", "Ride Conductor")
George = Manager("George", "Manager")
