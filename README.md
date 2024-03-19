**Patrones implementados**

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

***Decorator:***
Para este patrón se ha creado las clases ParedBomba y JuegoBombas
```
Crea la clase BomberWall que hereda de Wall, BomberWall tiene que tener un metodo que se llame entrar en el cual comprueba que sea una bomba y este activa y en el caso de que sea cierto le muestra un mensaje "¡Boom! Te has chocado con una pared-bomba", en el caso de que no sea alguna de esas cosas se llamara a entrar de Wall.
Crea la clase BomberGame la cual hereda de Game y que tenga el método create_wall el cual devuelve una instancia de BomberWall.
```
***Strategy:***
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
Para este patrón se han creado Contenedor y Hoja que heredan de ElementoMapa.
```
Crea la clase Contenedor que hereda de MapElement, esta clase tiene los siguinetes atributos: hijos, orientaciones, este, oeste, norte y sur.
Crea la clase Hoja que hereda de MapElement.
```
***Iterator:***
Creación del método recorrer en ElementoMapa
```

```
***Template Method:***
Este define el esqueleto de operaciones. En este caso creamos el método actua en Modo para que los tipos de modo creen a su gusto el método.
```

```
***Abstract Factory:***
```

```
***Singleton:***
```

```
***Proxy:***
```

```
