import random

# Configuração do tabuleiro
tabuleiro = []

for x in range(0, 5):
  tabuleiro.append(["O"] * 5)

def print_tabuleiro(tabuleiro):
  for linha in tabuleiro:
    print(" ".join(linha))

print("Vamos jogar Batalha Naval!")
print_tabuleiro(tabuleiro)

# Definindo a localização do navio
def linha_aleatoria(tabuleiro):
  return random.randint(0, len(tabuleiro) - 1)

def coluna_aleatoria(tabuleiro):
  return random.randint(0, len(tabuleiro[0]) - 1)

navio_linha = linha_aleatoria(tabuleiro)
navio_coluna = coluna_aleatoria(tabuleiro)

# Jogando o jogo
for turno in range(4):
  print("Turno", turno + 1)
  
  palpite_linha = int(input("Adivinhe a linha:"))
  palpite_coluna = int(input("Adivinhe a coluna:"))

  if palpite_linha == navio_linha and palpite_coluna == navio_coluna:
    print("Parabéns! Você afundou meu navio!")
    break
  else:
    if palpite_linha not in range(5) or \
      palpite_coluna not in range(5):
      print("Oops, isso não é nem mesmo no oceano.")
    elif tabuleiro[palpite_linha][palpite_coluna] == "X":
      print("Você já tentou esse.")
    else:
      print("Você errou meu navio!")
      tabuleiro[palpite_linha][palpite_coluna] = "X"
    if (turno == 3):
      print("Fim do jogo")
    print_tabuleiro(tabuleiro)
