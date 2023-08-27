from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

def translate_it():

    try:

        for key, value in langauges.items():
            if (value == original_combo.get()):
                from_language_key = key

        for key, value in langauges.items():
            if (value == translated_combo.get()):
                to_language_key = key

        print(from_language_key, to_language_key)
        
        words = textblob.TextBlob(original_text.get(1.0, END))
        words = words.translate(from_lang=from_language_key, to=to_language_key)
        translated_text.delete(1.0, END)
        translated_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)

# text boxes
original_text = Text(root, height = 10, width = 40)
original_text.grid(row = 0, column = 0, pady = 20, padx = 10)

translate_button = Button(root, text = "Translate!", font = ("Helvetica", 24), command = translate_it)
translate_button.grid(row = 0, column = 1, padx = 10)


def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# languege list
langauges = googletrans.LANGUAGES
langauge_list = list(langauges.values())

translated_text = Text(root, height = 10, width = 40)
translated_text.grid(row = 0, column = 2, pady = 20, padx = 10)

original_combo = ttk.Combobox(root, width = 50, value = langauge_list)
original_combo.current(21)
original_combo.grid(row = 1, column = 0)

translated_combo = ttk.Combobox(root, width = 50, value = langauge_list)
translated_combo.current(26)
translated_combo.grid(row = 1, column = 2)

# clear 
clear_button = Button(root, text = "Clear", command = clear)
clear_button.grid(row = 2, column = 1)

root.mainloop()