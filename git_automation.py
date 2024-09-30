import flet as ft
import pyautogui as auto
import time

# Função para executar comandos Git
def executar_git(comando):
    auto.PAUSE = 0.5
    
    # Abrir o menu iniciar
    auto.press('win')
    auto.write('vscode')
    auto.press('enter')

    # Aguardar o Visual Studio Code abrir
    time.sleep(5)

    # Abrir o terminal integrado no VSCode (Ctrl + j)
    auto.hotkey('ctrl', 'j')

    # Aguardar o terminal abrir
    time.sleep(1.2)

    # Executar o comando Git
    auto.write(comando)
    auto.press('enter')

# Função principal da interface
def main(page):
    page.title = "Gerenciador Git com Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20  # Adiciona um padding para a interface

    # Campos de entrada
    commit_message_input = ft.TextField(label="Mensagem do Commit", width=300)
    feedback_text = ft.Text()

    def on_init_click(e):
        try:
            executar_git('git init')
            feedback_text.value = "Repositório inicializado com sucesso."
        except Exception as ex:
            feedback_text.value = f"Erro: {ex}"

    def on_add_click(e):
        try:
            executar_git('git add .')
            feedback_text.value = "Arquivos adicionados com sucesso."
        except Exception as ex:
            feedback_text.value = f"Erro: {ex}"

    def on_commit_click(e):
        commit_message = commit_message_input.value
        if commit_message.strip() == "":
            feedback_text.value = "Por favor, insira uma mensagem para o commit."
            return
        
        try:
            executar_git(f'git commit -m "{commit_message}"')
            feedback_text.value = "Commit realizado com sucesso."
            commit_message_input.value = ""  # Limpa o campo após o commit
        except Exception as ex:
            feedback_text.value = f"Erro: {ex}"

    # Layout da interface
    page.add(
        ft.Column(
            controls=[
                ft.Text("Gerenciador Git", size=24, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton("Inicializar Git", on_click=on_init_click),
                ft.ElevatedButton("Adicionar Arquivos", on_click=on_add_click),
                commit_message_input,
                ft.ElevatedButton("Fazer Commit", on_click=on_commit_click),
                feedback_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
    )

ft.app(target=main)
