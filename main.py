# Başlangıç-Bitiş Tarihi: 10.09.2020
# instagram.com/yazilimfuryasi
# yazilimfuryasi.com


from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import pytesseract
import threading

window = Tk()
window.title("Görselden Yazıya Çevir | 03.11.2020 | V1")

# Program ekranı ortalama
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth()/3 - windowWidth/3)
positionDown = int(window.winfo_screenheight()/3 - windowHeight/1)

# Pencere boyutu
window.geometry(f"420x720+{positionRight}+{positionDown}")
# Yeniden boyutlandırmayı engelle
window.resizable(width=False, height=False)

def mouseClick(event): 
    try:
        global L2
        window.clipboard_clear()
        txt = output.get("1.0", END)
        window.clipboard_append(txt)
        L2 = Label(window)
        L2.place(x=150,y=694)
        L2["text"] = ("Yazı Kopyalandı")
        L2.after(3000, L2.destroy)
    except Exception as e:
        messagebox.showerror("Hata", e)


frame = Frame(window)
frame.place(x=5,y=320)

# Scrollbar
scrol = Scrollbar(frame, orient="vertical")
scrol.pack(side = RIGHT, expand=True, fill="y")
output = Text(frame, width="49", height=23,yscrollcommand=scrol.set)
output.pack(side = LEFT)
scrol.config(command=output.yview)

def resim():
    try:
        resimselect = filedialog.askopenfilename(initialdir ="Desktop", filetypes = [('Image files', '*.jpg'),('Image files', '*.jpeg'),('Image files', '*.png')])
        if not resimselect:
            return
        
        # Resimi yeniden boyutlandırıp labele koyma. Yani önizleme gibi yapmak.
        im = Image.open(resimselect)
        im = im.resize((375,200), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(im)
        lresim = Label(window,image=tkimage,bd=0.5, relief="solid")
        lresim.image = tkimage
        lresim.place(x=20,y=80)
        
        output.delete("1.0", END)
        L1["text"] = ("Dönüştürülüyor...")
        
        pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
        ckt = pytesseract.image_to_string(resimselect, lang="tur").strip().strip("")
        
        if ckt == "":
            L1["text"] = ("Yazı Bulunamadı.")
        else:
            L1["text"] = ("Bir şeyler bulundu.")
            output.insert("1.0",ckt)

            label = Label(window, text="Yazıyı kopyala", font="Vardana 10 bold",cursor="hand2",bd=0.5, relief="solid")
            label.place(x=7,y=694)
            label.bind("<Button>", mouseClick)
    except Exception as e:
        messagebox.showerror("Hata", e)

def thread():
    threading.Thread(target=resim).start()

Button(window, text="Resim Yükle",command=thread).place(x=170,y=20)
L1 = Label(window)
L1.place(x=170, y=290)
window.mainloop()
