import numpy as np

n_jogos=int(input("Quantos jogos?"))

locais = np.empty(n_jogos,"U30")
golos = np.empty(n_jogos)

for i in range(n_jogos):
    locais[i] = input("Local do jogo: ")
    golos[i] = int(input("Golos marcados: "))

#nº máximo de golos marcados
max_golos=golos[0]
max_jogo=0
contar_jogos_fora=0
total = 0
for i in range(n_jogos):
    if golos[i]>=max_golos:
        max_golos=golos[i]
        max_jogo=i+1
    if locais[i].lower()=="viseu".lower():
        contar_jogos_fora += 1
    total += golos[i]

#percentagem de jogos fora
percentagem = contar_jogos_fora/n_jogos * 100

mensagem = f"O recorde de golos num jogo foi de {max_golos}, obtido na {max_jogo}ª jornada.{percentagem:.0f}% dos jogos da temporada foram em casa. A equipa marcou {total:.0f} golos na totalidade."
print(mensagem)
