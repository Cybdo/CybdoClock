import time
import board
import digitalio
import adafruit_74hc595
import socketpool
import adafruit_ntp
import wifi
import os
import asyncio



latch_pin = digitalio.DigitalInOut(board.D3)
sr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), latch_pin)

rows = [sr.get_pin(14), sr.get_pin(13), sr.get_pin(12), sr.get_pin(11), sr.get_pin(10), sr.get_pin(9), sr.get_pin(8),
        sr.get_pin(6), sr.get_pin(5), sr.get_pin(4), sr.get_pin(3), sr.get_pin(2), sr.get_pin(1), sr.get_pin(0)]

cols = [sr.get_pin(30), sr.get_pin(29), sr.get_pin(28), sr.get_pin(27), sr.get_pin(26), sr.get_pin(25), sr.get_pin(24),
        sr.get_pin(22), sr.get_pin(21), sr.get_pin(20), sr.get_pin(19), sr.get_pin(18), sr.get_pin(17), sr.get_pin(16)]




'''
C	Y	B	D	O	C	L	O	C	K	N	A	U	S
I	T	C	I	S	Y	T	E	N	F	O	R	T	Y
T	W	E	N	T	Y	B	T	H	I	R	T	Y	D
H	A	L	F	I	F	T	Y	O	T	W	O	N	E
Q	U	A	R	T	E	R	S	I	X	F	O	U	R
C	S	E	V	E	N	I	N	E	L	E	V	E	N
T	H	R	E	E	I	G	H	T	W	E	L	V	E
T	E	E	N	C	F	I	V	E	E	T	O	K	V
T	H	A	C	K	P	C	L	U	B	P	A	S	T
T	E	N	I	N	E	I	G	H	T	W	O	N	E
O	F	O	U	R	S	E	V	E	N	S	I	X	N
F	I	V	E	L	E	V	E	N	T	H	R	E	E
T	W	E	L	V	E	E	O	N	C	L	O	C	K
P	T	F	A	L	L	O	U	T	A	P	N	D	K
'''



clock_hour_pos = {
    
    1: {11:9, 12:9, 13:9},
    2: {9:9, 10:9, 11:9},
    3: {9:11, 10:11, 11:11, 12:11, 13:11},
    4: {1:10, 2:10, 3:10, 4:10},
    5: {0:11, 1:11, 2:11, 3:11},
    6: {10:10, 11:10, 12:10},
    7: {5:10, 6:10, 7:10, 8:10, 9:10},
    8: {5:9, 6:9, 7:9, 8:9, 9:9},
    9: {2:9, 3:9, 4:9, 5:9},
    10: {0:9, 1:9, 2:9},
    11: {3:11, 4:11, 5:11, 6:11, 7:11, 8:11},
    12: {0:12, 1:12, 2:12, 3:12, 4:12, 5:12}
    
}


clock_minute_pos = {
        # minute: {col: row, col: row, ...}
    0: {7:12, 9:12, 10:12, 11:12, 12:12, 13:12},
    1: {11:3, 12:3, 13:3},
    2: {9:3, 10:3, 11:3},
    3: {0:6, 1:6, 2:6, 3:6, 4:6},
    4: {10:4, 11:4, 12:4, 13:4},
    5: {5:7, 6:7, 7:7, 8:7},
    6: {7:4, 8:4, 9:4},
    7: {1:5, 2:5, 3:5, 4:5, 5:5},
    8: {4:6, 5:6, 6:6, 7:6, 8:6},
    9: {5:5, 6:5, 7:5, 8:5},
    10: {6:1, 7:1, 8:1},
    11: {8:5, 9:5, 10:5, 11:5, 12:5, 13:5},
    12: {8:6, 9:6, 10:6, 11:6, 12:6, 13:6}, 
    13: {7:2, 8:2, 9:2, 10:2},
    14: {10:4, 11:4, 12:4, 13:4},
    15: {3:3, 4:3, 5:3},
    16: {7:4, 8:4, 9:4},
    17: {1:5, 2:5, 3:5, 4:5, 5:5},
    18: {4:6, 5:6, 6:6, 7:6},
    19: {5:5, 6:5, 7:5},
    20: {0:2, 1:2, 2:2, 3:2, 4:2, 5:2},
    30: {7:2, 8:2, 9:2, 10:2, 11:2, 12:2},
    40: {9:1, 10:1, 11:1, 12:1, 13:1},
    50: {3:3, 4:3, 5:3, 6:3, 7:3}
}

