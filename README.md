<h1>Proyecto de Diseño Software</h1>
<h2>Introducción:</h2>

<p>Creación de un juego laberinto mediantes SmallTalk pasado a Python con la ayuda de Copilot.</p>
<p>En este proyecto se intentará implementar todos los patrones de diseño que hemos implementado en clase, dejando aqui una breve explicación y descripcion que le hemos dado al Copilot para la implementación de cada uno de los patrones de diseño, así como su representación en el diagrama UML que hemos estado actualizando.</p>
<h2>Diagrama al completo</h2>

![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/2ef3f1d8-72cd-4f3f-a5b8-001652b0b738)


<br>
<h2>Patrones</h2>

***Factory Method:***
Creación de métodos de fabricación en juego.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/6cac04c5-dcf7-4366-808e-caac914fbc1e)



```
Crea en la clase Juego que utilizando el patron factory method cree el método fabricarLaberinto2Habitaciones en el cual fabricamos un laberinto con 2 habitaciones. La hab1 tiene al sur la hab2 unidas por una puerta, y que luego se añadan al laberinto.
```
Una vez me da este metodo los siguientes es modificarlos, los métodos más fáciles como frabricarBomba, fabricarPuerta... los hago a mano.<br>
También hemos hecho este patrón en Builder con lo siguiente:
```
Crea un método que pasado unNum y unCont cree un Armario y agregue las orientaciones correspondientes y la respectiva puerta entre el armario y la variable de entrada unCont y esta luego deberá de agregar la variable de armario que hemos creado y la devolvera.
Crea un método que pasado un strModo y unaHab obtenga una habitacion pasandole la variable unaHab y luego compruebe que strModo sea o bien Agresivo o bien Perezono, en cada caso se fabricaraBichoAgresivo o Perezoso con la habitación antes creada.

```
Algunos métodos como fabricarBichoAgresivo, fabricarBichoPerezoso, fabricarEste, fabricarOeste, entre otros es copiarlos de Game o bine hacer algún cambio simple.<br><br>
***Decorator:***
Añade responsabilidad de forma transparente(funciones).<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/7f98c4a2-739d-4d7d-84d3-c2f9ac45f325)

<br>
Para este patrón se ha creado las clases ParedBomba y JuegoBombas

```
Crea la clase ParedBomba que hereda de Pared, ParedBomba tiene que tener un metodo que se llame entrar en el cual comprueba que sea una bomba y este activa y en el caso de que sea cierto le muestra un mensaje "¡Boom! Te has chocado con una pared-bomba", en el caso de que no sea alguna de esas cosas se llamara a entrar de Pared.
Crea la clase JuegoBombas la cual hereda de Juego y que tenga el método crearPared el cual devuelve una instancia de ParedBomba.
```

***Strategy:***
Encapsula los diferentes algoritmos para poder cambiarlos en tiempo de ejecución.En nuestro caso permite cambiar el modo de bicho en tiempo de ejecución.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/84b88965-d2f5-4789-948d-817ba83bda44)
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

Crea las clases Noreste, Noroeste, Sureste y Suroeste que utilicen el patrón Bridge tal y como lo utilizan las subclases de Orientacion.
```
***Composite:***
Estructuras estáticas del modo todo-parte. Permite que se utilizan tanto los objetos individuales como los objetos compuestos.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/7654c4a6-e208-41da-914e-34fb32e652d0)

<br>
Para este patrón se han creado Contenedor y Hoja que heredan de ElementoMapa.

```
Crea la clase Contenedor que hereda de MapElement, esta clase tiene los siguinetes atributos: hijos, orientaciones, este, oeste, norte y sur.
Crea la clase Hoja que hereda de MapElement.
```
***Iterator:***
Estructuras que permiten la recursión o jerarquías.<br><br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/cf588952-eda2-4d5d-a4fc-edcefd217eec)

<br>
Creación del método recorrer en ElementoMapa que sera implementado por las subclases. 

```
En MapElement:
def recorrer(self,unBloque):
	pass
```
Ahora ha de ser implementado por la subclases de MapElement.
<br>Contenedor:
```
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
def actua(self, Bicho):
        self.dormir(Bicho)
        self.caminar(Bicho)
        self.atacar(Bicho)
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

Crea la clase Hexagono que utilice el patron Bridge tal y como lo utiliza la clase Cuadrado.

