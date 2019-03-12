import numpy as np
from numpy import sin,cos

import pygame
import pygame.draw as pygDraw
from pygame.time import Clock as pygClock

zeros3d = np.zeros((3,1))

def regularLinEqSolve(A,b, epsilon):
    """Solves A.x=b in a robust fashion (Tinkhonov-regularization)"""
    uu, ss, vv = np.linalg.svd(A)
    Aplus = np.dot(np.dot(vv, 1./(ss+epsilon)), uu.t)
    return np.dot(Aplus, b)

class pendule:
    def __init__(self, m1, m2, l1, l2, g, mu):
        self.m = m
        self.l = l
        self.g = g
        self.mu = mu

        self.nq = 1
        self.nu = 1

        self.q = np.zeros((1,1))
        self.qd = np.zeros((1,1))
    
    """
    For all functions:
    Passing q/Q/X with default None allows to execute the function either with external inputs or
    the ones stored in the class
    """
    def MGD(self,q=None):
        """Direct geometrical model"""
        q=self.q if q is None else q
        return self.l*np.array([[-sin(q[0,0]),cos(q[0,0]),0]]).T

    def getJac(self,q=None):
        """Get the Jacobian"""
        q=self.q if q is None else q
        return self.l*np.array([[-cos(q[0,0]),-sin(q[0,0]),0]]).T

    def getqdd(self, Q=None, u=None):
        """Get acceleration"""
        q=self.q if Q is None else Q[:self.nq, [0]]
        qd=self.qd if Q is None else Q[self.nq:, [0]]
        u = np.zeros((self.nu,1)) if u is None else u
        return np.array([[(u[0,0]+self.m*self.l*sin(q[0,0])-self.mu*qd[0,0])/(self.m*self.l**2)]])

    def getQd(self, Q=None, u=None, useSelfQd=False):
        """Get state-space velocity (derivative of the position of the system in the state-space)"""
        q=self.q if Q is None else Q[:self.nq, [0]]
        if useSelfQd:
            qd = self.qd
        else:
            qd=self.qd if Q is None else Q[self.nq:, [0]]
        return np.vstack((qd, self.getqdd(np.vstack((q,qd)), u)))

    def getXdfromQ(self, Q=None):
        """Get task space velocity from position and velocity"""
        Q = np.vstack((self.q, self.qd)) if Q is None else Q
        q = Q[:self.nq, [0]]
        qd = Q[self.nq:, [0]]
        return np.dot(self.getJac(q), qd)

    def getQdFromXd(self, Xd, q=None, epsilon=1e-4):
        """Get joint space velocity seeking to generate the given task space velocity"""
        q = self.q if q is None else q
        J = self.getJac(q)
        return regularLinEqSolve(J,Xd, epsilon)
    
    def drawPyGame(self, screen, color = (255,255,255), scale=1., offset=np.zeros((2,), dtype=np.int_), q=None):
        """Draw a simple pendulum, radius corresponds to the (squareroot of the) mass"""
        #Unfortunately,origin is top left in pygame -> up is down down is up
        q = self.q if q is None else q
        xEnd= (self.MGD(q).squeeze()[:2]*scale).astype(np.int_)
        xEnd[1] *= -1
        xEnd += offset  # Only take x-y, adjust for offset
        r = int((self.m*scale)**0.5)+1
        width = int(scale**0.25+1)
        pygDraw.line(screen, color, offset, xEnd, width)
        pygDraw.circle(screen, color, xEnd, r)
        
        return None

def singleShotSim(aPend, qInit):
    """Direct simulation without plotting"""
    from scipy.integrate import solve_ivp
    
    """Define the dynamics with 0 control input <-> uncontrolled"""
    fInt = lambda t,Q: myPend.getQd(Q.reshape((2,1)),u=np.zeros((1,1)))

    sol = solve_ivp(fInt,[0.,2.], qInit.squeeze(), vectorized=True)
    
    print(sol)
    
    return None
    

def simulationNoControlComp(aPend:pendule, qInit):
    """Simulate no control pendulum and show the difference between solve_ivp and forward euler"""
    from scipy.integrate import solve_ivp
    from time import time
    QForward = qInit.copy()
    QSolve = qInit.copy()
    
    # Init pygame
    pygame.init()
    thisClock = pygClock()
    screen = pygame.display.set_mode((600, 600))
    
    scale = 100
    offset = np.array([300,300]).astype(np.int_)
    
    # Function for integration
    fInt = lambda t,Q:myPend.getQd(Q.reshape((2, 1)), u=np.zeros((1,1)))
    
    tStart = time()
    thisClock.tick()
    t = 0. # current time
    while time()<tStart+20.: #Simulate twenty seconds
        screen.fill((255, 255, 255)) #Make screen white again -> otherwise all are displayed
        # Plot current
        # Plot euler -> red
        aPend.drawPyGame(screen, (255,0,0), scale, offset, q=QForward[:1,[0]])
        # Plot solve -> black
        aPend.drawPyGame(screen, (0,0,0), scale, offset, q=QSolve[:1, [0]])
        dt = float(thisClock.tick(30))/1000.# Let time pass, at least as much to have 30fps max
        # Refresh
        pygame.display.flip()
        # Compute new pos
        # Euler
        QForward += dt*aPend.getQd(QForward,np.zeros((1,1)))
        #Solve
        sol = solve_ivp(fInt, [t, t+dt], QSolve.squeeze(), vectorized=True)
        QSolve = sol['y'][:,[-1]]
        
        # Update time
        t+=dt
    
    pygame.display.quit()
    
    return None

