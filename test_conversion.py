import os
from pydub import AudioSegment

allSubDirs = [x[0] for x in os.walk('.')]
audioSubDirs = []
for i in allSubDirs:
    if '\\Audios' in i:
        audioSubDirs.append(i)

subdirs = subdirs [1:]

for direc in subdirs:
    audioFiles = os.listdir(direc)
    for audioName in audioFiles:
        audioDirec = direc + '\\' + audioName
        acceptableFileTypes = ['aac', 'mp3']
        if audioDirec[-3:] == ("wav"):
            print("Audio file " + audioName + " is already in .wav format.")
        elif audioName[-3:] in acceptableFileTypes:
            print(audioDirec)
            newLocName = audioDirec[:-3]+'wav'
            AudioSegment.from_file(audioDirec).export(newLocName, format = 'wav')
            os.remove(audioDirec)
        else:
            if('.' not in audioName):
                print("Folder detected.")
            else:
                print("File is not an acceptable audio format")