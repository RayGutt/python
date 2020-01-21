import builtins

fun = input("which function ?")
my_str = getattr(builtins, fun)
print(my_str.__doc__)
