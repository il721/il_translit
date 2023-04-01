import PySimpleGUI as sg

sg.theme('DarkGrey11')
# Устанавливаем цвет внутри окна
layout = [[sg.Text(" ж-zh  ё-joo  ф-f  ы-y  ю-ju  ю-ju  я-ja "
                   " й-j  ш-sh  щ-sch  х-h  ч-ch  ь-'  ъ-~ ")],
          [sg.Text('Input Text'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# sg.theme_previewer()
# Создаем окно
window = sg.Window('Название окна', layout)
# Цикл для обработки "событий" и получения "значений" входных данных
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        # если пользователь закрыл окно или нажал «Cancel»
        break
    print('Молодец, ты справился с вводом', values[0])

window.close()
