import ctypes
import random
import time
import tkinter
from PIL import Image, ImageTk


# ГОЛОВНЕ МЕНЮ І ЙОГО КНОПКИ
def MainMenu():
    game_label.pack()
    start_button.pack()
    space1.pack()
    continue_button.pack()
    space2.pack()
    quit_button.pack()

def startGameButtonFunc():
    leaveMainMenu()
    enterName_label.pack()
    space3.pack()
    enterName_entry.pack()
    space4.pack()
    enterName_button.pack()
    space5.pack()
    returnMenu_button.pack()

def continueButtonFunc():
    clibrary.loadChar.argtypes = [GameHandle]
    clibrary.loadChar(game)
    leaveMainMenu()
    enterGame()

def leaveMainMenu():
    game_label.forget()
    start_button.forget()
    space1.forget()
    continue_button.forget()
    space2.forget()
    quit_button.forget()



# НОВА ГРА
def getName():
    if enterName_entry.get() != "" and " " not in enterName_entry.get():
        clibrary.initializeGame.argtypes = [GameHandle, ctypes.c_char_p]
        name = ctypes.create_string_buffer(enterName_entry.get().encode('utf-8'))
        clibrary.initializeGame(game, name)
        clibrary.saveChar(game)
        enterName_label.forget()
        space3.forget()
        enterName_entry.forget()
        space4.forget()
        enterName_button.forget()
        space5.forget()
        returnMenu_button.forget()
        enterGame()

def returnMenu():
    leaveMainMenu()
    enterName_label.forget()
    space3.forget()
    enterName_entry.forget()
    space4.forget()
    enterName_button.forget()
    returnMenu_button.forget()
    space5.forget()
    MainMenu()



# ГРА
def enterGame():
    space6.grid(row=0, column=0)
    curgame_text.grid(row=1, column=0, rowspan=3)
    curgame_entry.grid(row=5, column=0)

    character_button.grid(row=1, column=1)
    action_button.grid(row=2, column=1)
    snl_button.grid(row=3, column=1)

def characterButtonFunc():
    character_button.forget()
    action_button.forget()
    snl_button.forget()

    curgame_text.grid(row=1, column=0, rowspan=4)
    curgame_entry.grid(row=6, column=0)
    charsheet_button.grid(row=1, column=1)
    levelup_button.grid(row=2, column=1)
    usestatpoint_button.grid(row=3, column=1)
    returnCharacter_button.grid(row=4, column=1)

def actionButtonFunc():
    character_button.forget()
    action_button.forget()
    snl_button.forget()

    travel_button.grid(row=1, column=1)
    goToVillage_button.grid(row=2, column=1)
    returnAction_button.grid(row=3, column=1)

def snlButtonFunc():
    clibrary.saveChar(game)
    window.quit()



# КНОПКА "ПЕРСОНАЖ"
def charsheetButtonFunc():
    curgame_text.config(state="normal")
    curgame_text.delete("1.0", "end")

    clibrary.printCharSheet.argtypes = [GameHandle, ctypes.c_char_p, ctypes.c_size_t]
    clibrary.printCharSheet.restypes = ctypes.c_char_p

    result = ctypes.create_string_buffer(500)
    clibrary.printCharSheet(game, result, ctypes.sizeof(result))
    curgame_text.insert("1.0", result.value.decode('utf-8'))
    curgame_text.config(state="disabled")

def levelupButtonFunc():
    curgame_text.config(state="normal")
    curgame_text.delete("1.0", "end")

    clibrary.levelUp.argtypes = [GameHandle]
    clibrary.levelUp.restypes = ctypes.c_int

    level = clibrary.levelUp(game)
    if level != 0:
        curgame_text.insert("1.0", "Ви підняли рівень до " + str(level) + "!")

    else:
        curgame_text.insert("1.0", "Недостатньо досвіду для підняття рівня!")
    curgame_text.config(state="disabled")

