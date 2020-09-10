import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

#Sonido 2
wave_697 = frecuencia697.make_wave(duration=0.5, start=0, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=0, framerate=44100)

wave_sonido2 = wave_697 + wave_1336

#Sonido 4
wave_770 = frecuencia770.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_sonido4 = wave_770 + wave_1209

#Sonido 2
wave_697 = frecuencia697.make_wave(duration=0.5, start=1.0, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=1.0, framerate=44100)

wave_sonidonuevo2 = wave_697 + wave_1336

#Sonido 4
wave_697 = frecuencia697.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido3 = wave_697 + wave_1336

#Sonido Final
wave_sonido_final = wave_sonido2 + wave_sonido4 + wave_sonidonuevo2 + wave_sonido3

wave_sonido_final.write("sonidoexamen.wav")
