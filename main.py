"""
Classes skal implemeteres.
Problemer med arcade interpeuter.
SSD gået i stykker.
1 time program
"""


import arcade
import math

#Konstanter
BREDDE = 1920
HOEJDE = 1080
CIRKEL = 2000

LINJE = 10
#Taget fra vektorprojekt, det er basically punkter der definere
def linje(tid, origo, retningsvektoren):
    x_0, y_0 = origo
    r_x, r_y = retningsvektoren
    x = x_0 + r_x * tid
    y = y_0 + r_y * tid
    return x, y

#Taget fra vektorprojekt, det er basically punkter der definere
def cirkel(tid, centrum, radius, vinkelhastighed, fase=0):
    x_c, y_c = centrum
    x = x_c + radius * math.cos(vinkelhastighed * tid + fase)
    y = y_c + radius * math.sin(vinkelhastighed * tid + fase)
    return x, y

# Delta tid også kendt som delta time, óver en periode af tid.
def tegn(delta_tid):
    #starter en render da det skal renders overtid og hvis man ikke starter et render kommer der ikke noget frem da der skal være et objekt der rykker sig.
    arcade.start_render()
#vand
    arcade.draw_lrtb_rectangle_filled(0, 1920, 600, 0, arcade.csscolor.SKY_BLUE)
#bro
    arcade.draw_lrtb_rectangle_filled(0, 200, 630, 590, arcade.csscolor.SADDLE_BROWN)
#sten under vores bro
    arcade.draw_lrtb_rectangle_filled(0, 200, 590, 0, arcade.csscolor.SLATE_GRAY)
# første sky
    arcade.draw_ellipse_filled(100, 1000, 150, 100, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(150, 1000, 150, 120, arcade.csscolor.WHITE)
# anden sky
    arcade.draw_ellipse_filled(400, 1000, 150, 120, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(480, 1000, 150, 100, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(440, 970, 130, 100, arcade.csscolor.WHITE)


#osv
    arcade.draw_ellipse_filled(700, 1000, 150, 120, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(750, 1000, 150, 100, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(740, 1070, 130, 100, arcade.csscolor.WHITE)

    arcade.draw_ellipse_filled(1000, 1020, 150, 120, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(1050, 1000, 150, 100, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(1040, 1070, 130, 100, arcade.csscolor.WHITE)

    arcade.draw_ellipse_filled(1330, 900, 150, 120, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(1320, 970, 150, 100, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(1360, 970, 130, 100, arcade.csscolor.WHITE)

    arcade.draw_ellipse_filled(1600, 950, 150, 120, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(1650, 910, 150, 100, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(1640, 980, 130, 100, arcade.csscolor.WHITE)


# Koden for linjen som vores cirkel følger
    x_linje,y_linje = linje(tegn.tid, (0,650),(75,-0.5))
#vores usynelige punkt:
# arcade.draw_circle_filled(x_linje, y_linje, 5, arcade.csscolor.RED)



# Koden for cirklen og begynder at tegne vores punkter
    x, y = cirkel(tegn.tid, (x_linje, y_linje), -100, -0.3, 1)
    x1, y1 = cirkel(tegn.tid, (x , y), -300, -0.3, 0)
    arcade.draw_circle_filled(x1, y1, 5, arcade.csscolor.WHITE)
    if len(tegn.track) == CIRKEL:
        tegn.track.fjern(CIRKEL)
    for punkt in tegn.track:
        arcade.draw_circle_filled(*punkt, 2, arcade.csscolor.WHITE)
    tegn.tid += delta_tid

    #Vores første cirkel som kører rundt om vores anden cirkel.
    #tegn.spor.append((x, y))

    tegn.track.append((x1, y1))

def main():
    arcade.open_window(BREDDE, HOEJDE, "Cat goes fishing")

    arcade.set_background_color(arcade.csscolor.GREEN)

    tegn.track_linje = list()
    tegn.tid = 0.0
    tegn.track = list()
    #Funktion kan ikke køre hvis der ikke er en tidsbeløb
    arcade.schedule(tegn, 1 / 60)
    #Kører det overtid
    arcade.run()


main()


