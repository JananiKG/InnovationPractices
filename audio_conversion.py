import os
from pydub import AudioSegment

allSubDirs = [x[0] for x in os.walk('.')]
audioSubDirs = []
for i in allSubDirs:
    if '\\Audios' in i:
        audioSubDirs.append(i)

audioSubDirs = audioSubDirs[1:]

for direc in audioSubDirs:
    audioFiles = os.listdir(direc)
    c = 0
    for audioName in audioFiles:
        audioDirec = direc + '\\' + audioName
        acceptableFileTypes = ['aac', 'mp3']
        if audioDirec[-3:] == ("wav"):
            print("Audio file " + audioName + " is already in .wav format.")
        elif audioName[-3:] in acceptableFileTypes:
            c += 1
            newLocName = direc + '\\Audio_File_' + str(c) + '.wav'
            AudioSegment.from_file(audioDirec).export(newLocName, format = 'wav')
            os.remove(audioDirec)
        else:
            if('.' not in audioName):
                print("Folder detected.")
            else:
                print("File is not an acceptable audio format")