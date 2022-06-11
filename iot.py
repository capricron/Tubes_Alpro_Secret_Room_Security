import os

def openGate():
        os.system('py ampy/cli.py --port COM5 run iot/openGate.py')

def closeGate():
        os.system('py ampy/cli.py --port COM5 run iot/closeGate.py')

