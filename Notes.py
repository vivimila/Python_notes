#  Необходимо написать проект, содержащий функционал работы с заметками. 
# Программа должна уметь :
    # создавать заметку, 
    # сохранять её, 
    # читать список заметок, 
    # редактировать заметку, 
    # удалять заметку.

from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

def new_file():
    global file_name
    file_name = "Нет названия"
    text.delete ('1.0', END)

def save_file():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)

def open_file():
    global file_name
    int = askopenfile(mode='r')

def delete_note(self): 
        #self.last = None
        if len(self.notesList.selectedItems()) != 0:
            note_name = self.notesList.selectedItems()[0].text(0)
            if note_name.strip() == "":
                note_name = "untitled"
            self.notesList.takeTopLevelItem(
                self.notesList.indexOfTopLevelItem(
                    self.notesList.selectedItems()[0]
                    )
                )
            self.notes_dict.pop(note_name)

root = Tk()
root.title("Заметки")
root.geometry("500x400")

text = Text(root)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
file_menu.add_command(label="Создать", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_command(label="Удалить", command=delete_note)
menu_bar.add_cascade(label="Файл", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()