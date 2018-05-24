from tkinter import *

tk = Tk()
tk.title("Juego")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=300, bd=0, highlightthickness=0)
canvas.pack()

imagen1 = PhotoImage(file='balon.gif')
imagen2 = PhotoImage(file='cancha.gif')


def movBalon(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
        posicion(0,-3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
        posicion(0,3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
        posicion(-3,0)
    else:
        canvas.move(1, 3, 0)
        posicion(3,0)


canvas.bind_all('<KeyPress-Up>', movBalon)
canvas.bind_all('<KeyPress-Down>', movBalon)
canvas.bind_all('<KeyPress-Left>', movBalon)
canvas.bind_all('<KeyPress-Right>', movBalon)


canvas.create_image(400,50,ancho=NW, image=imagen1)
canvas.create_image(0, 0, ancho=NW, image=imagen2)

def posicion(x,y):

    a = 400 + x
    b = 50 + y

    pos = [a,b]



tk.mainloop()
