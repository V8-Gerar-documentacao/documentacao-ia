# Documentação do Repositório

**Último Commit**

- **Autor**: felipe
- **Data do Commit**: 02/10/2024 14:09:06
- **Tempo desde o Commit**: 231 days, 2:20:31 (hh:mm:ss)
- **Mensagem do Commit**: Script de automação

## repositorio_clonado/ansible/provisioning.yml

# Implementação de Infraestrutura como Código com Ansible para Aplicação WordPress e Banco de Dados MySQL

## Descrição Geral

Este documento descreve como implementar a infraestrutura como código para uma aplicação WordPress e um banco de dados MySQL usando Ansible. A infraestrutura é configurada para ser gerenciada e versionada, permitindo a fácil recriação e atualização em diferentes ambientes.

## Pré-requisitos

* Ansible instalado na máquina local
* Conta no GitHub para armazenar o playbook Ansible
* Repositório público com o arquivo de playbook Ansible

## Estrutura do Playbook `playbook.yml`

```yaml
---
- name: Deploy WordPress and MySQL
  hosts: wordpress, mysql
  become: true

  roles:
    - wordpress
    - mysql
```

### Role `wordpress`

```yaml
---
- name: Install and configure WordPress
  apt:
    name: wordpress
    state: present
  service:
    name: apache2
    state: started
    enabled: yes
  template:
    src: templates/wp-config.php.j2
    dest: /etc/wordpress/wp-config.php
    mode: '0644'
  notify: restart apache2
```

### Role `mysql`

```yaml
---
- name: Install and configure MySQL
  apt:
    name: mysql-server
    state: present
  service:
    name: mysql
    state: started
    enabled: yes
  mysql_user:
    name: wordpress
    password: wordpress
    priv: '*.*:ALL'
  notify: restart mysql
```

### Notificações

```yaml
---
- name: Restart Apache2
  service:
    name: apache2
    state: restarted

- name: Restart MySQL
  service:
    name: mysql
    state: restarted
```

## Boas Práticas DevOps

✅ Versione o playbook Ansible no GitHub e faça commits regulares para rastrear alterações.

✅ Use variáveis de ambiente para armazenar informações de configuração sensíveis, como senhas e URLs.

✅ Utilize o Ansible para gerenciar e versionar a infraestrutura, permitindo a fácil recriação e atualização em diferentes ambientes.

🛑 Certifique-se de que o playbook Ansible esteja configurado corretamente e testado em um ambiente de desenvolvimento antes de ser deployado para produção.

**Observações**

* O playbook Ansible assume que a máquina local está configurada com o ambiente de desenvolvimento.
* O arquivo `wp-config.php` é gerado a partir do template `templates/wp-config.php.j2` e é configurado com as informações de conexão do banco de dados.
* O playbook Ansible utiliza o modulo `mysql_user` para criar um usuário e conceder permissões no banco de dados.

## repositorio_clonado/ansible/roles/apache/tasks/main.yml

# Implementação de Servidor Web com Apache, PHP e Ansible

## Descrição Geral

Este documento descreve como implementar um servidor web com Apache, PHP e Ansible. O objetivo é criar um ambiente de desenvolvimento seguro e escalável para aplicações web.

## Pré-requisitos

* Ansible instalado na máquina local
* Conta no servidor web (ex: Ubuntu 20.04)
* Conhecimento básico de Ansible e YAML

## Estrutura do Script Ansible `playbook.yml`

```yaml
---
- name: Configurar servidor web
  hosts: web-server
  become: yes

  tasks:
    - name: Instalar Apache
      apt:
        name: apache2
        state: latest
    - name: Instalar PHP
      apt:
        name: php
        state: latest
      - name: Instalar dependências PHP
        apt:
          name:
            - php-bcmath
            - php-curl
            - php-imagick
            - php-intl
            - php-json
            - php-mbstring
            - php-mysql
            - php-xml
            - php-zip
          state: latest
    - name: Configurar Apache
      template:
        src: templates/apache.conf.j2
        dest: /etc/apache2/apache.conf
        mode: '0644'
    - name: Reiniciar Apache
      service:
        name: apache2
        state: restarted
    - name: Instalar Ghostscript
      apt:
        name: ghostscript
        state: latest
    - name: Instalar PHP-XML
      apt:
        name: php-xml
        state: latest
```

