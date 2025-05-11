# 假设数据，单位统一为：质量g，温度°C，比热J/(g·°C)
# 可根据实际实验数据替换

# 容器和搅拌器
m1 = 106.34   # 内筒质量
m2 = 8.60    # 搅拌器质量
c1 = 0.385      # 内筒比热容
c2 = 0.370      # 搅拌器比热容

# 水的质量（m 水本身质量，m + m1 为容器中水和内筒的总质量）
m = 279.78-106.34-8.6    # 初始水的质量
c=4.1868
theta_1 = 33.8  # 初始水温
theta_2 = 10.2  # 平衡温度

# 冰块
theta_0_prime = 0.0  # 冰的初始温度
theta_0 = 0.0         # 冰的溶解温度（0°C）
c_ice = 2.1           # 冰的比热容 J/(g·°C)

# 总质量（溶解后测得），减去原系统质量，得冰质量
total_mass = 338.97  # 加冰后总质量
m_ice = total_mass - (m + m1 + m2)

# 计算冰的溶解热 λ
numerator = m*c* (theta_1 - theta_2) + m1 * c1 * (theta_1 - theta_2) + m2 * c2 * (theta_1 - theta_2)
lambda_ice = numerator / m_ice  -c*theta_2# 单位：J/g

# 输出结果
print(f"冰的质量: {m_ice:.2f} g")
print(f"冰的溶解热 λ ≈ {lambda_ice:.2f} J/g")


# 假设数据，单位统一为：质量g，温度°C，比热J/(g·°C)
# 可根据实际实验数据替换

# 容器和搅拌器
m1 = 107.38   # 内筒质量
m2 = 9.40    # 搅拌器质量
c1 = 0.385      # 内筒比热容
c2 = 0.370      # 搅拌器比热容

# 水的质量（m 水本身质量，m + m1 为容器中水和内筒的总质量）
m = 269.57-m1-m2    # 初始水的质量
c=4.1868
theta_1 = 33.7  # 初始水温
theta_2 = 6.8  # 平衡温度

# 冰块

# 总质量（溶解后测得），减去原系统质量，得冰质量
total_mass = 326.89  # 加冰后总质量
m_ice = total_mass - (m + m1 + m2)

# 计算冰的溶解热 λ
numerator = m*c* (theta_1 - theta_2) + m1 * c1 * (theta_1 - theta_2) + m2 * c2 * (theta_1 - theta_2)
lambda_ice = numerator / m_ice  -c*theta_2# 单位：J/g

# 输出结果
print(f"冰的质量: {m_ice:.2f} g")
print(f"冰的溶解热 λ ≈ {lambda_ice:.2f} J/g")



# 假设数据，单位统一为：质量g，温度°C，比热J/(g·°C)
# 可根据实际实验数据替换

# 容器和搅拌器
m1 = 107.13   # 内筒质量
m2 = 9.43    # 搅拌器质量
c1 = 0.385      # 内筒比热容
c2 = 0.370      # 搅拌器比热容

# 水的质量（m 水本身质量，m + m1 为容器中水和内筒的总质量）
m = 292.58-m1-m2    # 初始水的质量
c=4.1868
theta_1 = 33.7  # 初始水温
theta_2 = 11.2  # 平衡温度

# 冰块

# 总质量（溶解后测得），减去原系统质量，得冰质量
total_mass = 342.62  # 加冰后总质量
m_ice = total_mass - (m + m1 + m2)

# 计算冰的溶解热 λ
numerator = m*c* (theta_1 - theta_2) + m1 * c1 * (theta_1 - theta_2) + m2 * c2 * (theta_1 - theta_2)
lambda_ice = numerator / m_ice  -c*theta_2# 单位：J/g

# 输出结果
print(f"冰的质量: {m_ice:.2f} g")
print(f"冰的溶解热 λ ≈ {lambda_ice:.2f} J/g")