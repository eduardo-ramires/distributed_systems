package chat;

import java.net.Socket;

public class ThreadRecebedora implements Runnable {

    private Socket socket;
    private Servidor servidor;

    // Usado pelo cliente
    public ThreadRecebedora(Socket socket) {
        this.socket = socket;
        this.servidor = null;
    }

    // Usado pelo servidor
    public ThreadRecebedora(Socket socket, Servidor servidor) {
        this.socket = socket;
        this.servidor = servidor;
    }

    @Override
    public void run() {

      try {

            while (true) {

                String mensagem =Comunicador.recebeMensagem(socket);

                if (mensagem == null) {

                    System.out.println("Conexão encerrada: "+ socket.getInetAddress());

                    if (servidor != null) {
                        servidor.removerCliente(socket);
                    }

                    break;
                }

                // Se estiver no servidor
                if (servidor != null) {

                    System.out.println("[" + socket.getInetAddress()+ "] " + mensagem);

                    servidor.enviaParaTodos(socket,mensagem);
                } else {

                    // Se estiver no cliente
                    System.out.println(mensagem);
                }
            }

        } catch (Exception e) {

            System.out.println("Erro na conexão com "+ socket.getInetAddress());
        }
    }
}
