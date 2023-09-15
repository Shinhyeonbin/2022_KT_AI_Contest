import speech_recognition as sr
import soundfile as sf
import librosa

def recode(filename):
    filename = "converse_recode/" + filename

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
        with open(filename, "wb") as file:
            file.write(audio.get_wav_data())
    down_sample(filename)

def recode_time():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=2)
        try:
            text = r.recognize_google(audio, language="ko")
            text = text.replace(".", "")
        except:
            text =""
            pass
        #r.pause_threshold = 0.8
    return text

def down_sample(filename):
    y, sr = librosa.load(filename, sr=16000)
    #resample = librosa.resample(y, sr, 16000)
    sf.write(filename, y, sr, format='WAV', endian='LITTLE', subtype='PCM_16')

    #print("original wav sr: {}, original wav shape: {}, resample wav sr: {}, resmaple shape: {}".format(sr, y.shape, resample_sr, resample.shape))
