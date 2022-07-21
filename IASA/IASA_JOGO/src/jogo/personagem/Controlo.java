package jogo.personagem;

import jogo.ambiente.Evento;
import jogo.maqest.Estado;
import jogo.maqest.MaquinaEstados;

/**
 * Controlo das ações, através da percepção das mesmas
 * Material de apoio: relacao com a teoria: slide 15(agente inteligente)
 * Consoante o controlo da personagem, esta processa uma determinada accao
 *
 * Referencia aos slides 06-mod-din, pag 6/12, 7/12 e 9/12 e 11/12
 */
public class Controlo {

	private MaquinaEstados<Evento,Accao> maqEst;

	public Controlo(){

	//Definir estados
	Estado<Evento,Accao> procura = new Estado<>("Procura");
	Estado<Evento,Accao> inspecao = new Estado<>("Inspecao");
	Estado<Evento,Accao> observacao = new Estado<>("Observacao");
	Estado<Evento,Accao> registo = new Estado<>("Registo");

	/**
	 * Nas variaveis abaixo, contemos a funcao de transicao de estado e a funcao de saida
	 * Neste caso iremos conter:
	 *  -> um conjunto de simbolos de entrada (ou alfabeto de entrada), no caso do trabalho pratico, os Eventos
	 *  -> um conjunto de simbolos de saida (ou alfabeto de saida), no caso do trabalho pratico, sao as acoes da personagem
	 *  -> um conjunto de estados, que neste caso, representam os diferentes estados da personagem
	 *
	 * 	Podendo associar dois tipos de maquinas:
	 *   -> maquinas de mealy, nas quais a funcao de saida depende das entradas
	 *   -> maquina de moore, nas quais a funica de saida nao depende das entradas
	 *	Posto isto, estamos perante um modelo de dinamica de um sistema, onde esta pode ser expressa
	 *  como uma funcao de transformacao, que perante o estado atual e as entradas atuais, produz o estado e saidas seguintes,
	 * e podemos associar a maquina de mealy, visto que este projeto depende dos valores de entrada, visto que passamos sempre ume vento, com um novo estado, contendo, ou nao, uma acao
	 */

	//Definir transicoes
	procura
		.transicao(Evento.ANIMAL,observacao,Accao.APROXIMAR)
		.transicao(Evento.RUIDO,inspecao,Accao.APROXIMAR)
		.transicao(Evento.SILENCIO,procura,Accao.PROCURAR);

	inspecao
		.transicao(Evento.ANIMAL,observacao,Accao.APROXIMAR)
		.transicao(Evento.RUIDO,inspecao,Accao.PROCURAR)
		.transicao(Evento.SILENCIO,procura);

	observacao
		.transicao(Evento.FUGA,inspecao)
		.transicao(Evento.ANIMAL,registo,Accao.OBSERVAR);

	registo
		.transicao(Evento.ANIMAL,registo,Accao.FOTOGRAFAR)
		.transicao(Evento.FUGA,procura)
		.transicao(Evento.FOTOGRAFIA,procura);


	maqEst = new MaquinaEstados<>(procura);
	
	}

	/**
	 * 
	 * @return o estado da maquina de estados
	 */
	public Estado<Evento,Accao> getEstado(){
		return maqEst.getEstado();
	}

	/**
	 * Processa o controlo da maquina de estados
	 * @param percepcao
	 * @return
	 */
	public Accao processar(Percepcao percepcao) {
		Accao accao = maqEst.processar(percepcao.getEvento());
		return accao;
	}

	/**
	 * Imprime na consola o estado com o seu respetivo nome
	 */
	public void mostrar(){
		System.out.println("Estado %s: " + getEstado().getNome());

	}
}
