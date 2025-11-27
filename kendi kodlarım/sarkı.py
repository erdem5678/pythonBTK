import time
from colorama import Fore, Style, init
# Renklerin düzgün çalışması için colorama'yı başlatıyoruz
init()

def print_lyrics():
    lyrics = [
        (Fore.RED, "I can't feel my face when I'm with you (I can't feel my face)"),
        (Fore.WHITE, "But I love it (but I love it), but I love it, oh (oh, I love it)"),
        (Fore.RED, "I can't feel my face when I'm with you (said, I can't feel my face)"),
        (Fore.WHITE, "But I love it (but I love it), but I love it, oh (still I love it)"),
        (Fore.RED, "I can't feel my face when I'm with you (I can't feel my face when I'm with you)"),
        (Fore.WHITE, "But I love it, but I love it, oh (love, love it, told you I did)"),

    ]
    for color, line in lyrics:
        print(color + line + Style.RESET_ALL)
        time.sleep(0.8)  # Burada bekleme süresini değiştirebilirsiniz

if __name__ == "__main__":
    print_lyrics()
