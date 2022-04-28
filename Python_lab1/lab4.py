from Drums import Drum
from Synths import Synth

def play_instrument(instrument):
    instrument.play()

drums = Drum()
play_instrument(drums)

synth = Synth()
play_instrument(synth)