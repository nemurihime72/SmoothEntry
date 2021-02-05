from firebase.firebase import FirebaseApplication
import time
from datetime import datetime
import socket
import sys

# url created from "NP Student Card" firebase database
url = "https://smoothentry-74b63-default-rtdb.firebaseio.com/"

firebase = FirebaseApplication(url, None)


def populate_stores_firebase():
    
    storename = ["4 Fingers Crispy Chicken","7 Eleven","AIBI","Akimitsu","ASICS",
                 "Bengawan Solo", "BreadTalk", "Châteraisé", "Four Leaves", "Twelve Cupckaes",
                 "3T Mobile", "6IXTY8IGHT Outlet", "Daiso", "Jean Yip", "OWNDAYS",
                 "CHARLES & KEITH", "McDonald's", "HUAWEI", "Eu Yan Sang", "Decathlon"]
    storeaddress = ["68 Orchard Rd, Singapore 238839","68 Orchard Rd, Singapore 238839", "68 Orchard Rd, Singapore 238839", "68 Orchard Rd, Singapore 238839", "68 Orchard Rd, Singapore 238839",
                    "23 Serangoon Central, Singapore 556083", "23 Serangoon Central, Singapore 556083", "23 Serangoon Central, Singapore 556083", "23 Serangoon Central, Singapore 556083", "23 Serangoon Central, Singapore 556083",
                    "2 Jurong East Street 21, Singapore 609601", "2 Jurong East Street 21, Singapore 609601", "2 Jurong East Street 21, Singapore 609601", "2 Jurong East Street 21, Singapore 609601", "2 Jurong East Street 21, Singapore 609601",
                    "4 Tampines Central 5, Singapore 529510", "4 Tampines Central 5, Singapore 529510", "4 Tampines Central 5, Singapore 529510", "4 Tampines Central 5, Singapore 529510", "4 Tampines Central 5, Singapore 529510"]
    storenumber = ["B1-07","01-28A, 01-51","04-65","02-04", "B2-69",
                   "B2-58/59", "B2-49A", "B2-43", "B2-47", "01-18A",
                   "01-23, 01-23A/24","03-50", "02-61","01-11/12", "04-20",
                   "01-13/14","01-33","04-03","B1-17","01-33A"]

    totalnumpeoplevisitedstore1 = [401, 300, 50, 200, 250,
                                   400, 380, 169, 290, 212,
                                   21, 198, 623, 51, 191,
                                   270, 701, 99, 12, 476]
    totalnumpeoplevisitedstore2 = [321, 233, 39, 152, 150,
                                   304, 301, 121, 245, 170,
                                   14, 157, 454, 20, 82,
                                   189, 670, 45, 8, 304]
    totalnumpeoplevisitedstore3 = [312, 233, 36, 125, 105,
                                   340, 310, 112, 254, 127,
                                   15, 175, 445, 26, 81,
                                   198, 606, 41, 27, 340]
    totalnumpeoplevisitedstore4 = [350, 276, 40, 156, 125,
                                   340, 323, 123, 221, 99,
                                   24, 154, 412, 26, 130,
                                   23, 558, 40, 11, 88]
    totalnumpeoplevisitedstore5 = [340, 200, 40, 150, 150,
                                   300, 300, 120, 240, 160,
                                   10, 160, 450, 20, 80,
                                   190, 560, 50, 10, 90]
    i = 0

    while i < 20:
        firebase.put("/stores/", i+1, {"storename":storename[i],
                                     "storeaddress":storeaddress[i],
                                     "storenumber":storenumber[i],
                                     "28-01-2021":totalnumpeoplevisitedstore1[i],
                                     "29-01-2021":totalnumpeoplevisitedstore2[i],
                                     "30-01-2021":totalnumpeoplevisitedstore3[i],
                                     "31-01-2021":totalnumpeoplevisitedstore4[i],
                                     "01-02-2021":totalnumpeoplevisitedstore5[i]})
        i += 1

