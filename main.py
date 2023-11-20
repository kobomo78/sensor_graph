# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import csv
    from datetime import datetime as dt
    import matplotlib.dates as mdates

    X = []
    Y = []

    with open('data.txt', 'r') as datafile:
        plotting = csv.reader(datafile, delimiter=',')

        for ROWS in plotting:
            X.append(dt.fromisoformat(ROWS[0]))
            Y.append([float(ROWS[1]),float(ROWS[3]),float(ROWS[5]),float(ROWS[7]),float(ROWS[9])])

    plt.plot(X, Y)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
    plt.title('Line Graph using CSV')
    plt.xlabel('Время')
    plt.ylabel('Температура')
    plt.legend(['sensor 1', 'sensor 2','sensor 3','sensor 4','sensor 5'])
    plt.show()
