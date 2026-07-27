# Prometheus

> A ferramenta Prometheus está sendo desenvolvida com o objetivo de automatizar tarefas e auxiliar o usuário, proporcionando maior agilidade, eficiência e produtividade no sistema operacional Windows 10/11.

---

## ⚠️ Atenção

> A ferramenta possui algumas funcionalidades que podem ser consideradas ilegais em determinadas circunstâncias. O uso dessas funcionalidades é opcional e de inteira responsabilidade do usuário.

---

## 📌 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Composição do Projeto](#composicao-do-projeto)
- [Download e Instalação](#download-e-instalação)
- [Configuração](#configuração)
- [Como usar](#como-usar)
- [Licença](#licença)

---

### Sobre o Projeto

- Visão geral
    > A ferramenta visa automatizar processos e tarefas no Windows, proporcionando ao usuário mais comodidade, produtividade e segurança.
    Ela está em estágios iniciais de desenvolvimento, mas já conta com diversas funcionalidades, entre elas:

        1. Sistema de atalhos para abrir pastas e aplicativos apenas digitando o nome no prompt;
        2. Limpeza de arquivos temporarios;
        3. EasySharing (sistema web para FTP, igual a drive)/
        4. Self-defense (alguns instrumentos para ajudar a proteger seu computador/usuário);
        5. Ytdlp para download de músicas e vídeos do YouTube;

- Informações
    > Desenvolvedor: Xzhyan (Bravo Dynamics)
    > Linguagem: Python
    > Versão: 1.0.10
    > Plataforma: Windows 10/11

---

### Composição do Projeto

> A ferramenta opera por meio de um terminal do Windows e de uma interface de linha de comando; ou seja, todos os comandos são inseridos através do prompt.

Tecnologias usadas:
    - Código fonte: Python
    - Bibliotecas Python: sys, os, subprocess, colorama, yt-dlp, pydantic, json, pathlib, pywebview, time, ctypes
    - Recursos nativos do sistema operacional

---

### Download e Instalação

Requisitos: Windows 10/11 e Python 3.14.2 ou superior instalado

Download:
    Use git clone para clonar o repositório em um diretório de sua preferência

    ```bash
    git clone https://github.com/Xzhyan/Prometheus.git
    ```

Instalação:

    1. Acesse a pasta clonada

    ```bash
    cd Prometheus
    ```

    2. Crie um novo ambiente virtual

    ```bash
    python -m venv .venv
    ```

    3. Ative o ambiente virutal

    ```bash
    .venv\Scripts\activate
    ```

    4. Instale as libs python

    ```bash
    pip install -r requirements.txt
    ```

> Agora é só configurar...

---

### Configuração

> Siga o passo-a-passo para configurar a ferramenta

Ajusar o .env

    1. Clone o arquivo '.evn.example' e renomeie para '.env'

Configurando o EasySharing (apenas se você fizer uso do mesmo)

    2. Edite o arquivo '.env' no seguinte trecho, alterando as informações

    ```bash
    # EasySharing
    EASY_PATH="" # aqui vai o caminho absoluto do seu EasySharing
    EASY_SERVER_IP= # aqui vai o IP local da sua máquina (PC) na porta 8000, ex: 192.168.0.10:8000
    ```

Se você notar problemas com os seguintes links, você pode atualizar eles manualmente

    ```bash
    # SelfDefense
    BIT_LINK_CHECKER_URL = 'https://www.bitdefender.com/en-us/consumer/link-checker'
    VIRUS_TOTAL_URL = 'https://www.virustotal.com/gui/home/upload'
    BITWARDEN = 'https://bitwarden.com/'
    PROTON_VPN = 'https://protonvpn.com/'
    ```

---

### Como usar

Após a ferramnenta configurada basta basta abrir ela usando o '.bat' Prometheus.bat

---

### Linceça

A ferramenta possui código aberto visando maior transparência em relação ao seu funcionamento e às suas funções específicas. É permitido adicionar scripts próprios para ampliar ou personalizar seu uso, desde que respeitados os termos de utilização.

Entretanto, o código-fonte não é de uso totalmente livre: fica expressamente proibida a utilização, modificação, distribuição ou incorporação do código para fins comerciais, exploração financeira ou obtenção de lucro próprio sem autorização prévia.
