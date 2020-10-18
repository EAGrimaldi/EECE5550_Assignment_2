import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt

class pendulum:
    def __init__(self):
        self.initvals = [0,10]
        self.t = np.linspace(0,10,10000)
        self.odesol = np.array(integ.odeint(self.derfunc, self.initvals, self.t))
    def derfunc(self, y, t):
        g = 32 #gravity
        L = 2 #length of pendulum
        k = 1.2 #pendulum damping factor
        ydot = [0,0]
        ydot[0] = y[1]
        ydot[1] = -(g/L)*np.sin(y[0])-k*y[1]
        return ydot
    def plot(self):
        plt.plot(self.t, self.odesol[:,0], 'r')
        plt.plot(self.t, self.odesol[:,1], 'b')
        plt.suptitle("theta, theta' vs t")
        plt.ylabel("theta, theta'")
        plt.xlabel("t")
        plt.legend(["theta", "theta'"])
        plt.show()

ans=pendulum()
ans.plot()