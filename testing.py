string = "a"
try:
    string_int = int(string)
except ValueError:
    # Handle the exception
    print('Please enter an integer')
else: 
    print("ELSE")
finally:
    print("FINALLY")