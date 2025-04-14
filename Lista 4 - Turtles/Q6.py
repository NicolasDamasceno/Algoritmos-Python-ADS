# Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados.
# Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.
import turtle
def polygon(t, length, n):
    angulo = (360/n)
    for i in range(n):
        t.fd(length)
        t.lt(angulo)

quadrado = turtle.Turtle()
polygon(quadrado, 50 , 6)
turtle.mainloop()