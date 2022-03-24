ids = [line.strip() for line in open('Week2- Complexities\Ids.in')]
print(ids)

details = [list(line.strip().split(",")) for line in open('Week2- Complexities\Details.in')]
print(details)

map = []
# mapping each key to the details
for i in range(len(ids)):
    for j in range(len(details)):
        if ids[i] in details[j]:
            map.append(",".join(str(x) for x in details[j]))

with open(r'Week2- Complexities\results.out', 'a') as the_file:
    for string in map:
        the_file.write('{}\n'.format(string))
print(map)