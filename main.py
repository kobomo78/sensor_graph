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

    fig, ax = plt.subplots(2,1)
    ax[0].plot(X, Y_Temperature)
    ax[1].plot(X, Y_Humidity)
    plt.title(' ')
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
    ax[0].set_xlabel('Время')
    ax[0].set_ylabel('Температура')
    ax[0].legend(['sensor 1', 'sensor 2','sensor 3','sensor 4','sensor 5','outdoor'])
    ax[0].grid(True, linestyle='-.')
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
    ax[1].set_xlabel('Время')
    ax[1].set_ylabel('Влажность')
    ax[1].legend(['sensor 1', 'sensor 2', 'sensor 3', 'sensor 4', 'sensor 5','outdoor'])
    ax[1].grid(True, linestyle='-.')
    plt.show()