## Explicação dos Comandos

* `hosts: web-server`: Define o grupo de hosts que o playbook será executado.
* `become: yes`: Permite que o playbook execute comuns de usuário root para instalar pacotes e realizar alterações de sistema.
* `tasks`: Define as tarefas que serão executadas.
* `apt`: Instala pacotes com o gerenciador de pacotes APT.
* `template`: Substitui variáveis em um arquivo template e o salva em um local específico.
* `service`: Gerencia serviços do sistema, como o reinício do Apache.
* `notify`: Notifica o serviço Apache de que ele precisa ser reiniciado.

## Boas Práticas

* ✅ Use Ansible para automatizar tarefas de configuração e instalação.
* ✅ Use templates para substituir variáveis em arquivos de configuração.
* ✅ Use o gerenciador de pacotes APT para instalar pacotes.
* ✅ Use o serviço Apache para gerenciar o servidor web.
* 🛑 Certifique-se de que o servidor web esteja configurado corretamente e que o Apache esteja rodando antes de executar o playbook.

## Exemplo de Uso

Para executar o playbook, execute o comando abaixo:
```bash
ansible-playbook -i <hosts_file> playbook.yml
```
Substitua `<hosts_file>` pelo nome do arquivo de hosts que você criou anteriormente.

## repositorio_clonado/ansible/roles/mysql/tasks/main.yml

# Configuração de Infraestrutura como Código com Ansible para Aplicação em Go

## Descrição Geral

Este documento descreve como configurar a infraestrutura como código (IaC) para uma aplicação em Go utilizando Ansible. A configuração inclui a instalação de dependências, criação de uma tabela no banco de dados MySQL e configuração de privilégios para o usuário do banco de dados.

## Pré-requisitos

- Ansible instalado na máquina local
- Conta no GitHub
- Projeto Go com estrutura de módulos (`go.mod`)
- Máquina virtual com sistema operacional Ubuntu

## Estrutura do Playbook `playbook.yml`

```yaml
---
- name: Configuração de Infraestrutura para Aplicação em Go
  hosts: ubuntu
  become: yes

  tasks:
    - name: Install dependencias
      apt:
        pkg:
          - mysql-server
          - python3-pymysql
        state: latest
        update_cache: yes

    - name: Criando uma tabela no BD
      mysql_db:
        name: wp_db_name
        state: present
        login_unix_socket: /run/mysqld/mysqld.sock

    - name: Cria um usuário, sua senha e os privilégios 
      mysql_user:
        name: wp_db_user
        password: wp_db_passw
        priv: wp_db_name.*:SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER
        state: present
        login_unix_socket: /run/mysqld/mysqld.sock
        host:
          - localhost
          - 127.0.0.1
          - {{ wp_ip }}

    - name: Configuraçãp do banco de dados para permitir acesso
      replace:
        path: /etc/mysql/mysql.conf.d/mysqld.cnf
        regexp: "127.0.0.1"
        replace: "0.0.0.0"
      notify:
        - restart mysql
```

## Explicação das Tarefas

* A tarefa `Install dependencias` instala as dependências necessárias, incluindo o MySQL e o Python3-Pymysql, usando o modulo `apt`.
* A tarefa `Criando uma tabela no BD` cria uma tabela no banco de dados MySQL com o nome `wp_db_name` usando o modulo `mysql_db`.
* A tarefa `Cria um usuário, sua senha e os privilégios` cria um usuário no banco de dados MySQL com o nome `wp_db_user`, senha `wp_db_passw` e privilégios para acessar a tabela `wp_db_name`. O modulo `mysql_user` é usado para criar o usuário e configurar os privilégios.
* A tarefa `Configuraçãp do banco de dados para permitir acesso` configura o arquivo de configuração do MySQL para permitir acesso a partir de qualquer IP usando o modulo `replace`.

## Boas Práticas DevOps

