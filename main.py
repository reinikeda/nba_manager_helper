from tkinter import *
import tkinter.messagebox
import webbrowser

window = Tk()
window.iconbitmap('nba.ico')
window.title('NBA manager helper 2022/2023 season')
window.geometry('700x540')
window.resizable(width=False, height=False)

team_list = StringVar()
team_list.set('76ers: \nBucks: \nBulls: \nCavaliers: \nCeltics: \nClippers: \nGolden State Warriors: \nGrizzlies: \nHawks: \nHeat: \nHornets: \nJazz: \nKings: \nKnicks: \nLakers: \nMagic: \nMavericks: \nNets: \nNuggets: \nPacers: \nPelicans: \nPistons: \nRaptors: \nRockets: \nSpurs: \nSuns: \nThunder: \nTimberwolves: \nTrail Blazers: \nWizards: ')

team_list_2 = StringVar()
team_list_2.set('76ers: \nBucks: \nBulls: \nCavaliers: \nCeltics: \nClippers: \nGolden State Warriors: \nGrizzlies: \nHawks: \nHeat: \nHornets: \nJazz: \nKings: \nKnicks: \nLakers: \nMagic: \nMavericks: \nNets: \nNuggets: \nPacers: \nPelicans: \nPistons: \nRaptors: \nRockets: \nSpurs: \nSuns: \nThunder: \nTimberwolves: \nTrail Blazers: \nWizards: ')

def clear():
    t_text.delete(1.0, END)
    l_result['textvariable'] = team_list_2

def analize():
    if len(t_text.get(1.0, END)) == 1:
        tkinter.messagebox.showinfo(title='Error', message='No text was added')
    else:
        full_list = ['76ers', 'Bucks', 'Bulls', 'Cavaliers', 'Celtics', 'Clippers', 'Golden State Warriors', 'Grizzlies', 'Hawks', 'Heat', 'Hornets', 'Jazz', 'Kings', 'Knicks', 'Lakers', 'Magic', 'Mavericks', 'Nets', 'Nuggets', 'Pacers', 'Pelicans', 'Pistons', 'Raptors', 'Rockets', 'Spurs', 'Suns', 'Thunder', 'Timberwolves', 'Trail Blazers', 'Wizards']
        team_count = {}
        for team in full_list:
            result = (t_text.get(1.0, END)).count(team)
            team_count[team] = result
            team_list.set('\n'.join(f'{team}: {count}' for team, count in team_count.items()))

def link():
    webbrowser.open_new_tab('https://www.krepsinis.net/menedzeris')

def help():
    help_window = Toplevel(window)
    help_window.iconbitmap('nba.ico')
    help_window.title('Help')
    help_window.geometry('290x190')
    help_window.resizable(width=False, height=False)
    l_help = Label(help_window, wraplength='250', pady=10, justify=LEFT, text='Program is adapted for krepsinis.net NBA manager. It may not work propertly with other NBA managers.\nHow it works? Just add (copy paste text) NBA teams schedule of single tour to analyze it. You will get a number of games played per team which will help to make better players substitutes for NBA manager.')
    b_exit_help = Button(help_window, text='Exit', command=help_window.destroy)
    l_help.pack(padx=10)
    b_exit_help.pack()

f_main = Frame(window)
l_text = Label(f_main, text='Add tour schedule to analize', font=14)
t_text = Text(f_main, width=60)
text_scroll = Scrollbar(f_main, command=t_text.yview)
t_text.config(yscrollcommand=text_scroll.set)

f_buttons = Frame(window)
b_link = Button(f_buttons, text='Link to website', command=link)
b_analize = Button(f_buttons, text='Analize text', command=analize)
b_help = Button(f_buttons, text='Help', command=help)
b_clean = Button(f_buttons, text='Clear', command=clear)
b_exit = Button(f_buttons, text='Exit', command=window.destroy)

f_teams = Frame(window)
l_info = Label(f_teams, text='Games played on tour', font=14)
l_result = Label(f_teams, width=20, justify=LEFT, textvariable=team_list)

f_main.grid(row=0, column=1, sticky=EW, padx=10, pady=10)
l_text.pack()
t_text.pack(side=LEFT)
text_scroll.pack(side=RIGHT, fill=Y)

f_buttons.grid(row=1, column=1, sticky=EW, padx=10)
b_analize.pack(pady=20)
b_exit.pack(side=RIGHT)
b_help.pack(side=RIGHT, padx=10)
b_link.pack(side=RIGHT)
b_clean.pack(side=RIGHT, padx=10)

f_teams.grid(row=0, column=0, rowspan=2, sticky=NW, padx=10, pady=10)
l_info.pack()
l_result.pack()

window.mainloop()