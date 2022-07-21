package jogo.maqest;

/**
 * Representa a maquina de estados da personagem
 */
public class MaquinaEstados<EV, AC>{

    private Estado<EV, AC> estado;

    /**
     * Construtor da classe que permite inicializar o estado inicial da maquina de estados
     * @param estado representa o estado inicial
     */
    //Argumento do construtor, corresponde ao estado inicial
    public MaquinaEstados(Estado<EV, AC> estado){
        this.estado = estado;
    }

    /**
     * 
     * @return retorna o estado
     */
    public Estado<EV, AC> getEstado(){
        return estado;
    }


    /**
     * Permite processar a transicao do estado
     * @param evento
     * @return true se existir uma transacao, caso contrario retorna null, caso nao exista acao
     */
    public AC processar(EV evento){
        Transicao<EV, AC> transicao = estado.processar(evento);
        if(transicao != null){
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        }else{
            return null;
        }
    }


    
}
