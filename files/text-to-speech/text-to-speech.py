from gtts import gTTS
import os


text = 'Hi, there! Hope you are doing fine, stay safe!'
output = gTTS(text=text,  lang='en', slow=False)
output.save('output.mp3')

os.system("start output.mp3")

