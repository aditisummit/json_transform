import jsonpatch
import json


with open(r'spread_template_business(1).json') as f1:
  data1 = json.load(f1)

with open(r'spread_template_business(2).json') as f2:
  data2 = json.load(f2)

patch = jsonpatch.JsonPatch.from_diff(data1,data2)
print(patch)

final = patch.apply(data1)
finalprint=json.dumps(final)

print(finalprint)
