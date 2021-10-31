############################################################################
# A sample program to create a single-track MIDI file, add a note,
# and write to disk.
############################################################################

#Import the library
from midiutil.MidiFile3 import MIDIFile
import random

# Create the MIDIFile Object
MyMIDI = MIDIFile(1)

# Improvisation Technique 1
a_minor_scale = [69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91]
chord_set_one = [
    (57, 60, 64),
    (53, 57, 60),
    (55, 59, 62),
    (52, 55, 59)
]

# Improvisation Technique 2 & 3
c_blue_melody = [72, 75, 77, 78, 79, 82, 84]
e_blue_melody = [64, 67, 69, 70, 71, 74, 76]
chord_set_three = [
    (48, 52, 55, 58),
    (48, 52, 55, 58),
    (48, 52, 55, 58),
    (48, 52, 55, 58),
    (53, 57, 60, 63),
    (53, 57, 60, 63),
    (48, 52, 55, 58),
    (48, 52, 55, 58),
    (55, 59, 62, 65),
    (53, 57, 60, 63),
    (48, 52, 55, 58),
    (48, 52, 55, 58),
]

# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
time = 0
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time, 120)

# Add a note. addNote expects the following information:
channel = 0
pitch = 69
duration = 1
volume = 100

# Pass in melody and bass lists
def play_music(melody, bass, m_t):
    m_time = 0
    m_tempo = m_t
    m_duration = 2

    b_time = 0
    b_tempo = 2
    b_duration = 4

    for b in bass:
        #for i in range(4): #play chords 4 times
        for n in b: #at note of each chord tuple
            # Create chord
            MyMIDI.addNote(track, channel, n, b_time, b_duration, volume)

            m_key = random.choice(melody)
            MyMIDI.addNote(track, channel, m_key, m_time, m_duration, volume)
            m_time += m_tempo
        b_time += b_tempo

    binfile = open("music.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()


play_music(a_minor_scale, chord_set_one, 0.5)
#play_music(c_blue_melody, chord_set_three, 0.5)
#play_music(e_blue_melody, chord_set_three, 0.5)

# Now add the note.
#MyMIDI.addNote(track,channel, 60, 0,duration,volume)
#MyMIDI.addNote(track,channel, 69, 1,duration,volume)

# And write it to disk.
#binfile = open("output.mid", 'wb')
#MyMIDI.writeFile(binfile)
#binfile.close()