def data_type(args):
    if args is None:
        return 'no value'
    elif isinstance(args, str):
        return len(args)
    elif isinstance(args, bool):
        return args
    elif isinstance(args, list):
        if len(args) > 2: 
            return args[2]
        else:
            return None
    elif isinstance(args, int):
        if args < 100:
            return 'less than 100'
        elif args > 100:
            return 'more than 100'
        else:
            return "equal to 100"
    else:
        return "invalid input"
    
def fizz_buzz(num):
    if not isinstance(num, (int,float)):
        return num
    elif num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num
    
class Car(object):
    def __init__(self, name = 'General', model = 'GM', car_type = 'saloon'):
        self.car_type = car_type
        self.model = model
        self.name = name
        self.speed = 0
        self.car_doors()
        self.car_wheels()
        
    def car_doors(self):
        if self.name == 'Porshe':
            self.num_of_doors = 2
        elif self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
            
    def car_wheels(self):
        self.num_of_wheels = 4
        if self.car_type == 'trailer':
            self.num_of_wheels = 8
            
    def is_saloon(self):
        if self.car_type == 'trailer':
            return False
        return True
        
    def drive(self, spd):
        self.speed = 10 ** 3
        if self.car_type == 'trailer':
            self.speed = spd * 11
        return self    
                      
            
man = Car('MAN', 'Truck', 'trailer')
parked_speed = man.speed
moving_speed = man.drive(7)
print moving_speed.speed, 'speed'
            