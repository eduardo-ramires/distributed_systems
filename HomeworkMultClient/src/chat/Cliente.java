package chat;

import java.io.IOException;
import java.net.Socket;

public class Cliente {

    private Socket socket;

    public Cliente() {conectarServidor();
        if (socket != null) {
            iniciarThreads();
        }
    }

    private void conectarServidor() {
        try {
            socket = new Socket("127.0.0.1", 1234);

            System.out.println("Conectado ao servidor com sucesso!");

        } catch (IOException e) {System.out.println("Não foi possível conectar ao servidor.");
        }
    }

    private void iniciarThreads() {

        Thread threadRecebedora = new Thread(new ThreadRecebedora(socket));

        Thread threadEnviadora = new Thread(new ThreadEnviadora(socket));

        threadRecebedora.start();
        threadEnviadora.start();
    }

    public static void main(String[] args) {
        new Cliente();
    }
}
