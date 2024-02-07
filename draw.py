import matplotlib.pyplot as plt
import numpy as np




def draw_vector(vec, ori = [0, 0], norm = 0, color = 'k'):#if norm = 1 then set length of vector to 1
    if norm == 1:
        vec = vec/np.linalg.norm(vec)
    plt.quiver(ori[0], ori[1], vec[0], vec[1], angles = 'xy', scale_units = 'xy', scale = 1, color = color)
    plt.text(ori[0], ori[1], '('+str(ori[0])+', '+str(ori[1]) +')', fontsize=12, ha='right')
    plt.text(vec[0], vec[1], '('+str(vec[0])+', '+str(vec[1]) +')', fontsize=12, ha='right')
    
    # set limit based on vector length and equal length for x and y axis

    maxx = max(max(vec[0], ori[0]) + 0.3 * abs(vec[0] - ori[0])+1, max(vec[1], ori[1]) + 0.3 * abs(vec[1] - ori[1])+1)
    minn = min(min(vec[0], ori[0]) - 0.3 * abs(vec[0] - ori[0])-1, min(vec[1], ori[1]) - 0.3 * abs(vec[1] - ori[1])-1)

    plt.xlim(minn, maxx)
    plt.ylim(minn, maxx)




    # equal axis
    plt.gca().set_aspect('equal', adjustable='box')
    # force grid on
    plt.grid(True)






if __name__ == "__main__":
    pass