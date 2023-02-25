from gtts import gTTS

import os



name = input ("enter name: ")

town = input("enter town: ")
adj = input("enter adjective: ")
adv = input ("enter adverb: ")
story = "Once upon a time, there was a young girl named (name). She lived in a small (village) on the edge of a vast forest. (name) was a curious and (adventurous) girl who loved to explore the woods and discover (new) things."
new_story = story.replace('(name)', name)
new_story = new_story.replace('(village)', town)
new_story = new_story.replace('(adventurous)', adj)
new_story = new_story.replace('(new)', adv)

language = 'en'


myobj = gTTS(text=new_story, lang=language, slow=False)
myobj.save("story.mp3")


print(new_story)
