# Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados. 
# Teste a sua função com uma série de valores de r.
# Dica: descubra a circunferência do círculo e certifique-se de que length * n = circumference.
import turtle
from Q6 import polygon
def circle(t, r):
    comprimento = 2 * 3,14 * r
    n = 70
    length = comprimento / n
    polygon(t, n, length)

circulo = turtle.Turtle
turtle.mainloop()