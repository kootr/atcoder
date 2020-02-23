import numpy as np

number = np.random.randint(0,100)
if number >= 4:
    number = 4
dict_location = {
    0:'岩手',
    1:'青森',
    2:'沖縄', 
    3:'長野',
    4:'金沢'
    }

print('旅行先は', dict_location[number])