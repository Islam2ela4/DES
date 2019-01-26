from tkinter import *                                                                                                   #k = 'AABB09182736CCDD'
from tkinter import messagebox
from DES_structure import *                                                                                             #m = '123456ABCD132536'
from DEF import *                                                                                                       #c = 'c0b7a8d05f3a829c'

class GUI:

    Des = DES_structure()
    Def = DEF()

    def __init__(self, window):
        self.window = window
        window.geometry('900x450+200+50')
        window.title('Data Encryption Standard (DES)')
        window.configure(bg='gray')
        window.overrideredirect(1)


        self.main_label = Label(text='Data Encryption Standard (DES)', fg='white', bg='gray', font=("Times New Roman", 30, "bold"))
        self.main_label.pack(pady=30)
        self.plain_label = Label(text='Plain Text : ', fg='white', bg='gray', font=("Times New Roman", 18, "bold"))
        self.plain_label.place(x=50, y=130)
        self.key_label = Label(text='Key : ', fg='white', bg='gray', font=("Times New Roman", 18, "bold"))
        self.key_label.place(x=50, y=200)
        self.cipher_label = Label(text='cipher text : ', fg='white', bg='gray', font=("Times New Roman", 18, "bold"))
        self.cipher_label.place(x=50, y=270)

        self.plain = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.plain.place(x=200, y=130)
        self.key = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.key.place(x=200, y=200)
        self.cipher = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.cipher.place(x=200, y=270)

        self.encryption = Button(text='ENCRYPTION', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='green',
                            fg='white', bd=14, cursor='pirate', activebackground='red', activeforeground='black', command=self.encryption_)
        self.encryption.place(x=300, y=350)

        self.decryption = Button(text='DECRYPTION', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='red',
                            fg='white', bd=14, cursor='heart', activebackground='green', activeforeground='black', command=self.decryprion_)
        self.decryption.place(x=550, y=350)

        self.close = Button(text='X', font=("Times New Roman", 14, "bold"), width=3, height=1, bg='red', fg='white',
                       cursor='pirate', activebackground='green', activeforeground='black', command=self.close_)
        self.close.place(x=860, y=0)


    def set_text(self, var, text):
        var.delete(0, END)
        var.insert(0, text)

    def set(self, var, text):
        var.insert(END, text)

    def encryption_(self):
        k = self.key.get()
        m = self.plain.get()

        if len(m) == 0:
            messagebox.showwarning('Warning Message !!!', 'Plain text is empty !!')
        elif len(k) == 0:
            messagebox.showwarning('Warning Message !!!', 'Key is empty !!')
        elif self.Def.is_hexa(k) is False or self.Def.is_hexa(m) is False:
            messagebox.showwarning('Warning Message !!!', 'Please enter hexadecimal !!')
        else:
            k_ = self.Def.check(k)

            for i in range(0, len(m), 16):
                m_ = m[i:i+16]

                m_ = self.Def.check(m_)

                Key_ = self.Def.hexa2bin(k_)
                Plain_ = self.Def.hexa2bin(m_)

                print('--------------------------------------')
                print('Key = ' + k_)
                print('Plain text = ' + m_)
                print('--------------------------------------')

                Cipher = self.Des.encryption(Plain_, Key_)
                if i == 0:
                    self.set_text(self.cipher, Cipher)
                else:
                    self.set(self.cipher, Cipher)



    def decryprion_(self):
        k = self.key.get()
        c = self.cipher.get()

        if len(c) == 0:
            messagebox.showwarning('Warning Message !!!', 'Cipher text is empty !!')
        elif len(k) == 0:
            messagebox.showwarning('Warning Message !!!', 'Key is empty !!')
        elif self.Def.is_hexa(k) is False or self.Def.is_hexa(c) is False:
            messagebox.showwarning('Warning Message !!!', 'Please enter hexadecimal !!')
        else:
            k_ = self.Def.check(k)

            for i in range(0, len(c), 16):
                c_ = c[i:i+16]

                c_ = self.Def.check(c_)

                Key_ = self.Def.hexa2bin(k_)
                Cipher_ = self.Def.hexa2bin(c_)

                print('--------------------------------------')
                print('Key = ' + k_)
                print('Cipher text = ' + c_)
                print('--------------------------------------')

                Plain = self.Des.decryption(Cipher_, Key_)
                if i == 0:
                    self.set_text(self.plain, Plain)
                else:
                    self.set(self.plain, Plain)



    def close_(self):
        self.window.destroy()


window = Tk()
gui = GUI(window)
window.mainloop()

