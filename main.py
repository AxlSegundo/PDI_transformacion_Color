from PIL import Image
import numpy as np
from division_transformacion import rgb_to_grayscale, div_color,grayscale_to_rgb


Imagen_original = Image.open("img/Flores_original.jpg")
array_original = np.array(Imagen_original)
red_channel,green_channel,blue_channel = div_color(array_original)
array_grises = rgb_to_grayscale(red_channel,green_channel,blue_channel)
imagen_gris = Image.fromarray(array_grises)
imagen_gris.save("img/Flores_grises.jpg")
imagen_color_n = array_grises
vr=int(input("Por favor introduzca el valor para el color rojo: "))
vg=int(input("Por favor introduzca el valor para el color verde: "))
vb=int(input("Por favor introduzca el valor para el color azul: "))
vcr=int(input("Por favor introduzca el valor para el central de recoloracion: "))
nuevo_RGB = grayscale_to_rgb(imagen_color_n,vr,vg,vb,vcr)
nueva_imagen = Image.fromarray(nuevo_RGB)
nueva_imagen.save("img/Flores_CN.jpg")
Imagen_original.show()
imagen_gris.show()
nueva_imagen.show()
