1. Arquitetura Cliente-Servidor e o Modelo TCP/IP
A comunicação em rede baseia-se no modelo cliente-servidor, onde:

Servidor: Fica escutando por conexões em um endereço e porta específicos, pronto para atender requisições.

Cliente: Inicia a comunicação, enviando uma requisição para o servidor.

Modelo TCP/IP: É a pilha de protocolos padrão que viabiliza essa troca de dados na internet, garantindo que pacotes sejam endereçados e entregues corretamente.

2. O Papel do IP e da Porta
Para que dois processos se encontrem na rede, utiliza-se a combinação de:

Endereço IP: Identifica unicamente a máquina (dispositivo) na rede.

Porta: Identifica qual aplicação ou serviço específico dentro daquela máquina deve tratar a comunicação (ex: porta 80 para HTTP, 443 para HTTPS).

Protocolo: Define as regras de comunicação (como o TCP, que garante entrega confiável e ordenada dos dados).

3. Sockets de Baixo Nível e Manipulação
O socket é a interface de programação (API) que permite a uma aplicação enviar e receber dados através da rede usando os protocolos de transporte.

No Servidor (ServerSocket):

O programa cria um ServerSocket associado a um Endereço IP e a uma Porta específica de escuta.

Fica em estado de espera (listen) até que um cliente tente se conectar.

Quando a conexão é aceita, o servidor cria um Socket dedicado para se comunicar com aquele cliente específico.

No Cliente (Socket):

O cliente instancia um Socket informando o IP e a porta do servidor ao qual deseja se conectar.

4. Fluxo de Dados: Input e Output
Uma vez estabelecida a conexão via socket, a manipulação dos dados ocorre através de fluxos (streams):

Output Stream (Saída): Utilizado para enviar dados da aplicação para a rede (escrever no socket).

Input Stream (Entrada): Utilizado para ler os dados que chegam da rede (receber do socket).