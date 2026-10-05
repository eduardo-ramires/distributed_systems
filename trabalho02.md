O que é e por que é importante

A Comunicação Inter-Processos (IPC) é um conjunto de interfaces de programação e mecanismos fornecidos pelo sistema operacional que permite que processos separados troquem dados, sinais e recursos entre si, seja rodando na mesma máquina ou distribuídos em sistemas diferentes (SPASOJEVIC, 2025).

Ela é fundamental porque os processos tradicionais rodam de forma isolada e não compartilham o mesmo espaço de memória. Como existe essa barreira, o IPC surge para solucionar o problema não só da cooperação entre eles, mas também da coordenação, fazendo com que consigam conversar e trocar informações de forma organizada. Silberschatz, Galvin e Gagne (2015) apontam que permitir a cooperação entre processos traz vantagens como o compartilhamento de informações, o aumento da velocidade de computação, a modularidade e a conveniência para o usuário. Além disso, segundo Spasojevic (2025), o IPC desempenha um papel crucial no gerenciamento de dependências, na sincronização e no compartilhamento de recursos em ambientes de computação paralela e multitarefa.

Mecanismos de Comunicação entre Processos e Threads
Pipes: Um pipe funciona como um canal de comunicação no qual um processo grava dados em uma extremidade e outro processo os lê na extremidade oposta, em um fluxo contínuo de bytes. Silberschatz, Galvin e Gagne (2015) distinguem dois tipos. Os pipes comuns (ou anônimos) são criados pela chamada de sistema pipe() e são unidirecionais. Como não possuem nome, só podem ser usados entre processos com relação de parentesco, geralmente um processo pai que cria o pipe e o compartilha com um processo filho gerado por fork(). Esses pipes deixam de existir quando os processos que os utilizam terminam. Os pipes nomeados (FIFOs), criados pela chamada mkfifo(), aparecem como arquivos no sistema de arquivos. Isso permite que processos sem qualquer parentesco se comuniquem, e o canal continua existindo mesmo após o término dos processos, até ser explicitamente removido (SILBERSCHATZ; GALVIN; GAGNE, 2015).

Filas de mensagens (ou mailboxes): As filas de mensagens fazem parte do modelo de troca de mensagens, no qual a comunicação ocorre por meio de duas primitivas básicas, send() e receive() (SILBERSCHATZ; GALVIN; GAGNE, 2015). O mailbox caracteriza a chamada comunicação indireta: em vez de um processo enviar a mensagem diretamente a outro, ele a deposita em uma caixa postal identificada, da qual o processo receptor a retira. Assim, um mesmo mailbox pode ser compartilhado por vários processos. As mensagens podem ser consumidas na ordem de chegada (FIFO) ou de acordo com sua prioridade (SPASOJEVIC, 2025). As operações de envio e recebimento podem ser bloqueantes (síncronas), quando o processo aguarda a conclusão da operação, ou não bloqueantes (assíncronas), quando o processo segue sua execução imediatamente. A fila possui ainda uma capacidade de armazenamento, que pode ser zero, limitada ou ilimitada (SILBERSCHATZ; GALVIN; GAGNE, 2015). Como o emissor não precisa esperar o receptor, esse mecanismo é adequado para a comunicação assíncrona e para o desacoplamento entre processos (SPASOJEVIC, 2025).

Memória compartilhada (entre processos): Nesse modelo, os processos estabelecem uma região de memória comum, mapeada no espaço de endereçamento de cada um deles. Em sistemas POSIX, isso é feito com chamadas como shm_open(), que cria o objeto de memória compartilhada, e mmap(), que o mapeia no espaço do processo (SILBERSCHATZ; GALVIN; GAGNE, 2015). O sistema operacional participa apenas da criação e do mapeamento dessa região. Depois disso, os acessos são feitos como leituras e escritas comuns na memória, sem intervenção do kernel e sem cópia de dados entre processos. Por isso a memória compartilhada é considerada o mecanismo de IPC mais rápido (SPASOJEVIC, 2025). Em contrapartida, a responsabilidade de coordenar os acessos passa a ser dos próprios processos, que precisam de mecanismos de sincronização, como semáforos, para evitar condições de corrida (SILBERSCHATZ; GALVIN; GAGNE, 2015).

