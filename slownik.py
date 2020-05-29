slow = { "tworzyc" : "create",
    "laczyc" : "merge",
    "podstawa" : "basic",
    "matematyka" : "math",
    "fizyka" : "physics",
    "wf" : "PE",
    "chemia" : "chemistry",
    "licencja" : "license",
    "rower" : "bike",
    "mleko" : "milk"
}
print ("Podaj slowo ktore chcesz przetlumaczyc:")
word = input()
print ("Twoje slowo to " + word)
#  for word in slow:
#     print (word)

#import pdb; pdb.set_trace()
def is_in_eng(x):
    rt = x in slow
    return rt
def is_in_pol(x):
    rt2 = x in slow.values()
    return rt2
if is_in_eng(word):
    print ("jest po ang")
    print ("Twoje przetlumaczone slowo to:")
    print (slow.get(word))
elif is_in_pol(word):
    print ("jest po polsku")
    print ("Twoje przetlumaczone slowo to:")
    for pol, eng in slow.items():
        if eng == word:
            print (pol)
else:
    print ("nie znam tlumaczenia tego slowa")








# pass


