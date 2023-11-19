
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import csv
    from datetime import datetime as dt

    X = []
    Y = []

    with open('data.txt', 'r') as datafile:
        plotting = csv.reader(datafile, delimiter=',')

        for ROWS in plotting:
            X.append(dt.fromisoformat(ROWS[0]))
            Y.append([float(ROWS[1]),float(ROWS[3]),float(ROWS[5]),float(ROWS[7]),float(ROWS[9])])

    plt.plot(X, Y)
    plt.title('Line Graph using CSV')
    plt.xlabel('Время')
    plt.ylabel('Температура')
    plt.legend(['sensor 1', 'sensor 2','sensor 3','sensor 4','sensor 5'])
    plt.show()

'''
import socket
import csv
import json
from datetime import datetime as dt

if __name__ == '__main__':

    localIP = "172.20.22.171"

    localPort = 34004

    bufferSize = 1024


    # Create a datagram socket

    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip

    UDPServerSocket.bind((localIP, localPort))

    print("UDP server up and listening")

    # Listen for incoming datagrams

    while (True):

        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(clientMsg)
        print(clientIP)

        ll = json.loads(message)

        f = csv.writer(open("test.csv", "a", newline=''))

        x = dt.now().isoformat(" ","seconds")

        f.writerow([x,ll["sensor_0"]["temperature"],ll["sensor_0"]["humidity"],
                    ll["sensor_1"]["temperature"],ll["sensor_1"]["humidity"],
                    ll["sensor_2"]["temperature"],ll["sensor_2"]["humidity"],
                    ll["sensor_3"]["temperature"],ll["sensor_3"]["humidity"],
                    ll["sensor_4"]["temperature"],ll["sensor_4"]["humidity"]])

'''
        # Sending a reply to client

        #UDPServerSocket.sendto(bytesToSend, address)
'''
if __name__ == '__main__':

    with open('log.txt') as f:
        lines = f.readlines()

    channels = dict()
    for index in lines:
        str_1=index.split()
        if len(str_1)>4:
           if str_1[3]== "COMM":
               channel=int(str_1[5],16) + int(str_1[6],16)*256

               if channel not in channels:
                       channels[channel]=1
               else:
                       channels[channel] = channels[channel] +1

    print(channels)

'''


'''
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('log.txt') as f:
        lines = f.readlines()

    graf = dict()

    for index in lines:
        str_1=index.split(".")
        if str_1[0] not in graf:
            graf[str_1[0]] = 1
        else:
            graf[str_1[0]]+=1

    f = open('log.csv', 'w', encoding="utf-8")

    for k, v in graf.items():
        str2=k+";"+str(v)+"\n"
        f.write(str2)

    f.close()


    graf_sorted=dict(sorted(graf.items(), key=lambda item: item[1],reverse=True))

    i=0
    for k, v in graf_sorted.items():
       i+=1
       if i>20: break
       print(k,v)



'''
'''
if __name__ == '__main__':
    global_list = []
    def F(l,input_list):
        list1 = input_list.copy()
        list2 = input_list.copy()
        list3 = input_list.copy()
        if l >= 2400:
            list1.append(2400)
            F(l-2400,list1)

        if l >= 1200:
            list2.append(1200)
            F(l-1200,list2)
        if l >= 900:
            list3.append(900)
            F(l-900,list3)


        input_list.append(l)
        global_list.append(input_list)

    def Ident(list1,list2):
        if len(list1) != len(list2):
            return False
        if list1[len(list1) - 1] != list2[len(list2) - 1]:
            return False
        kol = 0
        for n in range (len(list1) - 1):
            kol = 0
            for a in range (len(list2) - 1):
                if list1[n] == list2[a]:
                    kol = kol + 1
            if kol == 0:
                return False
        for n in range (len(list2) - 1):
            kol = 0
            for a in range (len(list1) - 1):
                if list2[n] == list1[a]:
                    kol = kol + 1
            if kol == 0:
                return False

        return True

    p = int(input())
    input_list1 = []
    F(p,input_list1)
    global_list1 = []
    for n in range(len(global_list)):
        if global_list[n][len(global_list[n]) - 1] < 900:
            global_list1.append(global_list[n])

    global_list2 = []
    for n in range (len(global_list1)):
        k = False
        for a in range (len(global_list2)):
            if Ident(global_list1[n],global_list2[a]):
                k = True
        if not k:
             global_list2.append(global_list1[n])

    for n in range (len(global_list2)-1):
        for a in range (n+1,len(global_list2)):
            if global_list2 [a][len(global_list2[a]) - 1] < global_list2[n][len(global_list2[n]) - 1]:
                m = global_list2[n]
                global_list2[n] = global_list2[a]
                global_list2[a] = m

    for n in range(len(global_list2)):
        print(global_list2[n])
'''