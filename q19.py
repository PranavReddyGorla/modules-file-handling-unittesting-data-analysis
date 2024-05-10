try:
    # Code may raise an exception
    x = 10/ 0
except ZeroDivisionError:
    # This block will run if there is a ZeroDivisionError
    print("ZeroDivisionError")
finally:
    # This block will run whatever happens
    print("Always run")