```
***Mediator:***
Permite semplificar la comunicación entre objetos.<br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/184e39fe-250a-4221-a99d-8b285fa47e12)
<br>Para la implementación de este patrón hemos creado la clase Ente el cual tiene como subclases Personaje y Bicho que son ConcreteCollegues y Juego hace de mediador etre estas dos subclases.
<br>
```
Crea la clase Ente utilizando el patrón Mediator para que las subclases de Ente que son Personaje y Bicho se comuniquen mediante la clase Juego.
```

***State:***
Permite que un objeto cambie su comportamiento cuando su estado interno cambia, encapsulando cada estado en una clase separada y permitiendo que el objeto delegue su comportamiento a si estado actual.
<br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/58d6e7bb-2dfd-4411-abf5-af7cc5bab597)
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/7900c488-b383-4e2c-8c1f-b6b53f0c7dac)
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/d35fbb7d-59bc-40ca-a243-afb776789621)

<br>Lo que hemos implementado en este patrón de diseño es formas de estado en este caso hemos puesto tanto en Ente como en Puerta pero también se puede implementar en Bomba (Activa/Desactivada) o también las fases del juego como inicio(selección de personaje...), inicio del juego y fin(muerte o muerte de todos los bichos).

```
Crea mediante el patron de diseño state la clase EstadoEnte que tiene las subclases Muerto y Vivo.
Crea mediante el patron de diseño state la clase EstadoPuerta que tiene las subclases Abierta y Cerrada.
```

***Prototype:***
Permite la creación de nuevos objetos duplicando un prototipo existente mediante clonación.<br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/6b6fa8a3-fb41-4ffd-901d-f25a4b5ac089)
<br>Hemos creado el método clonarLaberinto. Para a la hora de que el personae pase por un tunel se cree un laberinto nuevo al momento.
```
Crea un metodo clonarLaberinto utilizando del patron prototype.
```
***Observer:***
Permite que un objeto, llamado sujeto, notifique automáticamente a una lista de objetos, llamados observadores, sobre cualquier cambio de estado, sin acoplar en exceso el sujeto y los observadores.<br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/377826d8-a2f2-4156-be2d-29d0c4653d7d)
<br>Lo hemos implementado como un nuevo tag llamado Vista donde hemos creado la clase LaberintoGUI el cual tiene el método agregarPersonaje el cual añade dependencia - este es el método attach del observer sobre el sujeto.
```
Crea una nueva clase que haga de observer del proyecto, como minimo tiene que tener los siguientes atributos: juego, win, person, ancho, alto ademas de crear un método agregarPersonaje en el cual le pasamos unaCadena agregue al personaje, a peson le agregamos el juego y le añadimos dependencia a person.
```
***Command:***
Encapsula una solicitud como un objeto, permitiendo parametrizar a los clientes con diferentes peticiones y soportar operaciones deshace.<br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/8391f86e-732d-4bfa-bb6b-0bbe41420760)

<br>Lo hemos implementado mediante una nueva clase llamada Comando, además de introducir una nueva variable en ElementoMapa llamada comandos que es una colección de comandos.
<br>Dentro de Comando tenemos la variable receptor, y las subclases Abrir, Cerrar, Entrar, ya que nos estamos centrando en las Puertas.<br>
```
Crea una clase llamada Comandos que tenga como atributo receptor y mediante el patron de diseño comander tenga el metodo ejecutar, y las subclases abrir, cerrar y entrar.
```

***Visitor:***
Permite agregar nuevas operaciones a una estructura de objetos sin modificar esas clases de objetos.
<br>
El Visitor solo ejecuta una operación, como el Decorator, pero hace que haga más cosas de las que tenía definidas.<br>
![imagen](https://github.com/MariaPicazoSanchez/Dise-oSoftwareProyect/assets/129367348/f1320521-4fff-49d5-95f9-373bb6d8316d)

<br>Dentro del LaberintoGUI hemos creado el método de iniciarJuego el cual tiene una serie de comandos, el comando que en nuestro caso hemos implementado el patrón es el de dibujarLaberinto.
```

```

***Flyweight:***
Utiliza compartir para soportar de manera eficiente un gran número de objetos pequeños
<br><br>No implementado.

***Memento:***
Sin violar la encapsulación, captura y externaliza el estado interno de un objeto de modo que el objeto pueda recuperar ese estado más adelante.
<br><br>No implementado.

***Chain of Responsability:***
Evita acoplar el emisor de una petición con su receptor dando la oportunidad, a más de un objeto, de gestionar (o manejar) la petición. Encadena a los objetos receptores y pasa la petición a lo largo de esa cadena hasta encontrar un objeto que la atienda.
<br><br>No implementado

