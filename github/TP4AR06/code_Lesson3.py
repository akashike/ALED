#You can comment this if it poses you problems
import matplotlib
matplotlib.use('Qt5Agg')

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

# File implementing several methods to numerically solve a free falling particle

# Most simple case -> explicit euler, also called forward euler
# x : point in the state-space
# dx : derivate of the state with respect to time (state-space velocity)
# Given the (vector-valued, generally nonlinear) system dynamics f we get the ode
# dx = f(x)

# Update rule for numeric integration for foward euler
# x_{k+1} = x_k + h*dx_k
# with
# dx_k=f(x_k) being the "current velocity"
# this means that we approximate the solution to f by its tangent at x_k

# Here we have a free-falling particle, so we define
# x = [pos_x, pos_y, vel_x, vel_y].T
# Therefore we have f(x) = [vel_x, vel_y,0,g].T
# Note that newtons second law reads
# m*ddx = sum of forces with ddx being the second derivative of the position -> acceleration
# so its a second order system.
# This cannot be directly solved, as numerical integration only works for first order differential equations
# which is why we have to add the velocity to the state of the system.

#"Direct code"
g=-9.81 #gravity
yOffset = 40.

# Convenience function to compute the total energy
# E_tot = E_kin + E_pot
def fEnergy(X):
    Etot= (X[1,:]*(-g) + np.sum(np.square(X[2:,:]),axis=0)/2.)
    Etot -= Etot[0]
    return Etot

T = 2. #final time
hList = [1e-3,1e-2,1e-1] #list of time steps for which we want to compare the results

x0 = np.random.rand(4,1)*5. # Randomized initial state
x0[1,:]+=yOffset
dx_k = np.zeros((4,)) # Uni-dimensional array for current state-space velocity
dx_k[3] = g #Acceleration does not change in this example

fig, subplots = plt.subplots(2,2)
subplots[0,0].set_title("trajectory in the plane")
subplots[0,0].set_xlabel("pos_x")
subplots[0,0].set_ylabel("pos_y")
subplots[0,1].set_title("vel_y over time")
subplots[0,1].set_xlabel("t")
subplots[0,1].set_ylabel("vel_y")
subplots[1,0].set_title("total energy")
subplots[1,0].set_xlabel("t")
subplots[1,0].set_ylabel("E")

for h in hList:
    nSteps = int(T/h) # integration steps necessary
    t = np.arange(0,T,h) # corresponding time vector
    X = np.zeros((4,nSteps)) # Array to store results
    X[:,[0]] = x0 #Set initial

    # Actual integration
    for k in range(nSteps-1):
        dx_k[:2] = X[2:,k] # Update velocity
        X[:,k+1] = X[:,k] + h*dx_k # Update rule

    #Plot
    subplots[0,0].plot(X[0,:],X[1,:])
    subplots[0,1].plot(t,X[3,:])
    subplots[1,0].plot(t,fEnergy(X))

plt.tight_layout()
fig.savefig("euler1.pdf", format="pdf")

# Generalising the concept:
# In the above example everything is mixed up into one code block: the dynamics function f and the integration rule
# To keeps things separated, we can define corresponding functions (normally these should be put into separate module but let this file be self-contained...)

# the dynamics -> defined for your system
def f(x:np.ndarray)->np.ndarray:
    """
    Dynamics of a free-falling particle
    """
    x = x.reshape((4,-1)) # force correct shape; Note that -1 will automatically chose the correct size, always 2d
    dx = np.zeros_like(x)
    dx[:2,:] = x[2:,:] #Velocity
    dx[3,:] = g #acceleration, g defaults to global g

    return dx
# Note that this function is what one can call "vectorized"
# We can stack multiple initial conditions (column vectors) into one 2d-array
# We can stack multiple time-steps along a new axis (3d-array)
# This is nice because the total cpu time of calling a numpy function (on small arrays)
# is mainly determined by the slow python part ("overhead") and the actual computations
# (done in C) cost almost nothing in comparison
# So computing the trajectories for 2 initial conditions is basically as quick as computing one.


def forwardEuler(f:Callable,t:np.ndarray,x0:np.ndarray):
    """
    Forward euler scheme
    :param f: callable for the dynamics
    :param t: unidimensional array with all timepoints
    :param x0: Initial conditions
    """

    #Storage
    X = np.zeros((x0.shape[0],x0.shape[1],t.size),dtype=x0.dtype) # Here it is usefull to append time as third axis as this allows to nicely remove one axis if x0.shape[1] == 1
    # Initial
    X[:,:,0] = x0
    #Integration
    for k in range(t.size-1):
        h = t[k+1]-t[k] # time vector given, integration step not necessarily constant
        #Update
        X[:,:,k+1] = X[:,:,k] + h*f(X[:,:,k])

    return X.squeeze() # Go back to storage layout seen above if only one initial point

