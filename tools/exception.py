try :
    numerator = int(input("Input number to divide: "))
    denominator = int(input("Input number to divide by: "))
    result = numerator/denominator
except ValueError as e:
    print(e)
    print('Only int allowed.')
except ZeroDivisionError as e:
    print(e)
    print('No division by zero here. Go to collage for this.')
except Exception as e:
    print(e)
    print('Something went wrong =(')
else:
    print(result)
finally:
    print('Bye!')