def inputStatPoint():
    clibrary.getStatPoints.argtypes = [GameHandle]
    clibrary.getStatPoints.restypes = ctypes.c_int
    statpoints = clibrary.getStatPoints(game)

    curgame_text.config(state="normal")
    if statpoints > 0:
        curgame_text.insert("end", "\n\nВи покращили атрибут: ")
        clibrary.getStatPoints.argtypes = [GameHandle, ctypes.c_int]
        if curgame_entry.get() == "Сила":
            clibrary.useStatPoints(game, 1)
            curgame_text.insert("end", "Сила")
        elif curgame_entry.get() == "Спритність":
            clibrary.useStatPoints(game, 2)
            curgame_text.insert("end", "Спритність")
        elif curgame_entry.get() == "Інтелект":
            clibrary.useStatPoints(game, 3)
            curgame_text.insert("end", "Інтелект")
    else:
        curgame_text.insert("end", "\n\nУ вас немає очків атрибутів!")
    curgame_text.config(state="disabled")

def useStatPointButton():
    curgame_text.config(state="normal")
    curgame_text.delete("1.0", "end")

    clibrary.getStatPoints.argtypes = [GameHandle]
    clibrary.getStatPoints.restypes = ctypes.c_int
    statpoints = clibrary.getStatPoints(game)

    if statpoints <= 0:
        curgame_text.insert("end", "У вас немає очків атрибутів!")
    else:
        curgame_text.insert("end", "У вас є " + str(statpoints) +" невикористаних очків атрибутів!")
        curgame_text.insert("end", "\n\nВикористати очко атрибутів на:" +
                            "\nСила" + "\nСпритність" + "\nІнтелект");

    curgame_text.config(state="disabled")

def returnCharacter():
    charsheet_button.grid_forget()
    levelup_button.grid_forget()
    returnCharacter_button.grid_forget()
    usestatpoint_button.grid_forget()
    enterGame()



# КНОПКА "ДІЯ"
def travelButtonFunc():
    curgame_text.config(state="normal")
    clibrary.getStamina.argtypes = [GameHandle]
    clibrary.getStamina.restypes = ctypes.c_int
    stamina = clibrary.getStamina(game)
    if stamina > 0:
        curgame_text.delete("1.0", "end")
        result = ctypes.create_string_buffer(500)
        clibrary.Travel(game, result, ctypes.sizeof(result))
        curgame_text.insert("1.0", result.value.decode('utf-8'))
    else:
        curgame_text.delete("1.0", "end")
        curgame_text.insert("1.0", "Ви надто змучилися для того щоб подорожувати\n"+
                            "Вам необхідно поспати(у Таверні) для того щоб відпочити...")
    curgame_text.config(state="disabled")

def goToVillageButtonFunc():
    travel_button.grid_forget()
    goToVillage_button.grid_forget()
    returnAction_button.grid_forget()
    character_button.grid_forget()
    action_button.grid_forget()
    snl_button.grid_forget()

    curgame_text.grid(row=1, column=0, rowspan=4)
    curgame_entry.grid(row=6, column=0)
    goToWitch_button.grid(row=1, column=1)
    goToStreetFight_button.grid(row=2, column=1)
    restInTavern_button.grid(row=3, column=1)
    returnToAction_button.grid(row=4, column=1)

def returnAction():
    travel_button.grid_forget()
    goToVillage_button.grid_forget()
    returnAction_button.grid_forget()
    enterGame()



# КНОПКА "ПОДОРОЖ"
def inputPressEnter(event):
    if curgame_entry.get() == "1" or curgame_entry.get() == "2" or curgame_entry.get() == "3":
        puzzleInput()
    elif curgame_entry.get() == "Сила" or curgame_entry.get() == "Спритність" or curgame_entry.get() == "Інтелект":
        inputStatPoint()
    elif curgame_entry.get() == "Атакувати":
        fight()

