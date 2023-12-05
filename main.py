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
    Y = []

    with open('data.txt', 'r') as datafile:
        plotting = csv.reader(datafile, delimiter=',')


        for ROWS in plotting:
            X.append(dt.fromisoformat(ROWS[0]))
            Y.append([float(ROWS[1]),float(ROWS[3]),float(ROWS[5]),float(ROWS[7]),float(ROWS[9]),float(ROWS[11])])

    fig, ax = plt.subplots()
    ax.plot(X, Y)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
    plt.title('Line Graph using CSV')
    plt.xlabel('Время')
    plt.ylabel('Температура')
    plt.legend(['sensor 1', 'sensor 2','sensor 3','sensor 4','sensor 5','outdoor'])
    ax.grid(True, linestyle='-.')
    plt.show()