* Utilizar Ansible para configurar a infraestrutura como código é uma boa prática DevOps pois permite a automatização e a reprodutibilidade da configuração.
* Utilizar variáveis de ambiente para armazenar informações sensíveis, como senhas, é uma boa prática DevOps pois ajuda a manter a segurança e a confidencialidade dos dados.
* Utilizar o modulo `notify` para notificar o restart do serviço MySQL após a configuração é uma boa prática DevOps pois ajuda a garantir que o serviço esteja disponível após a configuração.

**Observações**

* Certifique-se de substituir as variáveis `wp_db_name`, `wp_db_user`, `wp_db_passw` e `wp_ip` com os valores corretos para sua aplicação.
* Certifique-se de que o arquivo de configuração do MySQL esteja configurado corretamente para permitir acesso a partir de qualquer IP.

## repositorio_clonado/ansible/roles/mysql/handlers/main.yml

# Automação de Restart de Serviço com Ansible

## Descrição Geral

Este documento descreve como utilizar Ansible para automatizar o restart de um serviço, especificamente o MySQL, em um ambiente de produção. Essa automação é útil para garantir que o serviço esteja sempre disponível e em um estado consistente.

## Pré-requisitos

- Ansible instalado na máquina local
- Conta com permissões de acesso ao servidor
- Servidor com o serviço MySQL instalado e configurado

## Estrutura do Playbook `restart_mysql.yml`

```yaml
---
- name: Restart MySQL
  hosts: mysql-server
  become: yes

  tasks:
  - name: Restart MySQL service
    service:
      name: mysql
      state: restarted
```

## Explicação das Seções

**hosts**: Essa seção define o nome do host que Ansible deve se conectar para executar as tarefas. Nesse caso, estamos usando o nome de host `mysql-server`.

**become**: Essa opção permite que Ansible execute as tarefas com privilégios elevados, necessários para restartar o serviço MySQL.

**tasks**: Essa seção define as tarefas que Ansible executará no host especificado. Nesse caso, estamos executando apenas uma tarefa, que é restartar o serviço MySQL.

**service**: Essa tarefa utiliza o módulo `service` para restartar o serviço MySQL. A opção `name` especifica o nome do serviço que deve ser restartado, e a opção `state` especifica que o serviço deve ser restartado.

## Boas Práticas

✅ Utilize Ansible para automatizar tarefas de manutenção em seu ambiente de produção.

✅ Certifique-se de que o Ansible esteja configurado corretamente para se conectar ao servidor e executar as tarefas com privilégios elevados.

🛑 Se o serviço MySQL não estiver configurado corretamente, o restart pode causar problemas de disponibilidade do serviço.

**Observações**

* Se você estiver usando um ambiente de produção, certifique-se de que o playbook esteja testado em um ambiente de desenvolvimento antes de executá-lo no ambiente de produção.
* Se você estiver usando um ambiente de desenvolvimento, certifique-se de que o playbook esteja configurado para se conectar ao servidor correto e executar as tarefas com privilégios elevados.

## repositorio_clonado/ansible/roles/wordpress/tasks/main.yml

# Configuração de Ansible para Instalação e Configuração de WordPress

## Descrição Geral

Este documento descreve como configurar um playbook Ansible para instalar e configurar o WordPress em um servidor Linux. O playbook utiliza a estrutura de módulos Ansible para gerenciar as configurações do servidor e do WordPress.

## Pré-requisitos

- Ansible 2.9 ou superior
- Conta no GitHub
- Projeto WordPress com estrutura de módulos (`wp-config.php`)
- Servidor Linux com Apache, MySQL e PHP instalados

## Estrutura do Playbook `playbook.yml`

