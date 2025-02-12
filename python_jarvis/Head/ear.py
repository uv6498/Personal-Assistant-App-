import speech_recognition as sr
from deep_translator import GoogleTranslator

def listen_and_translate():
    recognizer = sr.Recognizer()
    translator = GoogleTranslator(source="hi", target="en")

    with sr.Microphone() as source:
        print("Speak something in Hindi...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5)
            hindi_text = recognizer.recognize_google(audio, language="hi")
            print(f"Recognized Hindi Text: {hindi_text}")

            translated_text = translator.translate(hindi_text)
            return translated_text

        except sr.UnknownValueError:
            return "Sorry, could not understand the speech."
        except sr.RequestError:
            return "Could not request results, check your internet connection."

# Example usage:
output_text = listen_and_translate()
print(f"Translated English Text: {output_text}")
