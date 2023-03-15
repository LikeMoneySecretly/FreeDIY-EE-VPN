import time
from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')
    return device,client
def toggleAeroplaneMode(device):
    device.shell('input keyevent 66')
if __name__ == '__main__':
    device, client = connect()
    device.shell('am force-stop com.android.settings')
    time.sleep(0.5)
    device.shell('am start -a android.settings.AIRPLANE_MODE_SETTINGS')
    time.sleep(0.5)
    toggleAeroplaneMode(device)
    time.sleep(5)
    toggleAeroplaneMode(device)
    #Keyevnt 19 goes up and keyevent 20 goes down on an s7 keyevent toggles the buttons