import speech_recognition as sr

r = sr.Recognizer()

audio = 'harvard.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print('Done!')

try:
    value = r.recognize_google(audio)

    if str is bytes:
        result = u"{}".format(value).encode("utf-8")

    else:
        result = "{}".format(value)

    with open("outputs.txt", "a") as f:
        f.write(result)
    print(result)

except sr.UnknownValueError:
    print("")

except sr.RequestError as e:
    print("{0}".format(e))

except KeyboardInterrupt:
    pass

except Exception as e:
    print(e)