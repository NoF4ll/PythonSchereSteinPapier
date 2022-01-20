from tkinter import *

player_symbol = 0


def chose_rock(window):
    global player_symbol
    player_symbol = "stein"


def chose_paper(window):
    global player_symbol
    player_symbol = "papier"


def chose_scissors(window):
    global player_symbol
    player_symbol = "schere"


def chose_lizard(window):
    global player_symbol
    player_symbol = "echse"


def chose_spock(window):
    global player_symbol
    player_symbol = "spock"


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    bar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + bar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def choosing_window():
    window = Tk()

    frame = LabelFrame(
        window,
        text='Choose your Symbol',
        bg='#f0f0f0',
        font=20
    )
    frame.pack(expand=True, fill=BOTH)

    window.geometry("853x200")

    rock = PhotoImage(file=r"C:\Users\Maximilian Neuner\Documents\Schule\5te Klasse\SWP\Python\rock.png")
    paper = PhotoImage(file=r"C:\Users\Maximilian Neuner\Documents\Schule\5te Klasse\SWP\Python\paper.png")
    scissors = PhotoImage(file=r"C:\Users\Maximilian Neuner\Documents\Schule\5te Klasse\SWP\Python\scissors.png")
    lizard = PhotoImage(file=r"C:\Users\Maximilian Neuner\Documents\Schule\5te Klasse\SWP\Python\lizard.png")
    spock = PhotoImage(file=r"C:\Users\Maximilian Neuner\Documents\Schule\5te Klasse\SWP\Python\spock.png")



    rockImage = rock.subsample(5, 5)
    paperImage = paper.subsample(3, 3)
    scissorsImage = scissors.subsample(3, 3)
    lizardImage = lizard.subsample(3, 3)
    spockImage = spock.subsample(5, 5)


    window.title("Rock, Paper, Scissors, Lizard, Spock")

    bRock = Button(window, text="Rock", command=lambda: [chose_rock(window), window.destroy()],
                   activeforeground="red", activebackground="gray", image=rockImage, height=200, width=200)
    bPaper = Button(window, text="Paper", command=lambda: [chose_paper(window), window.destroy()],
                    activeforeground="blue", activebackground="white", image=paperImage, height=200, width=200)
    bScissor = Button(window, text="Scissor", command=lambda: [chose_scissors(window), window.destroy()],
                      activeforeground="green", activebackground="gray", image=scissorsImage, height=200, width=200)
    bLizard = Button(window, text="Lizard", command=lambda: [chose_lizard(window), window.destroy()],
                     activeforeground="yellow", activebackground="green", image=lizardImage, height=200, width=200)
    bSpock = Button(window, text="Spock", command=lambda: [chose_spock(window), window.destroy()],
                    activeforeground="yellow", activebackground="blue", image=spockImage, height=200, width=200)

    bRock.pack(side=LEFT)
    bPaper.pack(side=LEFT)
    bScissor.pack(side=LEFT)
    bLizard.pack(side=LEFT)
    bSpock.pack(side=LEFT)

    center(window)
    window.mainloop()

    return player_symbol
