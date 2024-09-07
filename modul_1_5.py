immutable_var = (3, 7, 'f', 'k')
print(immutable_var)
immutable_var[3] =100
print(immutable_var)
#Это невозможно, т к кортеж не поддерживает изменение элементов внутри него
mutable_list =[1, 5, 'g', 'a']
print(mutable_list)
mutable_list[1] = 100
print(mutable_list)
