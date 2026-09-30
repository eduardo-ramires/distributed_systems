package Controller;

import Model.Pessoa;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.util.ArrayList;
import java.util.List;

public class RecebedorUDP {
    DatagramSocket socket;
    // Lista para salvar as pessoas e evitar duplicatas
    private List<Pessoa> listaPessoas = new ArrayList<>();

    public RecebedorUDP() {
        criaServerSocket();
        System.out.println("Servidor ativo à espera do cliente/enviador");
        
        DatagramPacket pacote = ComunicadorUDP.recebeMensagem(socket);
        String mensagem;               
        
        while (pacote != null) {
            mensagem = new String(pacote.getData(), 0, pacote.getLength()).trim();
            System.out.println("Recebi " + mensagem);
            System.out.println("De: " + pacote.getAddress().getHostName() + ":" + pacote.getPort());

            // 1. Processa a mensagem (Cadastro ou Token)
            String resposta = processarMensagem(mensagem);

            // 2. Envia a resposta de volta para o cliente
            try {
                DatagramPacket pacoteResposta = ComunicadorUDP.montaMensagem(
                    resposta, 
                    pacote.getAddress().getHostAddress(), 
                    pacote.getPort()
                );
                ComunicadorUDP.enviaMensagem(socket, pacoteResposta);
            } catch (Exception e) {
                e.printStackTrace();
            }

            // Aguarda o próximo pacote
            pacote = ComunicadorUDP.recebeMensagem(socket);
        }
    }

    private String processarMensagem(String mensagem) {
        String[] partes = mensagem.split(";");
        String acao = partes[0];

        if (acao.equalsIgnoreCase("CADASTRO")) {
            String nome = partes[1];
            String email = partes[2];

            // Verifica se o e-mail já existe na lista
            for (Pessoa p : listaPessoas) {
                if (p.getEmail().equalsIgnoreCase(email)) {
                    return "ERRO: E-mail já cadastrado!";
                }
            }

            // Se não existe, cria e adiciona
            Pessoa novaPessoa = new Pessoa(nome, email);
            listaPessoas.add(novaPessoa);
            return "SUCESSO: Cadastrado! Token inicial: " + novaPessoa.atualizarOuManterToken();

        } else if (acao.equalsIgnoreCase("SOLICITAR_TOKEN")) {
            String email = partes[1];

            // Procura a pessoa pelo e-mail
            for (Pessoa p : listaPessoas) {
                if (p.getEmail().equalsIgnoreCase(email)) {
                    // Pega o token atual (mantém ou atualiza a cada 60s)
                    return "TOKEN:" + p.atualizarOuManterToken();
                }
            }
            return "ERRO: Cliente não encontrado.";
        }

        return "ERRO: Ação desconhecida.";
    }

    private void criaServerSocket() {
        try {
            socket = new DatagramSocket(1234);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public static void main(String[] args) {
        RecebedorUDP receptor = new RecebedorUDP();
    }
}