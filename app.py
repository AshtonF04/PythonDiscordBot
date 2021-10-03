# Imports
import tkinter as tk

# Start Window
root = tk.Tk()

# Initialize Variables
scoreStr = tk.StringVar()
score = 0
backgroundColor = "#f6b26b"


# Functions
def updateScoreText():
    scoreStr.set("SCORE: " + str(score))
    scoreLabel = tk.Label(root, text=scoreStr.get(), bg=backgroundColor, fg="white")
    scoreLabel.grid(columnspan=1, column=5, row=4)


def increaseScore():
    global score
    global scoreStr
    score += 1
    updateScoreText()


# Canvas
canvas = tk.Canvas(root, width=600, height=300, bg=backgroundColor)
canvas.grid(columnspan=11, rowspan=11)

# Text
updateScoreText()

# Button
scoreButton = tk.Button(root, text="CLICK!", height=2, width=10, bg="#445588", fg="white",
                        command=lambda: increaseScore())
scoreButton.grid(column=5, row=5)

# End Window
root.mainloop()
