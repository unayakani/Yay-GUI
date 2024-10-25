from tkinter import *
import os

# =======================================
window = Tk() # Initiate window
# ---------------------------------------
window.geometry("1920x1080")
window.title("YayGUI")

icon = PhotoImage(file='./Icons/package.png')
window.iconphoto(True, icon)

window.config(background='#1a1a1a')
# ---------------------------------------
# FUNCTIONS
def instPackage():
    package = text.get('1.0', END)
    os.system(f'yay -S {package}')

def uninstPackage():
    package = text.get('1.0', END)
    os.system(f'yay -R {package}')
# ---------------------------------------
# BUTTONS
installPackagePng = PhotoImage(file='./Icons/installPackage.png')
installPackage = Button(
        window,
        text='Install package',
        command = instPackage,
        width='367',
        height='96'
        )
installPackage.config(image=installPackagePng)
installPackage.pack(side = LEFT, padx = 20, pady = 10)

uninstallPackagePng = PhotoImage(file='./Icons/uninstallPackage.png')
uninstallPackage = Button(
        window,
        text = 'Uninstall package',
        command = uninstPackage,
        width = '367',
        height = '96',
        )
uninstallPackage.config(image=uninstallPackagePng)
uninstallPackage.pack(side = RIGHT, padx = 20, pady = 10)
# ---------------------------------------
# TEXT
text = Text(window)
text.config()
text.pack(side = TOP, anchor = CENTER, pady = 100, expand = TRUE)
# ---------------------------------------
window.mainloop() # Display window
# =======================================
