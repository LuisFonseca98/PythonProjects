package jogo.maqest;

public class Transicao<EV, AC> {


    /**
     * Representa a transicao de uma acao para o estado sucessor
     */

    private AC accao;
    private Estado<EV, AC> estadoSucessor;

    /**
     * Construtor da classe que inicializa a transicao da acao para o estado sucessor
     * @param estadoSucessor
     * @param accao
     */
    public Transicao (Estado<EV, AC> estadoSucessor, AC accao){
        this.accao = accao;
        this.estadoSucessor = estadoSucessor;
    }


    /**
     * @return o estado sucessor
     */
    public Estado<EV, AC> getEstadoSucessor(){
        return estadoSucessor;
    }

    /**
     * @return a accao
     */
    public AC getAccao(){
        return accao;
    }
    
}
