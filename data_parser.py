file = open('data.txt', 'r')
lines = file.readlines()
data = [line.replace('\n', '').replace('ACC:', '')
            .replace('#', ',')
            .replace('DT:', '')
            .replace('GYR:', '')
            .replace('FIL:', '')
            .split(',') for line in lines]
for datum in data:
    print(datum)

