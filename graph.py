import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator,IndexLocator,LogLocator, MaxNLocator
import numpy as np

end_price = np.array([9981.78, 10230.47, 9651.77, 19498.57, 20007.07, 20215.97, 20021.27,20494.24, 20544.72,19954.94, 20526.96, 21054.76,
                      21195.94, 22122.78, 22267.13, 22574.48, 22413.88,22136.33])
day_offer = np.arange(1, len(end_price) + 1, 1)
count_day_offer = len(day_offer)

#Настрйока ввывода графика(Qt5, wxPython, Tkinter)
matplotlib.use('Qt5Agg')# Использую PyQT5
print(matplotlib.get_backend())

fig = plt.figure(figsize=(14, 5))
nl = NullLocator()  #Используется для скрытия делений по определеной оси(x, y)
ll = LinearLocator() # Используется для задания определенного числа меток по выбранной оси
ml1 = MultipleLocator() # Изменяет шаг  значений между рисками делений
ml2 = MultipleLocator()
idx = IndexLocator(base=100, offset=0)


# Гистограмма
ax1 = plt.subplot(1,2,1) # Создание осей координат
ax1.set(xlim=(0, count_day_offer + 1), ylim=(9500, 25000)) # Устанавливает границиные значения
plt.yticks(np.arange(9000, int(max(end_price)),100), size=10) 
ax1.bar(day_offer, end_price)
ax1.xaxis.set_major_locator()
ax1.yaxis.set_major_locator(IndexLocator(base=100, offset=0))
ax1.yaxis.set_major_locator(MaxNLocator(25))
plt.grid()



# Линейный график
ax2 = plt.subplot(1,2,2 ) # Создание второй оси координат
ax2.set(xlim=(0, len(end_price)), ylim=(int(min(end_price)), int(max(end_price))))
plt.yticks(np.arange(9000, int(max(end_price)),200), size=10)
ax2.xaxis.set_major_locator(MaxNLocator())
ax2.yaxis.set_major_locator(IndexLocator(base=100, offset=0))
ax2.yaxis.set_major_locator(MaxNLocator(40))
plt.grid()


plt.plot(day_offer, end_price, 'r-o')
plt.show()