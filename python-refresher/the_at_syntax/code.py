import functools

user = {"username": "jose", "access_level": "admin"}



# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"
def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions"
        
    return secure_function

@make_secure  
def get_admin_password():
    return "1234"

get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