# Now to obtain the same results as above
fig, subplots = plt.subplots(2,2)
subplots[0,0].set_title("trajectory in the plane")
subplots[0,0].set_xlabel("pos_x")
subplots[0,0].set_ylabel("pos_y")
subplots[0,1].set_title("vel_y over time")
subplots[0,1].set_xlabel("t")
subplots[0,1].set_ylabel("vel_y")
subplots[1,0].set_title("total energy")
subplots[1,0].set_xlabel("t")
subplots[1,0].set_ylabel("E")

for h in hList:
    t = np.arange(0,T,h) # corresponding time vector
    X = forwardEuler(f,t,x0) #Integration
    #Plot
    subplots[0,0].plot(X[0,:],X[1,:])
    subplots[0,1].plot(t,X[3,:])
    subplots[1,0].plot(t,fEnergy(X))

plt.tight_layout()
fig.savefig("euler1_function.pdf", format="pdf")

# Or for multiple points
x0 = np.random.rand(4,5)*5.
x0[1,:]+=yOffset
t = np.arange(0,T,hList[0]) # corresponding time vector
X = forwardEuler(f,t,x0) #Integration

fig, subplots = plt.subplots(2,2)
subplots[0,0].set_title("trajectory in the plane")
subplots[0,0].set_xlabel("pos_x")
subplots[0,0].set_ylabel("pos_y")
subplots[0,1].set_title("vel_y over time")
subplots[0,1].set_xlabel("t")
subplots[0,1].set_ylabel("vel_y")
subplots[1,0].set_title("total energy")
subplots[1,0].set_xlabel("t")
subplots[1,0].set_ylabel("E")

for k in range(x0.shape[1]):
    subplots[0,0].plot(X[0,k,:],X[1,k,:])
    subplots[0,1].plot(t,X[3,k,:])
    subplots[1,0].plot(t,fEnergy(X[:,k,:]))

plt.tight_layout()
fig.savefig("eulerMultiInit1.pdf", format="pdf")

# Forward euler with fixed step size is the simplest integration scheme and suffers from numerical drawbacks
# To use the correct ode solver, one has to have an idea of the "stiffness" of the problem (basically how fast the time-constants hange)
# For very stiff problems, implicit solvers have to be used. For moderately stiff problems we can really on Runge-Kutta with variable step-size
# so most important features of a solver
# implicit vs explicit
# precision / order
# variable step-size
# event driven

#Scipy provides a common api for many different solvers
from scipy.integrate import solve_ivp #solve ode initial value problem

# In addition we want to define an event that corresponds to the particle hitting the ground
# An event is triggerd when the value attains zero
def hitGround(t:float, x:np.ndarray)->float:
    return float(x[1])
#Tell scipy that this is terminal
hitGround.terminal=True #Note that this is possible as a function is just a special kind of object

#Little hack as (like most solvers) solve_ivp expects the dynamics functions to take the current time as first and the current state as second argument
#Moreover, its expects the state to have the shape (n,) [This should be modifiable with the vectorized option but it does not seem to woerk for me]
fOde = lambda t,x: f(x).squeeze()

x0 = np.random.rand(4,1)*5.
x0[1,:]+=5

solScipy = solve_ivp(fOde, [0.,T], x0.squeeze(), events=[hitGround])

t=solScipy.t
X = solScipy.y

# Here we plot only the timepoints generated by the variable step-size solvers (by default runge-kutta45)
# Therefore this looks very unsmooth. The most efficient way is to integrate with variable step size and then interpolate for plotting (not done here)
# Note how this solvers achieves (insanely) higher accuracy (energy error) with an average time step of
# Note that the trajectory ends exactly at y=0.
print("Average timestep of RK45: {0}".format(T/t.size))

fig, subplots = plt.subplots(2,2)
subplots[0,0].set_title("trajectory in the plane")
subplots[0,0].set_xlabel("pos_x")
subplots[0,0].set_ylabel("pos_y")
subplots[0,1].set_title("vel_y over time")
subplots[0,1].set_xlabel("t")
subplots[0,1].set_ylabel("vel_y")
subplots[1,0].set_title("total energy")
subplots[1,0].set_xlabel("t")
subplots[1,0].set_ylabel("E")
subplots[0,0].plot(X[0,:],X[1,:])
subplots[0,1].plot(t,X[3,:])
subplots[1,0].plot(t,fEnergy(X))

plt.tight_layout()
fig.savefig("rk45Integration.pdf", format="pdf")





plt.show()