def populate_users_firebase():
    UID = ["C177E6BF63", "49F15312C9", "2C961939B8", "0C714E7535", "6DA95D8B69",
           "4FD5BE43A1", "123BA9720D", "31BEFB129B", "C2F43FCC1E", "EF45D482C3",
           "8E36FD0339", "5A28A65D2C", "5B1421CF93", "4737B76BF2", "5F959C2EFF",
           "DF2B879DB3", "BDF7EE2F0B", "D957DEEA38", "41EDC7D491", "08015DA1F3",
           "55078364F3", "B7340CFF63", "1AEE6E997B", "2017757702", "8DDE653E56",
           "4873BE9212", "A4A4E447AF", "EE2EE4F0DF", "6556BCE737", "6B0519D4BE",
           "4EEE4F33CF", "C339003466", "51C056403B", "D8F85EA966", "E0D463E5E3",
           "0424438F84", "C8C58D70B4", "B5578695EF", "1D2962DBB6", "9728234D3D",
           "A475B5712A", "80460A683B", "2546A16BEA", "6DF3F65B9E", "EF99426057",
           "7D02458A4E", "CB205801DB", "0A24811F40", "ED3AE73E39", "37226B831D"]
    NRIC = ["T2633348A", "T5557747N", "T9042666E", "T7510743X", "T3035518D",
            "T6662452A", "T5476858I", "T2135128I", "T7781718O", "T2290300I",
            "T5060005C", "T2829315S", "T5106814D", "T5585556I", "T8595764A",
            "T9842412B", "T9254256Z", "T6399036C", "T2667200I", "T3237771I",
            "T1134413G", "T1869979U", "T2565199C", "T8009622I", "T6467498B",
            "T6220646C", "T6162803O", "T5091963A", "T5495155D", "T2879059I",
            "T8858189D", "T2051129I", "T8171832B", "T5867162I", "T1954558E",
            "T5879288D", "T9401205X", "T4343057F", "T6257237F", "T7473532I",
            "T8786996H", "T1305324O", "T3620366A", "T5923230I", "T1929052I",
            "T8036193E", "T2674431F", "T2562886F", "T0475764E", "T8050424I"]
    name = ["Golden Blumenthal", "Gustavo Butt", "Tori Margolis", "Daren Gehlert", "Karine Kmetz",
            "Terica People", "Domenic Franco", "Merlyn Mawson", "Lolita Vanderhoof", "Min Fullenkamp",
            "Ginger Hiebert", "Noella Heavener", "Frieda Simental", "Ivan Buesing", "Dorethea Mercier",
            "Hanna Mccargo", "Fe Tozier", "Ona Carta", "Santina Chauez", "Griselda Light",
            "Edward Fines", "Randal Mikula", "Detra Schlueter", "Lue Eggebrecht", "Annita Carnevale",
            "Chase Goodwyn", "Katherina Poulin", "Vinnie Provost", "Kesha Mixon", "Mahalia Estrada",
            "Irina Cheslock", "Lakita Latour", "Adolfo Welsh", "Tammie Arend", "Norman Loveless",
            "Eugenie Kennington", "Francisca Cracraft", "Page Zaragosa", "Tereasa Almon", "Yun Lukach",
            "Simona Wofford", "Melissa Heeren", "Marie Topper", "Mirella Melson", "Agustin Bleich",
            "Lara Samuel", "Edgar Warden", "Bertram Blood", "Wiley Sieber", "Stan Amey"]
    phonenum = ["80488396", "93387756", "97796361", "98897008", "90077289",
                "80992282", "93322818", "99432638", "89821137", "94020923",
                "80095389", "86416474", "83629196", "80401595", "81905017",
                "94804508", "81067721", "85757628", "83536305", "98472135",
                "88234532", "94232785", "80265783", "98749083", "86417205",
                "99979890", "89869794", "82579286", "87773644", "80939793",
                "92960308", "86873705", "87136247", "88231129", "85272847",
                "85279241", "84543718", "93490406", "86178298", "90579011",
                "93132279", "80988690", "84656944", "89316239", "92113591",
                "99182732", "95576031", "99572050", "80059165", "99840765"]
    temp = [36.8, 36.9, 37.1, 36.5, 38.5, 37.4, 37.4, 37.1, 37.5, 36.9,
            37.3, 37.3, 36.6, 37.0, 36.7, 37.0, 37.3, 36.8, 37.3, 36.8,
            37.3, 40.1, 36.7, 36.2, 36.3, 36.4, 35.9, 36.7, 36.8, 37.5,
            37.1, 37.3, 37.5, 37.2, 37.5, 36.6, 37.0, 36.5, 37.0, 37.3,
            37.5, 36.6, 36.8, 36.8, 36.7, 36.5, 37.2, 37.2, 36.9, 36.5]
    height = [175, 167, 160, 156, 168, 170, 175, 153, 175, 173,
              175, 157, 177, 171, 168, 169, 157, 156, 154, 159,
              164, 167, 169, 163, 152, 172, 159, 158, 152, 178,
              179, 160, 173, 175, 162, 180, 154, 170, 171, 173,
              172, 179, 158, 159, 163, 159, 151, 155, 176, 158]
    i = 0
    while i < 50:
        firebase.put("/users/", UID[i], {"nric": NRIC[i],
                                         "name":name[i],
                                         "phone_number":phonenum[i],
                                         "checked_in":"false",
                                         "latest_temp":temp[i],
                                         "height":height[i]})
        i += 1

