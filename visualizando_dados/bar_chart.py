from matplotlib import pyplot as plt
from collections import Counter

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.figure("char bar")
# Plote as barras com cordenadas x à esquerda [0, 1, 2, 3, 4], alturas [num_oscars]
plt.bar(range(len(movies)), num_oscars)
plt.title("My Favorites Movies")
plt.ylabel("# of Academy Awards")
plt.xlabel("Movies")

# Rotule o eixo x com os nomes dos filmes no centro das barras
plt.xticks(range(len(movies)), movies)
# plt.show()
plt.savefig("../img/cap_3_chart_movies.png")
plt.gca().clear()

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Agrupar as notas por decil, mas coloque o 100 com o noventa
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.figure("histogram")
plt.bar([x + 5 for x in histogram.keys()], histogram.values(), 10, edgecolor=(0, 0, 0))
plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
# plt.show()
plt.savefig("../img/cap_3_chart_grades.png")
plt.gca().clear()

mentions = [500, 505]
years = [2017, 2018]

plt.figure(3)
plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")
plt.ticklabel_format(useOffset=False)
plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Look at the 'Huge' Increase!")
# plt.show()
plt.savefig("../img/cap_3_chart_misleading_y_axis.png")
plt.gca().clear()

plt.figure(4)
plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")
plt.ticklabel_format(useOffset=False)
plt.axis([2016.5, 2018.5, 0, 550])
plt.title("Not So Huge Anymore")
# plt.show()
plt.savefig("../img/cap_3_chart_non_misleading_y_axis.png")
plt.gca().clear()
