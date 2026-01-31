my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

contact_info = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-8765"
}
#print(contact_info)

alice_phone = contact_info["Alice"]
print("Alice's phone number is:", alice_phone)

bob_phone = contact_info["Bob"]
print("Bob's phone number is:", bob_phone)

contact_info["Alice"] = "555-4321"
print("Alice's phone number is:", contact_info["Alice"])

#Add new entry:
contact_info["Eve"] = "555-5678"
print(contact_info)

#Delete entry:
del contact_info["Bob"]
print(contact_info)

#Get all keys:
keys = contact_info.keys()
print(keys)

#Values:
values = contact_info.values()
print(values)

#Get all items
items = contact_info.items()
print(items)

#Dictionary methods:

#clear() - removes all items from the dictionary.
#copy() - returns a shallow copy of the dictionary.
#get() - returns the value for a specified key.
#items() - returns a view object of the dictionary's key-value pairs.
#keys() - returns a view object of the dictionary's keys.
#pop() - removes the item with the specified key and returns its value.
#popitem() - removes and returns the last inserted key-value pair.
#update() - updates the dictionary with elements from another dictionary or iterable.
#values() - returns a view object of the dictionary's values.

contact_infornation = {
    "Alice": {
        "phone_number": "555-1234",
        "email": "alice@gmail.com",
        "home_address": "123 Main St",
        "birthdate": "1992/05/15"
    }

}
print(contact_infornation)