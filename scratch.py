#!/Users/kgaylord/Documents/MidiAlgo/venv/bin/python

#Time is number of ticks, which is related to beats by way of ticks_per_beat
#Tempo is the number of microseconds per beat. tempo2bpm() will convert to bpm
#tick2second() will tell you at which second the tick is.


from mido import Message, MidiFile, MidiTrack
from mido import MetaMessage
from mido import bpm2tempo
import mido
import midi_tools
import pygame

print('START')

# mid_file = MidiFile('new_midfile.mid', clip=True)

# merged_tracks = mido.merge_tracks(mid_file.tracks)
#
# for track in merged_tracks:
#     print(track)
#
# print('END')

# mid = MidiFile()
# mid.tracks.append(merged_tracks)
# mid.save('new_midfile.mid')


# mid_arr = midi_tools.mid2arry(mid_file)
#
# print(mid_arr)
# print(mid_arr.shape)

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

mytempo = bpm2tempo(90)
track.append(MetaMessage('set_tempo', tempo=mytempo, time=0))
track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=64, velocity=64, time=0))
track.append(Message('note_on', note=100, velocity=64, time=0))
track.append(Message('note_on', note=64, velocity=0, time=0))
track.append(Message('note_on', note=100, velocity=0, time=1000))
track.append(Message('note_on', note=30, velocity=120, time=0))
track.append(Message('note_on', note=30, velocity=0, time=1000))

mid.save('my.mid')

mid_file = MidiFile('my.mid', clip=True)

merged_tracks = mido.merge_tracks(mid_file.tracks)

for track in merged_tracks:
    print(track)

pygame.init()
pygame.mixer.music.load("my.mid")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)