```yaml
---
- name: Instalar e configurar WordPress
  hosts: localhost
  become: yes

  tasks:
    - name: Criar um novo repositório que não existe
      file:
        path: /srv/www
        state: directory
        owner: www-data
        group: www-data
      become: yes

    - name: Descompactar arquivos de fora
      unarchive:
        src: https://wordpress.org/latest.tar.gz
        dest: /srv/www
        remote_src: yes
      become: yes

    - name: Copiar e alterar permissões
      template:
        src: templates/wordpress.conf.j2
        dest: /etc/apache2/sites-available/000-default.conf
      become: yes
      notify: 
        - restart apach

    - name: Copiar e alterar permissões
      copy:
        src: '{{wp_dir}}/wp-config-sample.php'
        dest: '{{wp_dir}}/wp-config.php'
        force: no
        remote_src: yes 
      become: yes

    - name: Configurar o wp-config com o banco de dados
      replace:
        path: '{{wp_dir}}/wp-config.php'
        regexp: "{{ item.regexp }}"
        replace: "{{ item.replace }}"
      with_items:
      - { regexp: "database_name_here", replace: "{{wp_db_name}}"}
      - { regexp: "username_here", replace: "{{wp_db_user}}"}
      - { regexp: "password_here", replace: "{{wp_db_passw}}"}
      - { regexp: "localhost", replace: "{{db_ip}}"}
      become: yes

    - name: Trocar o local host buscando por uma string
      lineinfile:
        path: '{{wp_dir}}/wp-config.php'
        search_string: "{{ item.search_string}}"
        line: "{{ item.line }}"
      with_items:
      - { search_string: "define( 'AUTH_KEY',         'put your unique phrase here' );", line: "define('AUTH_KEY',         '.)=68!5A;=@/[]}I`)WWRE!| 1SG1s]z@E5Zr#UQ0g_ieIeh/L#b%f@P8r})Goyi');"}
      - { search_string: "define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );", line: "define('SECURE_AUTH_KEY',  'e.m}h>G.^0R|!JI4CCMvYevy^y5-ghtJKiKXPz)mj[S89gvcy9=+QaK]<eoG@b/d');"}
      - { search_string: "define( 'LOGGED_IN_KEY',    'put your unique phrase here' );", line: "define('LOGGED_IN_KEY',    '{ms>Tms58|}7*02RI88&]OK@a-Mb?1.%%uhhEH zVQJ4@nUL:XlVo@g`T$JBx9Z_');"}
      - { search_string: "define( 'NONCE_KEY',        'put your unique phrase here' );", line: "define('NONCE_KEY',        ' .A@,J:]K^QXCC^&6Z{m`+2g #P,#.EOkw$i,;UFdX<K8wvx,6ytVUCZ_QweH-*)');"}
      - { search_string: "define( 'AUTH_SALT',        'put your unique phrase here' );", line: "define('AUTH_SALT',        '@pU|R3{N>MQAe]f.hKV$|4a4k@-$AUhu-7Q5LJj/z1b[lK@G|n_W|2M~g$dKB9oq');"}
      - { search_string: "define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );", line: "define('SECURE_AUTH_SALT', '(V42q4Gm-erU|uT4M?D:fbG+GG#`|)Llpt;fA=>]zoj|l<94w~S(qbXEg!IVaAJ`');"}
      - { search_string: "define( 'LOGGED_IN_SALT',   'put your unique phrase here' );", line: "define('LOGGED_IN_SALT',   'psd[~aDFK4JI5`_YW[Lo^[Z/*5oCP@]?P#@Vk2,TK&suPt}2KH5F*otp2VXCB|V{');"}
      - { search_string: "define( 'NONCE_SALT',       'put your unique phrase here' );", line: "define('NONCE_SALT',       'ng MO?(l+*f|Xu@-~jL{)!Kw[T/XN@lzM5Q|Nh))#L)J?syf_pkmlyq?sS@rWsb{');"}
      become: yes
