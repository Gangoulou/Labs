import math
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

T0 = 30  # End temperature
delta_t = 1  # Time interval
r = .12
n = 2
m = 100

T = {}
t = {}

T[0] = 100  # Start temperature
t[0] = 0

i = 0

# Euler Method
while 1:
    T[i + 1] = T[i] - r * (T[i] - T0) * delta_t
    t[i + 1] = t[i] + delta_t
    print(T[i + 1] - T[i])

    if math.fabs(T[i + 1] - T[i]) <= 0.05:
        break
    i += 1

T1 = [0 for i in range(len(T))]
t1 = [0 for i in range(len(t))]

for i in range(0, len(T)):
    T1[i] = T[i]
    t1[i] = t[i]

plt.plot(t1, T1, "-")
plt.xlabel("Time")
plt.ylabel("Temperatue")
plt.title("Approximate solution for coffee problem")
plt.show()
