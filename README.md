<h1>Proyecto de Diseño Software</h1>
<h2>Introducción:</h2>

<p>Creación de un juego laberinto mediantes SmallTalk pasado a Python con la ayuda de Copilot.</p>
<p>En este proyecto se intentará implementar todos los patrones de diseño que hemos implementado en clase, dejando aqui una breve explicación y descripcion que le hemos dado al Copilot para la implementación de cada uno de los patrones de diseño, así como su representación en el diagrama UML que hemos estado actualizando.</p>
<h2>Diagrama al completo</h2>

![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/6ec1f38f-1547-4dfa-9610-69769e7fa6ae)

<br>
<h2>Patrones implementados</h2>

***Factory Method:***
Creación de métodos de fabricación en juego.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/6cac04c5-dcf7-4366-808e-caac914fbc1e)



```
Crea en la clase Juego el siguiente método: fabricarLaberinto2Habitaciones
	"fabrica un laberinto con 2 habitaciones. La hab1 tiene al sur la hab2 unidas por una puerta"
	
 |hab1 hab2 puerta |

	hab1 := Habitacion new num:1.
	hab2 := Habitacion new num:2.
	puerta := Puerta new.
	
	hab1 norte: Pared new.
	hab1 este: Pared new.
	hab1 oeste: Pared new.
	
	hab2 sur: Pared new.
	hab2 este:Pared new.
	hab2 oeste:Pared new.
	
	puerta lado1:hab1.
	puerta lado2:hab2.
	
	hab1 sur:puerta.
	hab2 norte:puerta.
	
	self laberinto: Laberinto new.
	
	self laberinto agregarHabitacion: hab1.
	self laberinto agregarHabitacion: hab2.
 
	
```
Una vez me da este metodo los siguientes es modificarlos, los métodos más fáciles como frabricarBomba, fabricarPuerta... los hago a mano.<br>
También hemos hecho este patrón en Builder con lo siguiente:
```
Crea un método que pasado unNum y unCont haga lo siguiente: | arm pt|
	arm:=Armario new num:unNum.
	arm agregarOrientacion: self fabricarNorte; agregarOrientacion: Este default;
	agregarOrientacion: Sur default; agregarOrientacion: Oeste default.
	arm orientaciones do:[:each | arm ponerEn:each elemento:self fabricarPared].
	pt:=self fabricarPuertaLado1: arm lado2:unCont.
	arm ponerEn: Este default elemento: pt.
	
	unCont agregarHijo:arm.
	^arm
Crea un método que pasado un strModo y unaHab haga lo siguiente:
	|hab|
	hab:=self juego obtenerHabitacion: unaHab.
	"ojo la habitacion puede no existir"
	strModo='Agresivo' ifTrue:[self fabricarBichoAgresivo: hab].
	strModo='Perezoso' ifTrue:[self fabricarBichoPerezoso: hab].

```
Algunos métodos como fabricarBichoAgresivo, fabricarBichoPerezoso, fabricarEste, fabricarOeste, entre otros es copiarlos de Game o bine hacer algún cambio simple.<br><br>
***Decorator:***
Añade responsabilidad de forma transparente(funciones).<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/4a77460f-4a5b-4a61-b502-1e1889d70947)

<br>
Para este patrón se ha creado las clases ParedBomba y JuegoBombas

```
Crea la clase ParedBomba que hereda de Pared, ParedBomba tiene que tener un metodo que se llame entrar en el cual comprueba que sea una bomba y este activa y en el caso de que sea cierto le muestra un mensaje "¡Boom! Te has chocado con una pared-bomba", en el caso de que no sea alguna de esas cosas se llamara a entrar de Pared.
Crea la clase JuegoBombas la cual hereda de Juego y que tenga el método crearPared el cual devuelve una instancia de ParedBomba.
```

***Strategy:***
Encapsula los diferentes algoritmos para poder cambiarlos en tiempo de ejecución.En nuestro caso permite cambiar el modo de bicho en tiempo de ejecución.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/5917a49f-3be7-4bd8-b9bc-63709c78d22f)
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/20a65a91-9be4-4fc1-99e8-802cf41d3d53)

<br>
Para la creación de este patrón es necesario la creación de modo y de tipos de modo, en este caso hemos hecho Agresivo y Perezoso.

