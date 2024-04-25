**rgb_to_grayscale**<br>
Se encarga de llevar una imagen de RGB a escala de grises.<br>
Esto lo hace mediante multplicar un valor constante a cada canal.<br>
Después se juntan los 3 canales y regresa el array para la escala en grises<br>
**div_color**<br>
Divide la matriz original en 3, una para cada canal RGB.<br>
**grayscale_to_rgb**<br>
Creamos un canal para cada color, se especifica que tengan el mismo tamaño que el de escala de grises.<br>
Con el algoritmo del inciso e, si el valor de la posición en escala de grises es menor a el establecido como central de recoloración entonces multiplica para cada canal el valor de la posición en escala de grises por el color propuesto en cada canal y después divide entre el valor central de recoloración<br>
Caso contrario si es mayor multiplica los resultado de restar 255 menos el valor para cada canal por la resta entre el valor en escala de grises menos el valor central de recoloración. Después le suma el valor asignado a cada color y lo divide sobre el valor central de recoloración.