def puzzleInput():
    curgame_text.config(state="normal")
    clibrary.inputPuzzleAnswer.argtypes = [GameHandle, ctypes.c_int]
    check = clibrary.inputPuzzleAnswer(game, int(curgame_entry.get()))
    if check == 1:
        curgame_text.insert("end", "\n\n*** Правильна відповідь! ***")

        clibrary.gainExp.argtypes = [GameHandle]
        clibrary.gainExp.restype = ctypes.c_int
        curgame_text.insert("end", "\n\nВи получили " + str(clibrary.gainExp(game)) +" досвіду.")

        clibrary.gainGold.argtypes = [GameHandle, ctypes.c_int]
        clibrary.gainGold.restype = ctypes.c_int
        curgame_text.insert("end", "\nВи получили " + str(clibrary.gainGold(game, -1)) +" золота.")
    elif check == 2:
        curgame_text.insert("end", "\n\n*** Неправильна відповідь! ***")
    curgame_text.config(state="disabled")

def fight():
    switch = 1
    quantity = 0

    curgame_text.config(state="normal")

    clibrary.getCharHP.argtypes = [GameHandle]
    clibrary.getCharHP.restypes = ctypes.c_int
    char_hp = clibrary.getCharHP(game)

    clibrary.getEnemyHP.argtypes = [GameHandle]
    clibrary.getEnemyHP.restypes = ctypes.c_int
    enemy_hp = clibrary.getEnemyHP(game)

    clibrary.Attack.argtypes = [GameHandle]
    clibrary.Attack.restypes = ctypes.c_int
    clibrary.Defend.argtypes = [GameHandle]
    clibrary.Defend.restypes = ctypes.c_int
    while char_hp > 0 and enemy_hp > 0:
        if quantity > 10:
            curgame_text.delete("1.0", "end")
            quantity = 0

        if switch == 1:
            damage = clibrary.Attack(game)
            if damage == 0:
                curgame_text.insert("end", "\n\nВи промахнулися!")
            else:
                curgame_text.insert("end", "\n\nВи завдали " + str(damage) + " шкоди!")

            switch = 2
            quantity += 1
        else:
            damage = clibrary.Defend(game)
            if damage == 0:
                curgame_text.insert("end", "\n\nВи заблокували удар противника!")
            else:
                curgame_text.insert("end", "\n\nПротивник завдав вам " + str(damage) + " шкоди!")

            switch = 1
            quantity += 1

        char_hp = clibrary.getCharHP(game)
        enemy_hp = clibrary.getEnemyHP(game)
        if char_hp <= 0:
            curgame_text.insert("end", "\n\n *** Ви загинули... ***")
            window.after(3000, death)
            break
        elif enemy_hp <= 0:
            curgame_text.insert("end", "\n\nВи перемогли!")

            clibrary.gainExp.argtypes = [GameHandle]
            clibrary.gainExp.restype = ctypes.c_int
            curgame_text.insert("end", "\n\nВи получили " + str(clibrary.gainExp(game)) +" досвіду.")

            clibrary.gainGold.argtypes = [GameHandle, ctypes.c_int]
            clibrary.gainGold.restype = ctypes.c_int
            curgame_text.insert("end", "\nВи получили " + str(clibrary.gainGold(game, -1)) +" золота.")
            break
    curgame_text.config(state="disabled")



# КНОПКА "ПІТИ ДО НАЙБЛИЖЧОГО СЕЛА"
def goToWitchButtonFunc():
    curgame_text.config(state="normal")
    clibrary.getGold.argtypes =[GameHandle]
    clibrary.getGold.restypes = ctypes.c_int
    gold = clibrary.getGold(game)
    if gold >= 50:
        clibrary.heal.argtypes = [GameHandle]
        clibrary.heal(game)
        curgame_text.delete("1.0", "end")
        curgame_text.insert("end", "Ви прийшли до знахарки.\n\n" +
                            "За 50 золота вона дала вам дивне червоне зілля\n\n" +
                            "Випивши його, ваші рани швидко загоїлися і ви стали почуватися краще!\n" +
                            "(Ви втратили 50 золота і відновили своє здоров'я до максимуму)")
    else:
        curgame_text.delete("1.0", "end")
        curgame_text.insert("end", "Ви прийшли до знахарки.\n\n" +
                            "Побачивши, що у вас немає 50 золота, вона вас прогнала...")
    curgame_text.config(state="disabled")

