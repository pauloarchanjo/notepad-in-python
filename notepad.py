import tkinter as tk
from tkinter import filedialog, messagebox

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas")
        
        self.dark_mode = False
        self.font_size = 12
        self.text_widget = tk.Text(self.root, wrap="word", font=("Calibri", self.font_size))
        self.text_widget.pack(fill="both", expand=True)
        
        self.create_menu()
        self.create_dark_mode_button()
        self.create_font_size_buttons()
        
        self.root.geometry("800x600")
        self.fixed = False

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Novo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)
        
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Visualizar", menu=view_menu)
        view_menu.add_command(label="Modo Escuro", command=self.toggle_dark_mode)
        view_menu.add_separator()
        view_menu.add_command(label="Aumentar Fonte", command=self.increase_font_size)
        view_menu.add_command(label="Diminuir Fonte", command=self.decrease_font_size)
        view_menu.add_separator()
        view_menu.add_command(label="Fixar Janela", command=self.toggle_fixed)

    def create_dark_mode_button(self):
        self.dark_mode_button = tk.Button(self.root, text="Modo Escuro", command=self.toggle_dark_mode)
        self.dark_mode_button.pack()

    def create_font_size_buttons(self):
        font_size_frame = tk.Frame(self.root)
        font_size_frame.pack()
        
        increase_button = tk.Button(font_size_frame, text="Aumentar Fonte", command=self.increase_font_size)
        increase_button.pack(side="left")
        
        decrease_button = tk.Button(font_size_frame, text="Diminuir Fonte", command=self.decrease_font_size)
        decrease_button.pack(side="right")

    def create_fixed_button(self):
        fixed_button = tk.Button(self.root, text="Fixar Janela", command=self.toggle_fixed)
        fixed_button.pack()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        bg_color = "#1e1e1e" if self.dark_mode else "white"
        fg_color = "white" if self.dark_mode else "black"
        
        self.root.configure(bg=bg_color)
        self.text_widget.configure(bg=bg_color, fg=fg_color)
        self.dark_mode_button.configure(bg=bg_color, fg=fg_color)

    def increase_font_size(self):
        self.font_size += 2
        self.text_widget.configure(font=("Arial", self.font_size))

    def decrease_font_size(self):
        self.font_size -= 2
        self.text_widget.configure(font=("Arial", self.font_size))

    def toggle_fixed(self):
        if not self.fixed:
            self.root.attributes("-topmost", True)
            self.fixed = True
        else:
            self.root.attributes("-topmost", False)
            self.fixed = False

    def new_file(self):
        self.text_widget.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get("1.0", tk.END)
                file.write(content)

def main():
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
