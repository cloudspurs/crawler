import json

with open('../temp.json', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(type(line))
    print(line)
    jo = json.loads(line)
    print(jo)
    print(jo['title'])

    # while line:
    #     jo = json.dumps(line)
    #     print(jo)
    #     line = f.readline()
