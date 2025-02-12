import cv2
import speech_recognition as sr
import pyttsx3
import datetime

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    """Speak the given text aloud."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for the command to take a picture...")
        speak("Say ' jarvis take a picture' to click an image.")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            speak("I couldn't understand. Please try again.")
            return None

def take_picture():
    """Capture an image from the webcam and save it."""
    cam = cv2.VideoCapture(0)  # Open the webcam
    ret, frame = cam.read()  # Capture a frame
    if ret:
        filename = f"picture_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)  # Save the image
        speak(f"Picture taken and saved as {filename}.")
        print(f"Picture saved as {filename}.")
    else:
        speak("Failed to capture image.")
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    command = listen()
    if command and "take a picture" in command:
        take_picture()
    else:
        speak("Command not recognized.")
