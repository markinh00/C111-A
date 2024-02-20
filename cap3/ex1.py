
print("Exercício 1 ---------------------------------------------------------------------------------------------------")
times = ['Barcelona', 'Quinze de Limeira', 'Íbis', 'Manchester City', 'Volta Redonda']
print(f"Lista dos 5 primeiros colocados do Campeonato Mundial de Futebol: {times}")

# a)
print(f"Mostrando apenas os 3 primeiros: {times[:3]}")
# b)
print(f"Mostrando os 2 ultimos colocados: {times[3:]}")
# c)
print(f"Mostrando uma lista com os times em ordem alfabética: {sorted(times)}")
# d)
print(f"Posição do Barcelona: {times.index('Barcelona') + 1}°")
