#
# AI
# ver. 1.0.0
# subjt. makes neuron
# langs. python
# maker. ray na
# group. exciting
# dates. 2018. 10. 08.
#

import random

neuron = []
alt = 0

for i in range(0, 10) :
    neuron.append(random.randint(0, 100)) # neuron[]
    alt += neuron[i]


def lead(alt) :
    if alt >= 500 :
        return "Good Study"
    elif alt <= 400 and alt >= 301 :
        return "Nice Study"
    elif alt <= 300 and alt >= 201 :
        return "Not Bad Study"
    elif alt <= 200 and alt >= 101 :
        return "Bad Study"
    else :
        return "Terrible Study"


print("Study Result :", lead(alt), " // value points :", alt)
