from functools import wraps

def validate_details(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        print("validator running")
        return func(*args,**kwargs)
    return decorator        