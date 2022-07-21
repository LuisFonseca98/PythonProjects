package jogo.maqest;

import java.util.HashMap;
import java.util.Map;


/**
 * Representa o estado onde podemos efetuar transicoes
 */
public class Estado<EV,AC> {

    private Map<EV,Transicao<EV, AC>> transicoes;
    private String nome;

    /**
     * Construtor da classe, que necessita de conhecer as transicoes e o nome do estado
     * @param nome
     */
    public Estado(String nome){
        transicoes = new HashMap<>();
        this.nome = nome;
    }

    /**
     * 
     * @return o nome do estado
     */
    public String getNome(){
        return nome;
    }

    /**
     * Processa uma transicao consoante um evento
     * @param evento
     * @return a transicao desse evento
     */
    public Transicao<EV, AC> processar(EV evento){
        return transicoes.get(evento);
    }

    /**
     * Efetua uma transicao, consoante a personagem nao contenha uma acao
     * @param evento
     * @param estadoSucessor
     * @return a transicao dum evento para o estado seguinte
     */
    public Estado<EV,AC> transicao(EV evento, Estado<EV, AC> estadoSucessor){
        return transicao(evento,estadoSucessor,null);
    }

    /**
     * Metodo que permite retornar uma transicao, quando passada uma acao
     * @param evento
     * @param estadoSucessor
     * @param accao
     * @return a transicao de um evento, para um estado, contento uma acao
     */
    public Estado<EV,AC> transicao(EV evento, Estado<EV, AC> estadoSucessor, AC accao){
        transicoes.put(evento, new Transicao<>(estadoSucessor, accao));
        return this;
    }
    
}
