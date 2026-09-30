package chat;

import java.net.ServerSocket;
import java.net.Socket;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Servidor {

    private ServerSocket servidor;

    private final List<Socket> clientesConectados;

    private final ExecutorService poolDeThreads;

    public Servidor() {

        clientesConectados = new CopyOnWriteArrayList<>();

        poolDeThreads = Executors.newCachedThreadPool();

        criarServidor();
        aguardarClientes();
    }

    private void criarServidor() {

        try {
            servidor =new ServerSocket(1234);

            System.out.println("Servidor iniciado na porta 1234...");

        } catch (Exception e) {

            System.out.println("Erro ao iniciar servidor.");
            e.printStackTrace();
        }
    }

    private void aguardarClientes() {

        try {

            while (true) {

              System.out.println("Aguardando cliente..." );

              Socket cliente =servidor.accept();

              clientesConectados.add(cliente);

              System.out.println("Novo cliente conectado: "+ cliente.getInetAddress());

              System.out.println("Clientes conectados: "+ clientesConectados.size());

              poolDeThreads.execute(new ThreadRecebedora(cliente,this));
            }

        } catch (Exception e) {

            System.out.println("Erro ao aceitar cliente.");

            e.printStackTrace();
        }
    }

    public void enviaParaTodos(Socket remetente, String mensagem) {

        for (Socket cliente : clientesConectados) {

            // Não devolve a mensagem para quem enviou
            if (cliente != remetente) {

                Comunicador.enviaMensagem(cliente,"Cliente "+ remetente.getPort()+ ": "+ mensagem);
            }
        }
    }

    public void removerCliente(Socket cliente) {
        clientesConectados.remove(cliente);

        try {
            cliente.close();
        } catch (Exception e) {
            // conexão já pode estar fechada
        }

        System.out.println("Cliente removido.");

        System.out.println("Clientes conectados: "+ clientesConectados.size());
    }

    public static void main(String[] args) {
        new Servidor();
    }
}
