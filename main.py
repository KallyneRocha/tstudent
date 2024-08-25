import pandas as pd
from scipy.stats import ttest_ind

def carregar_dados(configuracao):
    return pd.read_csv(f'dados/{configuracao}.csv')

def realizar_teste_t(configuracao1, configuracao2):
    dados1 = carregar_dados(configuracao1)
    dados2 = carregar_dados(configuracao2)

    dados1.rename(columns={'Cromossomo          |            Fitness': 'Fitness'}, inplace=True)
    dados2.rename(columns={'Cromossomo          |            Fitness': 'Fitness'}, inplace=True)
    
    fitness1 = dados1['Fitness']
    fitness2 = dados2['Fitness']

    media_fitness1 = fitness1.mean()
    media_fitness2 = fitness2.mean()

    t_stat, p_value = ttest_ind(fitness1, fitness2)
    
    print(f"Comparação entre {configuracao1} e {configuracao2}:")
    print(f"T-Statistic: {t_stat}, P-Value: {p_value}")
    print("\n")

    nivel_significancia = 0.05
    if p_value < nivel_significancia:
        print("A diferença é estatisticamente significativa.")
        if t_stat > 0:
            melhorResultadoT = configuracao1
        elif t_stat < 0:
            melhorResultadoT = configuracao2
        else:
            melhorResultadoT = "Empate"

        print(f"Melhor Resultado com base na estatística T: {melhorResultadoT}")
        
        if media_fitness1 > media_fitness2:
            melhorResultadoMedia = configuracao1
        elif media_fitness2 > media_fitness1:
            melhorResultadoMedia = configuracao2
        else:
            melhorResultadoMedia = "Empate"

        print(f"Melhor Resultado com base na média dos Fitness: {melhorResultadoMedia}")
    else:
        print("A diferença não é estatisticamente significativa.")
        print("Não é possível determinar qual configuração é melhor com base nos dados atuais.")

    print("\n")

comparacoes = [
    ('roleta', 'torneio'),
    ('uniforme', 'dois_pontos'),
    ('mutacao1', 'mutacao5'),
    ('elitismo', 'somente_filhos')
]

for config1, config2 in comparacoes:
    realizar_teste_t(config1, config2)