from particulas import particulas
from manim import *
import numpy as np

class Particulas(Scene):
    def construct(self):
        p_1 = particulas(masa=2.0 , x_i=0.0, y_i=3.8, v=0, alpha=1.5*np.pi, a=9.8, beta=1.5*np.pi, r=0.2)
       # p_2 = particulas(3.0, 1.0, 1.0, 1.0, 0.0, 0.3)

        listaP = [p_1]
        grupoP = VGroup()

        for p in listaP:
            dibujo = Dot(point=[p.x_i, p.y_i, 0], radius=p.r, color=RED)
            def actualizar(particula):
                def movimiento(mob, dt):
                    V_i = np.array([particula.V[0], particula.V[1], 0.0])
                    A_i = np.array([particula.A[0], particula.A[1], 0.0])
                    V_i1 = V_i + A_i * dt
                    particula.V = V_i1
                    mob.shift(V_i1 * dt)
                return movimiento
            dibujo.add_updater(actualizar(p))
            grupoP.add(dibujo)
        grupoP.scale(0.3)
        self.add(grupoP)
        self.wait(10) 
