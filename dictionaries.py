d = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
}

print(d['key1'])
print(d['key2'])
# print(d['key4'])

print('key1' in d)
print('key4' in d)

print(d.get('key4', 'default'))

value = d.get('key4')
if value:
    print(value)
else:
    print("key4 dose not exist!")

for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)
