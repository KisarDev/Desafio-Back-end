# Desafio-Back-end
Fui convidado a participar de um desafio de desenvolvimento.



# Sistema de Gerenciamento de Ordens de Produção

## Introdução

Este projeto é um sistema de gerenciamento de ordens de produção para uma fábrica, criado como parte de um desafio técnico. O sistema permite aos usuários realizar várias operações, como registrar novas ordens de produção, listar ordens existentes, verificar a disponibilidade de materiais, atualizar o status de uma ordem e gerar relatórios de produção.

## Tecnologias Utilizadas

- Linguagem de Programação: Python
- Paradigma de Programação: Orientação a Objetos (POO)
- Armazenamento de Dados: Banco de Dados SQLite
- Interface: Linha de Comando (CLI)

## Estrutura do Projeto

O projeto é organizado em várias partes:

- `main.py`: O arquivo principal que inicia o sistema e interage com o usuário.
- `entities`: Contém as classes que definem os objetos principais, como `Fabrica`, `Produto` e `OrdemProducao`.
- `utils`: Contém funções utilitárias, como a função para criar o banco de dados.
- `fabrica.db`: O arquivo do banco de dados SQLite que armazena informações sobre produtos e ordens de produção.

## Como Utilizar o Sistema

Siga estas etapas para executar o sistema em sua máquina:

1. Clone o repositório para a sua máquina local:
   git clone https://github.com/KisarDev/Desafio-Back-end.git
2. Navegue até o diretório do projeto
3. Execute o arquivo `main.py`:
   python main.py
   ou
   python3 main.py
4. Você verá um menu de opções no terminal que permite registrar ordens de produção, listar ordens existentes, entre outras funcionalidades. Siga as instruções no terminal para interagir com o sistema.

- certifique de ter o python instalado em sua maquina, certifique de estar no diretório do projeto.








# Desafio Técnico - Sistema de Gerenciamento de Ordens de Produção para uma Fábrica
### Você foi designado para criar um sistema de gerenciamento de ordens de produção para uma fábrica. Este sistema deve permitir que os usuários realizem as seguintes operações:
- 1.Registrar uma nova ordem de produção, especificando o produto a ser fabricado, a quantidade desejada e a data de entrega.
- 2.Listar todas as ordens de produção existentes, mostrando os detalhes de cada ordem, como o produto, a quantidade e a data de entrega.
- 3.Verificar se o produto pode ser produzido com base nos materiais disponíveis. Caso contrário, o sistema deve avisar que a produção não é possível devido à falta de materiais.
- 4.Atualizar o status de uma ordem de produção, indicando se foi concluída ou não.
- 5.Visualizar relatórios de produção que mostrem as ordens em andamento e as concluídas.

____________________________________

Requisitos Técnicos:
- 1.O sistema deve ser implementado usando uma linguagem de programação de sua escolha.
- 2.O armazenamento das ordens de produção pode ser feito em um banco de dados simples (SQLite, por exemplo) ou em um arquivo.
- 3.O sistema deve ser executado em linha de comando, sem interface gráfica.
- 4.O código deve ser organizado e comentado de forma clara, seguindo as boas práticas de programação.

_______________________


Critérios de Avaliação:
- 1.Funcionalidade: O sistema deve atender a todos os requisitos mencionados acima.
- 2.Clareza e organização do código: O código deve ser legível e estar bem estruturado.
- 3.Tratamento de erros: O sistema deve lidar adequadamente com situações de erro e entrada inválida.

_______________________________________________________________
Entrega:
- 1.Você deve fornecer o código fonte completo, juntamente com um arquivo README que explique como configurar e executar o sistema.
- 2.Inclua exemplos de entrada e saída para demonstrar o funcionamento do sistema.
- Mantenham o código limpo e organizado, demonstre um entendimento claro do funcionamento de um sistema de gerenciamento de produção. Boa sorte!
_______________________________
