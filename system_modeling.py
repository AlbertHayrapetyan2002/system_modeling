import math as mt
#հենքային հավասարաչափ թվերի ստացումը [0,1] միջակայքում
def randomizing(first_value, num_of_characters, t_variable):
    mods_meaning = 2 ** num_of_characters
    lambda_variable = (8 * t_variable) - 3
    list_of_our_variables = [first_value/mods_meaning]
    for i in range(num_of_characters):
        our_value =  (first_value * lambda_variable) % mods_meaning
        list_of_our_variables.append(our_value/mods_meaning)
        first_value = our_value
    return list_of_our_variables

first_value = int(input("first_value="))
num_of_characters = int(input("num_of_characters="))
t_variable = int(input("t_variable="))


our_variable = randomizing(first_value,num_of_characters,t_variable)
print("r_variables=",our_variable)

# հավասարաչափ բաշխման օրենք
def equality_law():
    a=eval(input("a="))
    b=eval(input("b="))
    if 0<=a<=b:
        x_equal_list=[]
        for i in range(len(our_variable)):
            x_equal_list.append(a+(b-a)*our_variable[i])
        return x_equal_list
#ցուցչային բաշխման օրենք
def indicative_low():
    lyamda=eval(input("lyamda="))
    if lyamda>0:
        x_indicative_list=[]
        for i in range(len(our_variable)):
            x_indicative_list.append((-1/lyamda)*mt.log(our_variable[i]))
        return x_indicative_list
#նորմալ բաշխման օրենք
def normal_low():
    myu=eval(input("myu="))
    sigma=eval(input("sigma="))
    s=0
    for i in range(12):
        s+=our_variable[i]
    x_normal_list=[]
    for i in range(len(our_variable)):
        x_normal_list.append(myu+sigma*(s-6))
    return x_normal_list

#Պուասոնյան բաշխում
def Puason():
    lyamda=eval(input("lyamda="))
    i=0
    puason_list=[]
    while i<len(our_variable):
        s=1
        s*=our_variable[i]
        if s<mt.exp(-lyamda):
            puason_list.append(our_variable[i])
            i+=1
        else:
            i+=1
    return puason_list

equality_distribution=equality_law()
print("equality_distribution=",equality_distribution)
indicative_distribution=indicative_low()
print("indicative_distribution=",indicative_distribution)
normal_distribution=normal_low()
print("normal_distribution=",normal_distribution)
Puason_distribution=Puason()
print("Pusaon_distribution=",Puason_distribution)
