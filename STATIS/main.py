import pandas as pd
import matplotlib.pyplot as plt

# Baca file xlsx
df = pd.read_excel('STATIS2.xlsx')

# Buat grafik teta x, teta y, dan teta z terhadap time dalam satu gambar
plt.figure(figsize=(10, 6))

plt.plot(df['time'], df['teta x'], label='Teta x')
plt.plot(df['time'], df['teta y'], label='Teta y')
plt.plot(df['time'], df['teta z'], label='Teta z')

plt.xlabel('Time')
plt.ylabel('Teta')
plt.title('Grafik Teta x, Teta y, dan Teta z terhadap Time')
plt.legend()

plt.show()

# Buat grafik αx, αy, dan αz terhadap time dalam satu gambar
plt.figure(figsize=(10, 6))

plt.plot(df['time'], df['αx'], label='αx (rad/s^2)')
plt.plot(df['time'], df['αy'], label='αy (rad/s^2)')
plt.plot(df['time'], df['αz'], label='αz (rad/s^2)')

plt.xlabel('Time')
plt.ylabel('α')
plt.title('Grafik αx, αy, dan αz terhadap Time')
plt.legend()

plt.show()
