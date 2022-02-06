from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('dark')
layout = [
    [sg.Text('Usuário:'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de login', layout)

#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar': #caso apertar no botao entrar
        if valores['usuario'] == 'jhean' and valores['senha'] == '123456':
            print('Bem Vindo!!')