import warnings

def deprecated(since=None, message=None, removal=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if since is not None:
                warnings.warn(f"Function {func.__name__} is deprecated since version {since}.", DeprecationWarning)
                print("**************************************")
            if message is not None:
                warnings.warn(message, DeprecationWarning)
                print("**************************************")

            if removal is not None:
                warnings.warn(f"It will be removed in version {removal}.", DeprecationWarning)
                print("**************************************")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@deprecated(since="0.3.0", message="This function is deprecated and will be removed in the next version.")
def my_function():
    print("This is a deprecated function.")

my_function()
print("成功运行，只是一个警告")