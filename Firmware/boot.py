import asyncio
from time import sleep
import board
import digitalio
import adafruit_74hc595


import os, wifi




latch_pin = digitalio.DigitalInOut(board.D3)
sr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), latch_pin)

rowsarr = [sr.get_pin(14), sr.get_pin(13), sr.get_pin(12), sr.get_pin(11), sr.get_pin(10), sr.get_pin(9), sr.get_pin(8),
        sr.get_pin(6), sr.get_pin(5), sr.get_pin(4), sr.get_pin(3), sr.get_pin(2), sr.get_pin(1), sr.get_pin(0)]

colsarr = [sr.get_pin(30), sr.get_pin(29), sr.get_pin(28), sr.get_pin(27), sr.get_pin(26), sr.get_pin(25), sr.get_pin(24),
        sr.get_pin(22), sr.get_pin(21), sr.get_pin(20), sr.get_pin(19), sr.get_pin(18), sr.get_pin(17), sr.get_pin(16)]


refreshtime = 0.02





async def draw_column(column, rows):
    colsarr[column].value = True
    for row in rows:
        rowsarr[row].value = True
    await asyncio.sleep(refreshtime)
    colsarr[column].value = False
    for row in rows:
        rowsarr[row].value = False

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
    

    


# draw CYBDOCLOCK, HACK CLUB, FALLOUT

startup_matrix = {
    0: [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    1: [1,0,0,0,0,0,0,0,1,0,0,0,0,0],
    2: [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
    3: [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
    4: [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
    5: [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    6: [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
    7: [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
    8: [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
    9: [1,0,0,0,0,0,0,0,1,0,0,0,0,0],
    10: [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    11: [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    12: [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    13: [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
}


no_wifi_matrix = {
    0:  [0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    1:  [0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    2:  [0,0,0,0,0,1,1,1,0,0,0,0,0,0],
    3:  [0,0,0,0,1,1,1,1,0,0,0,0,0,0],
    4:  [0,0,0,0,0,1,0,0,1,0,0,0,0,0],
    5:  [0,0,1,1,1,1,1,1,1,1,1,1,1,0],
    6:  [0,1,1,0,0,1,0,0,1,0,0,0,0,0],
    7:  [0,1,1,0,0,1,0,0,1,0,0,0,0,0],
    8:  [0,0,1,1,1,1,1,1,1,1,1,1,1,0],
    9:  [1,0,0,0,0,1,0,0,1,0,0,0,0,0],
    10: [0,0,0,0,1,0,0,1,1,0,0,0,0,0],
    11: [0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    12: [0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    13: [0,0,0,0,0,0,0,0,0,1,0,0,0,0],
}


async def main():
    
    if os.getenv('CIRCUITPY_WIFI_SSID') is None or os.getenv('CIRCUITPY_WIFI_PASSWORD') is None:
        print("no wifi creds")
        
        
        
        
    print("connecting...")
    await wifi.radio.connect(ssid=os.getenv('CIRCUITPY_WIFI_SSID'),
                            password=os.getenv('CIRCUITPY_WIFI_PASSWORD'))

    print("my IP addr:", wifi.radio.ipv4_address)