def goToStreetFightFunc():
    curgame_text.config(state="normal")
    clibrary.getGold.argtypes = [GameHandle]
    clibrary.getGold.restypes = ctypes.c_int
    gold = clibrary.getGold(game)
    if gold >= 100:
        clibrary.upgrade.argtypes = [GameHandle]
        clibrary.upgrade(game)
        curgame_text.delete("1.0", "end")
        curgame_text.insert("end", "Ви вирішили взяти участь у вуличних боях.\n\n"+
                            "Ви заплатили 100 золота за участь і почали битися з місцевим чемпіоном")

        cointoss = random.randint(1, 3)
        if cointoss == 1:
            clibrary.gainGold.argtypes = [GameHandle, ctypes.c_int]
            clibrary.gainGold(game, 150)
            curgame_text.insert("end", "\n\nВи перемогли!!!\n" +
                                "За це вам дали 150 золота, а також ви вивчили декілька нових прийомів!\n" +
                                "(Ви отримали 150 золота і 1 очко атрибутів)")
        else:
            curgame_text.insert("end", "\n\nВи програли...\n" +
                                "Але ви не засмутилися, бо вивчили декілька нових прийомів!\n" +
                                "(Ви отримали 1 очко атрибутів)")
    else:
        curgame_text.delete("1.0", "end")
        curgame_text.insert("end", "Ви вирішили взяти участь у вуличних боях.\n\n"+
                            "Ви побачили, що у вас немає 100 золота щоб взяти участь, тому ви подивилися бої інших і пішли.")
    curgame_text.config(state="disabled")

def restInTavernButtonFunc():
    curgame_text.config(state="normal")
    clibrary.getGold.argtypes =[GameHandle]
    clibrary.getGold.restypes = ctypes.c_int
    gold = clibrary.getGold(game)
    if gold >= 20:
        clibrary.rest.argtypes = [GameHandle]
        clibrary.rest(game)
        curgame_text.delete("1.0", "end")
        curgame_text.insert("end", "Ви прийшли у таверну і орендували кімнату за 20 золота.\n\n"
                            "Ви зайшли у свою кімнату і добряче виспалися!\n" +
                            "(Ви відновили свою витривалість до максимуму)")
    else:
        curgame_text.delete("1.0", "end")
        curgame_text.insert("end", "Ви прийшли у таверну.\n\n"
                                   "Коли власник таверни побачив, що у вас ні гроша за душею, він прогнав вас з таверни...")
    curgame_text.config(state="disabled")

def returnToCharacterButtonFunc():
    goToWitch_button.grid_forget()
    goToStreetFight_button.grid_forget()
    restInTavern_button.grid_forget()
    returnToAction_button.grid_forget()
    curgame_text.grid(row=1, column=0, rowspan=3)
    curgame_entry.grid(row=5, column=0)
    actionButtonFunc()



# МЕНЮ СМЕРТІ
def death():
    returnAction()
    space6.grid_forget()
    curgame_text.grid_forget()
    curgame_entry.grid_forget()
    character_button.grid_forget()
    action_button.grid_forget()
    snl_button.grid_forget()

    space7.pack()
    death_label.pack()
    space8.pack()
    returnDeath_button.pack()

def returnFromDeath():
    space7.forget()
    death_label.forget()
    space8.forget()
    returnDeath_button.forget()
    MainMenu()





