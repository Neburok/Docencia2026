from manim import *
from base_scene import BaseVectorScene

class VideoRepresentacion2D(BaseVectorScene):
    """Video 1: Representación de Vectores en 2D"""
    
    def construct(self):
        super().construct()
        
        # Título
        title = self.create_title(r"Representación de Vectores en $2D$")
        self.play(Write(title))
        self.wait()
        
        # Crear ejes
        axes = self.create_2d_axes()
        self.play(Create(axes))
        self.wait()
        
        # Mostrar notación matemática
        notacion = MathTex(
            r"\vec{v} = \langle 4, 1 \rangle",
            font_size=56,
            color=self.colors['text']
        )
        notacion.to_edge(DOWN, buff=1)
        self.play(Write(notacion))
        self.wait()

        # Definir vector
        vector_coords = [4, 1]
        
        # Crear vector v = (3, 2)
        vector = self.create_vector_2d(vector_coords, self.colors['vector_1'])
        
        # Animar aparición del vector
        self.play(GrowArrow(vector))
        self.wait()
        
        # Añadir explicación
        explicacion = Text(
            "Un vector tiene: magnitud y dirección",
            font_size=36,
            color=self.colors['text']
        )
        explicacion.next_to(notacion, UP)
        self.play(FadeIn(explicacion))
        self.wait(5)
        
        # Mostrar componentes
        componente_x = MathTex(r"x = 3", font_size=40, color=self.colors['vector_1'])
        componente_y = MathTex(r"y = 2", font_size=40, color=self.colors['vector_1'])
        
        componente_x.move_to(LEFT * 3 + UP * 2)
        componente_y.move_to(LEFT * 3 + UP * 1)
        
        self.play(Write(componente_x), Write(componente_y))
        self.wait(5)
        
        # Limpiar y finalizar
        self.play(
            FadeOut(componente_x),
            FadeOut(componente_y),
            FadeOut(explicacion),
            FadeOut(notacion),
            FadeOut(vector),
            FadeOut(axes),
            FadeOut(title)
        )
        self.wait()