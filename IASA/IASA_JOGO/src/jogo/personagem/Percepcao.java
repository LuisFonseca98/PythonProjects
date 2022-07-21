package jogo.personagem;

import jogo.ambiente.Evento;

/**
 * Classe que permite a realizar a percepção de um determinado evento
 * Material de apoio: conjunto de slides 02 na pagina 14(sistema autonomo inteligente)
 * Corresponde a personagem efetuar a percepcao do evento que ira ser gerado pelo ambiente
 */
public class Percepcao {
	private Evento evento;

	/**
	 * Construtor da classe, necessitando de conhecer um determinado evento
	 * @param evento
	 */
	public Percepcao(Evento evento) {
		this.evento = evento;
	}

	/**
	 * Retorna o evento
	 * @return evento
	 */
	public Evento getEvento() {
		return evento;
	}

}
