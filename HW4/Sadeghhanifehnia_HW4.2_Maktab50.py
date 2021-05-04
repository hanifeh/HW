scores = {'Art':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 4},
               {'first_name': 'Mary', 'last_name': 'Hernandez', 'score': 3}],
          'Math':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 1},
               {'first_name': 'Maria', 'last_name': 'Garcia', 'score': 2},
               {'first_name': 'Mary', 'last_name': 'Hernandez', 'score': 3}],
          'Literature':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 3},
               {'first_name': 'Maria', 'last_name': 'Garcia', 'score': 4},
               {'first_name': 'Mary', 'last_name': 'Hernandez', 'score': 1},
               {'first_name': 'James', 'last_name': 'Johnson', 'score': 2}],
          'Physics':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 4}],
          'Chemistry':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 2},
               {'first_name': 'James', 'last_name': 'Johnson', 'score': 3}]}

dict1 = {}
dict2 = {}
dict3 = {}
for i in scores:
    dict1[i] = [(n['score']) for n in scores[i]]
print(dict1)

for i in scores:
    for n in scores[i]:
        if n['first_name'] + ' ' + n['last_name'] in dict2:
            dict2.get(n['first_name'] + ' ' + n['last_name']).append(n['score'])
        else:
            dict2[n['first_name'] + ' ' + n['last_name']] = [n['score']]
print(dict2)

for i in scores:
    for n in scores[i]:
        if n['first_name'] + ' ' + n['last_name'] in dict3:
            dict3.get(n['first_name'] + ' ' + n['last_name']).update({i: n['score']})
        else:
            dict3[n['first_name'] + ' ' + n['last_name']] = {i: n['score']}
print(dict3)
for item in scores:
    print(item)