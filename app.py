import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio_data = r.record(source, duration=5)
        print("Recognizing...")

        text = r.recognize_google(audio_data, language='es-ES')
        print(text)

if __name__ == "__main__":
    main()