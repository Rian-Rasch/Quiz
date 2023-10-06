import PySimpleGUI as sg
from questions_list import quest_list

perguntas = []

#sg.theme('LightBlue1')
sg.theme('darkteal3')
layout = [
    
    [sg.Image("logo.png")],
    [sg.Text("QUIZ DA TABELA PERIÓDICA",size=(500,1), justification='center',font=('Arial', 25, 'bold'))],
    [sg.Button('Começar',size=(35,2),font=('Arial', 14, 'bold'),key='-START-')],
    [sg.Text('')],
    [sg.Button('Instruções',size=(35,2),font=('Arial', 11, 'bold'),key='-TUTORIAL-')],
    [sg.Button('Créditos',size=(35,2),font=('Arial', 11, 'bold'),key='-CREDITO-')],
    [sg.Text('')],
    [sg.Text("Trabalho da disciplina de Quimica Geral Teórica para Engenharia")]
]
def pergunta(x):
    
    
    perguntas = [
        [sg.Text(quest_list[x][0],size=(500,4), justification='center',font=('Arial', 20, 'bold'))],
        [sg.Button(f'{quest_list[x][1]}',size=(500,2),key='1',font=('Arial', 12, 'bold'))],
        [sg.Button(f'{quest_list[x][2]}',size=(500,2),key='2',font=('Arial', 12, 'bold'))],
        [sg.Button(f'{quest_list[x][3]}',size=(500,2),key='3',font=('Arial', 12, 'bold'))],
        [sg.Button(f'{quest_list[x][4]}',size=(500,2),key='4',font=('Arial', 12, 'bold'))],
    ]
    return perguntas


tamjanela = (700, 400)
window = sg.Window('Quiz Quimica geral Teorica para Engenharia.', layout, size=tamjanela, icon='logo_xif_icon.ico',element_justification='c')

while True:
    event, values = window.read()
    if event == '-TUTORIAL-':
        sg.popup(f"Neste Quiz, contamos com duas dificuldades:\n\n\nFacil: Quiz com {len(quest_list)} questões e no final o número de acertos.\n\nDifícil: Quiz com 15 Questões, se errar volta ao começo.\n\n", font=("Helvetica", 15, "bold"), title="Instruções", icon='logo_xif_icon.ico')
        # sg.popup(f"Este quiz conta com {len(quest_list)} Questões sobre quimica.\nCaso voce erre alguma questão voltamos ao inicio.\nBoa sorte.",title="Instruções",icon='logo_xif_icon.ico' )
    if event == '-CREDITO-':
        sg.popup("Criadores:\nRian Rasch Pereira\nMarcus Vinicius Pereira dos Santos\nMateus da Rosa Tonetto\nLeonardo Cardoso Nielsen(Eng. Telecom)\nEstudantes de Eng. Elétrica\nCentro de Tecnologia UFSM\nSanta Maria-RS 2023.2",title="Créditos")
    if event == '-START-':
        janela_escolha = [
            [sg.Button("Facil",key = "-FACIL-", size= (100,3))],
            [sg.Text('')],
            [sg.Button('Dificil',key = "-DIFICIL-", size= (100,3))]]
        jan_escolha = sg.Window(f'Escolha da Dificuldade.',janela_escolha,size = (300,180),icon='logo_xif_icon.ico')
        event, values = jan_escolha.read()
        if event == "-DIFICIL-":
            npergunta=0
            jan_escolha.close()
            while True:
                if npergunta+1 > 15 or npergunta+1 > len(quest_list):
                    sg.popup("Parabéns você ganhou")
                    break
                
                layoutpergunta = pergunta(npergunta)
                window_pergunta = sg.Window(f'Pergunta {npergunta+1}.',layoutpergunta,size=tamjanela)
                event, values = window_pergunta.read()
                if event == sg.WIN_CLOSED:
                    break
                
                if event != quest_list[npergunta][5]:
                    sg.popup(".....Perdeu.....",font=("Arial",16,'bold'),icon='logo_xif_icon.ico')
                    npergunta = 0
                    window_pergunta.close()
                    break
                elif (event == quest_list[npergunta][5]):
                    npergunta += 1
                    window_pergunta.close()
                jan_escolha.close()
        if event == "-FACIL-":
            npergunta = 0
            n_acertos = 0
            jan_escolha.close()
            ac_min = len(quest_list)*0.5
            while True:
                if npergunta+1 > len(quest_list):
                    if n_acertos >= ac_min:
                        sg.popup(f"Parabéns Você acertou {n_acertos} Questões.\n{n_acertos} de {len(quest_list)}",icon='logo_xif_icon.ico',font=("Helvetica", 15, "bold"),title="Parabéns.")
                        break
                    elif n_acertos < ac_min:
                        sg.popup(f"Você acertou {n_acertos} Questões",icon='logo_xif_icon.ico',font=("Helvetica", 15, "bold"),title="Acertos.")
                        break
                layoutpergunta = pergunta(npergunta)
                window_pergunta = sg.Window(f'Pergunta {npergunta+1}.',layoutpergunta,size=tamjanela)
                event, values = window_pergunta.read()
                if event == sg.WIN_CLOSED:
                    break

                elif event != quest_list[npergunta][5]:
                        npergunta += 1
                        window_pergunta.close()
                
                
                elif event == quest_list[npergunta][5]:
                        npergunta += 1
                        n_acertos += 1
                        window_pergunta.close()
                jan_escolha.close()

    if event == sg.WIN_CLOSED or event == 'OK':
         break
    

    #pyinstaller --w -onefile --icon=logo_xif_icon.ico