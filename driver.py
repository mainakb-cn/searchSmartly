import json
from calculator import Calculator

# Driver code
if __name__ == "__main__": 
    
    data_handler = open("data.json")
    
    price_rules = json.load(data_handler)

    calculator = Calculator(price_rules)
    calculator.add('B')
    calculator.add('B')
    calculator.add('R')
    calculator.add('B')
    calculator.add('B')
    calculator.add('ST')
    calculator.add('B')
    calculator.add('R')
    calculator.add('B')
    print(calculator.total())


    calculator = Calculator(price_rules)
    calculator.add('B')
    calculator.add('R')
    calculator.add('R')
    calculator.add('R')
    calculator.add('R')
    calculator.add('R')
    calculator.add('R')
    calculator.add('R')
    calculator.add('R')
    calculator.add('R')
    calculator.add('R')
    print(calculator.total())