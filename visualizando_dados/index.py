from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Cria um gráfico de linhas, years no eixo x, gdp no eixo y
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# Adiciona um titulo
plt.title("Nominal GDP")

# Adiciona uma label no eixo y
plt.ylabel("Billions of $")

# Mostra o gráfico
#plt.show()
# Salva o gráfico
plt.savefig('../img/cap_3_chart_gdp.png')
plt.gca().clear()