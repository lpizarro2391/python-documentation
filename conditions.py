try : 
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Edad no puede ser cero')
except ValueError:
    print('Invalid value')