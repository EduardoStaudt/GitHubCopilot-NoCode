# 🎮 Pedra, Papel e Tesoura - Interface Gráfica

Um jogo clássico de **Pedra, Papel e Tesoura** implementado em Python com interface gráfica usando Tkinter. Jogue contra o computador em uma interface moderna e intuitiva!

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📸 Screenshot

```
┌─────────────────────────────────────┐
│         Pedra, Papel e Tesoura      │
├─────────────────────────────────────┤
│    Placar: Jogador 0 - 0 Computador │
│                                     │
│  Sua Escolha    VS    Computador    │
│      ❓               ❓           │
│                                     │
│  [🪨 Pedra] [📄 Papel] [✂️ Tesoura] │
│                                     │
│            Faça sua escolha!        │
│                                     │
│         [� NOVO JOGO]              │
│                                     │
│ [🔄 Reset Rodada] [📊 Zerar Placar] [❌ Sair] │
└─────────────────────────────────────┘
```

## ✨ Funcionalidades

### 🎯 **Jogo Principal**
- ✅ Jogue contra o computador com escolhas aleatórias
- ✅ Interface gráfica intuitiva com emojis
- ✅ Placar em tempo real
- ✅ Mensagens de resultado coloridas
- ✅ Animação visual das escolhas

### 🎮 **Controles de Jogo**
- **� NOVO JOGO**: Inicia uma nova partida completa (reseta placar e escolhas)
- **🔄 Reset Rodada**: Limpa apenas a rodada atual, mantém o placar
- **📊 Zerar Placar**: Reseta diretamente o placar sem confirmação
- **❌ Sair**: Encerra o jogo mostrando o placar final

### ⌨️ **Atalhos de Teclado**
| Tecla | Função |
|-------|--------|
| `F1` | Novo Jogo |
| `F4` | Reset Rodada |
| `F5` | Novo Jogo (com confirmação) |
| `F6` | Zerar Placar |
| `ESC` | Sair do jogo |

### 🎨 **Interface**
- 🌈 Cores diferenciadas para cada opção
- 📱 Design responsivo e moderno
- 🔤 Texto em português brasileiro
- 💡 Dicas de atalhos na interface
- 🎯 Botões grandes e acessíveis

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- Tkinter (geralmente incluído com Python)

### Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/EduardoStaudt/GitHubCopilot-NoCode.git
   cd GitHubCopilot-NoCode
   ```

2. **Execute o jogo:**
   ```bash
   python rock_paper_scissors_com_interface.py
   ```

3. **Ou execute diretamente:**
   ```bash
   python -m rock_paper_scissors_com_interface
   ```

## 🎲 Como Jogar

1. **Inicie o jogo** executando o arquivo Python
2. **Escolha sua jogada** clicando em um dos botões:
   - 🪨 **Pedra**: Vence a tesoura, perde para o papel
   - 📄 **Papel**: Vence a pedra, perde para a tesoura  
   - ✂️ **Tesoura**: Vence o papel, perde para a pedra
3. **Veja o resultado** da rodada
4. **Acompanhe o placar** acumulado
5. **Use os controles** para gerenciar o jogo

### 🏆 **Regras do Jogo**
- **Pedra** esmaga **Tesoura** ✅
- **Papel** cobre **Pedra** ✅
- **Tesoura** corta **Papel** ✅
- Escolhas iguais = **Empate** 🤝

## 📁 Estrutura do Projeto

```
GitHubCopilot-NoCode/
├── rock_paper_scissors_com_interface.py  # Arquivo principal do jogo
├── test_drive.py                         # Arquivo de testes (vazio)
├── LICENSE                               # Licença MIT
├── README.md                             # Este arquivo
└── .venv/                               # Ambiente virtual Python
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**: Linguagem de programação principal
- **Tkinter**: Biblioteca para interface gráfica (GUI)
- **Random**: Para escolhas aleatórias do computador

## 🎯 Funcionalidades Técnicas

### 🔧 **Classe Principal: `RockPaperScissorsGUI`**
```python
class RockPaperScissorsGUI:
    def __init__(self, root)          # Inicialização da interface
    def create_widgets(self)          # Criação dos elementos visuais  
    def fazer_jogada(self, escolha)   # Lógica principal do jogo
    def determinar_resultado(self)    # Algoritmo de vitória/derrota
    def novo_jogo(self)              # Reset completo do jogo
    def reset_escolha(self)          # Reset da rodada atual
    def sair_jogo(self)              # Encerramento com placar final
```

### 🎨 **Design Patterns Utilizados**
- **MVC (Model-View-Controller)**: Separação entre lógica e interface
- **Event-Driven Programming**: Resposta a cliques e teclas
- **State Management**: Controle de estado do jogo e placar

## 🔄 Atualizações Recentes

### v2.0 - Nova Interface de Reset
- ➕ Botão principal "� NOVO JOGO" mais proeminente
- 🎨 Interface reorganizada e mais intuitiva
- ⌨️ Novos atalhos de teclado (F1 para novo jogo)
- 🔧 Múltiplas opções de reset para diferentes necessidades
- 💡 Dicas de atalhos atualizadas na interface

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Eduardo Andrei Staudt**
- GitHub: [@EduardoStaudt](https://github.com/EduardoStaudt)
- Projeto: [GitHubCopilot-NoCode](https://github.com/EduardoStaudt/GitHubCopilot-NoCode)

## 🎉 Divirta-se Jogando!

Que vença o melhor! 🏆

---
*Desenvolvido com ❤️ em Python*