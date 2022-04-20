import json
ready = ''
with open('Alphabet.json', 'r') as key:
    work = json.load(key)
with open('Abracadabra.txt', 'r') as value:
    text = value.read()
for i in text:
    if i in work.keys():
        for key, value in work.items():
            if key == i:
                ready += value
    else:
        ready += i
print(ready)