```

## Explicação das Tarefas

1. A primeira tarefa cria um novo repositório `/srv/www` com permissões corretas.
2. A segunda tarefa descompacta o arquivo de WordPress em `/srv/www`.
3. A terceira tarefa copia o arquivo de configuração do Apache e altera as permissões.
4. A quarta tarefa copia o arquivo `wp-config-sample.php` para `wp-config.php` e altera as permissões.
5. A quinta tarefa substitui as variáveis de configuração do WordPress com as informações fornecidas.
6. A sexta tarefa substitui as strings de configuração do WordPress com as informações fornecidas.

## Conclusão

Este playbook Ansible configura o WordPress em um servidor Linux e substitui as variáveis de configuração com as informações fornecidas. O playbook utiliza a estrutura de módulos Ansible para gerenciar as configurações do servidor e do WordPress.

## repositorio_clonado/ansible/roles/wordpress/meta/main.yml

Aqui está a documentação técnica comentada, em português, sobre a estrutura de pipeline CI/CD com GitHub Actions para aplicações em Go:

---

# Configuração de Pipeline CI/CD com GitHub Actions para Aplicações em Go

## Descrição Geral

Este documento descreve como configurar um pipeline de integração contínua (CI) usando o GitHub Actions para aplicações desenvolvidas em Go. O pipeline realiza testes automatizados a cada push na branch `main`.

## Pré-requisitos

- Conta no GitHub
- Projeto Go com estrutura de módulos (`go.mod`)
- GitHub Actions habilitado no repositório

## Estrutura do Workflow `.github/workflows/go.yml`

O arquivo `go.yml` é o arquivo de configuração do workflow do GitHub Actions. Ele define como o pipeline será executado e quais são as etapas que compõem o processo de integração contínua.

```yaml
name: Go CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Setup Go
        uses: actions/setup-go@v4
        with:
          go-version: 1.21
      - name: Run tests
        run: go test ./...
```

**Explicação da estrutura do workflow**

* `name`: Define o nome do workflow, que é "Go CI" nesse caso.
* `on`: Define quando o workflow será executado. Nesse caso, o workflow será executado a cada push na branch `main` e a cada pull request na branch `main`.
* `jobs`: Define a lista de tarefas que compõem o workflow. Nesse caso, há apenas uma tarefa chamada `build`.
* `build`: Define a tarefa `build`. Ela é executada no ambiente `ubuntu-latest`.
* `steps`: Define a lista de etapas que compõem a tarefa `build`. Nesse caso, há três etapas:
	+ `uses: actions/checkout@v3`: Faz o checkout do repositório no ambiente de build.
	+ `name: Setup Go`: Configura o ambiente de build com a versão do Go 1.21.
	+ `name: Run tests`: Executa os testes automatizados da aplicação com o comando `go test ./...`.

**Boas práticas DevOps**

* ✅ Utilize o GitHub Actions para automatizar a integração contínua e entrega contínua de sua aplicação em Go.
* ✅ Certifique-se de que o ambiente de build esteja configurado corretamente para que os testes sejam executados com sucesso.
* ✅ Utilize o `go test` para executar os testes automatizados da aplicação.

**Avisos e erros críticos**

🛑 Certifique-se de que o repositório esteja configurado corretamente para que o GitHub Actions possa acessá-lo.

## repositorio_clonado/ansible/roles/wordpress/handlers/main.yml

# Automação de Serviço com Docker e Ansible

## Descrição Geral

Este documento descreve como automatizar o restart do serviço Apache2 com Ansible e Docker. A automação é realizada utilizando um contêiner Docker que executa um script Ansible para restartar o serviço Apache2.

## Pré-requisitos

- Docker instalado na máquina local
- Ansible instalado na máquina local
- Serviço Apache2 configurado e rodando na máquina local

## Estrutura do Script Ansible `playbook.yml`

```yaml
---
- name: Restart Apache2 Service
  hosts: localhost
  become: yes

  tasks:
  - name: Restart Apache2 Service
    service:
      name: apache2
      state: restarted
