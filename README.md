# Chatbot Controle de Atendimento de Ordens de Serviço

## Arquitetura da Aplicação

![plot](https://github.com/wilermoraes/chatbot/blob/master/10-%20Arquitetura%20Geral.jpg?raw=true)

O fluxo ocorre da seguinte maneira:
1) Os usuários irão enviar uma mensagem/requisição através do aplicativo telegram (móvel ou desktop);
2) A requisição passa pela API do Telegram e, em seguida, um webhook é acionado enviando a requisição para a função serveless;
3) A função serveless irá se comunicar com a API do Chatbot;
4) A API do Chatbot irá realizar as tarefas solicitadas e retornará para o telegram.

Será utilizado função serveless para abstrair a implementação do Telegram. Isso facilita na hora de adicionar uma nova interface de comunicação (com o WhatsApp por exemplo), sendo necessário apenas a criação de um nova função serveless.

---

## Arquitetura da API ChatBot

![image](https://github.com/wilermoraes/chatbot/blob/master/9%20-%20Arquitetura%20Chatbot.png?raw=true)

A arquitetura da API do ChatBot segue o seguinte padrão:
1) **Presentation:** Camada de apresentação responsável por receber a requisição e transformar para as entidades de negócio;
2) **Business Logic:** Camada responsável para realizar todas as regras de negócio da aplicação, permitindo ou negando determinadas ações;
3) **Data Acess:** Camada de acesso ao banco de dados. É responsável por todas as operações que são realizadas no banco de dados (armazenamento, obtenção, etc..)

O banco de dados que será utilizado será o SQL Server.

---

Abaixo as imagens do protótipo do chatbot com as suas devidas explicações

## Tela Inicial 
Após o bot ter sido criado e configurado, a figura abaixo demonstra a primeira tela que o usuário irá visualizar ao iniciar o atendimento pela primeira vez.

![plot](https://raw.githubusercontent.com/wilermoraes/chatbot/master/1%20-%20Tela%20Inicial.png)

---

## Consulta de ordem de serviço realizada com sucesso 
A consulta a uma ordem de serviço pode ser realizada ao selecionar a opção "Consultar Ordem Serviço". Após isso, o bot irá solicitar o número da ordem de serviço e o CPF/CNPJ vinculado a ela. Caso ela seja encontrada, irá retornar os dados, como na figura abaixo:

![plot](https://github.com/wilermoraes/chatbot/blob/master/2%20-%20Tela%20de%20Consulta%20Bem%20Sucedida.png?raw=true)

---

## Consulta da ordem de serviço com dados inválidos 
Na consulta, caso o usuário informe algum dado inválido, a resposta do bot será como na figura abaixo:

![plot](https://github.com/wilermoraes/chatbot/blob/master/3%20-%20Tela%20Consulta%20Sem%20Dados.png?raw=true)

---

## Cadastro da Ordem de Serviço 
Caso o usuário selecione a opção "Cadastrar Ordem de Serviço", o bot irá solicitar vários dados pessoais como CPF/CNPJ, Endereço, entre outros. Ele irá solicitar também alguns dados relacionados ao equipamento como tipo e descrição dos defeitos. Após todo os dados serem preenchidos, o bot irá responder com o número da ordem de serviço gerada. Esse processo é demonstrado nas duas imagens abaixo:

![plot](https://github.com/wilermoraes/chatbot/blob/master/4%20-%20Tela%20Cadastro%201.png?raw=true)
![plot](https://github.com/wilermoraes/chatbot/blob/master/5%20-%20Tela%20Cadastro%202.png?raw=true)

---

## Mensagem automática após o status ser alterado para agendado 
Quando o agendamento for realizado pelo usuário (esse agendamento é realizado por atendente humano via telefone), o status da ordem de serviço será alterado para "Agendado". Com essa alteração, o usuário receberá um alerta com o usuário que agendou e a data/hora do agendamento, conforme imagem abaixo:

![plot](https://github.com/wilermoraes/chatbot/blob/master/6%20-%20Retorno%20status%20Agendado.png?raw=true)

---

## Mensagem automática após o status ser alterado para em atendimento 
Quando a ordem de serviço for alterada pelo técnico para o status “Em atendimento”, ou seja, quando o técnico estiver a caminho do local do atendimento, o cliente irá receber uma notificação do bot informando sobre essa mudança de status, conforme imagem abaixo. Nessa notificação, ele receberá o número da ordem de serviço, o técnico que irá atende-lo e a data do atendimento.

![plot](https://github.com/wilermoraes/chatbot/blob/master/7-%20Retorno%20Status%20Em%20Atendimento.png?raw=true)

---

## Mensagem automática após o status ser alterado para finalizado 
Quando a ordem de serviço for finalizada pelo técnico, o cliente irá receber uma notificação do bot informando sobre mudança de status, conforme imagem abaixo. Nessa notificação, o cliente receberá o número da ordem de serviço, o técnico que finalizou, a solução e a data da finalização.

![plot](https://github.com/wilermoraes/chatbot/blob/master/8-%20OS%20Finalizada.png?raw=true)

---
