import os
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading

try:
    # Compatibilidad con playsound o playsound3
    from playsound import playsound
except ImportError:
    from playsound3 import playsound  # type: ignore
# Carpeta base del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class AnimatedGif(tk.Label):
    #Widget que muestra un GIF animado repitiéndose en bucle.
    def __init__(self, master, gif_path: str, delay: int = 80):
        image = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(image)]
        self.delay = delay
        self.idx = 0
        super().__init__(master, image=self.frames[0])
        self.after(self.delay, self._animate)
    def _animate(self):
        self.idx = (self.idx + 1) % len(self.frames)
        self.configure(image=self.frames[self.idx])
        self.after(self.delay, self._animate)
def play_sound(sound_path: str):
    #Reproduce sonido en un hilo para no bloquear la GUI.
    threading.Thread(target=playsound, args=(sound_path,), daemon=True).start()
def main():
    root = tk.Tk()
    root.title('Animación con sonido – Tkinter')
    root.geometry('400x400')
    gif_path = os.path.join(BASE_DIR, 'animation.gif')
    sound_path = os.path.join(BASE_DIR, 'boing.wav')
    gif_widget = AnimatedGif(root, gif_path, delay=80)
    gif_widget.pack(expand=True)
    tk.Button(
        root,
        text='Reproducir sonido',
        command=lambda: play_sound(sound_path),
        font=('Arial', 12, 'bold'),
        padx=10,
        pady=5,
    ).pack(pady=10)
    root.mainloop()
if __name__ == '__main__':
    main()
