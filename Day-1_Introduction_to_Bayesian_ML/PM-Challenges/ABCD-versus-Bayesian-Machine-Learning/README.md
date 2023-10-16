## Mejora y generalización del método ABCD


El método ABCD es un método experimental para estimar background en una región del espacio de parámetros (usualmente la región "D") a partir de los datos en las regiones restantes ("A", "B"y "C").  Se puede leer más sobre este método en los siguientes links:

- <a href="https://particle.wiki/wiki/ABCD_method">ABCD en física de partículas, ideas principales</a>
- <a href="https://twiki.cern.ch/twiki/pub/Main/ABCDMethod/ABCDGuide_draft18Oct18.pdf?">PDF con más detalles</a>

El método es muy claro, y estima al background en la signal región de un modo muy astuto. 

Sin embargo, para ser tan claro utiliza métodos de cortes-duros y presunciones de no-señal en las background regions que no son óptimos y muchas veces no son satisfechos por la data.  Por esta razón, proponemos que un método basado en inferencia Bayesiana puede aumentar considerablemente la performance en el análisis de los datos.  Proponemos estudiar un método en el cual reemplazamos cortes duros por conocimientos a priori que permitan desentrañar la forma de la señal y el background dentro de los datos.

Analicemos un ejemplo concreto y simple para comenzar.

Supongamos un experimento que tiene 2 observables independientes, Obs1 y Obs2. O sea, el problema tiene dimensión 2.  Supongamos que en lo que uno observa hay un background y una señal, y que nosotros queremos identificar cuánto hay de señal.    Ambos observables tienen como output un número real. Para ser bien concretos, supongamos que para el background tenemos:

Obs1 ~ N(10,5)   (Una distribución normal centrada en 10 y con desviación estándar igual a 5) <br>
Obs2 ~ N(20,3)

Y para la señal tenemos:

Obs1 ~ N(15,2)<br>
Obs2 ~ N(18,1)

De este modo, podemos definir las regiones del método ABCD como

A : Obs1 < 11 & Obs2 > 20<br>
B : Obs1 > 11 & Obs2 > 20<br>
C : Obs1 < 11 & Obs2 < 20<br>
D : Obs1 > 11 & Obs2 < 22  (esta región es la única que en principio tiene señal)

Utilizando el método ABCD queda que la cantidad de señal en la región D sería:

señal(D) = D - C * B / A

Usted puede comenzar haciendo los siguientes puntos para entender mejor el problema:

- Entender el por qué del método ABCD y cuáles son sus hipótesis
- Crear data sintética y verificar que la fórmula funciona
- Modificar los parámetros y estudiar cuándo funciona mejor y cuándo peor.  Piense en plots que resuman los resultados.

Una vez ralizado esto puede plantear un modelo Bayesiano para averiguar cuánto de señal hay en total en los datos. Considere dibujar un Modelo Gráfico.   Suponiendo que comienza con priors que no son correctos, mostrar que la inferencia Bayesiana recupera buenas posteriors para las distribuciones, y además puede extraer cuánto de señal en total hay.   El trabajo también puede incluir explorar hasta qué punto y en qué situaciones la inferencia Bayesiana mejora y generaliza el método ABCD.  También sería bueno incluir escenarios en los que hay más de 2 observables independientes, ya que con el método ABCD esto no se puede encarar, mientras que con los métodos Bayesianos es natural hacerlo.


[Incluido en esta carpeta hallará una nota manuscrita (en PDF) sobre cómo mejorar y genralizar el método ABCD en el contexto de búsquedas de dos bosones de Higgs en el LHC.  Esta nota, aunque avanzada en física,  representa  es una aspecto práctico de lo que se plantea aquí.]






