def normal_func(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)


normal_func("python", 1, 3)

# 使用*args
print('######使用*args')
args_list = ("python", 1, 3)
normal_func(*args_list)

# 使用**kwargs
print('######使用**kwargs')
kwargs_dict = {"arg3": 3, "arg1": "python", "arg2": 1}
normal_func(**kwargs_dict)
