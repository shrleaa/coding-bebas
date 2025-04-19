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

        ("\nAduh, abang bukan maksudku begitu", 0.07),
        ("Masalah stecu bukan brarti tak mau", 0.07),
        ("Jual mahal dikit kan bisa", 0.06),
        ("Coba kase effort-nya saja", 0.06),
        ("Kalo memang cocok bisa datang ke rumah", 0.06),   
        ("Stecu, stecu, stelan cuek baru malu", 0.09),
        ("Aduh, ade ini mau juga abang yang rayu", 0.06),
        ("Stecu, stecu, stelan cuek baru malu", 0.09),
        ("Aduh, ade ini mau juga abang yang maju", 0.06),
        
    ]


    delays = [0.3, 3.7, 7.1, 8.7, 10.5, 13.7, 17.4, 20.4, 24.0]
    
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