# 01 - Import Modules/Lib/Packages
# !pip install matplotlib
from numpy import random
import matplotlib.pyplot as plt
import statistics



# 02 - Globals Variables
m, s, n = 10, 0.3, 5_000
path = r'C:\Users\tcunh\Downloads\Belugas_data.txt'

fig = {
    'name': 'Figure_4',
    'title': 'Scatter'
}



# 03 - Create data for exercise
liver, tooth = [], []
with open(path) as f:
    for row in f.readlines()[1:]:
        a, b = row.split(',')
        liver.append(float(a))
        tooth.append(float(b))


print(f'r={statistics.correlation(liver, tooth):0.3f}')


# 04 - Create figure
## Passo 1: Canvas
plt.figure()

## Passo 2: Elementos
plt.scatter(liver, tooth)

plt.title(fig.get('title'))
plt.xlabel('Liver')
plt.ylabel('Tooth')

## Passo 3: Mostrar ou Gravar
plt.savefig(fig.get('name', 'Figura_A'))