Bot de Candidatura Automática no LinkedIn
Status: Em desenvolvimento

Descrição:
Esse projeto tem como objetivo criar um bot em Python para automação de candidaturas a vagas no LinkedIn. O bot vai enviar seu currículo de forma automática para as vagas com candidaturas simplificadas, otimizando o tempo e tornando o processo de aplicação mais eficiente. A ideia é facilitar o envio de currículos em massa, sem a necessidade de interação manual, sempre respeitando as opções de candidatura mais simples.

Tecnologias Usadas:

Python

Selenium

WebDriver (Chrome, Firefox)

Python-dotenv (para carregar variáveis de ambiente)

Funcionalidades Planejadas:

O bot acessa o LinkedIn e se candidata automaticamente às vagas com "Easy Apply".

Ele preenche as informações necessárias, envia seu currículo e confirma a candidatura.

Em desenvolvimento: Futuramente, será adicionado suporte para outras plataformas como InfoJobs.

Status do Projeto: Este projeto ainda está em desenvolvimento e é um dos meus estudos sobre automação de processos. Neste momento, a funcionalidade é focada no LinkedIn, mas já estou planejando expandir para o InfoJobs, então fique de olho nas atualizações!

🚀 Como Usar:
1. Instalação:
Primeiro, instale as dependências necessárias:


pip install -r requirements.txt
O arquivo requirements.txt contém as bibliotecas como selenium e python-dotenv.

2. Configuração:
Crie um arquivo .env com suas credenciais do LinkedIn. Exemplo:


LINKEDIN_EMAIL=seu_email@example.com
LINKEDIN_PASSWORD=sua_senha
3. Rodando o Bot:
Execute o script:


python bot_linkedin.py
O bot vai abrir o navegador, fazer login no LinkedIn e começar a enviar seu currículo para as vagas com "Easy Apply".

Importante:
Não compartilhe suas credenciais e use esse bot com responsabilidade, evitando violar os Termos de Serviço do LinkedIn.

👨‍💻 Sobre o Desenvolvedor:
Esse projeto está em andamento como parte dos meus estudos em automação com Python. A ideia é ajudar a agilizar o processo de candidatura para vagas, economizando tempo e esforço. O projeto está em constante evolução, e a inclusão de outras plataformas, como o InfoJobs, é algo que estou planejando!
