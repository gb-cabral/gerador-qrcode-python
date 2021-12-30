import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageDraw


def pasta(label):
    caminho = filedialog.askdirectory()
    label['text'] = caminho


def gerarQrcode(entry, entryNome, label):
    img = qrcode.make(entry.get())
    caminho = r'{}\{}.png'.format(label['text'], entryNome.get())
    img.save(caminho)
    tk.messagebox.showinfo(title='Conclusão', message='QR Code gerado com sucesso!')
    

window = tk.Tk()
window.config(bg='black')
window.title('Gerador de QR Code')
window.geometry("300x200")

labelLink = tk.Label(text='Link:', fg='white', bg='black', padx=10, pady=10)
labelLink.grid(column=0, row=0)

labelSalvar = tk.Label(text='Salvar QR Code em:', fg='white', bg='black', padx=10, pady=10)
labelSalvar.grid(column=0, row=1)

labelNome = tk.Label(text='Nome do arquivo:', fg='white', bg='black', padx=10, pady=10)
labelNome.grid(column=0, row=3)

label = tk.Label(text='...', fg='white', bg='black', padx=10, pady=10)
label.grid(column=0, row=2, columnspan=2, sticky='nswe')

entry = tk.Entry()
entry.grid(column=1, row=0, columnspan=2)

entryNome = tk.Entry()
entryNome.grid(column=1, row=3)

botao = tk.Button(text='Salvar em', fg='black', bg='white', command=lambda : pasta(label))
botao.grid(column=1, row=1)

botaoConfirmar = tk.Button(text='Gerar QR Code', fg='white', bg='green', 
                           command=lambda : gerarQrcode(entry, entryNome, label))
botaoConfirmar.grid(column=1, row=4)

window.mainloop()