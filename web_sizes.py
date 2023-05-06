import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum = 0
empty_sites = 0

# testing raw data:
""" print(sites[0])
print(sites_new[0:2])
for e in sites_new[0:12]:
    print(e)

print(sites[0]['size'])

for index in range(0, len(sites)):
    print(sites[index]['size'], sites_new[index]['size']) """

# 1. Feladat 5 pont

for index in range(0, len(sites_new)):
    sum = sum + sites[index]['size']

sum = round((sum / 1024), 2)
avg = round(sum / len(sites_new), 2)
print(sum)
print(avg)

# 2. Feladat - 10 pont

for index in range(0, len(sites)):
    if sites[index]['size'] != sites_new[index]['size']:
        diff = sites_new[index]['size'] - sites[index]['size']
        diff_ratio = round(diff / (sites_new[index]['size'] / 100), 2)
        if diff_ratio > 0:
            print(f"{sites[index]['domain']} changed by: +{diff_ratio} %")
        else:
            print(f"{sites[index]['domain']} changed by: {diff_ratio} %")
    else:
        pass

# 3. Feladat - 5 pont

empty_sites = 0

for index in range(0, len(sites_new)):
    if sites_new[index]['size'] == 0:
        empty_sites = empty_sites + 1
    else:
        pass

print(f"there are {empty_sites} empty sites")

# 4. Feladat - 10 pont

for index in range(0, len(sites_new)):
    if sites_new[index]['size'] == 0:
        pass
    elif sites_new[index]['size'] < 1024:
        print(f"{sites[index]['domain']} is: {sites_new[index]['size']} Mb")
    else:
        print(
            f"{sites[index]['domain']} is: {round(sites_new[index]['size']/1024, 2)} Gb"
        )
