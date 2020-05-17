'''A class for algorithmically generating a midi song based on a chord choice evaluation engine
created for the Autonomous Digital Audio Workstation, by Devan Mallory'''



class generateMIDI():

    @staticmethod
    def generateMIDIc(track, note, notelength, startingpos):
        updatetext(notelength)
        startingposa = startingpos  # formula goes here
        newnote = midi.NoteOnEvent(tick=startingpos, velocity=50, pitch=note)
        track.append(newnote)
        newpos = startingpos + notelength
        noteend = midi.NoteOffEvent(tick=newpos, velocity=50, pitch=note)
        track.append(noteend)
        return ("MIDI note generated on", "for", note)

    @staticmethod
    def generateMIDIchordc(track, note1, note2, note3, note4, notelength, startingpos):
        generateMIDI.generateMIDIc(track, note1, notelength, startingpos)
        generateMIDI.generateMIDIc(track, note2, notelength, startingpos)
        generateMIDI.generateMIDIc(track, note3, notelength, startingpos)
        generateMIDI.generateMIDIc(track, note4, notelength, startingpos)

