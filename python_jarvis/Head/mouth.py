import asyncio
import threading
import os
import edge_tts
import pygame

VOICE = "en-AU-WilliamNeural"  
BUFFER_SIZE = 1024

def remove_file(file):
    
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            if os.path.exists(file):
                os.remove(file)
            break
        except Exception as e:
            print(f"Error removing file: {e}")
            attempts += 1

async def amain(TEXT, output_file) -> None:
    
    try:
        cm_text = edge_tts.Communicate(TEXT, VOICE)  # Fixed missing parameters
        await cm_text.save(output_file)
        
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
        print(f"Error in TTS processing: {e}")
    finally:
        remove_file(output_file)

def play_audio(file_path):
    
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.delay(10)  # Fixed incorrect function call
        
        pygame.quit()
    except Exception as e:
        print(f"Error playing audio: {e}")

def speak(TEXT, output_file=None):
    
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "speak.mp3")
    
    asyncio.run(amain(TEXT, output_file))

if __name__ == "__main__":
    speak("Hello Sir ,it's 8:00 am in the morning, time to hit the gym  ")
    