if __name__ == "__main__":
    # ПРИЄДНАННЯ С++ ДО ПАЙТОНА
    clibrary = ctypes.WinDLL("cmake-build-debug/libcoursework.dll")
    GameHandle = ctypes.POINTER(ctypes.c_char)
    clibrary.createGame.restype = GameHandle
    game = clibrary.createGame()


    # СТВОРЕННЯ ВІКНА ГРИ
    window = tkinter.Tk()
    image = Image.open("gamefiles/images/gamename.png")
    game_image = ImageTk.PhotoImage(image)

    icon = tkinter.PhotoImage(file="gamefiles/images/gameicon.png")
    window.iconphoto(False, icon)
    window.title("Lordaeron")

    window.geometry("1920x1080")
    window.config(bg="black")
    window.resizable(False, False)
    window.attributes('-fullscreen', True)


    # ГОЛОВНЕ МЕНЮ
    game_label = tkinter.Label(window,
                               image=game_image,
                               bg="black",
                               fg="white",
                               width=500,
                               height=400)

    start_button = tkinter.Button(window,
                                  text="Почати нову гру",
                                  command=startGameButtonFunc,
                                  bg="#303030",
                                  fg="white",
                                  width=40,
                                  height=5,
                                  activebackground="grey",
                                  font=("Comic Sans MS", 12, "normal"))

    space1 = tkinter.Label(window, height=3, bg="black")

    continue_button = tkinter.Button(window,
                                     text="Продовжити гру",
                                     command=continueButtonFunc,
                                     bg="#303030",
                                     fg="white",
                                     width=40,
                                     height=5,
                                     activebackground="grey",
                                     font=("Comic Sans MS", 12, "normal"))

    space2 = tkinter.Label(window, height=3, bg="black")

    quit_button = tkinter.Button(window,
                                 text="Вийти з гри",
                                 command=window.quit,
                                 bg="#303030",
                                 fg="white",
                                 width=40,
                                 height=5,
                                 activebackground="grey",
                                 font=("Comic Sans MS", 12, "normal"))

    returnMenu_button = tkinter.Button(window,
                                       text="Назад",
                                       command=returnMenu,
                                       width=15,
                                       height=2,
                                       bg="#303030",
                                       fg="white")


    # ВВІД ІМЕНІ
    space3 = tkinter.Label(window, height=3, bg="black")

    enterName_label = tkinter.Label(window,
                                    text="Введіть ім\'я персонажа:\n(без пробілів)",
                                    bg="black",
                                    fg="green",
                                    width=20,
                                    height=15,
                                    anchor="s",
                                    font=("Comic Sans MS", 16, "bold"))

    space4 = tkinter.Label(window, height=1, bg="black")

    enterName_entry = tkinter.Entry(window,
                                    bg="#D8D8D8",
                                    width=20,
                                    font=("Comic Sans MS", 15))

    space5 = tkinter.Label(window, height=1, bg="black")

    enterName_button = tkinter.Button(window,
                                      text="Підтвердити",
                                      command=getName,
                                      width=15,
                                      height=2,
                                      bg="#303030",
                                      fg="white")


    # ГРА
    space6 = tkinter.Label(window, height=5, bg="black")

    curgame_text = tkinter.Text(window,
                                width=140,
                                height=30,
                                bg="black",
                                fg = "green",
                                font=("Comic Sans MS", 15))
    curgame_text.insert("1.0", "Нажміть на \"Дія\" -> \"Подорожувати\" щоб почати подорож...")
    curgame_text.config(state= "disabled")


    curgame_entry = tkinter.Entry(window,
                                  bg="black",
                                  fg="green",
                                  width=140,
                                  font=("Comic Sans MS", 15))
    curgame_entry.insert(0, "Ввід...")
    curgame_entry.bind("<FocusIn>", lambda event: curgame_entry.delete(0, "end") if curgame_entry.get() == "Ввід..." else None)
    curgame_entry.bind("<FocusOut>", lambda event: curgame_entry.insert(0, "Ввід...") if curgame_entry.get() == "" else None)
    curgame_entry.bind("<Button-1>", lambda event: curgame_entry.delete(0, "end"))
    window.bind('<Return>', inputPressEnter)
    input = None


    character_button = tkinter.Button(window,
                                      text="Персонаж",
                                      command=characterButtonFunc,
                                      width=30,
                                      height=5,
                                      bg="#303030",
                                      fg="white")

    action_button = tkinter.Button(window,
                                   text="Дія",
                                   command=actionButtonFunc,
                                   width=30,
                                   height=5,
                                   bg="#303030",
                                   fg="white")

    snl_button = tkinter.Button(window,
                                text="Зберегти гру і вийти",
                                command = snlButtonFunc,
                                width=30,
                                height=5,
                                bg="#303030",
                                fg="white")




    # КНОПКА "ПЕРСОНАЖ"
    charsheet_button = tkinter.Button(window,
                                      text="Характеристика",
                                      command= charsheetButtonFunc,
                                      width=30,
                                      height=5,
                                      bg="#303030",
                                      fg="white")


    levelup_button = tkinter.Button(window,
                                    text="Підняти рівень",
                                    command=levelupButtonFunc,
                                    width=30,
                                    height=5,
                                    bg="#303030",
                                    fg="white")

    usestatpoint_button = tkinter.Button(window,
                                    text="Використати очки атрибутів",
                                    command=useStatPointButton,
                                    width=30,
                                    height=5,
                                    bg="#303030",
                                    fg="white")

    returnCharacter_button = tkinter.Button(window,
                                       text="Назад",
                                       command = returnCharacter,
                                       width=30,
                                       height=5,
                                       bg="#303030",
                                       fg="white")


    # КНОПКА "ДІЯ"
    travel_button = tkinter.Button(window,
                                   text="Подорожувати",
                                   command=travelButtonFunc,
                                   width=30,
                                   height=5,
                                   bg="#303030",
                                   fg="white")

    goToVillage_button = tkinter.Button(window,
                                        text="Піти до найближчого села",
                                        command=goToVillageButtonFunc,
                                        width=30,
                                        height=5,
                                        bg="#303030",
                                        fg="white")

    returnAction_button = tkinter.Button(window,
                                            text="Назад",
                                            command = returnAction,
                                            width=30,
                                            height=5,
                                            bg="#303030",
                                            fg="white")

    # КНОПКА "ПІТИ У СЕЛО"
    goToWitch_button = tkinter.Button(window,
                                         text="Піти до знахарки",
                                         command = goToWitchButtonFunc,
                                         width=30,
                                         height=5,
                                         bg="#303030",
                                         fg="white")

    goToStreetFight_button = tkinter.Button(window,
                                      text="Прийняти участь у вуличних битвах",
                                      command = goToStreetFightFunc,
                                      width=30,
                                      height=5,
                                      bg="#303030",
                                      fg="white")

    restInTavern_button = tkinter.Button(window,
                                      text="Переночувати у таверні",
                                      command = restInTavernButtonFunc,
                                      width=30,
                                      height=5,
                                      bg="#303030",
                                      fg="white")

    returnToAction_button = tkinter.Button(window,
                                           text="Назад",
                                           command = returnToCharacterButtonFunc,
                                           width=30,
                                           height=5,
                                           bg="#303030",
                                           fg="white")

    # МЕНЮ СМЕРТІ
    space7 = tkinter.Label(window, height=3, bg="black")

    death_label = tkinter.Label(window,
                                    text="Ви загинули",
                                    bg="black",
                                    fg="green",
                                    width=15,
                                    height=7,
                                    anchor="s",
                                    font=("Comic Sans MS", 35, "bold"))

    space8= tkinter.Label(window, height=1, bg="black")

    returnDeath_button = tkinter.Button(window,
                                      text="Повернутися до головного меню",
                                      command=returnFromDeath,
                                      width=30,
                                      height=4,
                                      bg="#303030",
                                      fg="white")



    MainMenu()

    window.mainloop()

    clibrary.deleteGame(game)
