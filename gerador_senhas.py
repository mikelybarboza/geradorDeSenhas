import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string

# Função para gerar senha
def gerar_senha():
    try:
        comprimento = int(entry_comprimento.get())
        if comprimento < 6:
            raise ValueError("O comprimento deve ser maior ou igual a 6.")

        incluir_maiusculas = var_maiusculas.get()
        incluir_minusculas = var_minusculas.get()
        incluir_numeros = var_numeros.get()
        incluir_simbolos = var_simbolos.get()
        evitar_ambiguos = var_ambiguos.get()

        if not (incluir_maiusculas or incluir_minusculas or incluir_numeros or incluir_simbolos):
            raise ValueError("Selecione pelo menos uma opção de caractere.")

        caracteres = ""
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_simbolos:
            caracteres += string.punctuation

        if evitar_ambiguos:
            ambiguos = "l1I0O"
            caracteres = ''.join(c for c in caracteres if c not in ambiguos)

        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)

        # Adiciona a senha ao histórico
        if senha not in lista_historico.get(0, tk.END):
            lista_historico.insert(tk.END, senha)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Função para salvar senha em arquivo
def salvar_senha():
    senha = entry_senha.get()
    if not senha:
        messagebox.showwarning("Aviso", "Nenhuma senha gerada para salvar.")
        return

    arquivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt")]
    )
    if arquivo:
        with open(arquivo, 'a') as f:
            f.write(senha + '\n')
        messagebox.showinfo("Sucesso", f"Senha salva em {arquivo}")

# Função para copiar senha para a área de transferência
def copiar_senha():
    senha = entry_senha.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        root.update()
        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência.")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha gerada para copiar.")

# Configuração da interface
root = tk.Tk()
root.title("Gerador de Senhas Seguras")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Comprimento da senha
tk.Label(frame, text="Comprimento da Senha:").grid(row=0, column=0, sticky="w")
entry_comprimento = tk.Entry(frame, width=5)
entry_comprimento.grid(row=0, column=1, sticky="w")
entry_comprimento.insert(0, "12")

# Opções de caracteres
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)
var_ambiguos = tk.BooleanVar(value=False)

tk.Checkbutton(frame, text="Incluir Letras Maiúsculas", variable=var_maiusculas).grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Incluir Letras Minúsculas", variable=var_minusculas).grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame, text="Incluir Números", variable=var_numeros).grid(row=3, column=0, sticky="w")
tk.Checkbutton(frame, text="Incluir Símbolos", variable=var_simbolos).grid(row=4, column=0, sticky="w")
tk.Checkbutton(frame, text="Evitar Caracteres Ambíguos (ex.: l, 1, 0, O)", variable=var_ambiguos).grid(row=5, column=0, sticky="w")

# Botões
tk.Button(frame, text="Gerar Senha", command=gerar_senha).grid(row=6, column=0, pady=10, sticky="w")
tk.Button(frame, text="Salvar Senha", command=salvar_senha).grid(row=6, column=1, pady=10, sticky="e")
tk.Button(frame, text="Copiar Senha", command=copiar_senha).grid(row=7, column=0, columnspan=2, pady=5)

# Campo de exibição da senha
tk.Label(frame, text="Senha Gerada:").grid(row=8, column=0, sticky="w", pady=(10, 0))
entry_senha = tk.Entry(frame, width=30)
entry_senha.grid(row=9, column=0, columnspan=2, pady=5)

# Histórico de senhas geradas
tk.Label(frame, text="Histórico de Senhas:").grid(row=10, column=0, sticky="w", pady=(10, 0))
lista_historico = tk.Listbox(frame, height=5, width=30)
lista_historico.grid(row=11, column=0, columnspan=2, pady=5)

root.mainloop()
