import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/User/.spyder-py3/ecommerce_estatistica.csv')
print(df.head().to_string)

# Histograma

plt.figure(figsize=(10, 6))
plt.hist(df['Qtd_Vendidos_Cod'], bins=50, color='green', alpha=0.8)
plt.title('Valores e Quantidade Vendidos')
plt.xlabel('Quantidade de Vendas')
plt.xticks(ticks=range(0, int(df['Qtd_Vendidos_Cod'].max())+2000, 5000))
plt.ylabel('Valor')
plt.grid(True)
plt.show()


# Grafico de Dispersão 

plt.scatter(df['Qtd_Vendidos_Cod'], df['Preço'], color='green', alpha=0.8, s=30)
plt.title('Dispersão - Valores e Vendas ')
plt.xlabel('Quantidade de Vendas')
plt.ylabel('Preço')
plt.xticks(ticks=range(0, int(df['Qtd_Vendidos_Cod'].max())+2000, 5000))
plt.show()

# Gráfico de Calor
corr = df[['N_Avaliações', 'Preço']].corr()
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação - Avaliações e Valor')
plt.tight_layout()
plt.show()

# Gráfico de Barra
plt.figure(figsize=(10, 6))
df['Qtd_Vendidos'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Numero de Vendas e Preço')
plt.xlabel('Vendas')
plt.ylabel('Preço')
plt.xticks(rotation=0)
plt.show()

# Grafico de Pizza
x = df['Qtd_Vendidos_Cod'].value_counts().index
y = df['Qtd_Vendidos_Cod'].value_counts().values


plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribução de Quantidade de Vendas')
plt.show()

# Grafico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade de Vendas')
plt.xlabel('Valores dos Itens')
plt.show()

# Grafico de Regressão
sns.regplot(x='Qtd_Vendidos_Cod', y='Preço', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Vendas e Valores')
plt.xlabel('Vendas')
plt.ylabel('Valores')
plt.show()
