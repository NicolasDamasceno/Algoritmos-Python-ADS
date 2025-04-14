# Fazendo um quadrado com o turltes
import turtle

quadrado = turtle.Turtle()

# Criando o primeiro lado
quadrado.fd(100)
# Criando o primeito vertice
quadrado.lt(90)
# Agora repetiremos o mesmo processo para criar os demais lados
quadrado.fd(100)
quadrado.lt(90)
quadrado.fd(100)
quadrado.lt(90)
quadrado.fd(100)

turtle.mainloop()