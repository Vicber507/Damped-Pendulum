import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.animation import FuncAnimation

def Graph3D(x, xbar, y, ybar, z, zbar, etiqueta, color_mapa, save_path=None, video=None):
    """
    Grafica datos en 3D y permite guardar la gráfica en un archivo.

    Parámetros:
    - x: datos para el eje x.
    - xbar: etiqueta para el eje x.
    - y: datos para el eje y.
    - ybar: etiqueta para el eje y.
    - z: datos para el eje z.
    - zbar: etiqueta para el eje z y la barra de colores.
    - etiqueta: título del gráfico.
    - color_mapa: mapa de colores para los puntos.
    - save_path: ruta completa donde se guardará la gráfica (opcional, debe incluir la extensión del archivo).
    """

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Crear la gráfica 3D
    p = ax.scatter(x, y, z, c=z, cmap=color_mapa, marker='o', edgecolor=(0.5, 0.5, 0.5, 1.0), s=50, alpha=0.7)

    # Configuración de la barra de color
    color_bar = fig.colorbar(p, ax=ax, shrink=0.6, aspect=10)
    color_bar.set_label(rf'{zbar}', fontsize=12)

    # Etiquetas y títulos
    ax.set_title(rf'{etiqueta}', fontsize=15, fontweight='bold')
    ax.set_xlabel(rf'{xbar}', fontsize=12, labelpad=10)
    ax.set_ylabel(rf'{ybar}', fontsize=12, labelpad=10)
    ax.set_zlabel(rf'{zbar}', fontsize=12, labelpad=10)

    # Estilo de la gráfica
    ax.xaxis.pane.set_edgecolor('gray')
    ax.yaxis.pane.set_edgecolor('gray')
    ax.zaxis.pane.set_edgecolor('gray')
    ax.xaxis.pane.set_alpha(0.1)
    ax.yaxis.pane.set_alpha(0.1)
    ax.zaxis.pane.set_alpha(0.1)
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.3)

    # Establecer la vista inicial
    initial_elev = 25
    initial_azim = 135
    ax.view_init(elev=initial_elev, azim=initial_azim)

    # Función para actualizar la vista durante la animación
    def update(frame):
        ax.view_init(elev=30, azim=frame)
        return ax,

    # Guardar la imagen si se proporciona una ruta
    if save_path:
        plt.savefig(save_path, format=save_path.split('.')[-1], dpi=300, bbox_inches='tight')
        print(f"Gráfica 3D guardada en: {save_path}")

    
    plt.show()

    
    if video:
        ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50, blit=False)
        ani.save(video, writer='ffmpeg', dpi=300)
        print(f"Video guardado en: {video}")

        

    
     


    
   

def Graph2D(x, xbar, y, ybar, etiqueta, color_mapa, save_path=None,  video=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    
    p = ax.scatter(x, y, c=y, cmap=color_mapa, marker='o', edgecolor=(0.5, 0.5, 0.5, 1.0), s=50, alpha=0.7)

    
    color_bar = fig.colorbar(p, ax=ax, shrink=0.6, aspect=10)
    color_bar.set_label(rf'{ybar}', fontsize=12)
    
    
    ax.set_title(rf'{etiqueta}', fontsize=15, fontweight='bold')
    ax.set_xlabel(rf'{xbar}', fontsize=12, labelpad=10)
    ax.set_ylabel(rf'{ybar}', fontsize=12, labelpad=10)
    
    
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_color('gray')
    
        
    if save_path:
        plt.savefig(save_path, format=save_path.split('.')[-1], dpi=300, bbox_inches='tight')
        print(f"Gráfica 3D guardada en: {save_path}")
        
    
    plt.show()
    
def ajuste(x_data, y_data, modelo_func, x_label, y_label, etiqueta, modelo_latex, color_mapa='viridis', p0=None, save_path=None):
    """
    Realiza el ajuste de una función modelo a datos experimentales, los grafica en 2D y permite guardar la gráfica.

    Parámetros:
    - x_data: array de datos para el eje x.
    - y_data: array de datos para el eje y.
    - modelo_func: función modelo para el ajuste.
    - x_label: etiqueta para el eje x.
    - y_label: etiqueta para el eje y.
    - etiqueta: título del gráfico.
    - modelo_latex: representación en LaTeX de la función modelo.
    - color_mapa: mapa de colores para los puntos experimentales.
    - p0: lista de valores iniciales para el ajuste (opcional).
    - save_path: ruta completa donde se guardará la gráfica (opcional, debe incluir la extensión del archivo).
    """
    
    
    popt, pcov = curve_fit(modelo_func, x_data, y_data, p0=p0, maxfev=10000)
    
    
    x_fit = np.linspace(min(x_data), max(x_data), 500)
    y_fit = modelo_func(x_fit, *popt)

    modelo_str = rf'{modelo_latex}'
    
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    
    sc = ax.scatter(x_data, y_data, c=y_data, cmap=color_mapa, marker='o', edgecolor=(0.5, 0.5, 0.5, 1.0), s=50, alpha=0.7, label='Datos experimentales')
    
    
    ax.plot(x_fit, y_fit, color='blue', linewidth=0.8, linestyle='--', alpha=0.9, label=modelo_str)
    
    
    ax.set_title(etiqueta, fontsize=15, fontweight='bold')
    ax.set_xlabel(x_label, fontsize=12, labelpad=10)
    ax.set_ylabel(y_label, fontsize=12, labelpad=10)
    
    
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_color('gray')

    
    ax.legend(loc='best')
    
    
    if save_path:
        plt.savefig(save_path, format=save_path.split('.')[-1], dpi=300, bbox_inches='tight')
        print(f"Gráfica guardada en: {save_path}")
    
    
    plt.show()
    
    
    print("Parámetros ajustados:")
    for i, param in enumerate(popt):
        print(f"Parámetro {i+1}: {param:.3f}")

    return popt