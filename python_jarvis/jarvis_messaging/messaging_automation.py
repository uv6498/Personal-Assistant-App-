import pywhatkit as kit
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand. Please try again.")
            return None
        except sr.RequestError:
            speak("There was an error connecting to the voice service.")
            return None

def words_to_numbers(spoken_text):
    """Convert spoken digits into a valid phone number."""
    digit_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    words = spoken_text.split()
    number = ""

    for word in words:
        if word in digit_map:
            number += digit_map[word]
        elif word.isdigit():
            number += word  # Directly append if recognized as a number

    return number

def get_phone_number():
    """Ask the user for a phone number and convert it to digits."""
    speak("Say the phone number including country code.")
    phone_spoken = listen()
    
    if phone_spoken:
        phone_number = words_to_numbers(phone_spoken)
        if phone_number.isdigit() and len(phone_number) >= 10:
            return f"+{phone_number}"
        else:
            speak("Invalid phone number. Please try again.")
            return None
    return None

def get_message():
    """Ask the user for a message to send."""
    speak("What message would you like to send?")
    return listen()

def send_whatsapp_message(phone, message):
    """Send a WhatsApp message instantly."""
    try:
        speak(f"Sending message to {phone}")
        kit.sendwhatmsg_instantly(phone, message)  # Send instantly
        speak("Message sent successfully.")
    except Exception as e:
        speak("Sorry, I was unable to send the message.")
        print(f"Error: {e}")

if __name__ == "__main__":
    speak("Hello! Sir")
    
    phone_number = get_phone_number()
    if phone_number:
        message = get_message()
        if message:
            send_whatsapp_message(phone_number, message)
        else:
            speak("No message detected.")
    else:
        speak("Phone number not recognized.")
