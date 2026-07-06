import os
import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("메모장")
        self.root.geometry("800x600")

        self.file_path = None

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        self.text = tk.Text(self.root, undo=True, wrap="word")
        self.text.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.text)
        scrollbar.pack(side="right", fill="y")
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="파일", menu=file_menu)
        file_menu.add_command(label="새 파일", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="열기", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="저장", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="다른 이름으로 저장", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="끝내기", command=self.on_close)

        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="편집", menu=edit_menu)
        edit_menu.add_command(label="잘라내기", accelerator="Ctrl+X", command=self.cut_text)
        edit_menu.add_command(label="복사", accelerator="Ctrl+C", command=self.copy_text)
        edit_menu.add_command(label="붙여넣기", accelerator="Ctrl+V", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="모두 선택", accelerator="Ctrl+A", command=self.select_all)

        self.root.bind_all("<Control-n>", lambda e: self.new_file())
        self.root.bind_all("<Control-o>", lambda e: self.open_file())
        self.root.bind_all("<Control-s>", lambda e: self.save_file())
        self.root.bind_all("<Control-a>", lambda e: self.select_all())

    def new_file(self):
        if self._should_save():
            self.text.delete("1.0", tk.END)
            self.file_path = None
            self.root.title("메모장")
            self.text.edit_modified(False)

    def open_file(self):
        if self._should_save():
            path = filedialog.askopenfilename(
                defaultextension=".txt",
                filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
            )
            if path:
                with open(path, "r", encoding="utf-8") as f:
                    self.text.delete("1.0", tk.END)
                    self.text.insert("1.0", f.read())

                self.file_path = path
                self.root.title(os.path.basename(path) + " - 메모장")
                self.text.edit_modified(False)

    def save_file(self):
        if self.file_path:
            self._write_file(self.file_path)
            return True
        return self.save_as()

    def save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
        )
        if path:
            self._write_file(path)
            self.file_path = path
            self.root.title(os.path.basename(path) + " - 메모장")
            return True
        return False

    def _write_file(self, path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.text.get("1.0", tk.END))
        self.text.edit_modified(False)

    def _should_save(self):
        if self.text.edit_modified():
            answer = messagebox.askyesnocancel("저장", "변경 내용을 저장하시겠습니까?")
            if answer is None:
                return False
            if answer:
                return self.save_file()
            return True
        return True

    def cut_text(self):
        self.text.event_generate("<<Cut>>")

    def copy_text(self):
        self.text.event_generate("<<Copy>>")

    def paste_text(self):
        self.text.event_generate("<<Paste>>")

    def select_all(self):
        self.text.tag_add("sel", "1.0", "end-1c")
        self.text.mark_set("insert", "1.0")

    def on_close(self):
        if self._should_save():
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()     