**Patrones implementados**

***Factory Method:***
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
> [!NOTE]
> Una vez me da este metodo los siguientes es modificarlos, los métodos más fáciles como frabricarBomba, fabricarPuerta... los hago a mano ya que no cuestan nada.
	
```
