import tkinter as tk

root = tk.Tk()
root.title("Рух кульки")

canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

x, y = 300, 200
r = 5
ball = canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")

def move(dx, dy):
    global x, y
    old_x, old_y = x, y
    x += dx
    y += dy
    canvas.move(ball, dx, dy)
    canvas.create_line(old_x, old_y, x, y)

root.bind("<Up>", lambda e: move(0, -10))
root.bind("<Down>", lambda e: move(0, 10))
root.bind("<Left>", lambda e: move(-10, 0))
root.bind("<Right>", lambda e: move(10, 0))

root.mainloop()
