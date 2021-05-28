import network



        # STAT_IDLE – no connection and no activity,

        # STAT_CONNECTING – connecting in progress,

        # STAT_WRONG_PASSWORD – failed due to incorrect password,

        # STAT_NO_AP_FOUND – failed because no access point replied,

        # STAT_CONNECT_FAIL – failed due to other problems,

        # STAT_GOT_IP – connection successful.


def connect():
    nic = network.WLAN(network.STA_IF)
    nic.active(True)

    wlans  = nic.scan()
    print("SELECT WLAN NETWORK")
    PRINT_NETWORKS(wlans)


def PRINT_NETWORKS(wlans):
    length = len(wlans)
    for i in range(length):
        print('[{}], {}, {}'. format(wlans[i][0], authmode(wlans[i][3])))

def authmode(num):
    if num is 0:
        return "Open" 
    elif num is 1:
        return "WEP"
    elif num is 2:
        return "WPA_PSK"
    elif num is 3:
        return "WPA2_PSK"
    elif num is 4:
        return "WPA_WPA2_PSK"