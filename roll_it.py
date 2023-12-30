from tkinter import *
import random

# GLOBAL
# ---------------
L1_BG = "black"  # label_1 background
L1_FG = "white"  # label_1 foreground
L2_BG = "white"  # label_2 background
L2_FG = "black"  # label_2 foreground
B_BG = "pink"  # button background


# END GLOBAL
# ---------------

# METHODS
# ----------------------------------------------
def roll_dice():
    """
    choose a random number between 1 and 6.
    change the text in labels
    :return: None
    """
    # numbers look deformed,
    # (I intentionally did it to make changes UI)
    dice_drawing = {
        1: """
  ֍  
֍ ֍     
  ֍  
     ֍     
֍ ֍ ֍
""",
        2: """
֍ ֍ ֍
         ֍
֍ ֍ ֍
֍         
֍ ֍ ֍
""",
        3: """
֍ ֍ ֍
             ֍    
֍ ֍ ֍
         ֍
֍ ֍ ֍
""",
        4: """
֍         
֍ ֍     
֍ ֍ ֍
     ֍     
  ֍  
""",
        5: """
֍ ֍ ֍
֍         
֍ ֍ ֍
         ֍
֍ ֍ ֍
""",
        6: """
֍ ֍ ֍
֍         
֍ ֍ ֍
֍      ֍
֍ ֍ ֍
""",
    }

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    label_1.config(text=dice_drawing[dice1])
    label_2.config(text=dice_drawing[dice2])

    # print("Dice Rolled : {} and {}".format(dice1, dice2))
    # print("\n".join(dice_drawing[dice1]) + "\n======")
    # print("\n".join(dice_drawing[dice2]))
    # roll = input("again?(y/n) : ").lower()
    # if roll != "y":
    #     quit()


# END METHODS
# ----------------------------------------------

# MAIN WINDOW
# =========================================================
window = Tk()
window.title("Roll it!")
window.resizable(False, False)

frame_1 = Frame(window)
frame_1.pack()

frame_2 = Frame(window)
frame_2.pack()

label_1 = Label(frame_1, font=("Arial", 18, "bold"), relief=RAISED,
                bd=5, foreground=L1_FG, width=15, height=10,
                background=L1_BG, text="Click the button")
label_1.grid(row=0, column=0)

label_2 = Label(frame_1, font=("Arial", 18, "bold"), relief=RAISED,
                bd=5, foreground=L2_FG, width=15, height=10,
                background=L2_BG, text="below to start.")
label_2.grid(row=0, column=1)

Button(frame_2, width=37, text="ROLL DICE !", font=("Arial", 15, "bold italic"), command=roll_dice, relief=RAISED,
       bd=5, padx=10, background=B_BG).pack(side=BOTTOM)

window.mainloop()

# END MAIN WINDOW
# =========================================================
