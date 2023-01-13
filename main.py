from tkinter import *
import tkinter.messagebox

window = Tk()
window.iconbitmap('nba.ico')
window.title('NBA manager helper 2022/2023 season')
window.geometry('700x520')
window.resizable(width=False, height=False)

def analize():
    if len(t_text.get(1.0, END)) == 1:
        tkinter.messagebox.showinfo(title='Error', message='No text was added')
    else:
        result = t_text.get(1.0, END)
        phil = result.count('76ers')
        bucks = result.count('Bucks')
        bulls = result.count('Bulls')
        cavaliers = result.count('Cavaliers')
        celtics = result.count('Celtics')
        clippers = result.count('Clippers')
        warriors = result.count('Golden State Warriors')
        grizzlies = result.count('Grizzlies')
        hawks = result.count('Hawks')
        heat = result.count('Heat')
        hornets = result.count('Hornets')
        jazz = result.count('Jazz')
        kings = result.count('Kings')
        knicks = result.count('Knicks')
        lakers = result.count('Lakers')
        magic = result.count('Magic')
        mavericks = result.count('Mavericks')
        nets = result.count('Nets')
        nuggets = result.count('Nuggets')
        pacers = result.count('Pacers')
        pelicans = result.count('Pelicans')
        pistons = result.count('Pistons')
        raptors = result.count('Raptors')
        rockets = result.count('Rockets')
        spurs = result.count('Spurs')
        suns = result.count('Suns')
        thunder = result.count('Thunder')
        timberwolves = result.count('Timberwolves')
        blazers = result.count('Trail Blazers')
        wizards = result.count('Wizards')
        l_result.config(text=f'76ers: {phil}\nBucks: {bucks}\nBulls: {bulls}\nCavaliers: {cavaliers}\nCeltics: {celtics}\nClippers: {clippers}\nGolden State Warriors: {warriors}\nGrizzlies: {grizzlies}\nHawks: {hawks}\nHeat: {heat}\nHornets: {hornets}\nJazz: {jazz}\nKings: {kings}\nKnicks: {knicks}\nLakers: {lakers}\nMagic: {magic}\nMavericks: {mavericks}\nNets: {nets}\nNuggets: {nuggets}\nPacers: {pacers}\nPelicans: {pelicans}\nPistons: {pistons}\nRaptors: {raptors}\nRockets: {rockets}\nSpurs: {spurs}\nSuns: {suns}\nThunder: {thunder}\nTimberwolves: {timberwolves}\nTrail Blazers: {blazers}\nWizards: {wizards}')

def clear():
    t_text.delete(1.0, END)
    l_result.config(text='76ers: \nBucks: \nBulls: \nCavaliers: \nCeltics: \nClippers: \nGolden State Warriors: \nGrizzlies: \nHawks: \nHeat: \nHornets: \nJazz: \nKings: \nKnicks: \nLakers: \nMagic: \nMavericks: \nNets: \nNuggets: \nPacers: \nPelicans: \nPistons: \nRaptors: \nRockets: \nSpurs: \nSuns: \nThunder: \nTimberwolves: \nTrail Blazers: \nWizards: ')

def help():
    help_window = Toplevel(window)
    help_window.iconbitmap('nba.ico')
    help_window.title('Help')
    help_window.geometry('290x160')
    help_window.resizable(width=False, height=False)
    l_help = Label(help_window, wraplength='250', justify=LEFT, text='Program is adapted for krepsinis.net NBA manager. It may not work propertly with other NBA managers.\nHow it works? Just add (copy paste text) NBA teams schedule of single tour to analyze it. You will get a number of games played per team which will help to make better players substitutes for NBA manager.')
    b_exit_help = Button(help_window, text='Exit', command=help_window.destroy)
    l_help.pack(padx=10)
    b_exit_help.pack()

f_main = Frame(window)
l_text = Label(f_main, text='Add tour schedule to analize', font=14)
t_text = Text(f_main, width=60)
text_scroll = Scrollbar(f_main, command=t_text.yview)
t_text.config(yscrollcommand=text_scroll.set)

f_buttons = Frame(window)
b_analize = Button(f_buttons, text='Analize text', command=analize)
b_help = Button(f_buttons, text='Help', command=help)
b_clean = Button(f_buttons, text='Clear', command=clear)
b_exit = Button(f_buttons, text='Exit', command=window.destroy)

f_teams = Frame(window)
l_info = Label(f_teams, text='Games played on tour', font=14)
l_result = Label(f_teams, width=20, justify=LEFT, text='76ers: \nBucks: \nBulls: \nCavaliers: \nCeltics: \nClippers: \nGolden State Warriors: \nGrizzlies: \nHawks: \nHeat: \nHornets: \nJazz: \nKings: \nKnicks: \nLakers: \nMagic: \nMavericks: \nNets: \nNuggets: \nPacers: \nPelicans: \nPistons: \nRaptors: \nRockets: \nSpurs: \nSuns: \nThunder: \nTimberwolves: \nTrail Blazers: \nWizards: ')

f_main.grid(row=0, column=1, sticky=EW, padx=10, pady=10)
l_text.pack()
t_text.pack(side=LEFT)
text_scroll.pack(side=RIGHT, fill=Y)

f_buttons.grid(row=1, column=1, sticky=EW, padx=10, pady=10)
b_analize.pack()
b_exit.pack(side=RIGHT, padx=10)
b_help.pack(side=RIGHT)
b_clean.pack(side=RIGHT, padx=10)

f_teams.grid(row=0, column=0, rowspan=2, sticky=NW, padx=10, pady=10)
l_info.pack()
l_result.pack()

window.mainloop()