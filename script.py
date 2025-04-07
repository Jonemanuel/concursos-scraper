import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser

def buscar_concursos():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.pciconcursos.com.br/concursos")
        driver.implicitly_wait(10)

        concursos = driver.find_elements(By.CSS_SELECTOR, "div.ca a")
        dados = []

        for concurso in concursos[:15]:
            titulo = concurso.text.strip()
            link = concurso.get_attribute("href")
            if titulo:
                dados.append((titulo, link))

        driver.quit()
        return dados

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        return []

def exibir_concursos():
    dados = buscar_concursos()
    for i in tree.get_children():
        tree.delete(i)
    if not dados:
        messagebox.showinfo("Aviso", "Nenhum concurso encontrado.")
    else:
        for titulo, link in dados:
            tree.insert("", "end", values=(titulo, link))

def abrir_link(event):
    item_selecionado = tree.focus()
    if item_selecionado:
        valores = tree.item(item_selecionado)["values"]
        if valores:
            link = valores[1]
            webbrowser.open(link)

# Janela principal
janela = tk.Tk()
janela.title("Buscador de Concursos")
janela.geometry("900x500")

# Botão
btn = tk.Button(janela, text="Buscar Concursos", command=exibir_concursos, font=("Arial", 12), bg="#4CAF50", fg="white")
btn.pack(pady=10)

# Tabela
colunas = ("Título", "Link")
tree = ttk.Treeview(janela, columns=colunas, show="headings")
tree.heading("Título", text="Título do Concurso")
tree.heading("Link", text="Link da Notícia")
tree.pack(fill="both", expand=True)

# Evento de duplo clique para abrir link
tree.bind("<Double-1>", abrir_link)

# Rodar app
janela.mainloop()
