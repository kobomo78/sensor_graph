# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import csv
    from datetime import datetime as dt
    import matplotlib.dates as mdates
    import urllib.request
    import ssl


    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    with urllib.request.urlopen('https://109.194.141.27:34002/sensor_data/data.txt',context=ctx) as f:
        html = f.read().decode('utf-8')

    html_new = html.replace("\r", "")


    with open('data.txt', 'w', encoding="utf-8") as datafile1:
         datafile1.write(html_new)


    X = []
    Y_Temperature = []
    Y_Humidity= []

    with open('data.txt', 'r') as datafile:
        plotting = csv.reader(datafile, delimiter=',')


        for ROWS in plotting:
            X.append(dt.fromisoformat(ROWS[0]))
            Y_Temperature.append([float(ROWS[1]),float(ROWS[3]),float(ROWS[5]),float(ROWS[7]),float(ROWS[9]),float(ROWS[11])])
            Y_Humidity.append([float(ROWS[2]), float(ROWS[4]), float(ROWS[6]), float(ROWS[8]), float(ROWS[10]), float(ROWS[12])])

    fig, ax = plt.subplots()
    plt.title(' ')
    ax.plot(X, Y_Temperature)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
    plt.xlabel('Время')
    plt.ylabel('Температура')
    plt.legend(['sensor 1', 'sensor 2','sensor 3','sensor 4','sensor 5','outdoor'])
    ax.grid(True, linestyle='-.')

    fig, ax = plt.subplots()
    plt.title(' ')
    plt.plot(X, Y_Humidity)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
    plt.xlabel('Время')
    plt.ylabel('Влажность')
    plt.legend(['sensor 1', 'sensor 2', 'sensor 3', 'sensor 4', 'sensor 5','outdoor'])
    ax.grid(True, linestyle='-.')

    plt.show()





