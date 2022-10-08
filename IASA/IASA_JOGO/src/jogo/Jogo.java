package jogo;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;
import jogo.personagem.Personagem;

/**
 * Classe principal que permite compilar e correr o programa
 * Esta classe conhece o ambiente (virtual) e uma personagem (agente inteligente)
 */

public class Jogo {
	private static Ambiente ambiente = new Ambiente();
	private static Personagem personagem = new Personagem(ambiente);

	/**
	 * Método que enquando o evento nao terminar permite executar a personagem, e evoluir o ambiente ao mesmo tempo. 
	 * 
	 */
	public static void executar() {
		do {
			personagem.executar();
			ambiente.evoluir();
		} while (ambiente.getEvento() != Evento.TERMINAR);

	}

	/**
	 * Método main que compila o programa na JVM, apresentando os resultados em modo texto
	 * @param args
	 */
	public static void main(String[] args) {
		executar();
	}
}
