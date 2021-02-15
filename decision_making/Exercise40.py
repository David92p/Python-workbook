#Sound Levels

sound = input('Enter the sound level expressed in DB ')
sound = int(sound)

Jackhammer = 130
Gas_Lawnmower = 106
Alarm_Clock = 70
Quiet_Room = 40

if sound < Jackhammer and sound > Gas_Lawnmower:
    print(sound, 'dB have a sound level between jackhammer and gas lawnmower')
elif sound < Gas_Lawnmower and sound > Alarm_Clock:
    print(sound, 'dB have a sound level between gas lawnmower and Alarm_Clock')
elif sound < Alarm_Clock and sound > Quiet_Room:
    print(sound, 'dB have a sound level between Alarm_Clock and Quiet room')
else:
     print('This noise has not been classified')