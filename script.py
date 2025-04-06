import webbrowser
import pyautogui
import time

# Abrir o Google
webbrowser.open("https://www.google.com")

# Esperar o navegador abrir
time.sleep(3)

# Digitar no campo de busca
pyautogui.write("Concursos abertos 2025")
time.sleep(1)

# Pressionar Enter para pesquisar
pyautogui.press("enter")

print("Pesquisa feita com sucesso!")
