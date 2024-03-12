import random

def main():
  def cria_aventureiro():
      vida = 100
      ataque = random.randint(10, 20)
      defesa = random.randint(1, 5)
      return vida, ataque, defesa

  def cria_monstro():
      vida = random.randint(60, 80)
      ataque = random.randint(20, 30)
      return vida, ataque

  aventureiro = cria_aventureiro()
  monstro = cria_monstro()

  print(f"A vida do aventureiro é {aventureiro[0]}, seu ataque é {aventureiro[1]} e sua defesa é {aventureiro[2]}")
  print(f"A vida do monstro é {monstro[0]}, seu ataque é {monstro[1]}")

  rodada = 1

  while aventureiro[0] > 0 and monstro[0] > 0:
      print(f"\nRodada {rodada}")
      monstro = atualiza_monstro(monstro, aventureiro[1], aventureiro[2])
      if monstro[0] <= 0:
          print("O monstro morreu!")
          break
      aventureiro = atualiza_aventureiro(aventureiro, monstro[1])
      if aventureiro[0] <= 0:
          print("O aventureiro morreu!")
      rodada += 1

  print(f"A vida do aventureiro é {aventureiro[0]}, seu ataque é {aventureiro[1]} e sua defesa é {aventureiro[2]}")
  print(f"A vida do monstro é {monstro[0]}, seu ataque é {monstro[1]}")

def atualiza_monstro(monstro, ataque_aventureiro, defesa_aventureiro):
  dano = random.randint(1, ataque_aventureiro) - defesa_aventureiro
  monstro = (monstro[0] - dano, monstro[1])
  return monstro

def atualiza_aventureiro(aventureiro, ataque_monstro):
  dano = random.randint(1, ataque_monstro)
  aventureiro = (aventureiro[0] - dano, aventureiro[1], aventureiro[2])
  return aventureiro

main()