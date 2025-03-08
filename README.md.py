# dictionary
#dictionary
capitals = {"usa": "washington dc",
"india": "new delhi",
"china": "beijing",
"russia": "moscow"
}

#to get value
print(capitals.get("usa"))
#to update
capitals.update({"japan": "tokyo"})
print(capitals)
capitals.update({"usa": "texas"})
print(capitals)
#to remove
capitals.pop("india")
print(capitals)
#to pop the latest one
capitals.popitem()
print(capitals)
#to clear
capitals.clear()
print(capitals)
#for keys only 
keys = capitals.keys()
print(keys)
#to get values only
values_only = capitals.values()
print(values_only)
#for items
items = capitals.items()
print(items)
