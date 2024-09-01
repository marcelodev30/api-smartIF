
## O passo a passo para configurar e rodar a aplicação.

### Passo 1: Obter o código do projeto

  #### 1.Clonar o repositório (se necessário):
  - Clone o repositório para o seu ambiente local:.
 ```bash 
  git clone https://github.com/marcelodev30/api-smartIF.git
```
  #### 2. Navegar até o diretório do projeto:
   ```bash 
  cd nome_do_projeto
  ```

### Passo 2:  Configurar o ambiente virtual
#### 1. Crie um ambiente virtual:
- Navegue até o diretório onde deseja criar o projeto e execute:
```bash 
  python -m venv nome_do_ambiente
```
- Substitua "nome_do_ambiente" pelo nome desejado para o ambiente virtual.
#### 2. Ative o ambiente virtual:
- No windows:
  ```bash 
  nome_do_ambiente\Scripts\activate
  ```
- No macOS/Linux:
  ```bash 
  source nome_do_ambiente/bin/activate
  ```
#### 3. Confirme que o ambiente está ativo:
- O prompt do terminal deve mostrar o nome do ambiente virtual no início.

### Passo 3:  Instalar as dependências do projeto
#### 1. Instalar pacotes listados no "requirements.txt" : 
- A maioria dos projetos Django inclui um arquivo requirements.txt com todas as dependências necessárias.
- Instale essas dependências usando o comando:
  ```bash 
  pip install -r requirements.txt
  ```
### Passo 4: Configurar o banco de dados
#### 1. Aplicar as migrações do banco de dados:
- Execute as migrações para configurar o banco de dados de acordo com os modelos do projeto:
  ```bash 
  python manage.py migrate
  ```
#### 2. Configurar o banco de dados local (se necessário):
- Se o projeto usa um banco de dados que não é SQLite (por exemplo, PostgreSQL, MySQL), configure as credenciais do banco de dados no arquivo "settings.py" ou em variáveis de ambiente.
- Certifique-se de que o banco de dados esteja criado e acessível antes de aplicar as migrações.

### Passo 5: Criar um superusuário.

#### 1. Criar um superusuário:
- Se você precisar acessar a interface administrativa do Django, crie um superusuário:
  ```bash 
  python manage.py createsuperuser
  ```
- Siga as instruções para definir nome de usuário, e-mail e senha.

### Passo 6: Executar o servidor de desenvolvimento
#### 1. Executar o servidor:
- Inicie o servidor de desenvolvimento Django com o comando:
  ```bash 
  python manage.py runserver
  ```
#### 2. Verificar o funcionamento:
- Acesse http://127.0.0.1:8000/ em seu navegador para verificar se o projeto está rodando corretamente.

#### 3. Acessar o painel de administração:
- Acesse http://127.0.0.1:8000/admin/ e faça login com o superusuário que você criou.
