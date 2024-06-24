from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img

    img = Image.open("855.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)

    try:
        music_path = "music1.mp3"
        mixer.music.load(music_path)
        mixer.music.play()
        pygame.time.delay(2000)  # Delay for 2 seconds
        mixer.music.stop()  # Stop the music after 2 seconds
    except pygame.error as e:
        print("Error loading music file:", e)

    for img_frame in ImageSequence.Iterator(img):
        img_frame = img_frame.resize((1000, 500))
        img_frame = ImageTk.PhotoImage(img_frame)
        lbl.config(image=img_frame)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()
