#
# Practice Questions
# ver. 1.0.0
# subjt. python based
# langs. python
# maker. ray na
# group. exciting
# dates. 2018. 10. 08.
#

# How many seconds is 1 hour?

# 2.1
minutes_1 = 60

# 2.2
hours_1 = minutes_1 * minutes_1
print("One Hour is", hours_1, "seconds")

# 2.3
seconds_per_hour = hours_1

# 2.4
seconds_per_day = seconds_per_hour * 24
print(seconds_per_day)

# 2.5
print( seconds_per_day/seconds_per_hour )

# 2.6
print( seconds_per_day//seconds_per_hour )



# 3.1 & 3.2
year_lists = [1980, 1981, 1982, 1983, 1984]

# 3.3
year_lists.sort(reverse=True)
print(year_lists[0])

# 3.4
things = ["mozzarella", "cinderalla", "salmonella"]

# 3.5 & 3.6 & 3.7
for i in range(0, 3) :
    things[i] = things[i].capitalize()

print(things)

# 3.8
surprise = ["Groucho", "Chico", "Harpo"]

# 3.9
surprise[2] = surprise[2].lower()
surprise.sort(reverse=True)
surprise[0] = surprise[0].capitalize()

print(surprise)

# 3.10
e2f = {"dog" : "chien", "cat" : "chat", "walrus" : "morse"}

# 3.11
print(e2f.get("walrus"))

# 3.12
f2e = {}
for english, french in e2f.items() :
    f2e[french] = english
print(f2e)

# 3.13
print(f2e.get("chien"))

# 3.14
# set(e2f.keys)

# 3.15
life = {'animals' : { 'cats' : ["Henri", "Grumpy", "Lucy"], 'octipi' : {}, 'emus' : {} }, 'plants' : {}, 'other' : {}}

# 3.16
print(life.keys())

# 3.17
print(life['animals'].keys())

# 3.18
print(life['animals']['cats'])
