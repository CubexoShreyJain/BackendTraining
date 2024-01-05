# Remember paranthesis is used to call function
def dec(func):
    print (" In outter function")
    def new_func():                               # a new function which... in one way modifies the original function 
        print (" In inner function")
        func()
    return new_func

def test_func():
    print("Hello Shrey")

test_func = dec(test_func)                      # This is the main thing, basically this line is the decorator 
test_func()                                     # Now test_function has the return value of dec which is also a function.


#                          Decorator is nothing more than calling a function with taking the function below as perameter and assigning 
#                                                      function below the return value of function called

@dec                                             # The function just below is the only argument a decorator takes
def test_func2():
    print("Hello Shrey")

test_func2()                                # A decorator only takes a function as an argument but can convert function below to any dataType