# radical-love-oracle
## Radical Love Oracle is an interactive experience that allows users to send love and affirmations through a simple graphical interface. its a conceptual art piece! On the screen, there are a few affirmations that cycle thru. with each click, close your eyes and channel your energy thru the buttons out into the world. No prior coding experience is needed

### We are always engaging in digital spaces and world that are lacking in love and community. This oracle is made to remind us of what can be, not what is. It is a testament to stay hopeful.



## install python and homebrew (for Mac OS)

Open Terminal and install homebrew using:
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
## install python using:
    brew install python 


## install required dependancies:
pygame and tkvideo:
    pip install pygame tkvideo
    
for handling videos
    brew install ffmpeg


## make changes to the valentines.py on lines 11,13,15 and 17 to set the locations locally to the audio and visual files in this project.


# Troubleshooting

Issue: "pygame.error: ModPlug_Load failed"

Solution: Ensure the audio files are in the correct location and correctly formatted (.mp3). If using .m4a, convert it to .mp3 using an online converter or FFmpeg:

    ffmpeg -i input.m4a output.mp3

Issue: "ffmpeg: command not found"

Solution: Install FFmpeg:

    brew install ffmpeg  # macOS

## Enjoy!

