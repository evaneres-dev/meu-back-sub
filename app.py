import numpy as np

batimentos = np.array([72, 75, 80, 78, 76, 66, 77])

exames = [
    ["IMC", 24.5, "Normal"],
    ["Glicemia", 90, "Normal"],
    ["Colesterol", 210, "Alto"]
]

#batimentos quarta-feira
print(batimentos[2])

#batimentos final de semana. omitindo o end
print(batimentos[5:])

#batimentos invertidos 
batimentos_invertidos = batimentos[::-1]    
print(batimentos_invertidos)

#do inicio ao fim, pulando de 2 em 2
dias_alternados = batimentos[::2]
print(dias_alternados)

#resultado do colesterol. é a 3 sublista, o resultado é o 2 item 
print(exames[2][1])

# status do IMC: IMC é a 1ª sublista (índice 0). O status é o 3º item (índice 2).
print(exames[0][2])

#apenas os nomes dos exames. jeito 1: loop tradicional
nomes_exames = []
for exame in exames:
    nomes_exames.append(exame[0])
print(nomes_exames)

#puxar apenas os dois primeiros exames. fatiar a lista principal  (do inicio ate o indice 2, excluindo o 2)
primeiros_exames = exames[:2]
print(primeiros_exames)

#variabilidade dos bpm 
maior_batimento = max(batimentos)
menor_batimento = min(batimentos)

variabilidade = maior_batimento - menor_batimento
print(f"Maior batimento: {maior_batimento}, Menor batimento: {menor_batimento}, Variabilidade: {variabilidade}")

try:
    altura = float(input("Digite a altura em metros (ex: 1,75): ").replace(',', '.'))
    peso = float(input("Digite o peso em kg (ex: 70,5): ").replace(',', '.'))

    if altura <= 0:
        print("A altura deve ser maior que zero.")
    else:
        imc = peso / (altura ** 2)
        print(f"\nSeu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso.")
            print("Você NÃO está na faixa adequada.")
        elif 18.5 <= imc <= 24.9:
            print("Classificação: Peso normal.")
            print("Parabéns! Você está na faixa adequada de saúde.")
        elif 25.0 <= imc <= 29.9:
            print("Classificação: Sobrepeso.")
            print("Você NÃO está na faixa adequada.")
        elif 30.0 <= imc <= 34.9:
            print("Classificação: Obesidade Grau I.")
            print("Você NÃO está na faixa adequada.")
        elif 35.0 <= imc <= 39.9:
            print("Classificação: Obesidade Grau II.")
            print("Você NÃO está na faixa adequada.")
        else:
            print("Classificação: Obesidade Grau III (Mórbida).")
            print("Você NÃO está na faixa adequada. Procure um médico.")

except ValueError:
    print("\n Erro: Você digitou letras ou símbolos. Digite apenas números.")

batitmentos_ajustados = batimentos + 5
print(batitmentos_ajustados)

print(np.mean(batimentos))
print(np.max(batimentos))
print(np.min(batimentos))