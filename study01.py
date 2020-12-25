def sum_many(*args):        # 여러개의 인자를 한번에 받을수있다. 그때그때 다른 개수 가능
    sum = 0 
    for i in args:
        sum = sum + i
    return sum

a = sum_many(1,2,3)
b = sum_many(3,4,5,6,7,8)

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k=="name"):
            print("당신의 이름은: " + k)

print(print_kwargs(name="kyunghun", b="2"))