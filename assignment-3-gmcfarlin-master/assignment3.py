## Assignment3 ME369P
## Name: Grant McFarlin
## EID : gjm923

## Fill in functions and answer the questions in the specified places below.



'''
## Writing portion of assignment
---------------------------------

# Problem 1
------------

I, Grant McFarlin, have personally completed the first two matplotlib tutorials and
have taken any necessary additional actions to understand the material.



# Problem 3
-----------

In the space below, discuss how the inclusion of additional points impacts the
values of a, b, and r^2: When there are only 2 points the linear fit between them
has an r^2 value of 1 because it can just intersect both points; the a value is not
near 1, and the b value is small. As you add points, the r^2 value will decrease
slightly and never go back to 1 becasue there are small random deviations from the
line y = x. The value of a will get closer and closer to 1 as more points are added
because the true mean slope should be close to 1. The values of b are seemingly
random and are assigned based on the where the curve needs to be to best fit the
data.

'''



def lineGIF():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import pandas as pd

    # Assume data file is in cwd
    data = pd.read_csv('data_3_2.csv')

    # Create the scatter plot.
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)

    # Split the data to x,y
    x = np.array(data.iloc[:,0])
    y = np.array(data.iloc[:,1])

    # This function updates the line in the plot when it is called to generate
    # each frame requested by the FuncAnimation method
    def update(i):
        label = 'timestep {0} ms'.format(i*5)
        # Update the line and the axes (with a new xlabel). Return a tuple of
        # "artists" that have to be redrawn for this frame.
        ax.plot(x[i], y[i], 'bo')
        ax.set_xlabel(label)
        return ax

    # Create an animation object from the created figure that includes
    # 10 frames viewed at intervals of 5 ms.
    anim = FuncAnimation(fig, update, frames=np.arange(0, len(data)), interval=5)

    # save a gif of the animation using the writing package from magick
    anim.save('line.gif', dpi=80, writer='imagemagick')


def linearFit():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import pandas as pd

    # Assume data file is in cwd
    data = pd.read_csv('data_3_3.csv', header=None)

    # Create the scatter plot.
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)

    # Put x, y data into arrays
    x = np.array(data.iloc[:,0])
    y = np.array(data.iloc[:,1])

    # Create the base for the linear fit line, and make it invisible
    line, = ax.plot(x,y, 'r-', linewidth=2, visible=False)
    # Reset the axis limits to fit the visible artists only
    ax.relim(visible_only=True)

    # This function updates the line in the plot when it is called to generate
    # each frame requested by the FuncAnimation method
    def update(i):
        # Update the line and the axes (with a new xlabel). Return a tuple of
        # "artists" that have to be redrawn for this frame.
        label = 'timestep {0}'.format(i)

        # Once two points are on the graph, draw a line between them
        if i == 1:
            # Get equation for linear fit via matrix algebra
            mat_1 = np.array([[sum(x[0:i+1]**2),sum(x[0:i+1])], [sum(x[0:i+1]),len(x[0:i+1])]])
            mat_2 = np.array([sum(x[0:i+1]*y[0:i+1]), sum(y[0:i+1])])
            a, b = np.around(np.matmul(np.linalg.inv(mat_1),mat_2), decimals=5)
            st = sum((y[0:i+1] - y.mean())**2)
            sr = sum((y[0:i+1] - a * x[0:i+1] - b)**2)
            r2 = np.around(((st - sr)/st), decimals=5)
            # Print equation to the screen
            if a >= 0 and b >= 0:
                print(f"y = {a:.5f}x + {b:.5f} where r^2={r2:.5f}")
            elif a < 0 and b < 0:
                print(f"y = - {abs(a):.5f}x - {abs(b):.5f} where r^2={r2:.5f}")
            elif a < 0 and b >= 0:
                print(f"y = - {abs(a):.5f}x + {abs(b):.5f} where r^2={r2:.5f}")
            elif a >= 0 and b < 0:
                print(f"y = {a:.5f}x - {abs(b):.5f} where r^2={r2:.5f}")
            # Update the line artist
            line.set_xdata(x[0:i+1])
            line.set_ydata(y[0:i+1])
            line.set_visible(True)
        # When there are more points on the graph, calculate and draw the best
        # fit line
        elif i > 1:
            # Get equation for linear fit via matrix algebra
            mat_1 = np.array([[sum(x[0:i+1]**2),sum(x[0:i+1])], [sum(x[0:i+1]),len(x[0:i+1])]])
            mat_2 = np.array([sum(x[0:i+1]*y[0:i+1]), sum(y[0:i+1])])
            a, b = np.around(np.matmul(np.linalg.inv(mat_1),mat_2), decimals=5)
            st = sum((y[0:i+1] - y.mean())**2)
            sr = sum((y[0:i+1] - a * x[0:i+1] - b)**2)
            r2 = np.around(((st - sr)/st), decimals=5)
            # Print data to the screen
            if a >= 0 and b >= 0:
                print(f"y = {a:.5f}x + {b:.5f} where r^2={r2:.5f}")
            elif a < 0 and b < 0:
                print(f"y = - {a:.5f}x - {b:.5f} where r^2={r2:.5f}")
            elif a < 0 and b >= 0:
                print(f"y = - {a:.5f}x + {b:.5f} where r^2={r2:.5f}")
            elif a >= 0 and b < 0:
                print(f"y = {a:.5f}x - {b:.5f} where r^2={r2:.5f}")
            # Update the line artist
            line.set_xdata(x[0:i+1])
            line.set_ydata(a * x[0:i+1] + b)
            line.set_visible(True)

        # Plot each point in sequence
        ax.plot(x[i], y[i], 'bo')
        ax.set_xlabel(label)

        return ax, line

    # Create an animation object from the created figure that includes
    # 10 frames viewed at intervals of 200 ms.
    anim = FuncAnimation(fig, update, frames=np.arange(0, len(data)), interval=200)

    # save a gif of the animation using the writing package from magick
    anim.save('problem3.gif', dpi=80, writer='imagemagick')

