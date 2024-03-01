#Introduction to programming':Task 7
#Tsadzikidze Arsen, FB-24, 26
print('Introduction to programming:Task 7')
print('Tsadzikidze Arsen, 26')

import pandas as pd
import matplotlib.pyplot as plt

def plot_sunspots_first_1000():
    data = pd.read_csv('sunspots.txt', delimiter='\s+', header=None, names=['Month', 'Sunspots'])

    plt.plot(data['Month'][:1000], data['Sunspots'][:1000])
    plt.xlabel('Місяць')
    plt.ylabel('Кількість затемнень')
    plt.title('Кількість сонячних затемнень за місяць (перші 1000 значень)')
    plt.show()

plot_sunspots_first_1000()

