import tkinter, tkinter.messagebox, tkinter.simpledialog, tkinter.scrolledtext, Crypto.Random, Crypto.Protocol.KDF, Crypto.Cipher.AES
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))

def crypto(pwd, iv):
    return Crypto.Cipher.AES.new(Crypto.Protocol.KDF.PBKDF2(pwd, iv, count=100000), Crypto.Cipher.AES.MODE_CFB, iv)

def save(e):
    global pwd
    if 'pwd' not in globals(): 
        pwd = tkinter.simpledialog.askstring('sdfgh', 'Password:', show="*").encode()
    iv = Crypto.Random.new().read(Crypto.Cipher.AES.block_size)
    cipher = crypto(pwd, iv).encrypt(b'sdfgh' + text.get("1.0", 'end-1c').encode())  # add a header 'sdfgh' to be able to test if password ok when decrypting
    with open('sdfgh.dat', 'wb') as f:
        f.write(iv + cipher)
    text.edit_modified(False)

def load():
    global pwd    
    try:
        with open('sdfgh.dat', 'rb') as f:
            s = f.read()
        iv, cipher = s[:Crypto.Cipher.AES.block_size], s[Crypto.Cipher.AES.block_size:]
        try:
            root.update_idletasks()
            pwd = tkinter.simpledialog.askstring('sdfgh', 'Password:', show="*").encode()
        except AttributeError:
            exit()
        while True:
            s = crypto(pwd, iv).decrypt(cipher)
            if s[:5] == b'sdfgh':  # is the header well decrypted? if not, wrong password!
                break
            try:
                root.update_idletasks()
                pwd = tkinter.simpledialog.askstring('sdfgh', 'Wrong password, try again:', show="*").encode()
            except AttributeError:
                exit()
        s = s[5:].decode()
    except FileNotFoundError:  # new file
        s = "Welcome! This is a new file. Basic documentation:\n* Save with CTRL+S\n* Quit with CTRL+W or ALT+F4\n* Find a pattern with CTRL+F or F3"
    text.insert(tkinter.END, s)
    text.mark_set("insert", "1.0")  # cursor position at the start
    text.edit_modified(False)
    text.focus()

def close(e=None):
    if not text.edit_modified() or tkinter.messagebox.askokcancel('sdfgh', "Some modifications have not been saved, do you really want to quit?", default=tkinter.messagebox.CANCEL):
        root.destroy()

def find(e, findnext=False):
    global query
    if not findnext or 'query' not in globals():
        query = tkinter.simpledialog.askstring('sdfgh', 'Query:')
        start = "1.0"
    else:
        start = text.index(tkinter.INSERT) + "+1c"
    pos = text.search(query, start, stopindex="end")
    if pos != '':
        text.mark_set("insert", pos)
    text.focus()

root = tkinter.Tk('sdfgh')  # root.withdraw()
root.title('sdfgh')
root.state('zoomed')
text = tkinter.scrolledtext.ScrolledText(master=root, wrap='word', bg='#272822', fg="#f8f8f2", insertbackground='#f8f8f2', font=("Consolas", 10))
text.pack(side="top", fill="both", expand=True, padx=0, pady=0)
root.bind('<Control-s>', save)  # CTRL+S too?
root.bind('<Control-w>', close)
root.bind('<Control-f>', find)
root.bind('<F3>', lambda e: find(e, True))
root.protocol("WM_DELETE_WINDOW", close)
load()
root.mainloop()
