#dictionaries are just key value pairs.

phonebook = {}
phonebook["Nathan"] = 9384775661
phonebook["Kathryn"] = 9384775662
phonebook["Morgan"] = 9384775663
print(phonebook)

#also valid dictionary 
phonebook = {
    "Nathan" : 9384775661,
    "Kathryn" : 9384775662,
    "Morgan" : 9384775663
}
print(phonebook)

#iterating
phonebook = {"Nathan" : 9384775661,"Kathryn" : 9384775662,"Morgan" : 9384775663}
for name, number in phonebook.items():
        print ("Phone number of %s is %d" % (name, number))

#removing
phonebook = {
    "Nathan" : 9384775661,
    "Kathryn" : 9384775662,
    "Morgan" : 9384775663
}
del phonebook["Morgan"]
print(phonebook)

#also valid delete
phonebook = {
    "Nathan" : 9384775661,
    "Kathryn" : 9384775662,
    "Morgan" : 9384775663
}
phonebook.pop("Morgan")
print(phonebook)

#excercise
phonebook = {
    "Nathan" : 9384775661,
    "Kathryn" : 9384775662,
    "Morgan" : 9384775663,
    "Jill" : 947662781
}
phonebook.update({"Jake" : 938273443})
phonebook.pop("Jill")
print(phonebook)

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
