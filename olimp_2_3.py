volume = []
while True:
    a = int(input())
    if a == 0:
        break
    volume.append(a)
min_volume = min(volume)
max_volume = max(volume)
range = max_volume - min_volume
print(range)

