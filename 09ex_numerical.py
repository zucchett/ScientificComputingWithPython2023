import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.fftpack import fft, fftfreq, fft2, fftshift
from matplotlib.colors import LogNorm

def six_hump_camelback(x):
    return (4 - 2.1 * x[0]**2 + (x[0]**4) / 3) * x[0]**2 + x[0] * x[1] + (-4 + 4 * x[1]**2) * x[1]**2

bounds = [(-2, 2), (-1, 1)]
global_minima = []

for x in np.linspace(-2, 2, 10):
    for y in np.linspace(-1, 1, 10):
        result = minimize(six_hump_camelback, [x, y], bounds=bounds)
        is_new_minimum = True
        for point, value in global_minima:
            if np.allclose(result.x, point, atol=1e-3):
                is_new_minimum = False
                break
        if is_new_minimum:
            global_minima.append((result.x, result.fun))

print("Number of global minima:", len(global_minima))
for i, (point, value) in enumerate(global_minima):
    print(f"Global minimum {i+1} at point {point} has function value: {value}")

x = np.linspace(-2, 2, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = six_hump_camelback([X, Y])

plt.figure()
plt.imshow(Z, extent=[-2, 2, -1, 1], origin='lower', cmap='viridis')
plt.colorbar()
plt.title('Six-Hump Camelback Function Contours')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

##############################END OF 2D minimization of a six-hump camelback function.#######################################

def pendulum_equations(y, t, Q, g, l, d, Omega):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -1 / Q * omega + (g / l) * np.sin(theta) + d * np.cos(Omega * t)
    return [dtheta_dt, domega_dt]

l = 10.0
Q = 2.0
d = 1.5
Omega = 1.0
g = 9.81
theta_0 = 0.0
omega_0 = 0.65

initial_conditions = [theta_0, omega_0]
time = np.linspace(0, 20, 200)
solution = odeint(pendulum_equations, initial_conditions, time, args=(Q, g, l, d, Omega))

plt.figure(figsize=(8, 6))

#theta x time
plt.subplot(2, 1, 1)
plt.plot(time, solution[:, 0])
plt.title('Pendulum Angle (theta) vs Time')
plt.xlabel('Time')
plt.ylabel('Theta')

#omega x time
plt.subplot(2, 1, 2)
plt.plot(time, solution[:, 1])
plt.title('Pendulum Angular Velocity (omega) vs Time')
plt.xlabel('Time')
plt.ylabel('Omega')

plt.tight_layout()
plt.show()

##############################END OF Non-linear ODE: the damped pendulum.#######################################

data = np.loadtxt('populations.txt', skiprows=1)
years = data[:, 0]
hare_population = data[:, 1]
lynx_population = data[:, 2]

hare_fft = fft(hare_population)
power_hare = np.abs(hare_fft)**2
freqs_hare = fftfreq(len(hare_population))

lynx_fft = fft(lynx_population)
power_lynx = np.abs(lynx_fft)**2
freqs_lynx = fftfreq(len(lynx_population))

#ignore zero-frequency component
nonzero_freqs_hare = freqs_hare[1:]
nonzero_power_hare = power_hare[1:]

nonzero_freqs_lynx = freqs_lynx[1:]
nonzero_power_lynx = power_lynx[1:]

#convert dominant frequencies to periods
period_hare = 1 / nonzero_freqs_hare[np.argmax(nonzero_power_hare)]
period_lynx = 1 / nonzero_freqs_lynx[np.argmax(nonzero_power_lynx)]

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.title('FFT Analysis - Hare Population')
plt.plot(freqs_hare, power_hare)
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid()

plt.subplot(2, 1, 2)
plt.title('FFT Analysis - Lynx Population')
plt.plot(freqs_lynx, power_lynx)
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid()

plt.tight_layout()
plt.show()

print(f"Period of hare population: {period_hare} years")
print(f"Period of lynx population: {period_lynx} years")

##############################END OF FFT of a simple dataset.#######################################

image = plt.imread("images/moonlanding.png")

plt.figure(figsize=(6, 6))
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()

image_fft = fft2(image)
image_fft_shifted = fftshift(image_fft)

plt.figure(figsize=(6, 6))
plt.title('FFT Spectrum of the Image')
plt.imshow(np.abs(image_fft_shifted), norm=LogNorm(vmin=5))
plt.colorbar()
plt.axis('off')
plt.show()

noise_threshold = 1500
filtered_fft_shifted = image_fft_shifted.copy()
filtered_fft_shifted[np.abs(filtered_fft_shifted) > noise_threshold] = 0

filtered_image = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_fft_shifted)))

plt.figure(figsize=(6, 6))
plt.title('Filtered Image')
plt.imshow(filtered_image, cmap='gray')
plt.axis('off')
plt.show()

##############################END OF FFT of an image.#######################################