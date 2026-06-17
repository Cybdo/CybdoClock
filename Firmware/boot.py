from time import sleep
import board
import digitalio
import adafruit_74hc595

latch_pin = digitalio.DigitalInOut(board.D3)
sr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), latch_pin)

rowsarr = [sr.get_pin(14), sr.get_pin(13), sr.get_pin(12), sr.get_pin(11), sr.get_pin(10), sr.get_pin(9), sr.get_pin(8),
        sr.get_pin(6), sr.get_pin(5), sr.get_pin(4), sr.get_pin(3), sr.get_pin(2), sr.get_pin(1), sr.get_pin(0)]

colsarr = [sr.get_pin(30), sr.get_pin(29), sr.get_pin(28), sr.get_pin(27), sr.get_pin(26), sr.get_pin(25), sr.get_pin(24),
        sr.get_pin(22), sr.get_pin(21), sr.get_pin(20), sr.get_pin(19), sr.get_pin(18), sr.get_pin(17), sr.get_pin(16)]


refreshtime = 0.02

def draw_column(column, rows):
    colsarr[column].value = True
    for row in rows:
        rowsarr[row].value = True
    sleep(refreshtime)
    colsarr[column].value = False
    for row in rows:
        rowsarr[row].value = False

def draw_matrix(matrix):
    for column in matrix.keys():
        rows = []
        for row in range(14):
            if matrix[column][row] == 1:
                rows.append(row)
        draw_column(column, rows)
    

    


# draw CYBDOCLOCK, HACK CLUB, FALLOUT

startup_matrix = {0: [1,1,1,1,1,1,1,1,1,1,0,0,0,0],
              8: [0,1,1,1,1,0,1,1,1,1,0,0,0,0],
              13: [0,0,1,1,1,1,1,1,1,0,0,0,0,0]
}

for i in range(5/refreshtime):
    draw_matrix(startup_matrix)




