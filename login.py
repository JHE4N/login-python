from PySimpleGUI import PySimpleGUI as sg

#Layout da tela de login
sg.theme('dark')
layout_login = [
    [sg.Text('Usuário:'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]
]
layout_configs = [
    [sg.]
]
#Janela
janela = sg.Window('Tela de login', layout_login)

#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar': #caso apertar no botao entrar
        if valores['usuario'] == 'jhean' and valores['senha'] == '123456':
            print('Bem Vindo!!')
            janela.close()
            
            
            