import random

name = "rk_"

for i in range(1, 10000):
    if i < 10:
        file_name = name + "000" + str(i) + ".py"
        with open(file_name, "w") as file:
            pass
        print(file_name)
    elif i < 100:
        file_name = name + "00" + str(i) + ".py"
        filename = name + str(i) + ".py"
        with open(file_name, "w") as file:
            pass
    elif i < 1000:
        file_name = name + "0" + str(i) + ".py"

    else:
        file_name = name + str(i) + ".py"


'''
万恶之源_rk
'''
