# Comparador de Configurações do Algoritmo Genético

Este repositório contém um projeto para comparar diferentes configurações de um algoritmo genético usado para resolver o Problema da Mochila. O projeto utiliza o teste estatístico t-Student para avaliar a significância das diferenças entre as configurações.

## Estrutura do Projeto

O projeto inclui:

- **`main.py`**: Script principal que realiza o teste t-Student entre as diferentes configurações.
- **`dados/`**: Diretório onde os arquivos CSV com os resultados das execuções são armazenados.

## Configurações Testadas

As seguintes configurações são avaliadas:

1. **Seleção para cruzamento**
   - Roleta
   - Torneio

2. **Cruzamento**
   - Uniforme
   - 2-pontos (aleatório)

3. **Mutação**
   - Taxa de 1%
   - Taxa de 5%

4. **Seleção para próxima geração**
   - Somente os filhos
   - Elitismo de 10%

Para cada configuração, foram realizadas 30 execuções, e o melhor resultado de cada execução foi exportado para um arquivo CSV.

## Requisitos

- Python 3.11.3
- Bibliotecas: `pandas`, `scipy`

Você pode instalar as bibliotecas necessárias com o seguinte comando:

```bash
pip install pandas scipy
```

## Execução
Para executar o script e realizar as comparações, siga os passos abaixo:

Certifique-se de que todos os arquivos CSV necessários estão na pasta dados/. Os arquivos devem seguir a nomenclatura {configuracao}.csv, onde {configuracao} é o nome da configuração testada (por exemplo, roleta.csv, torneio.csv, etc.).

Execute o script principal:

```bash
python main.py
```
## Resultados
Para cada comparação, o script exibe a estatística t, o valor-p e a conclusão sobre qual configuração é superior, com base no valor-p e na estatística t-Student.

## Detalhes do Teste t-Student
O teste t-Student é utilizado para determinar se existe uma diferença estatisticamente significativa entre duas amostras.

Valor-p < 0,05: Indica que há uma diferença significativa. A configuração com a maior estatística t é considerada melhor.
Valor-p ≥ 0,05: Não há evidências suficientes para afirmar que existe uma diferença significativa entre as configurações.
