__author__ = 'patrick'

cities = {
    "CA": "LA",
    "FL": "MI",
    "IL": "CH"
}

states = {
    "Ilinos": "IL",
    "California": "CA",
    "Florida": "FL"
}

for city in cities:
    print "city: %s" % city

for state in states:
    print "state %s" % state
    print "city of state %s : %s" %(state, cities[states[state]])

state = states.get("Texas", None)
# how None in boolean calculation todo need to understand
if not state:
    print "no state Texas existing!"

cities["2"] = "test_number"
#cities[2] = "test_number" will get wrong in iteration as int is not iterable
cities["New York"] = "NY"
#ValueError: need more than 1 value to unpack why??
for city in cities:
    print "city is %s, which is %s" % (city, cities[city])

print cities

del cities["2"]
print(cities)