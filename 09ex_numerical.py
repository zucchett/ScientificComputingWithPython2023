#!/usr/bin/env python
# coding: utf-8

# 1\. **2D minimization of a six-hump camelback function**
# 
# $$f(x,y) = \left(4-2.1x^2+\frac{x^4}{3} \right) x^2 +xy + (4y^2 -4)y^2$$
# 
# has multiple global and local minima.
# 
# - Find the global minima of this function
# - How many global minima are there, and what is the function value at those points?
# - What happens for an initial guess of $(x, y) = (0, 0)$?
# 
# Hints:
# 
# * Variables can be restricted to $-2 < x < 2$ and $-1 < y < 1$.
# * Use `numpy.meshgrid()` and `pylab.imshow()` to graphically display the regions.
# * Use `scipy.optimize.minimize()`, trying its optional arguments.

# In[1]:

print("************************************1.*************************************************************************")
import matplotlib.pyplot as plt
from scipy import fftpack
import scipy
from matplotlib.colors import LogNorm
import numpy as np
from pylab import meshgrid, cm, imshow, contour, clabel, colorbar
from scipy.integrate import odeint


# In[2]:


def f(z):
    x = z[0]
    y = z[1]
    return (4-(2.1*(x**2))+((x**4)/3))*(x**2)+(x*y)+((4*(y**2))-4)*(y**2)


# In[3]:


x = np.linspace(-2.0, 2.0, 1000)
y = np.linspace(-1.0, 1.0, 1000)
plt.plot(x,f([x, y]))
plt.show()


# In[4]:


X,Y = np.meshgrid(x, y)
Z = f([X, Y])
plt.figure(figsize=(15,10))
res = plt.imshow(Z,cmap='viridis', extent=[-2, 2, -1, 1])
colorbar(res)
plt.show()


# In[5]:


guesses =[[0.1,0.7],[-0.1,-0.7],[2.,0.7],[-2,-0.7]]
for guess in guesses:
    minima = scipy.optimize.minimize(f, guess)
    print("Minimum Coordinates: ", minima.x)
    print("Minimum Values:  ", minima.fun)


# In[6]:


minima = scipy.optimize.minimize(f, [0,0])
print("Minimum Coordinates: ", minima.x)    
print("Minimum Value:  ", minima.fun)
print("************************************2.*************************************************************************")

# 2\. **Non-linear ODE: the damped pendulum**
# 
# The equation of the motion of a forced pendulum, as a function of the angle $\theta$ with the vertical, is given by:
# 
# $$\frac{d^2\theta}{dt^2} = -\frac{1}{Q} \frac{d\theta}{dt} + \frac{g}{l}\sin\theta + d \cos\Omega t$$
# 
# where $t$ is time, $Q$ is the damping factor, $d$ is the forcing amplitude, and $\Omega$ is the driving frequency of the forcing. 
# 
# This second order ODE needs to be written as two coupled first order ODEs by defining a new variable $\omega \equiv d\theta/dt$:
# 
# $$\frac{d\theta}{dt} = \omega$$
# $$\frac{d\omega}{dt} = -\frac{1}{Q}\,\omega + \frac{g}{l}\sin\theta + d \cos\Omega t$$
# 
# Consider the initial conditions $\theta_0 = \omega_0 = 0$, and $l = 10$, $Q = 2.0$, $d = 1.5$, and $\omega = 0.65$.
# 
#  - Solve the ODE with `odeint` over a period of 200 time steps
#  - Create two plots, one of $\theta$ as a function of the time, and $\omega$ as a function of the time
#  - **Optional**: determine if there is a set of parameters for which the motion is chaotic.

# In[7]:


def f(X, t, Q, d, w):
    return(X[1], -1/Q*X[0] + np.sin(X[1]) + d*np.cos(w*t))


# In[8]:


t = np.linspace(0, 125, 200)
x = (0, 0)
Q = 2.0
d = 1.5
w = 0.65
X = odeint(f, x, t, args=(Q,d,w))


# In[9]:


plt.plot(t, X[:, 0], label="omega")
plt.plot(t, X[:, 1], label="theta")
plt.grid()
plt.legend()
plt.show()
print("************************************3.*************************************************************************")

# 3\. **FFT of a simple dataset**
# 
# Perform a periodicity analysis on the lynxs-hares population, i.e. determine what is the period of the population of these animals.
# 
# The dataset is the one downloaded at the beginning of Lecture 06:
# 
#  - `!wget https://www.dropbox.com/s/ebe1cnyd2gm836a/populations.txt -P data/`

# In[11]:


get_ipython().system('wget https://www.dropbox.com/s/ebe1cnyd2gm836a/populations.txt -P data/')


# In[14]:


year, hare, lynx, carrot = np.loadtxt('data/populations.txt').T

plt.plot(year, hare , label = 'Hares') 
plt.plot(year, lynx , label = 'Lynxs') 
plt.plot(year, carrot , label = 'Carrots') 
plt.xlabel('Year')
plt.ylabel('Population Count')
plt.legend()
plt.show()


# In[15]:


FFT_hare = fftpack.fft(hare)
FFT_lynx = fftpack.fft(lynx)
FFT_carrot = fftpack.fft(carrot)
f = fftpack.fftfreq(year.size)


# In[16]:


plt.plot(f, np.abs(FFT_hare), label = 'Hares')
plt.plot(f, np.abs(FFT_lynx), label = 'Lynxs')
plt.plot(f, np.abs(FFT_carrot), label = 'Carrot')
plt.xlabel('Frequency (Hz)')
plt.xlim([0, 0.5])
plt.legend()
plt.show()

print("************************************4.*************************************************************************")
# 4\. **FFT of an image**
# 
# Write a filter that removes the periodic noise from the `moonlanding.png` image by using a 2-dimensional FFT.
# 
# * Import the image as a 2D numpy array using `plt.imread("images/moonlanding.png")`. Examine the image with `plt.imshow()`, which is heavily contaminated with periodic noise.
# * Check the documentation of the `scipy.fftpack` package, and find the method that performs a 2D FFT. Plot the spectrum (Fourier transform of) the image. **Hint**: use `LogNorm` to plot the colors in log scale:
# ```Python
# from matplotlib.colors import LogNorm
# plt.imshow(image, norm=LogNorm(vmin=5))
# ```
# * Inspect the spectrum, and try to locate the 2D regions of the power spectrum that contain the signal and those which contain the periodic noise. Use array slicing to set the noise regions to zero.
# * Apply the inverse Fourier transform to plot the resulting image.

# In[18]:


image = plt.imread("images/moonlanding.png")
plt.imshow(image, cmap='gray')


# In[19]:


image_fft = fftpack.fft2(image)
plt.imshow(np.abs(image_fft), norm = LogNorm(vmin=5), cmap='gray')


# In[20]:


image_fft[np.abs(image_fft) > 2500] = 0
plt.imshow(np.abs(image_fft), cmap='gray')


# In[21]:


filtered_image = fftpack.ifft2(image_fft).real
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')


# In[ ]:




