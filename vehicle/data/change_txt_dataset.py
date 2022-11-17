import os

with open('./training.txt', 'w') as out:
    for img in [f for f in os.listdir('./training/train/Vehicle') if f.endswith('png')]:
        out.write('vehicle/data/training/train/Vehicle/' + img + '\n')


with open('./testing.txt', 'w') as out:
    for img in [f for f in os.listdir('./training/val/Vehicle') if f.endswith('png')]:
        out.write('vehicle/data/training/val/Vehicle/' + img + '\n')