def polyFit():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import pandas as pd

    # Assume data file is in cwd
    data = pd.read_csv('data.csv')

    # Split data into x,y
    x = data.iloc[:,0]
    y = data.iloc[:,1]

    # Create the scatter plot.
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)

    # This function updates the line in the plot when it is called to generate
    # each frame requested by the FuncAnimation method
    def update(frame):
        # Update the line and the axes (with a new xlabel). Return a tuple of
        # "artists" that have to be redrawn for this frame.
        label = 'timestep {0}'.format(frame-1)
        if frame in list(range(1,7)):
            order = frame
            # Generate matricies for curve fitting
            mat_1 = np.array([[sum(x**(2*order - col - row)) for col in range(order + 1)]
             for row in range(order + 1)])
            mat_2 = np.array([sum(y*x**(order - col)) for col in range(order + 1)])
            mat_1[-1][-1] = len(x)

            # Get coefficients
            coef = np.matmul(np.linalg.inv(mat_1),mat_2)

            # Multiply by x^order, x^order-1, ... to get y_pred
            x_orders = []
            for i in range(order):
                x_orders.append(x**(order - i))
            x_orders.append(np.ones(len(x)))
            x_orders = np.array(x_orders)
            y_pred = np.matmul(coef, x_orders)

            # Calculate r^2 values
            st = np.sum((y - y.mean())**2)
            sr = np.sum((y - y_pred)**2)
            r2 = ((st - sr)/st).round(5)

            # Print equations to the screen
            if coef[-2] >= 0 and coef[-1] >= 0:
                end_str = f"{coef[-2]:.5f}x + {coef[-1]:.5f} (r^2={r2:.5f})"
            elif coef[-2] < 0 and coef[-1] < 0:
                end_str = f"{abs(coef[-2]):.5f}x - {abs(coef[-1]):.5f} (r^2={r2:.5f})"
            elif coef[-2] < 0 and coef[-1] >= 0:
                end_str = f"{abs(coef[-2]):.5f}x + {abs(coef[-1]):.5f} (r^2={r2:.5f})"
            elif coef[-2] >= 0 and coef[-1] < 0:
                end_str = f"{abs(coef[-2]):.5f}x - {abs(coef[-1]):.5f} (r^2={r2:.5f})"
            if order == 1:
                print(f"{order}: y = " + end_str)
            else:
                beg_str = ''
                for i in range(order-1):
                    if coef[i+1] >= 0:
                        beg_str += f"{abs(coef[i]):.5f}x^{order-i} + "
                    else:
                        beg_str += f"{abs(coef[i]):.5f}x^{order-i} - "
                print(f"{order}: y = {beg_str}{end_str}")


            # Plot y_pred
            ax.plot(x,y,'ro')
            ax.plot(x,y_pred, label=f'x^{order}')
            ax.set_xlabel(label)
            ax.legend()

        return ax

    # Create an animation object from the created figure that includes
    # 10 frames viewed at intervals of 200 ms.
    anim = FuncAnimation(fig, update, frames=np.arange(0, 13), interval=500)

    # save a gif of the animation using the writing package from magick
    anim.save('problem4.gif', dpi=80, writer='imagemagick')

if __name__ == '__main__':
    lineGIF()
    linearFit()
    polyFit()
    print("Done")
