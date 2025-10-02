# Teste para verificar se os botões aparecem
import tkinter as tk

def teste_botoes():
    root = tk.Tk()
    root.title("Teste Botões")
    root.geometry("700x600")
    
    # Título
    title_label = tk.Label(root, text="Teste dos Botões", font=("Arial", 20, "bold"))
    title_label.pack(pady=10)
    
    # Botão principal
    main_btn = tk.Button(root, text="🎮 NOVO JOGO", font=("Arial", 12, "bold"),
                        bg="#4CAF50", fg="white", width=15, height=2)
    main_btn.pack(pady=10)
    
    # Frame para botões secundários
    control_frame = tk.Frame(root)
    control_frame.pack(pady=10)
    
    # Botões secundários
    btn1 = tk.Button(control_frame, text="🔄 Reset Rodada", font=("Arial", 9, "bold"),
                    bg="lightyellow", width=11, height=2)
    btn1.pack(side=tk.LEFT, padx=5)
    
    btn2 = tk.Button(control_frame, text="📊 Zerar Placar", font=("Arial", 9, "bold"),
                    bg="lightcyan", width=11, height=2)
    btn2.pack(side=tk.LEFT, padx=5)
    
    btn3 = tk.Button(control_frame, text="❌ Sair", font=("Arial", 9, "bold"),
                    bg="#f44336", fg="white", width=11, height=2)
    btn3.pack(side=tk.LEFT, padx=5)
    
    # Dicas
    tips_label = tk.Label(root, text="💡 Dicas: F1 = Novo Jogo | F4 = Reset Rodada", 
                         font=("Arial", 9), fg="gray")
    tips_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    teste_botoes()