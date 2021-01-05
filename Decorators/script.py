### Decorators

user = {"username": "markus", "access_level": "addmin"}

def user_has_permission(func):
    if user.get("access_level") == "admin":
        return func
    raise RuntimeError
    
def myfunction():
    return "Password is 1234"

my_secure_function = user_has_permission(myfunction)
my_secure_function()
