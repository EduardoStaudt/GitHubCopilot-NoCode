# Jogo de Pedra, Papel e Tesoura com interface gráfica usando Tkinter
# O jogador clica em botões para fazer sua escolha e joga contra o computador
# Interface mostra as escolhas, resultado e placar atualizado

import tkinter as tk
from tkinter import ttk, messagebox
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        """
        Inicializa a janela principal e as variáveis do jogo para a interface de Pedra, Papel e Tesoura.
        Args:
            root (tk.Tk): A janela raiz do Tkinter.
        Configura:
            - Título da janela, tamanho e comportamento não redimensionável.
            - Protocolo de fechamento da janela e atalhos de teclado (Escape para sair, F5 para resetar placar).
            - Variáveis do jogo para pontuação do jogador e do computador.
            - Opções do jogo, emojis e nomes traduzidos.
            - Chama o método para criar e posicionar os widgets na janela.
        """
        self.root = root
        self.root.title("Pedra, Papel e Tesoura")
        self.root.geometry("700x450")  # Aumentar mais para comportar 4 botões
        self.root.resizable(False, False)
        
        # Configurar comportamento ao fechar janela
        self.root.protocol("WM_DELETE_WINDOW", self.sair_jogo)
        
        # Atalhos de teclado
        self.root.bind('<Escape>', lambda e: self.sair_jogo())
        self.root.bind('<F1>', lambda e: self.novo_jogo())  # Novo jogo principal
        self.root.bind('<F4>', lambda e: self.reset_escolha())
        self.root.bind('<F5>', lambda e: self.resetar_placar())
        self.root.bind('<F6>', lambda e: self.resetar_placar_direto())
        
        # Variáveis do jogo
        self.pontuacao_jogador = 0
        self.pontuacao_computador = 0
        self.opcoes = ["rock", "paper", "scissors"]
        self.emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
        self.nomes = {"rock": "Pedra", "paper": "Papel", "scissors": "Tesoura"}
        
        self.create_widgets()
    
    def create_widgets(self):
        # Título
        title_label = tk.Label(self.root, text="Pedra, Papel e Tesoura", 
                            font=("Arial", 20, "bold"), fg="navy")
        title_label.pack(pady=10)
        
        # Frame para placar
        score_frame = tk.Frame(self.root)
        score_frame.pack(pady=10)
        
        self.score_label = tk.Label(score_frame, text="Placar: Jogador 0 - 0 Computador", 
                                font=("Arial", 14, "bold"), fg="darkgreen")
        self.score_label.pack()
        
        # Frame para escolhas
        choices_frame = tk.Frame(self.root)
        choices_frame.pack(pady=20)
        
        # Coluna do jogador
        player_frame = tk.Frame(choices_frame)
        player_frame.pack(side=tk.LEFT, padx=20)
        
        tk.Label(player_frame, text="Sua Escolha", font=("Arial", 12, "bold")).pack()
        self.player_choice_label = tk.Label(player_frame, text="❓", font=("Arial", 50))
        self.player_choice_label.pack(pady=10)
        
        # VS no meio
        vs_frame = tk.Frame(choices_frame)
        vs_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(vs_frame, text="VS", font=("Arial", 16, "bold"), fg="red").pack(pady=50)
        
        # Coluna do computador
        computer_frame = tk.Frame(choices_frame)
        computer_frame.pack(side=tk.LEFT, padx=20)
        
        tk.Label(computer_frame, text="Computador", font=("Arial", 12, "bold")).pack()
        self.computer_choice_label = tk.Label(computer_frame, text="❓", font=("Arial", 50))
        self.computer_choice_label.pack(pady=10)
        
        # Frame para botões de escolha
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)
        
        # Botões para cada escolha
        rock_btn = tk.Button(buttons_frame, text="🪨\nPedra", font=("Arial", 12, "bold"),
                            width=8, height=3, command=lambda: self.fazer_jogada("rock"),
                            bg="lightgray", activebackground="gray")
        rock_btn.pack(side=tk.LEFT, padx=10)
        
        paper_btn = tk.Button(buttons_frame, text="📄\nPapel", font=("Arial", 12, "bold"),
                            width=8, height=3, command=lambda: self.fazer_jogada("paper"),
                            bg="lightblue", activebackground="blue")
        paper_btn.pack(side=tk.LEFT, padx=10)
        
        scissors_btn = tk.Button(buttons_frame, text="✂️\nTesoura", font=("Arial", 12, "bold"),
                                width=8, height=3, command=lambda: self.fazer_jogada("scissors"),
                                bg="lightcoral", activebackground="red")
        scissors_btn.pack(side=tk.LEFT, padx=10)
        
        # Label para resultado
        self.result_label = tk.Label(self.root, text="Faça sua escolha!", 
                                    font=("Arial", 14, "bold"), fg="blue")
        self.result_label.pack(pady=20)
        
        # Frame para botão de reset principal (mais proeminente)
        reset_main_frame = tk.Frame(self.root)
        reset_main_frame.pack(pady=10)
        
        # Botão principal de Novo Jogo (maior e mais visível)
        new_game_main_btn = tk.Button(reset_main_frame, text="� NOVO JOGO", font=("Arial", 12, "bold"),
                                    command=self.novo_jogo, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white",
                                    width=15, height=2, relief="raised", bd=3)
        new_game_main_btn.pack()
        
        # Botões de controle secundários
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        # Botão Reset Escolha
        reset_choice_btn = tk.Button(control_frame, text="🔄 Reset Rodada", font=("Arial", 9, "bold"),
                                   command=self.reset_escolha, bg="lightyellow", activebackground="orange",
                                   width=11, height=2)
        reset_choice_btn.pack(side=tk.LEFT, padx=5)
        
        # Botão Reset Placar
        reset_score_btn = tk.Button(control_frame, text="📊 Zerar Placar", font=("Arial", 9, "bold"),
                                  command=self.resetar_placar_direto, bg="lightcyan", activebackground="cyan",
                                  width=11, height=2)
        reset_score_btn.pack(side=tk.LEFT, padx=5)
        
        # Botão Sair
        quit_btn = tk.Button(control_frame, text="❌ Sair", font=("Arial", 9, "bold"),
                           command=self.sair_jogo, bg="#f44336", fg="white", activebackground="darkred",
                           width=11, height=2)
        quit_btn.pack(side=tk.LEFT, padx=5)
        
        # Área de dicas
        tips_frame = tk.Frame(self.root)
        tips_frame.pack(pady=(10, 5))
        
        tips_label = tk.Label(tips_frame, text="💡 Dicas: F1 = Novo Jogo | F4 = Reset Rodada | F6 = Zerar Placar | ESC = Sair", 
                            font=("Arial", 9), fg="gray")
        tips_label.pack()
    
    def fazer_jogada(self, escolha_jogador):
        # Escolha do computador
        escolha_computador = random.choice(self.opcoes)
        
        # Atualizar interface com as escolhas
        self.player_choice_label.config(text=self.emojis[escolha_jogador])
        self.computer_choice_label.config(text=self.emojis[escolha_computador])
        
        # Determinar resultado
        resultado = self.determinar_resultado(escolha_jogador, escolha_computador)
        
        # Atualizar placar
        if resultado == 1:
            self.pontuacao_jogador += 1
            self.result_label.config(text=f"Você venceu! {self.nomes[escolha_jogador]} vence {self.nomes[escolha_computador]}", 
                                fg="green")
        elif resultado == -1:
            self.pontuacao_computador += 1
            self.result_label.config(text=f"Você perdeu! {self.nomes[escolha_computador]} vence {self.nomes[escolha_jogador]}", 
                                fg="red")
        else:
            self.result_label.config(text=f"Empate! Ambos escolheram {self.nomes[escolha_jogador]}", 
                                fg="orange")
        
        # Atualizar placar
        self.score_label.config(text=f"Placar: Jogador {self.pontuacao_jogador} - {self.pontuacao_computador} Computador")
    
    def determinar_resultado(self, jogador, computador):
        if jogador == computador:
            return 0  # Empate
        elif (
            (jogador == "rock" and computador == "scissors") or
            (jogador == "paper" and computador == "rock") or
            (jogador == "scissors" and computador == "paper")
        ):
            return 1  # Jogador vence
        else:
            return -1  # Computador vence
    
    def novo_jogo(self):
        """Inicia um novo jogo completo - reseta tudo"""
        self.pontuacao_jogador = 0
        self.pontuacao_computador = 0
        self.score_label.config(text="Placar: Jogador 0 - 0 Computador")
        self.player_choice_label.config(text="❓")
        self.computer_choice_label.config(text="❓")
        self.result_label.config(text="🎮 Novo jogo iniciado! Faça sua escolha!", fg="green")
    
    def reset_escolha(self):
        """Reset apenas a escolha atual, mantendo o placar"""
        self.player_choice_label.config(text="❓")
        self.computer_choice_label.config(text="❓")
        self.result_label.config(text="Faça sua escolha!", fg="blue")
    
    def resetar_placar_direto(self):
        """Reset direto do placar sem confirmação"""
        self.pontuacao_jogador = 0
        self.pontuacao_computador = 0
        self.score_label.config(text="Placar: Jogador 0 - 0 Computador")
        self.player_choice_label.config(text="❓")
        self.computer_choice_label.config(text="❓")
        self.result_label.config(text="Placar resetado! Faça sua escolha!", fg="blue")
    
    def resetar_placar(self):
        resposta = messagebox.askyesno("Resetar Placar", "Deseja realmente resetar o placar?")
        if resposta:
            self.pontuacao_jogador = 0
            self.pontuacao_computador = 0
            self.score_label.config(text="Placar: Jogador 0 - 0 Computador")
            self.player_choice_label.config(text="❓")
            self.computer_choice_label.config(text="❓")
            self.result_label.config(text="Faça sua escolha!", fg="blue")
    
    def sair_jogo(self):
        # Mostra o placar final antes de sair
        placar_final = f"Placar Final:\nJogador: {self.pontuacao_jogador}\nComputador: {self.pontuacao_computador}"
        
        if self.pontuacao_jogador > self.pontuacao_computador:
            mensagem = f"{placar_final}\n\n🎉 Parabéns! Você ganhou no geral!"
        elif self.pontuacao_computador > self.pontuacao_jogador:
            mensagem = f"{placar_final}\n\n😢 O computador ganhou desta vez!"
        else:
            mensagem = f"{placar_final}\n\n🤝 Empate no placar geral!"
        
        resposta = messagebox.askyesno("Sair do Jogo", f"{mensagem}\n\nDeseja realmente sair?")
        if resposta:
            self.root.destroy()  # Fecha a janela completamente

def main():
    try:
        print("Iniciando o jogo...")
        root = tk.Tk()
        print("Janela criada!")
        game = RockPaperScissorsGUI(root)
        print("Interface carregada! Abrindo janela...")
        root.mainloop()
    except Exception as e:
        print(f"Erro ao executar o jogo: {e}")
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()


