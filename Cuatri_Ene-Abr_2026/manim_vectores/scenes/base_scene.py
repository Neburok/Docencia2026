from manim import *

class BaseVectorScene(Scene):
    """Clase base para todas las escenas de vectores"""
    
    def setup(self):
        """Configuración inicial común a todas las escenas"""
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
    
    def create_2d_axes(self, x_range=(-5, 5), y_range=(-5, 5)):
        """Crear sistema de coordenadas 2D"""
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            axis_config={
                'color': self.colors['axes'],
                'stroke_width': 2,
            }
        )
        return axes
    
    def create_3d_axes(self):
        """Crear sistema de coordenadas 3D"""
        axes = ThreeDAxes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            z_range=(-5, 5, 1),
            axis_config={'color': self.colors['axes']}
        )
        return axes
    
    def create_vector_2d(self, coords, color=None, label=None):
        """Crear un vector 2D con etiqueta opcional"""
        if color is None:
            color = self.colors['vector_1']
        
        vector = Vector(
            coords,
            color=color,
            stroke_width=4
        )
        
        if label:
            coord_label = vector.coordinate_label(
                integer_labels=True,
                n_dim=2,
                color=self.colors['text']
            )
            return VGroup(vector, coord_label)
        
        return vector
    
    def create_title(self, text):
        """Crear título animado"""
        title = Tex(text, font_size=60, color=self.colors['text'])
        title.to_edge(UP)
        return title
    
    def add_formula(self, formula):
        """Añadir fórmula matemática"""
        math_formula = MathTex(formula, font_size=48, color=self.colors['text'])
        math_formula.to_edge(DOWN)
        return math_formula