def store_initialisation():
    i = 1;
    while True:  
        if firebase.get("/stores", i) == None:
            storename = input("Please enter store name: ")
            storeaddress = input("Please enter address number: ")
            storenumber = input("Please enter store number: ")
            firebase.put("/stores/", i, {"storename":storename, "storeaddress":storeaddress,
                                         "storenumber":storenumber, datetime.today().strftime("%d-%m-%Y"):0})
            break
        else:
            i += 1

## def link_tag():
            

###### TRYING TO DO ######
##            # Create a TCP/IP socket
##            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##
##            # Bind the socket to the port
##            server_address = ('153.20.92.86', 10000)
##            print('starting up on {} port {}'.format(*server_address))
##            sock.bind(server_address)
##
##            # Listen for incoming connections
##            sock.listen(1)
##
##            while True:
##                # Wait for a connection
##                print('waiting for a connection')
##                connection, client_address = sock.accept()
##                try:
##                    print('connection from', client_address)
##
##                    # Receive the data in small chunks and retransmit it
##                    while True:
##                        data = connection.recv(16)
##                        print('received {!r}'.format(data))
##                        if data:
##                            if firebase.get("/users", '{0}'.format(data)) == None:
##                                nric = input("Please enter user's NRIC: ")
##                                name = input("Please enter user's name: ")
##                                phonenumber = input("Please enter user's phone number: ")
##                                firebase.put("/users/", '{0}'.format(data), {"nric":nric, "name":name, "phone_number":phone_number, "checked_in":"false", "latest_temp":"none", "height":"none"})
##                                print("The user has been successfully linked to the RFID tag!")
##                            else:
##                                print("This RFID tag is already in use!")
##                        else:
##                            print('no data from', client_address)
##                            break
##
##                finally:
##                    # Clean up the connection
#                    connection.close()
            

def print_menu():
    menuList = ["Initialise Store", "Link Details to RFID Tag", "Populate Firebase", "Exit"]
    i = 0
    print("-------- SmoothEntry --------\n")
    for i in range(len(menuList)):
        if menuList[i] == "Exit":
            print("[0] {0}".format(menuList[i]))
        else:
            print("[{0}] {1}".format((i+1), menuList[i]))
    print("\n-----------------------------")

option = -1
while True:
    print_menu()
    option = input("Please enter option: ")
    if option == "1":
        store_initialisation()
    elif option == "2":
        link_tag()
    elif option == "3":
        populate_stores_firebase()
        populate_users_firebase()
    elif option == "0":
        print("Thank you and goodbye!")
    else:
        print("Invalid option. Please try again!")

         
        
    

####### ORIGINAL NFC CODE TO LINK NEW RFID TAG TO USER FOR RASPBERRY PI  #######
        
####import RPi.GPIO as GPIO
####import mfrc522 as MFRC522
####import signal
####import time
####
####GPIO.setwarnings(False)
####continue_reading = True
####
####GPIO.cleanup()
####
##### Capture SIGINT for cleanup when the script is aborted
####def end_read(signal,frame):
####    global continue_reading
####    print("Ctrl+C captured, ending read.")
####    continue_reading = False
####    
##### Hook the SIGINT
####signal.signal(signal.SIGINT, end_read)
####
##### Create an object of the class MFRC522
####MIFAREReader = MFRC522.MFRC522()
####
####def to_int(uid):
####    value = 0
####
####    for i in range(len(uid)):
####        value = value * 256 + uid[i]
####        return ####### ORIGINAL NFC CODE FOR RASPBERRY PI  #######
            
##def link_tag():
##    while continue_reading:
##
##        # Scan for cards
##        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
##
##        # Get the UID of the card
##        (status,uid) = MIFAREReader.MFRC522_Anticoll()
##        uid_value = to_int(uid)
##        UID = hex(uid_value)
##
##        # If we have the UID, continue
##        if status == MIFAREReader.MI_OK:
##            # To check if RFID is registered in the database

##    #because of the OS being updated, we were unable to 
##    
##    if firebase.get("/users", UID) == None:
            
##            nric = input("Please enter user's NRIC: ")
##            name = input("Please enter user's name: ")
##            phonenumber = input("Please enter user's phone number: ")
##            firebase.put("/users/", UID, {"NRIC":nric, "name":name, "phonenumber":phonenumber, "checked_in1":"false","checked_in2":"false", "current_temp":"none", "height":"test"})
##            print("The user has been successfully linked to the RFID tag!")
##    else:
##            print("This RFID tag is already in use!")

##        time.sleep(1)
        
   
##############################################################
