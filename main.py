import PySimpleGUI as sg
from questions_list import quest_list

perguntas = []


sg.theme('LightBlue1')
layout = [
    [sg.Text(' '*47),sg.Image('logo.png')],
    [sg.Text("QUIZ DA TABELA PERIODICA",size=(500,2), justification='center',font=('Arial', 20, 'bold'))],
    [sg.Text(' '*20),sg.Button('Começar',size=(35,3),key='-START-')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text(' '*20),sg.Button('Instruções',size=(35,2),key='-TUTORIAL-')],
    [sg.Text(' '*20),sg.Button('Créditos',size=(35,2),key='-CREDITO-')],
   
    [sg.Text()],
    [sg.Text()],
    [sg.Text()],
    [sg.Text()],
    
    [sg.Text("Trabalho da disciplina de Quimica Geral Teórica para Engenharia")]
]
def pergunta(x):
    
    
    perguntas = [
        [sg.Text(quest_list[x][0],size=(500,4), justification='center',font=('Arial', 16, 'bold'))],
        [sg.Button(f'{quest_list[x][1]}',size=(500,2),key='1')],
        [sg.Button(f'{quest_list[x][2]}',size=(500,2),key='2')],
        [sg.Button(f'{quest_list[x][3]}',size=(500,2),key='3')],
        [sg.Button(f'{quest_list[x][4]}',size=(500,2),key='4')],
    ]
    return perguntas


tamjanela = (500, 500)
window = sg.Window('Quiz Quimica geral Teorica para Engenharia.', layout, size=tamjanela, icon='logo_xif_icon.ico')

while True:
    event, values = window.read()
    if event == '-TUTORIAL-':
        sg.popup(f"Neste Quiz, contamos com duas dificuldades:\n\n\nFacil: Quiz com {len(quest_list)} questões e no final o número de acertos.\n\nDifícil: Quiz com 10 Questões, se errar volta ao começo.\n\n", font=("Helvetica", 15, "bold"), title="Instruções", icon='logo_xif_icon.ico')
        # sg.popup(f"Este quiz conta com {len(quest_list)} Questões sobre quimica.\nCaso voce erre alguma questão voltamos ao inicio.\nBoa sorte.",title="Instruções",icon='logo_xif_icon.ico' )
    if event == '-CREDITO-':
        sg.popup("Criadores:\nRian Rasch Pereira\nMarcus Vinicius Pereira dos Santos\nMateus da Rosa Tonetto\n\nEstudantes de Eng. Elétrica\nCentro de Tecnologia UFSM\nSanta Maria-RS 2023.2",title="Créditos")
    if event == '-START-':
        janela_escolha = [
            [sg.Button("Facil",key = "-FACIL-", size= (100,3))],
            [sg.Text('')],
            [sg.Button('Dificil',key = "-DIFICIL-", size= (100,3))]]
        jan_escolha = sg.Window(f'Escolha da Dificuldade.',janela_escolha,size = (300,160),icon='logo_xif_icon.ico')
        event, values = jan_escolha.read()
        if event == "-DIFICIL-":
            npergunta=0
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
                    sg.popup("Perdeu")
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
            ac_min = len(quest_list)*0.5
            while True:
                if npergunta+1 > len(quest_list):
                    if n_acertos >= ac_min:
                        sg.popup(f"Parabéns Você acertou {n_acertos} Questões.\n{n_acertos} de {len(quest_list)}",icon='logo_xif_icon.ico',font=("Helvetica", 15, "bold"),title="Parabéns.")
                    elif n_acertos < ac_min:
                        sg.popup(f"Você acertou {n_acertos} Questões",icon='logo_xif_icon.ico',font=("Helvetica", 15, "bold"),title="Acertos.")
                
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