#Richter Scale

magnitude = float(input('enter the magnitude '))

if magnitude < 2.0:
    print('magnitude', magnitude,'is considered to be a micro earthquake')
elif magnitude >= 2.0  and magnitude < 3.0:
    print('magnitude', magnitude,'is considered to be a very minor earthquake')
elif magnitude >= 3.0  and magnitude < 4.0:
    print('magnitude', magnitude,'is considered to be a minor earthquake')
elif magnitude >= 4.0  and magnitude < 5.0:
    print('magnitude', magnitude,'is considered to be a light earthquake')
elif magnitude >= 5.0  and magnitude < 6.0:
    print('magnitude', magnitude,'is considered to be a moderate earthquake')
elif magnitude >= 6.0  and magnitude < 7.0:
    print('magnitude', magnitude,'is considered to be a strong earthquake')
elif magnitude >= 7.0  and magnitude < 8.0:
    print('magnitude', magnitude,'is considered to be a major earthquake')
elif magnitude >= 8.0  and magnitude < 10.0:
    print('magnitude', magnitude,'is considered to be a great earthquake')
elif magnitude >= 10.0:
    print('magnitude', magnitude,'is considered to be a meteoric earthquake')