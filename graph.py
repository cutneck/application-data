import matplotlib
import matplotlib.pyplot as plt
import numpy as np

end_price = np.array([9981.78, 10230.47, 9651.77, 19498.57, 20007.07, 20215.97, 20021.27])
day_offer = np.arange(1, len(end_price) + 1, 1)


#Настрйока ввывода графика(Qt5, wxPython, Tkinter)
matplotlib.use('Qt5Agg')# Использую wxPython
print(matplotlib.get_backend())
fig = plt.figure(figsize=(6, 4))


# Гистограмма
ax1 = plt.subplot(1,2,1) # Создание осей координат
plt.yticks(np.arange(9000, int(max(end_price)),200), size=10)
ax1.bar(day_offer, end_price)
plt.grid()

# Линейный график
ax2 = plt.subplot(1,2,2 ) # Создание второй оси координат
plt.yticks(np.arange(5000, int(max(end_price)),200), size=10)
plt.grid()

plt.plot(day_offer, end_price, 'r--o')
plt.show()
