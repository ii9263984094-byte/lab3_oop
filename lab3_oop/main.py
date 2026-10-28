import random
import tkinter as tk
from tkinter import messagebox


class GuessNumberGame:

  def __init__(self, root):
    self.root = root
    self.root.title("Игра Угадай число")
    self.root.geometry("400x300")
    self.root.minsize(300, 250)

    self.secret_number = random.randint(1, 100)
    self.attempts = 0

    self.create_menu()
    self.create_widgets()

  def create_menu(self):
    menubar = tk.Menu(self.root)
    game_menu = tk.Menu(menubar, tearoff=0)
    game_menu.add_command(label="Новая игра", command=self.reset_game)
    game_menu.add_separator()
    game_menu.add_command(label="Выход", command=self.root.quit)
    menubar.add_cascade(label="Игра", menu=game_menu)
    self.root.config(menu=menubar)

  def create_widgets(self):
    self.label = tk.Label(
        self.root, text="Я загадал число от 1 до 100. Попробуйте угадать!"
    )
    self.label.pack(pady=20)

    self.entry = tk.Entry(self.root, font=("Arial", 14))
    self.entry.pack(pady=10)

    self.btn = tk.Button(
        self.root, text="Проверить", command=self.check_guess
    )
    self.btn.pack(pady=10)

  def check_guess(self):
    try:
      val = int(self.entry.get())
      self.attempts += 1
      if val < self.secret_number:
        messagebox.showinfo("Подсказка", "Загаданное число больше")
      elif val > self.secret_number:
        messagebox.showinfo("Подсказка", "Загаданное число меньше")
      else:
        messagebox.showinfo(
            "Победа", f"Вы угадали за {self.attempts} попыток!"
        )
        self.reset_game()
    except ValueError:
      messagebox.showerror(
          "Ошибка", "Пожалуйста, введите корректное число!"
      )

  def reset_game(self):
    self.secret_number = random.randint(1, 100)
    self.attempts = 0
    self.entry.delete(0, tk.END)


if __name__ == "__main__":
  root = tk.Tk()
  app = GuessNumberGame(root)
  root.mainloop()