Memória compartilhada (com multithreading): Diferentemente de processos distintos, que dependem do sistema operacional para estabelecer uma região de memória comum, as threads de um mesmo processo já compartilham nativamente o espaço de endereçamento do processo ao qual pertencem, incluindo variáveis globais, heap e arquivos abertos. Cada thread mantém apenas sua própria pilha, registradores e contador de programa (TANENBAUM; BOS, 2016). Dessa forma, a troca de dados entre threads é feita por simples acesso a variáveis compartilhadas, o que a torna leve e rápida. O cuidado com a sincronização, porém, continua essencial. Os trechos de código que acessam dados compartilhados, chamados de regiões críticas, devem ser protegidos para que apenas uma thread os execute por vez. Para isso, bibliotecas como POSIX Threads (Pthreads) oferecem mutexes, que garantem a exclusão mútua, e variáveis de condição, que permitem a uma thread aguardar até que determinada condição seja satisfeita por outra (TANENBAUM; BOS, 2016).
REFERÊNCIAS

SILBERSCHATZ, Abraham; GALVIN, Peter Baer; GAGNE, Greg. Fundamentos de sistemas operacionais. 9. ed. Rio de Janeiro: LTC, 2015.

SPASOJEVIC, Anastazija. O que é comunicação entre processos (IPC)? phoenixNAP, 28 maio 2025. Disponível em: https://phoenixnap.pt/glossário/comunicação-entre-processos/. Acesso em: 5 out. 2026.

TANENBAUM, Andrew S.; BOS, Herbert. Sistemas operacionais modernos. 4. ed. São Paulo: Pearson, 2016. 



Exemplo 1: Processo pai cria um processo filho e o filho escrevem mensagens para o pai, que as recebem:


const { spawn } = require("child_process");

if (process.argv[2] === "filho") {
    console.log("Mensagem 1");
    console.log("Mensagem 2");
    console.log("Mensagem 3");
} else {
    const filho = spawn("node", [__filename, "filho"]);

    // Quando chegar algo pelo pipe, o pai mostra na tela
    filho.stdout.on("data", (dados) => {
        console.log("Pai recebeu pelo pipe:");
        console.log(dados.toString());
    });

    // Quando o filho terminar
    filho.on("close", () => {
        console.log("O processo filho terminou.");
    });
}

Exemplo 2: Exemplo com memoria compartilhada, Duas threads somam +1 no mesmo contador, que fica numa memória compartilhada, um contador com sincronia e outro sem:


const { Worker, isMainThread, workerData } = require("worker_threads");

const VEZES = 10000000; // quantas vezes cada thread soma +1

if (isMainThread) {
    const memoria = new SharedArrayBuffer(8);
    const contador = new Int32Array(memoria);

    // Cria 2 threads e passa a MESMA memória para as duas
    const thread1 = new Worker(__filename, { workerData: memoria });
    const thread2 = new Worker(__filename, { workerData: memoria });

    // Espera as duas threads terminarem
    let terminadas = 0;
    function quandoTerminar() {
        terminadas++;
        if (terminadas === 2) {
            console.log("Valor esperado:        ", VEZES * 2);
            console.log("Sem sincronização deu: ", contador[0]);
            console.log("Com sincronização deu: ", contador[1]);
        }
    }
    thread1.on("exit", quandoTerminar);
    thread2.on("exit", quandoTerminar);
} else {
    const contador = new Int32Array(workerData);

    //Soma sem sincronização
    for (let i = 0; i < VEZES; i++) {
        contador[0] = contador[0] + 1;
    }

    //Soma com sincronização
    for (let i = 0; i < VEZES; i++) {
        Atomics.add(contador, 1, 1);
    }
}

