# Faz as importações necessarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

# Cria um DataFrame
gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df.head(10)

# Transforma o DataFrame em um grafico de linhas e salva em uma imagem .png
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data = gasolina_df, x = 'dia', y = 'venda',)
  grafico.set(title = 'Preço médio da gasolina em SP', xlabel = 'Dia', ylabel = 'Preço')
  grafico.legend(['Preço da gasolina'])
  plt.savefig('gasolina.png')