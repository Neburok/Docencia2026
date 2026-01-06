from manim import *
from base_scene import BaseVectorScene

class VideoRepresentacion3D(ThreeDScene):
    """Video 2: Representación de Vectores en 3D"""
    
    def construct(self):
        # Configuración
        self.camera.background_color = BLACK
        self.colors = {
            'vector_1': '#00FFFF',
            'vector_2': '#FF00FF',
            'vector_3': '#FFFF00',
            'vector_result': '#00FF00',
            'axes': '#666666',
            'text': '#FFFFFF',
            'highlight': '#FF6B6B'
        }
        
        # Título
        title = Tex(r"Representación de Vectores en $3D$", 
                   font_size=60, color=self.colors['text'])
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Crear ejes 3D
        axes = ThreeDAxes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            z_range=(-5, 5, 1),
            axis_config={'color': self.colors['axes']}
        )
        self.add(axes)
        self.wait()
        
        # Configurar cámara
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()
        
        # Crear vector 3D
        vector = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 3, 1]),
            color=self.colors['vector_1'],
            resolution=8,
            thickness=0.04
        )
        self.play(Create(vector))
        self.wait()
        
        # Mostrar notación
        notacion = MathTex(
            r"\vec{v} = \langle 2, 3, 1 \rangle",
            font_size=56,
            color=self.colors['text']
        )
        notacion.to_edge(DOWN)
        self.play(Write(notacion))
        self.wait()
        
        # Explicación
        explicacion = Text(
            "Coordenadas: x, y, z",
            font_size=36,
            color=self.colors['text']
        )
        explicacion.next_to(notacion, UP)
        self.play(FadeIn(explicacion))
        self.wait(3)
        
        # Limpiar
        self.stop_ambient_camera_rotation()
        self.play(
            FadeOut(explicacion),
            FadeOut(notacion),
            FadeOut(vector),
            FadeOut(axes),
            FadeOut(title)
        )
        self.wait()