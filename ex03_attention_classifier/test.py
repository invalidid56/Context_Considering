import json

data = []
with open('/media/invalidid/COMMON/DATA/ConCon/ex03/0.json') as f:
    data = json.load(f)
# ㅣ렇게 하며 ㄴ될듯
print(data[0]['id'])