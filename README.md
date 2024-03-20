<h1>**Patrones implementados**</h1>

***Factory Method:***
Creación de métodos de fabricación en juego.
```
Crea en la clase Game el siguiente método: fabricarLaberinto2Habitaciones
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
Una vez me da este metodo los siguientes es modificarlos, los métodos más fáciles como frabricarBomba, fabricarPuerta... los hago a mano ya que no cuestan nada.
También hemos hecho este patrón en Builder con lo siguiente:
```
Crea un método que pasado unNum y unCont haga lo siguiente: | arm pt|
	arm:=Armario new num:unNum.
	arm agregarOrientacion: self fabricarNorte; agregarOrientacion: Este default; 			agregarOrientacion: Sur default; agregarOrientacion: Oeste default.
	
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
Algunos métodos como fabricarBichoAgresivo, fabricarBichoPerezoso, fabricarEste, fabricarOeste, entre otros es copiarlos de Game o bine hacer algún cambio simple.
***Decorator:***
Añade responsabilidad de forma transparente(funciones).
Para este patrón se ha creado las clases ParedBomba y JuegoBombas
```
Crea la clase BomberWall que hereda de Wall, BomberWall tiene que tener un metodo que se llame entrar en el cual comprueba que sea una bomba y este activa y en el caso de que sea cierto le muestra un mensaje "¡Boom! Te has chocado con una pared-bomba", en el caso de que no sea alguna de esas cosas se llamara a entrar de Wall.
Crea la clase BomberGame la cual hereda de Game y que tenga el método create_wall el cual devuelve una instancia de BomberWall.
```
***Strategy:***
Encapsula los diferentes algoritmos para poder cambiarlos en tiempo de ejecución.En nuestro caso permite cambiar el modo de bicho en tiempo de ejecución.
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
Estructuras estáticas del modo todo-parte. Permite que se utilizan tanto los objetos individuales como los objetos compuestos.
Para este patrón se han creado Contenedor y Hoja que heredan de ElementoMapa.
```
Crea la clase Contenedor que hereda de MapElement, esta clase tiene los siguinetes atributos: hijos, orientaciones, este, oeste, norte y sur.
Crea la clase Hoja que hereda de MapElement.
```
***Iterator:***
Estructuras que permiten la recursión o jerarquías.
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
Este define el esqueleto de operaciones. En este caso creamos el método actua en Modo para que los tipos de modo creen a su gusto el método.
```
Crea un método llamado actua pasado un Bicho que llame a los métodos dormir,caminar y atacar.
```
***Abstract Factory:***
No lo hemos implementado.<br><br>
***Singleton:***
Hace que solo tengamos una sola instancia a la vez, como punto de acceso a esta.
Creamos Orientacion el cual también podría ser el patrón Strategy.
```
Crea una clase llamada Orientacion.
Crea la clase Este, Oeste, Norte y Sur que heredan de Orientación.
```
***Builder:***
Se crea para crear diferentes representaciones. En nuestro caso hemos creado un nuevo fichero llamado Builder en el cual hemos añadido lo siguiente.
```
Crea una clase llamada LaberintoBuilder que tenga dos atributos: juego y laberinto.
Crea una clase llamada Builder que tenga dos atributos: builder y diccionario.
```
***Proxy:***
Proporciona un sustituto a una referencia a otro objeto para controlar el acceso a este.
Hemos implementado el proxy virtual el cual carga un objeto caro bajo demanda.
Para ello creamos una clase llamada Tunel.
```
Crea una clase llamada Tunel que hereda de Hoja y que tiene como atributo laberinto.
```
***Adapter:***
```

```
