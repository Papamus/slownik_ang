import random
# print (random.random())
a = random.randint(0,20)
print ("Zgadnij liczbe od 0 do 20")
b = int(input())
# import pdb; pdb.set_trace()
while a!=b:
    if b > a:
        print ("Twoja liczba jest za mala, probuj dalej")
    elif b < a:
        print ("Twoja liczba jest za mala, probuj dalej")
    else:
        print("GRATULACJE, ZGADLES!")
        pass
    b = int(input())
if b == a:
    print("GRATULACJE, ZGADLES!")
    





