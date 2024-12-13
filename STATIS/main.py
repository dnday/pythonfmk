import pandas as pd
import matplotlib.pyplot as plt

# Baca file xlsx
df = pd.read_excel('STATIS.xlsx')

# Buat grafik teta x terhadap time
plt.plot(df['time'], df['teta x'])
plt._auto_draw_if_interactive
plt.xlabel('Time')
plt.ylabel('Teta x')
plt.title('Grafik Teta x terhadap Time')
plt.show()

# Buat grafik teta y terhadap time
plt.plot(df['time'], df['teta y'])
plt.xlabel('Time')
plt.ylabel('Teta y')
plt.title('Grafik Teta y terhadap Time')
plt.show()

# Buat grafik teta z terhadap time
plt.plot(df['time'], df['teta z'])
plt.xlabel('Time')
plt.ylabel('Teta z')
plt.title('Grafik Teta z terhadap Time')
plt.show()
