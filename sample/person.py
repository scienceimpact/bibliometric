import csv
from pprint import pprint
from collections import defaultdict
import sys
import matplotlib.pyplot as plt

person = {}

#
# read person data
#
with open('xd_persons.txt', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter='|')

    for entry in data:
        person[entry[0]] = {
            'number': entry[0],
            'firstname': entry[1],
            'middlename': entry[2],
            'lastname': entry[3],
            'organization': entry[4]
        }
        
# pprint (person)


#
# count lastname, firtsname, combined name
#
from collections import Counter

data = {}

kind = ["Firstname",
        "Lastname",
        "F Lastname",
        "F M Lastname",
        "Firstname Lastname",
        "Firstname Middlename Lastname"]
         
#        "Firstname Middlename Lastname Org"]

for graph in kind:
    data[graph] = []

pprint (data)

for entry in person:
    data["Lastname"].append(person[entry]['lastname'])
    data["Firstname"].append(person[entry]['firstname'])
    data["Firstname Lastname"].append(person[entry]['firstname'] + " " + person[entry]['lastname'])    
    data["Firstname Middlename Lastname"].append(person[entry]['firstname'] + " " + person[entry]['middlename'] + " " + person[entry]['lastname'])
#    data["Firstname Middlename Lastname Org"].append(person[entry]['firstname'] + " " + person[entry]['middlename']    + " " + person[entry]['lastname'] + " " + person[entry]['organization']) 
    data["F Lastname"].append(person[entry]['firstname'][0] + " " + person[entry]['lastname'])

    initial = person[entry]['middlename']
    if len(initial) > 0:
        initial = person[entry]['middlename'][0]
        
    data["F M Lastname"].append(person[entry]['firstname'][0] + " " + initial + " " + person[entry]['lastname'])            


def find_frequency(entries):
    freqs = Counter(entries)
    return sorted(freqs.items(), key=lambda i: i[1])


def get_freq_vector(freqs):
    vector = []
    for name in freqs:
        vector.append(name[1])
    return vector


def add_to_plot(entries, label=None):
    plt.plot(sorted(entries, reverse=True), label=label)
    

for graph in kind:
    print 70 * "+"
    print find_frequency(data[graph])
    add_to_plot(get_freq_vector(find_frequency(data[graph])), label=graph)

plt.legend()
plt.title("Name Ambiguity in XSEDE Data")
plt.xlabel("Unique Name")
plt.ylabel("Frequency")
plt.yscale('log')
plt.xscale('log')
plt.show()

