import tkinter as tk
import tkinter.messagebox
from tkvideo import tkvideo
import pygame
import time

class valentines:

    def __init__(self):
        #set location for static2.mp3
        static_audio = "/Users/francescatse/Desktop/radical-love-oracle/audio/static2.mp3"
        #set location for comp.mov
        comp_visual = "/Users/francescatse/Desktop/radical-love-oracle/visual/comp.mov"
        #set location for love.mp3
        love_audio = "/Users/francescatse/Desktop/radical-love-oracle/audio/love.mp3"
        #set location for affirm.mp3
        affirm_audio = "/Users/francescatse/Desktop/radical-love-oracle/audio/affirm.mp3"
       
    #main window configs
        self.main_window = tkinter.Tk()
        self.main_window.geometry("650x550")
        self.main_window.configure(bg="pink")
    
    #music configs
        pygame.mixer.init()
        pygame.mixer.music.load(static_audio)
        print("Audio file loaded successfully.")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.011)
        
       
    #video of comp configs
        self.video_label = tk.Label(self.main_window,text="Click to affirm yourself or send love")
        self.video_label.pack(pady=15)
        self.video = tkvideo(comp_visual, self.video_label, loop=1, size=(525, 410))
        self.video.play()
    #text in the computer overlay
        self.overlay_text = tk.Label(self.main_window, text="Sending Love", font=("Georgia", 12, "bold"), fg="black", padx=1, pady=1 ,bg="white")
        self.overlay_text.place(relx=0.5, rely=0.28, anchor="center")
        self.messages = [
            "𓆩⚝𓆪my love is ruled by mars𓆩⚝𓆪",
            "₊⊹my grief is a form of rebellion₊⊹",
            "⋆☾⋆my sensitivity is my power⋆☾⋆",
            "*༺·my joy is resilience·༻*",
            "𓂃 ࣪༯ my body is not a spectacle ༯𓂃",
            "✩₊˚my intuition is a compass˚₊✩",
            "⋆୨♡୧⋆my hope is unwavering⋆୨♡୧⋆",
            "ˋ♡ˎmy existance is a testimonyˋ♡ˎ"
        ]
 
        self.current_message_index = 0
        self.display_next_message()
        
    #buttons configs
        self.loveButton = tkinter.Button(self.main_window, text="LOVE", command=self.play_love_audio, width=12, height=3, font=("Helvetica", 16))
        self.affirmButton = tkinter.Button(self.main_window, text="AFFIRM",command=self.play_affirm_audio, width=12, height=3,font=("Helvetica", 16))
        
        self.loveButton.pack(side="left")
        self.affirmButton.pack(side="left")
        self.loveButton.pack(padx=120)
        self.loveButton.pack(pady=15)
        self.affirmButton.pack(pady=15)
        
     #button music configs
        self.love_audio = pygame.mixer.Sound(love_audio)
        self.affirm_audio = pygame.mixer.Sound(affirm_audio)
        tk.mainloop()
        
    def play_love_audio(self):
        """Play the LOVE button audio."""
        self.love_audio.play()
        tk.messagebox.showinfo('Love', 'love has been sent into the world')
    
    def play_affirm_audio(self):
        """Play the AFFIRM button audio."""
        self.affirm_audio.play()
        tk.messagebox.showinfo('Affirm', "you've been affirmed")
        
    def display_next_message(self):

        if self.current_message_index < len(self.messages):
            self.overlay_text.config(text=self.messages[self.current_message_index])
            
            self.current_message_index += 1
        else:
            self.current_message_index = 0
            self.overlay_text.config(text=self.messages[self.current_message_index])

        self.main_window.after(4500, self.display_next_message)



radicalLove = valentines()
