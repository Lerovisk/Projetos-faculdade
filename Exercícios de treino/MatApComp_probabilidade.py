'''Mônica inventou um jogo de bingo em que as bolas que são sorteadas contêm alternativas em vez de números.
Em uma das rodadas, foram usadas as alternativas da palavra VESTIBULAR,
'''

vestibular = ["V", "E", "S","T", "I", "B", "U", "L", "A", "R"]
for i in range(len(vestibular)):
    print(vestibular[i])
print("a) Ao sortear uma bola, qual é a probabilidade de que seja a letra V?")

probabilidade = 1 / len(vestibular)
print(f"1/ 10 = {probabilidade:.2f}")  # 0.10
print(probabilidade * 100, "%")



