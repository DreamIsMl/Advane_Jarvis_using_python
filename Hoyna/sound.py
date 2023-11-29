import ctypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from jervis import TakeCommand

def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return interface.QueryInterface(IAudioEndpointVolume)

def change_volume(volume_change):
    interface = get_volume_interface()
    current_volume = interface.GetMasterVolumeLevelScalar()
    new_volume = max(0, min(1, current_volume + volume_change))
    interface.SetMasterVolumeLevelScalar(new_volume, None)

def main():
    while True:
        print("Enter 'up' to increase volume, 'down' to decrease volume, or 'exit' to quit:")
        user_input = TakeCommand().lower()

        if user_input == 'up':
            change_volume(0.1)
            print("Volume increased.")
        elif user_input == 'down':
            change_volume(-0.1)
            print("Volume decreased.")
        elif user_input == 'exit':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
