import matplotlib.pyplot as plt
import numpy as np

# 示例数据
t = np.arange(0, 230, 10)
temperature = [
    33.7,29.1,25.4,23,19.9,17.8,16.3,
    14.8,13.6,12.5,11.8,11.0,10.3,
    9.9,9.4,8.8,8.6,8.3,7.7,
    7.5,7.5,7.2,6.7
]

# 环境温度
theta_e = 14

# 转为 NumPy 数组方便处理
temperature = np.array(temperature)

# 画图
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(t, temperature, label="Temperature over Time", color="blue", linewidth=2)
ax.axhline(y=theta_e, color="red", linestyle="--", label=r"Environment Temp $\theta_e$")

# 阴影区域
above_theta = temperature > theta_e
below_theta = temperature < theta_e
ax.fill_between(t, temperature, theta_e, where=above_theta, interpolate=True,
                color="skyblue", alpha=0.5, label=r"$S_A$")
ax.fill_between(t, temperature, theta_e, where=below_theta, interpolate=True,
                color="orange", alpha=0.5, label=r"$S_B$")

# 设置刻度（主刻度和副刻度）
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# X轴：主刻度每10s，副刻度每1s
ax.set_xlim(0, 230)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(1))

# Y轴：主刻度每1°C，副刻度每0.1°C
ax.set_ylim(4, 42)
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# 网格线
ax.grid(True, which='major', linestyle='--', linewidth=0.6)
ax.grid(True, which='minor', linestyle=':', linewidth=0.3, alpha=0.6)

# 轴标签、标题
ax.set_xlabel("Time $t$ (s)", fontsize=12)
ax.set_ylabel("Temperature $\\theta$ (°C)", fontsize=12)
ax.set_title("Heat of Fusion: Temperature vs. Time", fontsize=14)

# 图例
ax.legend(loc="upper right", fontsize=10)

# 面积估算（按格子面积）
grid_area = 10 * 1  # 大格子面积：10s × 1°C
sa_area = np.trapz(np.maximum(temperature - theta_e, 0), t)
sb_area = np.trapz(np.maximum(theta_e - temperature, 0), t)
sa_boxes = round(sa_area / grid_area)
sb_boxes = round(sb_area / grid_area)

# 添加面积说明
ax.text(3, 19, rf"$S_A \approx$ {sa_boxes} squares", fontsize=10, color="blue")
ax.text(140, 15, rf"$S_B \approx$ {sb_boxes} squares", fontsize=10, color="darkorange")

plt.tight_layout()
plt.show()

t = np.arange(0, 330, 10)
temperature = [
    33.7,30,29.6,26.4,21.4,20.3,20,19.6,
    19.4,18.1,17.1,16.2,15.4,15.0,
    14.8,14.5,14.1,13.9,13.7,13.3,
    13.1,12.6,12.2,12.0,11.7,11.7,
    11.7,11.4,11.2,11.2,11.1,10.6,10.2


]

# 环境温度
theta_e = 17

# 转为 NumPy 数组方便处理
temperature = np.array(temperature)

# 画图
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(t, temperature, label="Temperature over Time", color="blue", linewidth=2)
ax.axhline(y=theta_e, color="red", linestyle="--", label=r"Environment Temp $\theta_e$")

# 阴影区域
above_theta = temperature > theta_e
below_theta = temperature < theta_e
ax.fill_between(t, temperature, theta_e, where=above_theta, interpolate=True,
                color="skyblue", alpha=0.5, label=r"$S_A$")
ax.fill_between(t, temperature, theta_e, where=below_theta, interpolate=True,
                color="orange", alpha=0.5, label=r"$S_B$")

# 设置刻度（主刻度和副刻度）
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# X轴：主刻度每10s，副刻度每1s
ax.set_xlim(0, 450)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(1))

# Y轴：主刻度每1°C，副刻度每0.1°C
ax.set_ylim(4, 42)
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# 网格线
ax.grid(True, which='major', linestyle='--', linewidth=0.6)
ax.grid(True, which='minor', linestyle=':', linewidth=0.3, alpha=0.6)

# 轴标签、标题
ax.set_xlabel("Time $t$ (s)", fontsize=12)
ax.set_ylabel("Temperature $\\theta$ (°C)", fontsize=12)
ax.set_title("Heat of Fusion: Temperature vs. Time", fontsize=14)

# 图例
ax.legend(loc="upper right", fontsize=10)

# 面积估算（按格子面积）
grid_area = 10 * 1  # 大格子面积：10s × 1°C
sa_area = np.trapz(np.maximum(temperature - theta_e, 0), t)
sb_area = np.trapz(np.maximum(theta_e - temperature, 0), t)
sa_boxes = round(sa_area / grid_area)
sb_boxes = round(sb_area / grid_area)

# 添加面积说明
ax.text(3, 19, rf"$S_A \approx$ {sa_boxes} squares", fontsize=10, color="blue")
ax.text(140, 15, rf"$S_B \approx$ {sb_boxes} squares", fontsize=10, color="darkorange")

plt.tight_layout()
plt.show()


t = np.arange(0, 150, 10)
temperature = [
    33.7,29.3,26.0,22.6,20.0,17.5,15.4,
    14.4,13.3,12.6,12.2,12.1,11.7,
    11.3,11.2


]

# 环境温度
theta_e = 17

# 转为 NumPy 数组方便处理
temperature = np.array(temperature)

# 画图
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(t, temperature, label="Temperature over Time", color="blue", linewidth=2)
ax.axhline(y=theta_e, color="red", linestyle="--", label=r"Environment Temp $\theta_e$")

# 阴影区域
above_theta = temperature > theta_e
below_theta = temperature < theta_e
ax.fill_between(t, temperature, theta_e, where=above_theta, interpolate=True,
                color="skyblue", alpha=0.5, label=r"$S_A$")
ax.fill_between(t, temperature, theta_e, where=below_theta, interpolate=True,
                color="orange", alpha=0.5, label=r"$S_B$")

# 设置刻度（主刻度和副刻度）
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# X轴：主刻度每10s，副刻度每1s
ax.set_xlim(0, 160)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(1))

# Y轴：主刻度每1°C，副刻度每0.1°C
ax.set_ylim(4, 42)
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# 网格线
ax.grid(True, which='major', linestyle='--', linewidth=0.6)
ax.grid(True, which='minor', linestyle=':', linewidth=0.3, alpha=0.6)

# 轴标签、标题
ax.set_xlabel("Time $t$ (s)", fontsize=12)
ax.set_ylabel("Temperature $\\theta$ (°C)", fontsize=12)
ax.set_title("Heat of Fusion: Temperature vs. Time", fontsize=14)

# 图例
ax.legend(loc="upper right", fontsize=10)

# 面积估算（按格子面积）
grid_area = 10 * 1  # 大格子面积：10s × 1°C
sa_area = np.trapz(np.maximum(temperature - theta_e, 0), t)
sb_area = np.trapz(np.maximum(theta_e - temperature, 0), t)
sa_boxes = round(sa_area / grid_area)
sb_boxes = round(sb_area / grid_area)

# 添加面积说明
ax.text(3, 19, rf"$S_A \approx$ {sa_boxes} squares", fontsize=10, color="blue")
ax.text(140, 15, rf"$S_B \approx$ {sb_boxes} squares", fontsize=10, color="darkorange")

plt.tight_layout()
plt.show()