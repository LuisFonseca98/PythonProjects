package jogo.ambiente;

/*
 Biblioteas usadas:
  -HashMap e Map - permiter associar uma string a um determinado evento
  -Scanner - recebe o input do utilizador
*/
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Representa o ambiente virtual onde a personagem  interpreta determinados eventos
 *	- Permite gerar um determinado evento
 *	- Leitura desse evento 
 *	- evolui consoante o evento do ambiente
 * 	- mostra na consola os respetivos eventos
 * 
 * 
 * Material de apoio: conjunto de slides 02 introducao nas paginas 17(propriedades de um ambiente), 20-23(cognicao e racionalidade)
 *   
 *	No contexto do projeto, o ambiente virutal pode ser classificado com as seguintes propiedades:
 *	• Discreto - So reage quando ha input do user
 *	• Deterministico - o evento que interpreta uma accao e determinada pelo user
 *	• Estatico - o ambiente muda apenas consoante um evento
 *	• Totalmente observavel - o agente conhece todas as accoes
 *	• Agente unico - apenas um agente, que realiza accoes consoante os eventos do ambiente
 *
 */

public class Ambiente {

	private Evento evento;
	private Map<String, Evento> eventos;
	private Scanner sc = new Scanner(System.in);

	/**
	 * Contrustor da classe onde é possível inicializar a lista de eventos
	 */
	public Ambiente() {
		eventos = new HashMap<String, Evento>();
		eventos.put("s", Evento.SILENCIO);
		eventos.put("r", Evento.RUIDO);
		eventos.put("a", Evento.ANIMAL);
		eventos.put("fu", Evento.FUGA);
		eventos.put("fo", Evento.FOTOGRAFIA);
		eventos.put("t", Evento.TERMINAR);
		
	}

	/**
	 * Retorna o evento
	 * @return evento
	 */
	public Evento getEvento() {
		return evento;
	}

	/**
	 * Permite evoluir o ambiente, consoante o evento gerado
	 */
	public void evoluir() {
		evento = gerarEvento();
		mostrar();
	}

	/**
	 * Gera um evento consoante uma letra que o utilizador pedir
	 * @return o evento pedido pelo utilizador
	 */
	// gera um evento consoanto o input do utilizador
	private Evento gerarEvento() {
		System.out.println("Evento?");
		String input = sc.next();
		return eventos.get(input);

		/*switch(input){
			case "s":
				eventos.put(input, Evento.SILENCIO);
				break;
			case "r":
				eventos.put(input, Evento.RUIDO);
				break;
			case "a":
				eventos.put(input, Evento.ANIMAL);
				break;
			case "fu":
				eventos.put(input, Evento.FUGA);
				break;
			case "fo":
				eventos.put(input, Evento.FOTOGRAFIA);
				break;
			case "t":
				eventos.put(input, Evento.TERMINAR);
				break;
			default:
				System.out.println("Caracter invalido!");

		}
		return eventos.get(input);
		*/
		
	}

	/**
	 * Imprime o evento na consola 
	 */
	public void mostrar() {
		System.out.printf("Evento:%s \n", evento);
	}
}
