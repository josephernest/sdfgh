import tkinter, tkinter.messagebox, tkinter.simpledialog, tkinter.scrolledtext, Crypto.Random, Crypto.Protocol.KDF, Crypto.Cipher.AES, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def cipherAES_GCM(pwd, nonce):
    key = Crypto.Protocol.KDF.PBKDF2(pwd, nonce, count=100000)
    return Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_GCM, nonce=nonce, mac_len=16)
def save(e):
    global pwd
    if 'pwd' not in globals(): 
        pwd = tkinter.simpledialog.askstring('sdfgh', 'Password:', show="*").encode()
    nonce = Crypto.Random.new().read(16)
    ciphertext = nonce + b''.join(cipherAES_GCM(pwd, nonce).encrypt_and_digest(text.get("1.0", 'end-1c').encode()))
    with open('sdfgh.dat', 'wb') as f:
        f.write(ciphertext)
    text.edit_modified(False)
def load(root):
    global pwd    
    try:
        with open('sdfgh.dat', 'rb') as f:
            s = f.read()
        nonce, ciphertext, tag = s[:16], s[16:len(s)-16], s[-16:]
        while True:
            try:
                root.update_idletasks()
                pwd = tkinter.simpledialog.askstring('sdfgh', 'Password:', show="*").encode()
                s = cipherAES_GCM(pwd, nonce).decrypt_and_verify(ciphertext, tag).decode()
                break
            except AttributeError:
                exit()
            except ValueError:  # wrong password, let's try again
                pass
    except FileNotFoundError:  # new file
        s = "Welcome! This is a new file. Basic documentation:\n* Save with CTRL+S\n* Quit with CTRL+W or ALT+F4\n* Find a pattern with CTRL+F or F3"
    return s
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
    pos = text.search(query, start, stopindex="end", nocase=True, regexp=True)
    if pos != '':
        text.mark_set("insert", pos)
        text.see("insert")
    text.focus()
if __name__ == '__main__':
    root = tkinter.Tk('sdfgh')
    root.title('sdfgh')
    root.state('zoomed')
    text = tkinter.scrolledtext.ScrolledText(master=root, wrap='none', bg='#272822', fg="#f8f8f2", insertbackground='#f8f8f2', font=("Consolas", 10))
    text.pack(side="top", fill="both", expand=True, padx=0, pady=0)
    root.bind('<Control-s>', save)  # CTRL+S too?
    root.bind('<Control-w>', close)
    root.bind('<Control-f>', find)
    root.bind('<F3>', lambda e: find(e, True))
    root.protocol("WM_DELETE_WINDOW", close)
    s = load(root)
    text.insert(tkinter.END, s)
    text.mark_set("insert", "1.0")  # cursor position at the start
    text.edit_modified(False)
    text.focus()
    root.mainloop()