```
Crea la clase Modo y crea estos metodos:
El método actua el cual se le pasa Bicho, llama al metodo dormir al cual le pasamos Bicho y caminar que también le pasamos Bicho.
El método dormir el cual le pasamos unBicho el cual escribe por pantalla que tipo es y que "duerme".
El método caminar que también se le pasa unBicho y le mandamos a este bicho caminaraleatorio.

Crea la clase Agresivo que hereda de Modo que tenga un printOn de "Agresivo".
Crea la clase Perezoso que herede de Modo que tenga un printOn de "Perezoso".
```
***Composite:***
Estructuras estáticas del modo todo-parte. Permite que se utilizan tanto los objetos individuales como los objetos compuestos.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/2fed6927-c63f-4595-9253-d542800f661f)


<br>
Para este patrón se han creado Contenedor y Hoja que heredan de ElementoMapa.

```
Crea la clase Contenedor que hereda de MapElement, esta clase tiene los siguinetes atributos: hijos, orientaciones, este, oeste, norte y sur.
Crea la clase Hoja que hereda de MapElement.
```
***Iterator:***
Estructuras que permiten la recursión o jerarquías.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/07e51382-7d84-4fdd-98bc-a017b7cdf977)

<br>
Creación del método recorrer en ElementoMapa que sera implementado por las subclases. 

```
En MapElement:
def recorrer(self,unBloque):
	pass
Ahora ha de ser implementado por la subclases de MapElement.
Contenedor:
Crea un metodo que pasado unBloque le ponemos el valor self en unBloque y luego recorremos hijos que cada uno de estos utilicen el metodo recorrer(unBloque).
Hoja, Pared y Puerta:
def recorrer(unBloque):
	unBloque(self)
```

***Template Method:***
Este define el esqueleto de operaciones. En este caso creamos el método actua en Modo para que los tipos de modo creen a su gusto el método.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/fbf7502c-1660-4903-8058-01d7572394e2)


```
Crea un método llamado actua pasado un Bicho que llame a los métodos dormir,caminar y atacar.
```
***Abstract Factory:***
Crea una interfaz para crear familias de objetos similares.<br>
No lo hemos implementado.<br><br>
***Singleton:***
Hace que solo tengamos una sola instancia a la vez, como punto de acceso a esta.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/0e20e04f-55c2-4245-beaa-33980392aa08)

<br>
Creamos Orientacion el cual también podría ser el patrón Strategy.

```
Crea una clase llamada Orientacion.
Crea la clase Este, Oeste, Norte y Sur que heredan de Orientación.
```

***Builder:***
Se crea para crear diferentes representaciones. <br>
En nuestro caso hemos creado un nuevo fichero llamado Builder en el cual hemos añadido lo siguiente.
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/ea03d79b-0ce6-4a17-a285-d0d744e231c0)

```
Crea una clase llamada LaberintoBuilder que tenga dos atributos: juego y laberinto.
Crea una clase llamada Builder que tenga dos atributos: builder y diccionario.
```
***Proxy:***
Proporciona un sustituto a una referencia a otro objeto para controlar el acceso a este.<br><br>

![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/2be55876-68c4-483a-bf3c-b4ac7857eecb)

<br>Hemos implementado el proxy virtual el cual carga un objeto caro bajo demanda.<br>
Para ello creamos una clase llamada Tunel.
```
Crea una clase llamada Tunel que hereda de Hoja y que tiene como atributo laberinto.
```
***Adapter:***
Hace de intermediario entre clases(intefaces) que son incompatibles.<br>
No se ha implementado.<br><br>


***Bridge:***
Es un puente entre una abstracción y su implementación. Permite cambiar de un tipo a otro en tiempo de ejecución.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/cab752ec-4fb1-4ae8-9070-7c1ade35b5a4)

<br>Creamos una nueva clase, Forma la cual hace de intermediario entre Contenedor y el tipo de forma que por el momento solo hemos indicado que es de tipo Cuadrado.
```
Crea la clase Forma con el patron de diseño Bridge entre Contenedor y Cuadrado, siendo este ultimo heredado de Forma.
Añade un nuevo atributo a Contenedor que se llame forma.

```
***Mediator:***
Permite semplificar la comunicación entre objetos.<br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/184e39fe-250a-4221-a99d-8b285fa47e12)
<br>
```

```

***State:***
Permite que un objeto cambie su comportamiento cuando su estado interno cambia, encapsulando cada estado en una clase separada y permitiendo que el objeto delegue su comportamiento a si estado actual.
<br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/5d9632ea-cf9c-411c-b424-7d1eab2f297a)

```

```