```

## Explicação do Script Ansible

O script Ansible é composto por uma única tarefa que utiliza o módulo `service` para restartar o serviço Apache2. O parâmetro `name` especifica o nome do serviço a ser restartado, e o parâmetro `state` especifica que o serviço deve ser restartado.

## Execução do Script Ansible com Docker

Para executar o script Ansible com Docker, você precisará criar um contêiner Docker que execute o script Ansible. Isso pode ser feito utilizando o comando a seguir:
```bash
docker run -it --rm ansible /bin/sh -c "ansible-playbook -i localhost, playbook.yml"
```
Este comando cria um contêiner Docker com o nome `ansible` e executa o script Ansible `playbook.yml` dentro do contêiner. O parâmetro `-i localhost,` especifica que o host Ansible é a máquina local, e o parâmetro `playbook.yml` especifica o nome do arquivo de playbook a ser executado.

## Boas Práticas DevOps

✅ Utilize Ansible para automatizar tarefas de configuração e gerenciamento de serviços.

✅ Utilize Docker para criar contêineres isolados e seguros para executar scripts Ansible.

🛑 Certifique-se de que o serviço Apache2 esteja configurado e rodando corretamente antes de executar o script Ansible.

**Observações**

* O script Ansible pode ser personalizado para atender às necessidades específicas do seu ambiente.
* O contêiner Docker pode ser configurado para executar o script Ansible em background, permitindo que o serviço Apache2 seja restartado automaticamente em caso de falha.

## repositorio_clonado/ansible/group_vars/all.yml

# Configuração de Infraestrutura como Código com Terraform e AWS

## Descrição Geral

Este documento descreve como configurar a infraestrutura como código (IaC) para um ambiente de desenvolvimento utilizando o Terraform e a AWS. A configuração inclui a criação de um bucket S3, um grupo de segurança, uma instância EC2 e um banco de dados RDS.

## Pré-requisitos

- Conta na AWS
- Terraform instalado na máquina local
- Credenciais AWS configuradas na máquina local

## Configuração do Terraform

O código Terraform está organizado em um arquivo `main.tf`:
```terraform
# Define the AWS provider
provider "aws" {
  region = "us-east-1"
}

# Create an S3 bucket
resource "aws_s3_bucket" "example" {
  bucket = "example-bucket"
  acl    = "private"
}

# Create a security group
resource "aws_security_group" "example" {
  name        = "example-sg"
  description = "Example security group"
  vpc_id      = "vpc-12345678"

  # Allow inbound traffic on port 22
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create an EC2 instance
resource "aws_instance" "example" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.example.id]
  key_name               = "example-key"
}

# Create an RDS database
resource "aws_db_instance" "example" {
  engine           = "mysql"
  engine_version   = "8.0.23"
  instance_class   = "db.t2.micro"
  vpc_security_group_ids = [aws_security_group.example.id]
  db_subnet_group_name = "example-subnet-group"
  username         = "example-user"
  password         = "example-password"
}
```
## Explicação do Código

* A seção `provider` define o provedor AWS e a região que será utilizada.
* A seção `resource` define as respostas Terraform que serão criadas. Neste caso, são criados um bucket S3, um grupo de segurança, uma instância EC2 e um banco de dados RDS.
* A seção `ingress` define as regras de entrada para o grupo de segurança.
* A seção `aws_instance` define as configurações da instância EC2.
* A seção `aws_db_instance` define as configurações do banco de dados RDS.

## Boas Práticas

* ✅ Utilize variáveis de ambiente para armazenar credenciais AWS e outras informações sensíveis.
* ✅ Utilize recursos Terraform para gerenciar a infraestrutura, em vez de comandos AWS CLI.
* ✅ Utilize tags para rotular as respostas Terraform e facilitar a identificação e gerenciamento.
* 🛑 Certifique-se de que as credenciais AWS sejam configuradas corretamente e que as respostas Terraform sejam executadas com privilégios de usuário comum.

## repositorio_clonado/ansible/group_vars/mysql.yml

# Configuração de Infraestrutura como Código com Terraform para Aplicação em Containers

## Descrição Geral

Este documento descreve como configurar a infraestrutura como código para uma aplicação em containers utilizando o Terraform. O objetivo é provisionar um ambiente de desenvolvimento com um container Docker e um servidor Nginx para servir a aplicação.

## Pré-requisitos

- Terraform instalado na máquina local
- Conta no AWS (ou outro provedor de serviços em nuvem)
- Docker instalado na máquina local

## Estrutura do arquivo de configuração `main.tf`

```terraform
# Configuração do provedor AWS
provider "aws" {
  region = "us-east-1"
}

