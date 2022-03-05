import random
from tkinter import *
from tkinter import messagebox
 
running = True
            
while running:
    
    gui = Tk()
    gui.title('Wordle')
    gui.geometry('940x630')
    gui.configure(background = "white")
    gui.resizable(False, False)

    index = random.randint(0,5756)
    file = open('words.txt')
    l = file.readlines()
    Word = l[index].strip('\n').upper()
    tries = 0
    

    def color_tiles(r):
        global tries, guess
        guess = 0
        for i in range(r, r+5):
            if WordsEntered[i].get() == Word[i-r]:
                WordsEntered[i].configure({"background": "green", "foreground": "white"})
                guess += 1
            elif WordsEntered[i].get() in Word and WordsEntered[i].get() != '':
                WordsEntered[i].configure({"background": "#FFC900", "foreground": "white"})
                guess = 0
            elif WordsEntered[i].get() not in Word:
                WordsEntered[i].configure({"background": "black", "foreground": "white"})
                guess = 0
            else:
                messagebox.showinfo("ERROR", "Please enter a proper 5-letter word.")
                tries -= 1
                guess = 0
                break
                               
    def character_limit(*args):
        for i in range(tries*5, tries*5+5):
            if len(WordsEntered[i].get()) > 0:
                    Words[i].set(WordsEntered[i].get()[0])
                    if i != tries*5+4: WordsEntered[i+1].focus_set()

    def restartgame():
        running = True
        gui.destroy()

    def clickEnter(e):
        global tries, guess, running
        color_tiles(tries*5)
        winorlose()
        if tries != 5 and guess != 5:
            WordsEntered[tries*5+5].focus_set()


        tries += 1

    
    def winorlose():
        global tries, running
        if guess == 5:
               ask1 = messagebox.askquestion("Congratulations! You've won!", "Do you want to play again?")
               if ask1 == 'yes':
                   restartgame()
               else:
                   running = False
                   gui.destroy()
                        
        if tries == 5 and guess != 5:
            ask2 = messagebox.askquestion("Game Over", "The correct word was {}\nDo you want to play again?".format(Word))
            if ask2 == 'yes':
                restartgame()
            else:
                running = False
                gui.destroy()
                

    def rightclick(k):
            wi = gui.focus_get()
            wi = str(wi)
            wi = wi.lstrip('.!entry')
            if not wi:
                wi = 1
            else:
                wi = int(wi)
            WordsEntered[wi].focus_set()

    def leftclick(k):
            wi = gui.focus_get()
            wi = str(wi)
            wi = wi.lstrip('.!entry')
            if not wi:
                wi = 1
            else:
                wi = int(wi)
            WordsEntered[wi-2].focus_set()

    for i in range(30):
        exec('word{}= StringVar()'.format(i+1)) 
        exec('word{}.trace("w", character_limit)'.format(i+1))
        
    text = Label(gui, text = "Wordle", font = ('Impact 40'), bg = "white")
    text.place(x=400, y=0)

    wordEntered = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word1, justify = "center", bd = 3)

    wordEntered.place(x = 285, y = 100)

    wordEntered2 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word2, justify = "center", bd = 3)

    wordEntered2.place(x = 365, y = 100)

    wordEntered3 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word3, justify = "center", bd = 3)

    wordEntered3.place(x = 445, y = 100)

    wordEntered4 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word4, justify = "center", bd = 3)

    wordEntered4.place(x = 525, y = 100)

    wordEntered5 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word5, justify = "center", bd = 3)

    wordEntered5.place(x = 605, y = 100)

    wordEntered6 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word6, justify = "center", bd = 3)

    wordEntered6.place(x = 285, y = 180)

    wordEntered7 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word7, justify = "center", bd = 3)

    wordEntered7.place(x = 365, y = 180)

    wordEntered8 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word8, justify = "center", bd = 3)

    wordEntered8.place(x = 445, y = 180)

    wordEntered9 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word9, justify = "center", bd = 3)

    wordEntered9.place(x = 525, y = 180)

    wordEntered10 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word10, justify = "center", bd = 3)

    wordEntered10.place(x = 605, y = 180)

    wordEntered11 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word11, justify = "center", bd = 3)

    wordEntered11.place(x = 285, y = 260)

    wordEntered12 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word12, justify = "center", bd = 3)

    wordEntered12.place(x = 365, y = 260)

    wordEntered13 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word13, justify = "center", bd = 3)

    wordEntered13.place(x = 445, y = 260)

    wordEntered14 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word14, justify = "center", bd = 3)

    wordEntered14.place(x = 525, y = 260)

    wordEntered15 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word15, justify = "center", bd = 3)

    wordEntered15.place(x = 605, y = 260)

    wordEntered16 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word16, justify = "center", bd = 3)

    wordEntered16.place(x = 285, y = 340)

    wordEntered17 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word17, justify = "center", bd = 3)

    wordEntered17.place(x = 365, y = 340)

    wordEntered18 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word18, justify = "center", bd = 3)

    wordEntered18.place(x = 445, y = 340)

    wordEntered19 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word19, justify = "center", bd = 3)

    wordEntered19.place(x = 525, y = 340)

    wordEntered20 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word20, justify = "center", bd = 3)

    wordEntered20.place(x = 605, y = 340)

    wordEntered21 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word21, justify = "center", bd = 3)

    wordEntered21.place(x = 285, y = 420)

    wordEntered22 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word22, justify = "center", bd = 3)

    wordEntered22.place(x = 365, y = 420)

    wordEntered23 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word23, justify = "center", bd = 3)

    wordEntered23.place(x = 445, y = 420)

    wordEntered24 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word24, justify = "center", bd = 3)

    wordEntered24.place(x = 525, y = 420)

    wordEntered25 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word25, justify = "center", bd = 3)

    wordEntered25.place(x = 605, y = 420)

    wordEntered26 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word26, justify = "center", bd = 3)

    wordEntered26.place(x = 285, y = 500)

    wordEntered27 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word27, justify = "center", bd = 3)

    wordEntered27.place(x = 365, y = 500)

    wordEntered28 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word28, justify = "center", bd = 3)

    wordEntered28.place(x = 445, y = 500)

    wordEntered29 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word29, justify = "center", bd = 3)

    wordEntered29.place(x = 525, y = 500)

    wordEntered30 = Entry(gui, width = 2, font = ('Georgia 40'), textvariable = word30, justify = "center", bd = 3)

    wordEntered30.place(x = 605, y = 500)

    WordsEntered = [wordEntered, wordEntered2, wordEntered3, wordEntered4, wordEntered5,
                    wordEntered6, wordEntered7, wordEntered8, wordEntered9, wordEntered10,
                    wordEntered11, wordEntered12, wordEntered13, wordEntered14, wordEntered15,
                    wordEntered16, wordEntered17, wordEntered18, wordEntered19, wordEntered20,
                    wordEntered21, wordEntered22, wordEntered23, wordEntered24, wordEntered25,
                    wordEntered26, wordEntered27, wordEntered28, wordEntered29, wordEntered30]
    
    Words = [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12, word13, word14, word15,
             word16, word17, word18, word19, word20, word21, word22, word23, word24, word25, word26, word27, word28, word29, word30]

    gui.bind('<Right>', rightclick)
    gui.bind('<Left>', leftclick)
    gui.bind('<Return>',clickEnter)
    
    gui.mainloop()
