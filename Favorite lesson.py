import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [

        ("A story that I'll never tell", 0.09),
        ("'Cause our worlds just didn't collide", 0.12),
        ("You had yours, and I had mine", 0.18),
        ("Got lost in different directions", 0.15),
        ("But being with you was my favorite lesson", 0.18),    
        
    ]


    delays = [
        2.5,  # sebelum "A story..."
        3.8,  # sebelum "'Cause our worlds..."
        3.9,  # sebelum "You had yours..."
        4.0,  # sebelum "Got lost..."
        4.3,  # sebelum "But being with you..."
    ]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()