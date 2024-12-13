import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('dual sensor dinamis.xlsx')
plt.plot(data['time'], data['momentum'])
plt.xlabel('time')
plt.ylabel('momentum')
plt.title('Momentum vs Time')
plt.show()

plt.plot(data['time'], data['wx (deg)'], label='wx (deg)')
plt.plot(data['time'], data['wy (deg)'], label='wy (deg)')
plt.plot(data['time'], data['wz (deg)'], label='wz (deg)')
plt.xlabel('time')
plt.ylabel('w (deg)')
plt.title('wx, wy, wz vs Time')
plt.legend()
plt.show()

plt.plot(data['time'], data['wx'], label='wx')
plt.plot(data['time'], data['wy'], label='wy')
plt.plot(data['time'], data['wz'], label='wz')
plt.xlabel('time')
plt.ylabel('w (rad/s)')
plt.title('wx, wy, wz vs Time')
plt.legend()
plt.show()