# Criar um grupo de segurança para o container
resource "aws_security_group" "example" {
  name        = "example-sg"
  description = "Security group for example container"
  vpc_id      = "vpc-12345678"

  # Permite tráfego de entrada na porta 80
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Criar um container Docker
resource "docker_container" "example" {
  name  = "example-container"
  image = "nginx:latest"
  ports = ["80:80"]

  # Atribuir o grupo de segurança criado anteriormente
  security_groups = [aws_security_group.example.id]
}

# Criar um servidor Nginx
resource "aws_instance" "example" {
  ami           = "ami-abc12345"
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.example.id]

  # Configurar o Nginx para servir a aplicação
  user_data = <<EOF
#!/bin/bash
sudo yum install -y nginx
sudo tee /etc/nginx/nginx.conf > /dev/null <<EOF
http {
  server {
    listen 80;
    location / {
      proxy_pass http://localhost:8080;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
    }
  }
}
EOF
EOF
}
```

## Justificativas Técnicas

* O Terraform é escolhido por sua capacidade de gerenciar infraestrutura como código, permitindo a reproducibilidade e a automatização do processo de provisionamento.
* O grupo de segurança é criado para controlar o tráfego de entrada na porta 80 do container.
* O container Docker é criado com a imagem Nginx mais recente e atribuído ao grupo de segurança criado anteriormente.
* O servidor Nginx é criado com a imagem mais recente e configurado para servir a aplicação.

## Boas Práticas DevOps

✅ Utilize o Terraform para gerenciar a infraestrutura como código.
✅ Utilize o Docker para containerizar a aplicação.
✅ Utilize o Nginx como servidor web para servir a aplicação.
🛑 Verifique se o grupo de segurança está configurado corretamente para evitar acessos indevidos à aplicação.

## repositorio_clonado/ansible/group_vars/wordpress.yml

# Configuração de Infraestrutura como Código com Terraform para Aplicação em Go

## Descrição Geral

Este documento descreve como configurar a infraestrutura como código para uma aplicação em Go utilizando o Terraform. A configuração define um servidor web com um banco de dados MySQL e um container Docker para a aplicação.

## Pré-requisitos

- Terraform instalado na máquina local
- Conta no GitHub para armazenar o código de infraestrutura
- Docker instalado na máquina local

## Estrutura do Código de Infraestrutura `main.tf`

```terraform
# Configuração do provedor de nuvem AWS
provider "aws" {
  region = "us-east-1"
}

# Criar um grupo de segurança para o servidor web
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web server"

  # Permite tráfego HTTP e HTTPS
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Permite tráfego SSH
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Criar um servidor web com um container Docker
resource "aws_instance" "web" {
  ami           = "ami-0c94855ba95c71c99"
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.web.id]

  # Configuração do container Docker
  user_data = <<EOF
#!/bin/bash
sudo docker run -d --name wordpress \
  -p 8080:80 \
  -e WORDPRESS_DB_HOST=${db_ip} \
  -e WORDPRESS_DB_USER=wordpress \
  -e WORDPRESS_DB_PASSWORD=wordpress \
  wordpress:latest
EOF
}

# Configuração do banco de dados MySQL
resource "aws_rds_instance" "db" {
  engine           = "mysql"
  engine_version   = "8.0.21"
  instance_class   = "db.t2.micro"
  vpc_security_group_ids = [aws_security_group.web.id]
  db_name         = "wordpress"
  db_instance_identifier = "wordpress-db"
  db_username     = "wordpress"
  db_password     = "wordpress"
}
```

## Justificativas Técnicas

* O provedor de nuvem AWS é escolhido por ser uma opção popular e escalável.
* O grupo de segurança é criado para permitir tráfego HTTP, HTTPS e SSH.
* O servidor web é criado com um container Docker para isolamento e portabilidade.
* O banco de dados MySQL é criado com uma instância RDS para escalabilidade e segurança.

## Boas Práticas DevOps

* O código de infraestrutura é versionado no GitHub para controle de versões e colaboração.
* O Terraform é usado para definir a infraestrutura como código, permitindo a reproducibilidade e a automatização da configuração.
* O Docker é usado para criar containers isolados e portáteis.
* O AWS RDS é usado para criar um banco de dados gerenciado e escalável.

✅ Lembre-se de substituir `db_ip` com o IP da máquina do banco de dados.

