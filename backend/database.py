import json

def load_json(path):
    with open(path) as f:
        return json.load(f)

def append_json_line(path, data):
    with open(path, "a") as f:
        f.write(json.dumps(data) + "\n")
