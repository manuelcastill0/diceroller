#i got reference from your code teacher

import flet as ft
import random

def main(page: ft.Page):

    def diceroll(e):
        value = random.randint(1,6)
        diceNum.value = str(value)
        if value == 1:
            diceImage.src = "face1.png"
        elif value == 2:
            diceImage.src = "face2.png"
        elif value == 3:
            diceImage.src = "face3.png"
        elif value == 4:
            diceImage.src = "face4.png"
        elif value == 5:
            diceImage.src = "face5.png"
        elif value == 6:
            diceImage.src = "face6.png"
        page.update()

    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"

    diceImage = ft.Image(src="dice.png")
    diceNum = ft.Text(value="No roll yet", size= 40)
    button = ft.ElevatedButton(text="Roll the dice", height=40, width=200, on_click=diceroll)
    page.add(diceImage, diceNum, button)

ft.app(target=main)