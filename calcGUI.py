# Interface gráfica

import PySimpleGUI as psg

import mat

frame_layout = [
    [psg.Radio('Soma', 'RADIO1', default=True, key='soma')],
    [psg.Radio('Subtração', 'RADIO1', key='sub')]
]

layout = [
    [psg.Text('Informe Num1: '), psg.InputText(key='num1'), psg.Frame('Opções: ', frame_layout)],
    [psg.Text('Informe Num2: '), psg.InputText(key='num2')],
    [psg.Text('', key='total')],
    [psg.Button('Calcular'), psg.Button('Limpar')],
]

janela = psg.Window('Calculadora do Tio', layout)

while True:
    evento, valor = janela.read()

    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['num1'].update('')
        janela['num2'].update('')
        janela['total'].update('')
        janela['num1'].set_focus()
        janela['soma'].update(True)
    else:
        # Entrada
        v1 = int(valor['num1'])
        v2 = int(valor['num2'])
        # Processamento
        if valor['soma']:
            total = mat.soma(v1, v2)
        else:
            total = mat.sub(v1, v2)

        # Saída
        janela['total'].update('{}'.format(total))

janela.close()