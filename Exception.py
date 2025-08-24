
class NegativeAgeException(Exception):
    pass
def stage(age):
    try:
        stage(age)
        if age<0:
            raise NegativeAgeException('Age cannot be negative')
        if age<13:
            return 'Kid'
        elif age<19:
            return 'Teen'
        elif age < 50:
            return 'Young'
        else :
            return 'Old'
    except Exception as e :
        return str(e)
try:
    age = int(input('Enter the age '))
    c=stage(age)
    print(c)
except ValueError:
    print('Invalid input.Enter proper integer')

