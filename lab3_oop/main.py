import random
import tkinter as tk
from tkinter import messagebox


class GuessNumberGame:
  """Класс графического приложения для игры 'Угадай число'."""

  def __init__(self, root):
    self.root = root
    self.root.title("Игра Угадай число")
    self.root.geometry("400x350")
    self.root.minsize(300, 300)

    self.secret_number = random.randint(1, 100)
    self.attempts = 0

    self.create_menu()
    self.create_widgets()

  def create_menu(self):
    """Создание верхнего меню приложения."""
    menubar = tk.Menu(self.root)

    # Меню "Игра"
    game_menu = tk.Menu(menubar, tearoff=0)
    game_menu.add_command(label="Новая игра", command=self.reset_game)
    game_menu.add_separator()
    game_menu.add_command(label="Выход", command=self.root.quit)
    menubar.add_cascade(label="Игра", menu=game_menu)

    # Меню "Справка"
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="Правила", command=self.show_rules)
    menubar.add_cascade(label="Справка", menu=help_menu)

    self.root.config(menu=menubar)

  def create_widgets(self):
    """Создание элементов интерфейса (меток, полей ввода, кнопок)."""
    self.label_info = tk.Label(
        self.root,
        text="Я загадал число от 1 до 100.\nПопробуйте угадать!",
        font=("Arial", 11),
        justify=tk.CENTER,
    )
    self.label_info.pack(pady=15)

    self.entry = tk.Entry(self.root, font=("Arial", 14), justify=tk.CENTER)
    self.entry.pack(pady=10)
    # Привязка нажатия клавиши Enter к проверке числа
    self.entry.bind("<Return>", lambda event: self.check_guess())

    self.btn = tk.Button(
        self.root, text="Проверить", command=self.check_guess, width=15
    )
    self.btn.pack(pady=5)

    # Метка для вывода динамических результатов прямо на экран
    self.result_label = tk.Label(self.root, text="", font=("Arial", 11, "bold"))
    self.result_label.pack(pady=15)

  def check_guess(self):
    """Проверка введенного пользователем числа с обработкой исключений."""
    try:
      val = int(self.entry.get())

      # Проверка диапазона
      if val < 1 or val > 100:
        messagebox.showwarning(
            "Внимание", "Число должно быть в диапазоне от 1 до 100!"
        )
        return

      self.attempts += 1

      if val < self.secret_number:
        self.result_label.config(
            text=f"Попытка {self.attempts}: Загаданное число БОЛЬШЕ", fg="blue"
        )
      elif val > self.secret_number:
        self.result_label.config(
            text=f"Попытка {self.attempts}: Загаданное число МЕНЬШЕ",
            fg="orange",
        )
      else:
        messagebox.showinfo(
            "Победа!",
            f"Вы угадали число {self.secret_number} за {self.attempts}"
            " попыток!",
        )
        self.reset_game()

    except ValueError:
      messagebox.showerror(
          "Ошибка", "Некорректный ввод! Пожалуйста, введите целое число."
      )
      self.entry.delete(0, tk.END)

  def reset_game(self):
    """Сброс игры для нового раунда."""
    self.secret_number = random.randint(1, 100)
    self.attempts = 0
    self.result_label.config(text="")
    self.entry.delete(0, tk.END)
    self.label_info.config(text="Новая игра! Я загадал число от 1 до 100.")

  def show_rules(self):
    """Отображение правил игры."""
    messagebox.showinfo(
        "Правила игры",
        "Компьютер загадывает число от 1 до 100.\nВаша задача — угадать"
        " его за минимальное число попыток.",
    )


if __name__ == "__main__":
  root = tk.Tk()
  app = GuessNumberGame(root)
  root.mainloop()