clock_word_pos = {
    "it is": {0:1, 1:1, 3:1, 4:1},
    "half": {0:3, 1:3, 2:3, 3:3},
    "quarter": {0:4, 1:4, 2:4, 3:4, 4:4, 5:4, 6:4},
    "quarters": {0:4, 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4},
    "a": {1:3},
    "to": {10:7, 11:7},
    "past": {10:8, 11:8, 12:8, 13:8},
    "oclock": {7:12, 9:12, 10:12, 11:12, 12:12, 13:12},
    "teen": {0:7, 1:7, 2:7, 3:7}
    
}

latch_pin = digitalio.DigitalInOut(board.D3)
sr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), latch_pin)

rowsarr = [sr.get_pin(14), sr.get_pin(13), sr.get_pin(12), sr.get_pin(11), sr.get_pin(10), sr.get_pin(9), sr.get_pin(8),
        sr.get_pin(6), sr.get_pin(5), sr.get_pin(4), sr.get_pin(3), sr.get_pin(2), sr.get_pin(1), sr.get_pin(0)]

colsarr = [sr.get_pin(30), sr.get_pin(29), sr.get_pin(28), sr.get_pin(27), sr.get_pin(26), sr.get_pin(25), sr.get_pin(24),
        sr.get_pin(22), sr.get_pin(21), sr.get_pin(20), sr.get_pin(19), sr.get_pin(18), sr.get_pin(17), sr.get_pin(16)]


refreshtime = 0.02




async def draw_row(row, columns):
    rowsarr[row].value = True
    for column in columns:
        colsarr[column].value = True
    await asyncio.sleep(refreshtime)
    rowsarr[row].value = False
    for column in columns:
        colsarr[column].value = False

async def draw_matrix(matrix):
    for row in matrix.keys():
        columns = []
        for column in range(14):
            if matrix[row][column] == 1:
                columns.append(column)
        await draw_row(row, columns)
    


def parse_time(ntp):
    currenthour = ntp.tm_hour
    currentminute = ntp.tm_min
    
    matrix = {row: [0] * 14 for row in range(14)}

    def add_positions(position_map):
        if position_map is None:
            return
        for column, row in position_map.items():
            matrix[row][column] = 1

    if currentminute > 30:
        currenthour = (currenthour + 1) % 12
        if currenthour == 0:
            currenthour = 12
        currentminute = 60 - currentminute
        minute_tens = currentminute // 10
        minute_ones = currentminute % 10
        if currentminute != 0:
            add_positions(clock_word_pos["to"])
    else:
        minute_tens = currentminute // 10
        minute_ones = currentminute % 10
        if currentminute != 0:
            add_positions(clock_word_pos["past"])

    if currentminute == 15:
        add_positions(clock_word_pos["a"])
        add_positions(clock_word_pos["quarter"])
    elif currentminute == 30:
        add_positions(clock_word_pos["half"])
    elif currentminute in clock_minute_pos:
        add_positions(clock_minute_pos[currentminute])
    else:
        add_positions(clock_minute_pos[minute_tens * 10])
        add_positions(clock_minute_pos[minute_ones])

    if currentminute in [13, 14, 16, 17, 18, 19]:
        add_positions(clock_word_pos["teen"])


    

    add_positions(clock_word_pos["it is"])
    add_positions(clock_hour_pos[currenthour])



    return matrix


async def main():
    pool = socketpool.SocketPool(wifi.radio)
    ntp = adafruit_ntp.NTP(pool, tz_offset=int(os.getenv('CIRCUITPY_TZ_OFFSET')), cache_seconds=int(os.getenv('CIRCUITPY_NTP_CACHE_SECONDS')), server=os.getenv('CIRCUITPY_NTP_SERVER'))
    leds = parse_time(ntp.datetime)
    
    await draw_matrix(leds)
    




