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
    # Lirik dengan kecepatan mengetik dan jeda waktu antar-lirik berdasarkan analisis
    lyrics = [
        ("\nYou're the sunshine on my life", 0.15),
        ("I just wanna see how beautiful you are", 0.10),
        ("You know that I see it", 0.14),
        ("I know you're a star", 0.12),
        ("Where you go I'll follow", 0.15),
        ("No matter how far", 0.08),
        ("If life is a movie", 0.12),
        ("Oh, you're the best part", 0.10),
    ]

    # Jeda antar-lirik (dalam detik)
    delays = [
        0.3,  # sebelum "You're the sunshine..."
        7.1,  # sebelum "I just wanna see..."
        14.0,  # sebelum "You know that..."
        17.5,  # sebelum "I know you're..."
        20.9,  # sebelum "Where you go..."
        23.5,  # sebelum "No matter how..."
        26.5,  # sebelum "If life is a movie..."
        29.9,  # sebelum "Oh, you're the best part..."
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