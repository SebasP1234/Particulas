from particulas import particulas
from manim import *
import numpy as np
import random

class SimulacionNParticulas(Scene):
    def construct(self):
        N = 3
        listaP = []
        grupoP = VGroup()

        for _ in range(N):
            x = random.uniform(-5, 5)
            y = random.uniform(0, 3)
            radio = random.uniform(0.15, 0.4)
            masa = radio * 10 
            
            p = particulas(masa=masa, x_i=x, y_i=y, v=0.0, alpha=0.0, a=9.8, beta=1.5*np.pi, r=radio)
            p.V[0] = random.uniform(-3, 3)
            p.V[1] = random.uniform(-3, 3)    
            color = random.choice([RED, BLUE, YELLOW, GREEN, ORANGE, PURPLE])
            dibujo = Dot(point=[p.x_i, p.y_i, 0], radius=p.r, color=color)
            
            listaP.append(p)
            grupoP.add(dibujo)

        piso_y = -3.5
        pared_izq_x = -6.5
        pared_der_x = 6.5
        
        caja = VGroup(
            Line([-7, piso_y, 0], [7, piso_y, 0], color=WHITE),
            Line([pared_izq_x, -4, 0], [pared_izq_x, 4, 0], color=WHITE),
            Line([pared_der_x, -4, 0], [pared_der_x, 4, 0], color=WHITE)
        )
        self.add(caja, grupoP)

        def movimiento(grupo, dt):
            for i in range(N):
                p = listaP[i]
                dibujo = grupo[i]
                
                V_i = np.array([p.V[0], p.V[1], 0.0])
                A_i = np.array([p.A[0], p.A[1], 0.0])
                
                V_nueva = V_i + A_i * dt
                
                pos_y = dibujo.get_center()[1]
                if (pos_y - p.r) - piso_y <= 0.1:
                    V_nueva[1] = -V_nueva[1]
                
                pos_x = dibujo.get_center()[0]
                if (pos_x - p.r) - pared_izq_x <= 0.1:
                    V_nueva[0] = -V_nueva[0]
                    
                if (pos_x + p.r) - pared_der_x >= 0.1:
                    V_nueva[0] = -V_nueva[0]
                p.V = V_nueva
                dibujo.shift(V_nueva * dt)
            for i in range(N):
                for j in range(i + 1, N):
                    p1 = listaP[i]
                    p2 = listaP[j]
                    d1 = grupo[i]
                    d2 = grupo[j]
                    
                    pos1 = d1.get_center()
                    pos2 = d2.get_center()
                    
                    dist_vec = pos2 - pos1
                    distancia = np.linalg.norm(dist_vec)
                    suma_radios = p1.r + p2.r
                    
                    if distancia < suma_radios:
                        normal = dist_vec / distancia
                        
                        v1 = np.array([p1.V[0], p1.V[1], 0.0])
                        v2 = np.array([p2.V[0], p2.V[1], 0.0])
                        
                        v_relativa = v1 - v2
                        v_n = np.dot(v_relativa, normal)
                        
                        if v_n > 0:
                            restitucion = 1
                            impulso = (-(1 + restitucion) * v_n) / ((1 / p1.masa) + (1 / p2.masa))
                            
                            v1_final = v1 + (impulso / p1.masa) * normal
                            v2_final = v2 - (impulso / p2.masa) * normal
                            
                            p1.V[0], p1.V[1] = v1_final[0], v1_final[1]
                            p2.V[0], p2.V[1] = v2_final[0], v2_final[1]
                            
                        hundimiento = suma_radios - distancia
                        masa_total = p1.masa + p2.masa
                        
                        d1.shift(- (p2.masa / masa_total) * hundimiento * normal)
                        d2.shift(  (p1.masa / masa_total) * hundimiento * normal)
        grupoP.scale(0.3)
        grupoP.add_updater(movimiento)
        self.wait(15)
