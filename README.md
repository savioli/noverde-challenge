-
# noverde-challenge
Noverde Challenge - Senior Software Engineer

# Desafio Noverde

Solução do desafio proposto em [noverde/challenge](https://github.com/noverde/challenge) utilizando:

**Flask** + **MongoDB** + **Redis** + **RabbitMQ** + **NGINX** + **Celery Flower**



# Uso
É possível iniciar a aplicação com **Vagrant** ou com **Docker + Docker Compose**.

#### Observação

Antes de executar qualquer comando para iniciar a aplicação configure a variável **X_API_KEY** definindo uma chave de API válida, por exemplo:


```bash
...
X_API_KEY=AnAB1jQEFs2Ai3XtZdssa34gORT6jWPI4TWdXN98
...
```

Caso a variável seja definida como vazia o resultado da API de **score** e **commitment** será simulado.

## com Vagrant

O próprio **Vagrant** se encarregará de iniciar todo o ambiente. 

```bash
vagrant up
```

Além do Vagrant é necessário ter instalado plugin **vagrant-docker-compose**. Caso não esteja instalado, é possível instalá-lo através do comando abaixo:

```bash
vagrant plugin install vagrant-docker-compose
```

Após a máquina e todos os containers carregarem 
a API ficará disponível em: 

#### **ENDPOINT** [192.168.33.100/v1/](192.168.33.100)

#### **POST** `/loan` 
#### [192.168.33.100/v1/loan](192.168.33.100/v1/loan/)

#### **GET** `/loan/:id` 
#### [192.168.33.100/v1/loan/:id](192.168.33.100/v1/loan/)


#### Monitoramento da fila com Celery Flower

O monitoramento da fila com **Celery Flower** ficará disponível em:

#### [192.168.33.100:5555](192.168.33.100/v1/loan/)

## com Docker e Docker Compose

Criando containers diretamente com **Docker Compose**

```bash
docker-compose up -d --build
```

Após a máquina e todos os containers serem criados
a API ficará disponível em: 

#### **ENDPOINT** [localhost/v1/](192.168.33.100)

#### **POST** `/loan` 
#### [localhost/v1/loan](192.168.33.100/v1/loan/)

#### **GET** `/loan/:id` 
#### [localhost/v1/loan/:id](192.168.33.100/v1/loan/)


#### Monitoramento da fila com Celery Flower

O monitoramento da fila com **Celery Flower** ficará disponível em:

#### [localhost:5555](192.168.33.100/v1/loan/)


## Worker para Execução de Tarefas Celery

Ao inicializar a aplicação com **Vagrant** ou **Docker Compose** um container executará automaticamente para executar as tarefas enviadas para a fila.


## Testes Unitários

Os testes podem ser executados em através do comando

```bash
# Caso o pip não esteja instalado
sudo apt-get install python3-pip

# Para instalar as dependências
pip3 install --no-cache-dir -r src/requirements.txt

# Para executar os testes
python3 -m unittest discover tests
```




## Informações para Contato


Informações de contato enviadas no e-mail de entrega.