def simulationControl(aPend, Q0, QTarget, Kp,Kpd):
    from scipy.integrate import solve_ivp
    from time import time
    Qp = Q0.copy()
    Qpd = Q0.copy()
    
    # Init pygame
    pygame.init()
    thisClock = pygClock()
    screen = pygame.display.set_mode((600, 600))
    
    scale = 100
    offset = np.array([300, 300]).astype(np.int_)
    
    # Function for integration -> Proportional
    fIntP = lambda t, Q:myPend.getQd(Q.reshape((2, 1)), u=np.dot(Kp,Q-QTarget))
    fIntPD = lambda t, Q:myPend.getQd(Q.reshape((2, 1)), u=np.dot(Kpd, Q-QTarget))
    
    tStart = time()
    thisClock.tick()
    t = 0.  # current time
    while time() < tStart+20.:  # Simulate twenty seconds
        screen.fill((255, 255, 255))  # Make screen white again -> otherwise all are displayed
        pygDraw.line(screen, (125,125,125), (300,300), (300-int(1.5*aPend.l*scale*np.sin(QTarget[0,0])), 300-int(1.5*aPend.l*scale*np.cos(QTarget[0,0]))))
        # Plot current
        # Plot P -> red
        aPend.drawPyGame(screen, (255, 0, 0), scale, offset, q=Qp[:1, [0]])
        # Plot PD -> black
        aPend.drawPyGame(screen, (0, 0, 0), scale, offset, q=Qpd[:1, [0]])
        dt = float(thisClock.tick(30))/1000.  # Let time pass, at least as much to have 30fps max
        # Refresh
        pygame.display.flip()
        # Compute new pos
        # SP
        sol = solve_ivp(fIntP, [t, t+dt], Qp.squeeze(), vectorized=True)
        Qp = sol['y'][:, [-1]]
        sol = solve_ivp(fIntPD, [t, t+dt], Qpd.squeeze(), vectorized=True)
        Qpd = sol['y'][:, [-1]]
        
        # Update time
        t += dt
    
    pygame.display.quit()
    
    return None


def simulationControlPID(aPend, Q0, QTarget, Kpd, Ki):
    from scipy.integrate import solve_ivp
    from time import time
    Q = Q0.copy()
    
    #Attach integrative error
    Q = np.vstack((Q,0.))
    
    # Init pygame
    pygame.init()
    thisClock = pygClock()
    screen = pygame.display.set_mode((600, 600))
    
    scale = 100
    offset = np.array([300, 300]).astype(np.int_)
    
    # Function for integration -> Proportional
    fInt = lambda t, Q: np.vstack(( myPend.getQd(Q[:2].reshape((2, 1)), u=np.dot(Kpd, Q[:2].reshape((2, 1))-QTarget)+Ki*Q[2]), Q[0,0]-QTarget[0,0] ))
    
    tStart = time()
    thisClock.tick()
    t = 0.  # current time
    while time() < tStart+20.:  # Simulate twenty seconds
        screen.fill((255, 255, 255))  # Make screen white again -> otherwise all are displayed
        pygDraw.line(screen, (125, 125, 125), (300, 300), (300-int(1.5*aPend.l*scale*np.sin(QTarget[0, 0])), 300-int(1.5*aPend.l*scale*np.cos(QTarget[0, 0]))))
        # Plot current
        # Plot P -> red
        aPend.drawPyGame(screen, (255, 0, 0), scale, offset, q=Q[:1, [0]])
        dt = float(thisClock.tick(30))/1000.  # Let time pass, at least as much to have 30fps max
        # Refresh
        pygame.display.flip()
        # Compute new pos
        sol = solve_ivp(fInt, [t, t+dt], Q.squeeze(), vectorized=True)
        Q = sol['y'][:, [-1]]
        #print(Q)
        # Update time
        t += dt
    
    pygame.display.quit()
    
    return None


if __name__ == "__main__":

    

    myPend = pendule(1.,2.,9.81, 0.1)

    Q0 = np.array([[8, 0.]]).T
    
    myPend.MGD(Q0)
    
    singleShotSim(myPend, Q0)
    
    #simulationNoControlComp(myPend, Q0)

    #Control simulation with P and PD gain
    #Attention with angles as they wrap from 2pi to 0 (has no influence for the chosen positions but one has to take this into account for a generic controller...)
    #No input limitation
    Q0 = np.array([[.2, 0.]]).T
    QTarget = np.array ([[.4, 0.]]).T
    Kp = np.array([[-10.,0.]]) #Proportional only
    Kpd = np.array([[-10., -2.]])  # Proportional and derivative
    #simulationControl(myPend, Q0, QTarget, Kp,Kpd)
    
    # Add an integrative part.
    # Attention this augments the state-space by the internal state of the controller (The integral over the error)
    Ki = -1.
    simulationControlPID(myPend, Q0, QTarget, Kpd, Ki)


