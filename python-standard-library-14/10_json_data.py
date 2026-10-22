import json

data = {"next_id": 2, "expenses": [{"id": 1, "amount": 850}]}
text = json.dumps(data)
print(text)

back = json.loads(text)
print(back["expenses"][0]["amount"])
#json.dump and json.load (without the s) do the same thing, but write to and read from a file directly.