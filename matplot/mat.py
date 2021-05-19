import matplotlib.pyplot as plt
import numpy as np

def simple_plot():
    x = [0,1,2,3,4,5,6]
    y = [5,2,6,1,4,9,3]
    plt.scatter(x, y)
    plt.plot(x, y)

def plot_sinus():
    x = np.linspace(0, 50, 500)
    y = np.sin(x)
    print(x)
    print(y)
    plt.plot(x,y)

def plot_x_squared():
    x = np.linspace(-5, 5, 500)
    y = x * x
    print(x)
    print(y)
    plt.plot(x,y)

def load_csv(file_name, selected_columns):
    output = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            fields = line.split(',')
            selected_fields = []
            for c in selected_columns:
                selected_fields.append(float(fields[c]))
            output.append(selected_fields)
    return np.array(output)


def plot_silouetthe():
    data = load_csv('graf.csv', [0,1])
    x = data[:,0]
    y = 10-data[:,1]
    plt.plot(x,y)

def plot_water():
    data2 = load_csv('graf.csv', [0,1])
    x = 1+data2[:,0]
    y = data2[:,1]
    plt.plot(x,y)

def plot_text():
    data = load_csv('text.csv', [0,1])
    x = data[:,0]
    y = 2+data[:,1]
    plt.plot(x,y)

#simple_plot()
#plot_sinus()
#plot_x_squared()
plot_silouetthe()
plot_water()
plot_text()
plt.show()
