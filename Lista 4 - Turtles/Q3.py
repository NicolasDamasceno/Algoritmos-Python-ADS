# Agora para evitar repetições do código, usaremos um laço de repetição para reduzir e otimizar o código

import turtle
quadrado = turtle.Turtle()

# Laço de repetição que irá repetir o código 4 vezes para criar o quadrado
for i in range(4):
    quadrado.fd(100)
    quadrado.lt(90)

turtle.mainloop()