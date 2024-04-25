import numpy as np
#   A cada canal lo multiplicamos por un valor constante y sumamos
#   Los valores constantes de esta funcion tienen que ver con la sensibilidad
#   del ojo humano hacia esos colores, cualquier cosa los valores estaban en las diapositivas xd
def rgb_to_grayscale(red,green,blue):
    red = red * 0.21
    green = green * 0.72
    blue = blue * 0.07
    img = red + green + blue
    return img.astype(np.uint8)
#   Divimos la matriz en los 3 canales
def div_color(original):
    red_channel = original[:, :, 0]
    green_channel = original[:, :, 1]
    blue_channel = original[:, :, 2]
    return red_channel,green_channel,blue_channel   
#   Aplicamos el algoritmo del punto e
def grayscale_to_rgb(gray_channel,vr,vg,vb,vcr):
    new_red_channel = np.zeros_like(gray_channel)
    new_green_channel = np.zeros_like(gray_channel)
    new_blue_channel = np.zeros_like(gray_channel)
    #   Trabajamos los 3 canales por separado
    for i in range(gray_channel.shape[0]):
        for j in range(gray_channel.shape[1]):    
            A = gray_channel[i,j]
            if A < vcr:
                new_red_channel[i, j] = vr * A / vcr
                new_green_channel[i, j] = vg * A / vcr
                new_blue_channel[i, j] = vb * A / vcr
            else:
                new_red_channel[i, j] = vr + (255 - vr) * (A - vcr) / vcr
                new_green_channel[i, j] = vg + (255 - vg) * (A - vcr) / vcr
                new_blue_channel[i, j] = vb + (255 - vb) * (A - vcr) / vcr
    #   Verificar que los valores esten un rango valido
    new_red_channel = np.clip(new_red_channel,0,255)
    new_green_channel = np.clip(new_green_channel,0,255)
    new_blue_channel = np.clip(new_blue_channel,0,255)
    #   Unimos los 3 canales
    rgb_image = np.stack((new_red_channel, new_green_channel, new_blue_channel), axis=-1)
    return rgb_image