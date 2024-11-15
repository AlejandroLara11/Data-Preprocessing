import matplotlib.pyplot as plt

#SIMPLE LINE

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]

plt.plot(x,y)  #LINE
plt.scatter(x,y)  #POINTS
plt.xlabel("EJE X")
plt.ylabel("EJE Y")
plt.title("My first graphic")
plt.show()


#BAR GRAPHIC
#We need the labels or categories
categorias = ["A", "B", "C", "D"]
valores = [5, 10, 15, 10]
plt.bar(categorias,valores)
plt.title("Bar Graphic")
plt.xlabel("Categoria")
plt.ylabel("Valor")
plt.show()

x = [0,1,2,3,4,5]
y = [0,1,4,9,16,25]
plt.plot(x, y, color = "red", linestyle="--", marker = "o")
plt.grid("True")
plt.show()