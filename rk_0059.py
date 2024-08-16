class CallableClass:
    def __call__(self):
        print("I'm callable!")

callable_instance = CallableClass()
callable_instance()