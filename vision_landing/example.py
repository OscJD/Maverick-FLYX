from threading import Thread, Event
from Queue import Queue, Empty
from subprocess import Popen, PIPE
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil
from time import sleep, time
from datetime import datetime, timedelta
from sys import exit, stdout, stderr
from os import path, makedirs, symlink, remove
from math import pi
from re import sub, search
from collections import deque
from math import sqrt
import signal
import logging

vehicle = connect("/dev/ttyS0", wait_ready=True,baud=57600)

msg =vehicle.message_factory.timesync_encode(tc1=0,ts1=123455667)
vehicle.send_mavlink(msg)

@vehicle.on_message("TIMESYNC")
def listener_timesync(message):
    print("Soy listener_timesync")
