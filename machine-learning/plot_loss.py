import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams['xtick.major.pad']='10'
rcParams['ytick.major.pad']='10'
rcParams['font.size'] = 22
rcParams['axes.labelsize'] = 22
rcParams['axes.labelweight'] = 'bold'
rcParams['axes.titlesize'] = 17
rcParams['xtick.labelsize'] = 15
rcParams['ytick.labelsize'] = 15
rcParams['legend.fontsize'] = 16
rcParams['figure.titlesize'] = 1

def loss_function(b1,b2,y,x1,x2):
    error = y - b1*x1 - b2*x2
    loss = np.mean(error**2)
    return loss

def plot_loss_function(b1,b2,y,x1,x2):
    loss = np.asarray([[loss_function(i,j,y,x1,x2) for i in b1] for j in b2])
    fig, ax = plt.subplots(figsize = (10,10))
    CS = ax.contour(b1, b2, loss, levels = [0,10, 100, 500, 1000, 3000, 5000, 8000], colors='k')
    ax.clabel(CS, fontsize=9,fmt='%1.1f', inline=True)
    ax.set_title('Loss function without Regularization')
    plt.plot([0,0,0,0,0], [-150,0,10,50,150], color = 'grey', linestyle = 'dashed')
    plt.plot([-150,0,10,50,150],[0,0,0,0,0], color = 'grey', linestyle = 'dashed')
    plt.xlim(-50,150)
    plt.ylim(-50,150)
    plt.xlabel('b1')
    plt.ylabel('b2')
    return CS