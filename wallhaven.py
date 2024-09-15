import os

def wallhaven_dl(id):
    os.system(f"curl -o wallhaven-{id}.jpg https://w.wallhaven.cc/full/{id[:2:]}/wallhaven-{id}.jpg")

ids = []
while True:
    inp = input("Enter url or 'N' to stop:")
    if inp == 'N':
        break
    ids.append(inp[-6::])

for id in ids:
    wallhaven_dl(id)