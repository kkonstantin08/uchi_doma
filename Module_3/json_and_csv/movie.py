import json

with open(file='files/movies.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)

name = []
kp = []
for i in range(len(data['docs'])):
    kp.append(data['docs'][i]['rating']['kp'])
    name.append(data['docs'][i]['name'])

new_kp, new_name = zip(*[(b, a) for b, a in sorted(zip(kp, name), reverse=True)])  # Как отсортировать список на основе другого списка?

print(new_kp)
print(new_name)
