# Vulcano

## Descripcion

En una galaxia lejana, existen tres civilizaciones. Vulcanos, Ferengis y Betasoides.
Cada civilización vive en paz en su respectivo planeta.
Dominan la predicción del clima mediante un complejo sistema informático.

### Planetas

* El planeta Ferengi se desplaza con una velocidad angular de 1 grados/día en sentido horario. Su distancia con respecto al sol es de 500Km.
* El planeta Betasoide se desplaza con una velocidad angular de 3 grados/día en sentido horario. Su distancia con respecto al sol es de 2000Km.
* El planeta Vulcano se desplaza con una velocidad angular de 5 grados/día en sentido anti­horario, su distancia con respecto al sol es de 1000Km.
* Todas las órbitas son circulares.

### Clima

* Cuando los tres planetas están alineados entre sí y a su vez alineados con respecto al sol, el sistema solar experimenta un período de sequía.
* Cuando los tres planetas no están alineados, forman entre sí un triángulo. Es sabido que en el momento en el que el sol se encuentra dentro del triángulo, el sistema solar experimenta un período de lluvia, teniendo éste, un pico de intensidad cuando el perímetro del triángulo está en su máximo.
* Las condiciones óptimas de presión y temperatura se dan cuando los tres planetas están alineados entre sí pero no están alineados con el sol.


## Aplicación

Se utilizó  [Web2py](http://web2py.com) como framework de desarrollo ágil para la generación de la app web

## Código

Lenguaje *Python 3.7*

En *modules* se encuentra el código fuente principal que puede ser ejecutado fuera del framework 

En *modules/pruebas/grafica.py* se puede ejecutar una simulación de los tres planetas en movimiento con la info del clima para cada día (se necesita tener instalado matplotlib) 

En *modules/pruebas/pronostico.py* se puede ejecutar una simulación que simplemente devuelve la estadistica de la cantidad de periodos por clima y el día de máxima lluvia 

En *models/db.py* se encuentra la definicion de las tablas

En *models/scheduler.py* se encuentra la tarea programada task_cargar_clima que se corre todos los dias para generar el pronóstico si pasaron los 10 años desde el último generado


## Despliegue

Se realizó el despliegue sobre el host gratuito [PythonAnywhere](www.pythonanywhere.com)

Para visitar el sitio
http://casalromina.pythonanywhere.com/vulcano

Para consultar el clima para x día 
http://casalromina.pythonanywhere.com/vulcano/api/clima?dia=255
