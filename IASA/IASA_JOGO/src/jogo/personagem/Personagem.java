package jogo.personagem;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;

/**
 * Classe que representa a personagem (Agente inteligente) capaz de se adaptar aos diferentes eventos do ambiente virtual
 * 
 * Material de apoio: conjunto de slides 02 introducao nas paginas 14(sistema autonomo inteligente), 
 * 15(agente inteligente),20-23(agentes inteligentes, cognicao e racionalidade), 
 * 25(arquitecturas de agente)
 */

public class Personagem {
	private Ambiente ambiente;
	private Controlo controlo;

	/** 
	 * Construtor que recebe o ambiente como parametro e inicializa-o
	 * iniciliza tambem o controlo para controlar as accoes
	 */
	public Personagem(Ambiente ambiente) {
		this.ambiente = ambiente;
		this.controlo = new Controlo();
	}

	/**
	 * ciclo de funcionamento do agente de acordo com o slide 14
	 * No contexto do projeto o agente percepciona o ambiente, processa essa percepcao e consoante
	 * essa percepcao vai actuar
	 * Podemos inserir o conceito de cognicao onde consiste em o agente ser capaz de realizar a accao adequada dadas as condicoes do ambiente
	 */
	public void executar() {
		Percepcao percepcao = percepcionar();
		Accao accao = controlo.processar(percepcao);
		actuar(accao);
	}

	/**
	 * No contexto do projeto, a personagem age de acordo com o evento do ambiente, retornando uma nova percepcao desse mesmo evento
	 * Podemos introduzir o conceito de racionalidade. No contexto do projeto, podemos associar a personagem a um
	 * agente racional visto que escolhe a accao que maximiza o valor esperado da medida de desempenho dado o conhecimento disponivel sobre o ambiente(percepcao).
	 * @return um evento, gerado a partir da percpcao
	 */
	
	public Percepcao percepcionar() {
		Evento evento = ambiente.getEvento();
		return new Percepcao(evento);
	}

	/**
	 * Permite fazer atuar o agente, consoante uma acao fornecida
	 * @param accao
	 */
	public void actuar(Accao accao) {
		if (accao != null) {
			System.out.printf("Accao:%s \n", accao);
		}
	}
}
