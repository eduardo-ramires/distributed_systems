package Controller;

import java.io.*; 
import java.net.*;

public class EnviadorUDP {
    DatagramSocket socket;

    public EnviadorUDP() {
        criaClientSocket();
    }

    private void criaClientSocket() {
        try {
            // Cria um socket datagrama para enviar dados
            socket = new DatagramSocket();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    // Método para enviar o cadastro e receber a resposta do servidor
    public String enviarCadastro(String nome, String email) {
        try {
            String mensagem = "CADASTRO;" + nome + ";" + email;
            
            // Monta o pacote para o servidor na porta 1234
            DatagramPacket pacoteEnvio = ComunicadorUDP.montaMensagem(mensagem, "localhost", 1234);
            ComunicadorUDP.enviaMensagem(socket, pacoteEnvio);
            
            // Aguarda a resposta do servidor usando o ComunicadorUDP
            DatagramPacket pacoteResposta = ComunicadorUDP.recebeMensagem(socket);
            if (pacoteResposta != null) {
                return new String(pacoteResposta.getData(), 0, pacoteResposta.getLength()).trim();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "ERRO: Falha na comunicação com o servidor.";
    }

    // Método para solicitar o token periodicamente usando o e-mail
    public String solicitarToken(String email) {
        try {
            String mensagem = "SOLICITAR_TOKEN;" + email;
            
            DatagramPacket pacoteEnvio = ComunicadorUDP.montaMensagem(mensagem, "localhost", 1234);
            ComunicadorUDP.enviaMensagem(socket, pacoteEnvio);
            
            DatagramPacket pacoteResposta = ComunicadorUDP.recebeMensagem(socket);
            if (pacoteResposta != null) {
                return new String(pacoteResposta.getData(), 0, pacoteResposta.getLength()).trim();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "ERRO: Falha ao solicitar token.";
    }

    public void fecharSocket() {
        if (socket != null && !socket.isClosed()) {
            socket.close();
        }
    }
}