Passo 1: Instalar Python e pip
Verifique se Python está instalado:

No terminal, digite python --version ou python3 --version para verificar a versão do Python instalada.
Caso não esteja instalado, baixe e instale Python do site oficial python.org.
Instale o pip (gerenciador de pacotes Python):

O pip geralmente já vem com o Python. Verifique a instalação com pip --version ou pip3 --version.
Se não estiver instalado, siga as instruções no site oficial do pip.
Passo 2: Criar e ativar um ambiente virtual
Crie um ambiente virtual:

Navegue até o diretório onde deseja criar o projeto e execute:
bash
Copiar código
python -m venv nome_do_ambiente
Substitua nome_do_ambiente pelo nome desejado para o ambiente virtual.
Ative o ambiente virtual:

No Windows:
bash
Copiar código
nome_do_ambiente\Scripts\activate
No macOS/Linux:
bash
Copiar código
source nome_do_ambiente/bin/activate
Confirme que o ambiente está ativo:

O prompt do terminal deve mostrar o nome do ambiente virtual no início.
Passo 3: Instalar Django
Instale o Django usando pip:

bash
Copiar código
pip install django
Verifique a instalação:

Confirme a instalação do Django com:
bash
Copiar código
python -m django --version
Passo 4: Criar um novo projeto Django
Crie o projeto:

No terminal, execute:
bash
Copiar código
django-admin startproject nome_do_projeto
Substitua nome_do_projeto pelo nome desejado.
Navegue até o diretório do projeto:

bash
Copiar código
cd nome_do_projeto
Passo 5: Executar o servidor de desenvolvimento
Execute o servidor:

Dentro do diretório do projeto, execute:
bash
Copiar código
python manage.py runserver
Acesse o servidor:

Abra um navegador e vá para http://127.0.0.1:8000/.
Você deve ver a página padrão do Django, confirmando que o servidor está funcionando.
