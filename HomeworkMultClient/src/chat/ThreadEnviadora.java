package chat;

import java.net.Socket;
import java.util.Scanner;

public class ThreadEnviadora implements Runnable {

    private Socket socket;

    public ThreadEnviadora(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite suas mensagens:");

        while (!socket.isClosed()) {

            String mensagem = scanner.nextLine();

            if (!mensagem.trim().isEmpty()) {
                Comunicador.enviaMensagem(socket, mensagem);
            }
        }
    }
}
