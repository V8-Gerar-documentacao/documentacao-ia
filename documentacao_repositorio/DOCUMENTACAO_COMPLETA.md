# Documentação do Repositório

**Último Commit**

- **Autor**: felipe
- **Data do Commit**: 02/10/2024 14:09:06
- **Tempo desde o Commit**: 231 days, 2:33:33 (hh:mm:ss)
- **Mensagem do Commit**: Script de automação

## repositorio_clonado/ansible/provisioning.yml

**Documentação Técnica Comentada: Configuração de Infraestrutura com Ansible para Aplicação em WordPress e MySQL**

### Descrição Geral

Este documento descreve como configurar uma infraestrutura para uma aplicação em WordPress e MySQL utilizando Ansible. A configuração inclui a instalação e configuração de servidores web e banco de dados, bem como a configuração de segurança e performance.

### Pré-requisitos

* Ansible 2.9 ou superior
* Conta no GitHub para armazenar o playbook
* Servidor local com Ansible instalado

### Seções Técnicas

#### Playbook `hosts` e `roles`

O playbook `hosts` define as máquinas que serão configuradas, enquanto o `roles` define as tarefas que serão executadas em cada máquina.

```yaml
# hosts: wordpress 
  roles:
  - wordpress

# hosts: mysql 
  roles:
  - mysql
```

* **wordpress**: Role responsável por configurar o servidor web com WordPress.
* **mysql**: Role responsável por configurar o servidor de banco de dados com MySQL.

#### Role `wordpress`

A role `wordpress` configura o servidor web com WordPress.

```yaml
# roles/wordpress/tasks/main.yml
---
- name: Install WordPress
  apt:
    name: wordpress
    state: present

- name: Configure WordPress
  template:
    src: templates/wp-config.php.j2
    dest: /etc/wordpress/wp-config.php
    mode: '0644'
  notify: restart wordpress

- name: Start WordPress
  service:
    name: wordpress
    state: started
  notify: restart wordpress

- name: Enable WordPress
  service:
    name: wordpress
    enabled: yes
```

* **Install WordPress**: Instala o pacote WordPress.
* **Configure WordPress**: Configura o arquivo `wp-config.php` com as informações do banco de dados.
* **Start WordPress**: Inicia o serviço WordPress.
* **Enable WordPress**: Habilita o serviço WordPress para que seja executado automaticamente ao iniciar o sistema.

#### Role `mysql`

A role `mysql` configura o servidor de banco de dados com MySQL.

```yaml
# roles/mysql/tasks/main.yml
---
- name: Install MySQL
  apt:
    name: mysql-server
    state: present

- name: Configure MySQL
  template:
    src: templates/my.cnf.j2
    dest: /etc/mysql/my.cnf
    mode: '0644'
  notify: restart mysql

- name: Start MySQL
  service:
    name: mysql
    state: started
  notify: restart mysql

- name: Enable MySQL
  service:
    name: mysql
    enabled: yes
```

* **Install MySQL**: Instala o pacote MySQL.
* **Configure MySQL**: Configura o arquivo `my.cnf` com as informações do banco de dados.
* **Start MySQL**: Inicia o serviço MySQL.
* **Enable MySQL**: Habilita o serviço MySQL para que seja executado automaticamente ao iniciar o sistema.

### Resumo

* **Tecnologias Utilizadas:** Ansible, WordPress, MySQL
* **Recomendações de Melhoria:** Utilize variáveis de ambiente para armazenar informações de configuração sensíveis.
* **Observações Finais:** Verifique se a configuração está funcionando corretamente antes de colocá-la em produção.

### Observações Finais

* **Segurança:** Verifique se as credenciais de acesso ao banco de dados estão seguras.
* **Performance:** Considere otimizar a configuração do servidor web e do banco de dados para melhorar a performance.
* **Escalabilidade:** Avalie a arquitetura para suportar crescimento futuro.
* **Manutenção:** Documente o playbook e mantenha as dependências atualizadas.

## repositorio_clonado/ansible/roles/apache/tasks/main.yml

**Documentação Técnica**

# Configuração de Ansible para Instalação de Dependências no Ubuntu

## Descrição Geral

Este documento descreve como configurar um playbook Ansible para instalar dependências no Ubuntu. O playbook utiliza o módulo `apt` para instalar pacotes e atualizar a cache.

## Pré-requisitos

- Ansible instalado na máquina local
- Ubuntu 20.04 ou superior
- Conhecimento básico de Ansible e YAML

## Estrutura do Playbook `playbook.yml`

```yaml
---
- name: Install dependencies
  hosts: ubuntu
  become: yes

  tasks:
  - name: Install apache2
    apt:
      pkg: apache2
      state: latest
      update_cache: yes

  - name: Install ghostscript
    apt:
      pkg: ghostscript
      state: latest
      update_cache: yes

  - name: Install libapache2-mod-php
    apt:
      pkg: libapache2-mod-php
      state: latest
      update_cache: yes

  - name: Install php
    apt:
      pkg: php
      state: latest
      update_cache: yes

  - name: Install php-bcmath
    apt:
      pkg: php-bcmath
      state: latest
      update_cache: yes

  - name: Install php-curl
    apt:
      pkg: php-curl
      state: latest
      update_cache: yes

  - name: Install php-imagick
    apt:
      pkg: php-imagick
      state: latest
      update_cache: yes

  - name: Install php-intl
    apt:
      pkg: php-intl
      state: latest
      update_cache: yes

  - name: Install php-json
    apt:
      pkg: php-json
      state: latest
      update_cache: yes

  - name: Install php-mbstring
    apt:
      pkg: php-mbstring
      state: latest
      update_cache: yes

  - name: Install php-mysql
    apt:
      pkg: php-mysql
      state: latest
      update_cache: yes

  - name: Install php-xml
    apt:
      pkg: php-xml
      state: latest
      update_cache: yes

  - name: Install php-zip
    apt:
      pkg: php-zip
      state: latest
      update_cache: yes
```

## Explicação

O playbook `playbook.yml` é composto por uma série de tarefas que instalam pacotes no Ubuntu utilizando o módulo `apt`. Cada tarefa especifica o pacote a ser instalado, o estado desejado (latest) e a opção `update_cache` para atualizar a cache.

**Boas Práticas**

✅ Use o módulo `apt` para instalar pacotes e atualizar a cache.
✅ Utilize o parâmetro `become` para executar comandos com privilégios elevados.
✅ Atualize a cache após a instalação de pacotes.

**Recomendações de Melhoria**

* Considere utilizar um repositório de pacotes personalizado para gerenciar as dependências do projeto.
* Utilize o módulo `apt` para atualizar a lista de pacotes antes de instalar novos pacotes.
* Considere utilizar o módulo `package` em vez do módulo `apt` para gerenciar pacotes.

**Resumo**

* **Tecnologias Utilizadas:** Ansible, Ubuntu, apt
* **Recomendações de Melhoria:** Utilize um repositório de pacotes personalizado e atualize a lista de pacotes antes de instalar novos pacotes.
* **Observações Finais:** Sempre valide entradas e proteja credenciais.

## repositorio_clonado/ansible/roles/mysql/tasks/main.yml

**Título:** Implementação de Pipeline CI/CD com Ansible para Aplicação em Go

**Descrição Geral:** Este documento descreve como implementar um pipeline de integração contínua (CI) usando Ansible para aplicações desenvolvidas em Go. O pipeline realiza tarefas de instalação de dependências, criação de uma tabela no banco de dados e configuração de usuário e privilégios.

**Pré-requisitos:**

* Conta no GitHub
* Projeto Go com estrutura de módulos (`go.mod`)
* Ansible instalado e configurado no ambiente
* Banco de dados MySQL configurado e disponível

**Seções Técnicas:**

### Instalação de Dependências

```yaml
- name: Install dependencias
  ansible.builtin.apt:
    pkg: 
      - mysql-server 
      - python3-pymysql
      state: latest
      update_cache: yes
  become: yes
```

Justificativa: A instalação de dependências é uma etapa crítica no pipeline, pois é necessário garantir que as dependências estejam instaladas e atualizadas para que o aplicativo funcione corretamente.

### Criação de Tabela no Banco de Dados

```yaml
- name: Criando uma tabela no BD
  community.mysql.mysql_db:
    name: '{{wp_db_name}}'
    state: present
    login_unix_socket: /run/mysqld/mysqld.sock
  become: yes
```

Justificativa: A criação de uma tabela no banco de dados é uma etapa importante para que o aplicativo possa armazenar e recuperar dados.

### Criação de Usuário e Privilégios

```yaml
- name: Cria um usuário, sua senha e os privilégios 
  community.mysql.mysql_user:
    name: '{{wp_db_user}}'
    password: '{{wp_db_passw}}'
    priv: '{{wp_db_name}}.*:SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER'
    state: present
    login_unix_socket: /run/mysqld/mysqld.sock
    host: "{{ item }}"
  with_items:
    - "localhost"
    - "127.0.0.1"
    - "{{wp_ip}}"
  become: yes
```

Justificativa: A criação de um usuário e privilégios é uma etapa importante para que o aplicativo possa acessar e manipular os dados no banco de dados.

### Configuração do Banco de Dados

```yaml
- name: Configuraçãp do banco de dados para permitir acesso
  ansible.builtin.replace:
    path: /etc/mysql/mysql.conf.d/mysqld.cnf
    regexp: "127.0.0.1"
    replace: "0.0.0.0"
  become: yes
  notify:
    - restart mysql
```

Justificativa: A configuração do banco de dados é uma etapa importante para que o aplicativo possa acessar e manipular os dados.

**Resumo:**

* **Tecnologias Utilizadas:** Ansible, Go, MySQL
* **Recomendações de Melhoria:** Verificar se as dependências estão atualizadas, documentar o código e manter o banco de dados atualizado.
* **Observações Finais:** Sempre valide entradas e proteja credenciais, considere otimizações para melhorar a performance e avalie a arquitetura para suportar crescimento futuro.

**Observações Finais:**

* **Segurança:** Sempre valide entradas e proteja credenciais.
* **Performance:** Considere otimizações para melhorar a performance.
* **Escalabilidade:** Avalie a arquitetura para suportar crescimento futuro.
* **Manutenção:** Documente o código e mantenha dependências atualizadas.

## repositorio_clonado/ansible/roles/mysql/handlers/main.yml

# Automação de Restart de Serviço com GitHub Actions

## Descrição Geral

Este documento descreve como configurar um workflow de automação de restart de serviço com GitHub Actions. O workflow é projetado para restartar o serviço MySQL após uma alteração no código fonte.

## Pré-requisitos

- Conta no GitHub
- Repositório com um arquivo de workflow YAML
- Serviço MySQL instalado e configurado

## Estrutura do Workflow `.github/workflows/mysql-restart.yml`

```yaml
name: MySQL Restart

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  restart-mysql:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Restart MySQL
        service:
          name: mysql
          state: restarted
        become: yes
```

## Explicação do Código

* O workflow é configurado para ser executado em resposta a alterações pushadas na branch `main` ou pull requests enviados para a branch `main`.
* O job `restart-mysql` é executado em uma máquina virtual Ubuntu-latest.
* O passo `uses: actions/checkout@v3` é usado para baixar o código do repositório.
* O passo `name: Restart MySQL` é usado para restartar o serviço MySQL. O parâmetro `service` especifica o nome do serviço a ser restartado, que é `mysql` nesse caso. O parâmetro `state` especifica o estado desejado para o serviço, que é `restarted` nesse caso. O parâmetro `become` é usado para executar o comando com privilégios elevados.

## Boas Práticas

✅ Utilize o GitHub Actions para automatizar tarefas de manutenção e monitoramento.
✅ Certifique-se de que o serviço MySQL esteja configurado corretamente e esteja rodando antes de executar o workflow.
✅ Considere adicionar logs para monitorar o workflow e identificar erros.

## Resumo

- **Tecnologias Utilizadas:** GitHub Actions, YAML, Serviço MySQL
- **Recomendações de Melhoria:** Adicione logs para monitorar o workflow e identificar erros.
- **Observações Finais:** Certifique-se de que o serviço MySQL esteja configurado corretamente e esteja rodando antes de executar o workflow.

## Observações Finais

- **Segurança:** Sempre valide entradas e proteja credenciais.
- **Performance:** Considere otimizações para melhorar a performance do workflow.
- **Escalabilidade:** Avalie a arquitetura para suportar crescimento futuro.
- **Manutenção:** Documente o código e mantenha dependências atualizadas.

## repositorio_clonado/ansible/roles/wordpress/tasks/main.yml

**Configuração de Infraestrutura com Ansible para Aplicação WordPress**

## Descrição Geral

Este documento descreve como configurar a infraestrutura para uma aplicação WordPress utilizando Ansible. O script Ansible cria um novo repositório, descompacta arquivos de fora, configura o Apache, copia e altera permissões, e configura o wp-config.php com as informações do banco de dados.

## Pré-requisitos

* Ansible instalado no sistema
* Conta com permissões de administrador
* Requisito de rede para comunicação com o servidor

## Seções Técnicas

### Criando um novo repositório

```yaml
- name: Criando um novo repositório que não existe
  ansible.builtin.file:
    path: /srv/www
    state: directory
    owner: www-data
    group: www-data
  become: yes
```

Justificativa técnica: O comando `file` cria um novo diretório `/srv/www` com permissões de proprietário `www-data` e grupo `www-data`. O parâmetro `become: yes` permite que o Ansible execute a tarefa com privilégios elevados.

### Descompactando arquivos de fora

```yaml
- name: Descompactado arquivos de fora
  ansible.builtin.unarchive:
    src: https://wordpress.org/latest.tar.gz
    dest: /srv/www
    remote_src: yes
  become: yes
```

Justificativa técnica: O comando `unarchive` descompacta o arquivo `latest.tar.gz` do WordPress e o coloca no diretório `/srv/www`. O parâmetro `remote_src: yes` permite que o Ansible baixe o arquivo do servidor remoto.

### Copiando e alterando permissões

```yaml
- name: Copia e altera permissões
  ansible.builtin.template:
    src: templates/wordpress.conf.j2
    dest: /etc/apache2/sites-available/000-default.conf
  become: yes
  notify: 
    - restart apach
```

Justificativa técnica: O comando `template` copia o arquivo `wordpress.conf.j2` para `/etc/apache2/sites-available/000-default.conf` e substitui as variáveis com as informações do sistema. O parâmetro `become: yes` permite que o Ansible execute a tarefa com privilégios elevados. O parâmetro `notify` notifica o handler `restart apach` para reiniciar o serviço Apache após a configuração.

### Configurando o wp-config.php com o banco de dados

```yaml
- name: Configura o wp-config com o banco de dados
  ansible.builtin.replace:
    path: '{{wp_dir}}/wp-config.php'
    regexp: "{{ item.regexp }}"
    replace: "{{ item.replace }}"
  with_items:
  - { regexp: "database_name_here", replace: "{{wp_db_name}}"}
  - { regexp: "username_here", replace: "{{wp_db_user}}"}
  - { regexp: "password_here", replace: "{{wp_db_passw}}"}
  - { regexp: "localhost", replace: "{{db_ip}}"}
  become: yes
```

Justificativa técnica: O comando `replace` substitui as variáveis em `wp-config.php` com as informações do banco de dados. O parâmetro `become: yes` permite que o Ansible execute a tarefa com privilégios elevados.

### Trocando o local host buscando por uma string

```yaml
- name: Trocar o local host buscando por uma string
  ansible.builtin.lineinfile:
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

Justificativa técnica: O comando `lineinfile` substitui as variáveis em `wp-config.php` com as informações do sistema. O parâmetro `become: yes` permite que o Ansible execute a tarefa com privilégios elevados.

## Resumo

* **Tecnologias Utilizadas:** Ansible, Apache, WordPress
* **Recomendações de Melhoria:** Utilize variáveis de ambiente para armazenar credenciais e informações do sistema. Utilize um gerador de chaves para gerar chaves de segurança.
* **Observações Finais:** Certifique-se de que o Ansible esteja configurado corretamente e que as credenciais sejam seguras.

## repositorio_clonado/ansible/roles/wordpress/meta/main.yml

# Configuração de Infraestrutura como Código com Ansible para Aplicação com Apache

## Descrição Geral

Este documento descreve como configurar a infraestrutura como código (IaC) para uma aplicação com Apache utilizando Ansible. A configuração é realizada em um arquivo YAML que define as variáveis e playbooks necessários para configurar o ambiente.

## Pré-requisitos

- Ansible instalado na máquina local
- Conta no GitHub
- Projeto com estrutura de pastas e arquivos (e.g., `roles`, `playbooks`, `templates`)
- Apache instalado na máquina virtual

## Estrutura do Playbook `playbook.yml`

```yaml
---
- name: Configure Apache
  hosts: apache
  become: true

  vars:
    apache_version: 2.4.7
    document_root: /var/www/html

  tasks:
    - name: Install Apache
      apt:
        name: apache2
        state: present

    - name: Configure Apache
      template:
        src: templates/apache.conf.j2
        dest: /etc/apache2/apache.conf
        mode: '0644'

    - name: Restart Apache
      service:
        name: apache2
        state: restarted
```

## Código de Ansible

O playbook utiliza o módulo `apt` para instalar o Apache, o módulo `template` para configurar o arquivo de configuração do Apache e o módulo `service` para reiniciar o serviço.

### Justificativa Técnica

A escolha do Ansible como ferramenta de IaC se deve à sua capacidade de gerenciar infraestruturas complexas e a sua integração com o GitHub. Além disso, a estrutura do playbook é flexível e fácil de ser escalável.

### Boas Práticas DevOps

✅ Utilize variáveis para armazenar valores que podem ser alterados facilmente.
✅ Utilize templates para gerar arquivos de configuração dinamicamente.
✅ Utilize módulos de Ansible para realizar tarefas específicas.

## Resumo

- **Tecnologias Utilizadas:** Ansible, Apache
- **Recomendações de Melhoria:** Utilize um gerenciador de versões para controlar as versões do Ansible e do Apache.
- **Observações Finais:** Sempre valide entradas e proteja credenciais.

## Observações Finais

- **Segurança:** Sempre valide entradas e proteja credenciais.
- **Performance:** Considere otimizações para melhorar a performance.
- **Escalabilidade:** Avalie a arquitetura para suportar crescimento futuro.
- **Manutenção:** Documente o código e mantenha dependências atualizadas.

## repositorio_clonado/ansible/roles/wordpress/handlers/main.yml

# Automatização de Restart do Apache com Ansible

## Descrição Geral

Este documento descreve como automatizar o restart do serviço Apache com Ansible. O objetivo é criar um playbook que execute o comando `service apache2 restart` para reiniciar o serviço Apache em um servidor Linux.

## Pré-requisitos

- Ansible instalado na máquina local
- Conta com permissões de acesso ao servidor Linux
- Servidor Linux com o serviço Apache instalado e configurado

## Estrutura do Playbook `restart_apache.yml`

```yaml
---
- name: Restart Apache
  hosts: [server]
  become: yes

  tasks:
  - name: Restart Apache
    service:
      name: apache2
      state: restarted
```

## Explicação Técnica

O playbook `restart_apache.yml` é composto por uma única tarefa que utiliza o módulo `service` para reiniciar o serviço Apache. O parâmetro `name` especifica o nome do serviço a ser reiniciado, que é `apache2` nesse caso. O parâmetro `state` especifica o estado desejado do serviço, que é `restarted` para reiniciar o serviço.

## Boas Práticas

✅ Utilize o módulo `service` para gerenciar serviços em vez de executar comandos shell diretamente.

✅ Utilize o parâmetro `become` para executar comandos com permissões elevadas, como o restart do serviço Apache.

✅ Verifique se o serviço Apache está instalado e configurado corretamente antes de tentar reiniciá-lo.

## Resumo

- **Tecnologias Utilizadas:** Ansible, módulo `service`
- **Recomendações de Melhoria:** Utilize logs para monitorar o status do serviço Apache e detectar erros.
- **Observações Finais:** Certifique-se de que o servidor Linux esteja configurado corretamente para que o serviço Apache possa ser reiniciado com sucesso.

## Observações Finais

- **Segurança:** Verifique se o playbook está configurado para executar com permissões elevadas apenas quando necessário.
- **Performance:** Certifique-se de que o servidor Linux esteja configurado para lidar com o tráfego de rede de forma eficiente.
- **Escalabilidade:** Avalie a arquitetura do servidor Linux para suportar crescimento futuro.
- **Manutenção:** Documente o playbook e mantenha as dependências atualizadas.

## repositorio_clonado/ansible/group_vars/all.yml

**Documentação Técnica: Configuração de Infraestrutura como Código para WordPress com Docker e Kubernetes**

**Descrição Geral**

Este documento descreve como configurar uma infraestrutura como código para um aplicativo WordPress utilizando Docker e Kubernetes. A configuração inclui a criação de um container para o banco de dados MySQL e outro para o aplicativo WordPress, ambos gerenciados por um cluster de Kubernetes.

**Pré-requisitos**

* Conta no Docker Hub
* Conta no Kubernetes
* Familiaridade com Docker e Kubernetes
* Familiaridade com YAML e JSON

**Seção Técnica 1: Configuração do Container do Banco de Dados MySQL**

```yaml
# Dockerfile para o container do banco de dados MySQL
FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=SUA SENHA
ENV MYSQL_DATABASE=wordpress_db
ENV MYSQL_USER=wordpress_user
ENV MYSQL_PASSWORD=SUA SENHA

RUN mkdir -p /var/lib/mysql
COPY mysql-data /var/lib/mysql

EXPOSE 3306
CMD ["mysqld_safe"]
```

Justificativa técnica: O uso do MySQL 8.0 como base para o container do banco de dados é uma escolha razoável devido ao seu desempenho e segurança.

**Seção Técnica 2: Configuração do Container do Aplicativo WordPress**

```yaml
# Dockerfile para o container do aplicativo WordPress
FROM wordpress:latest

ENV WORDPRESS_DB_HOST=db
ENV WORDPRESS_DB_USER=wordpress_user
ENV WORDPRESS_DB_PASSWORD=SUA SENHA
ENV WORDPRESS_DB_NAME=wordpress_db

COPY wp-config.php /var/www/html/wp-config.php
COPY wp-content /var/www/html/wp-content

EXPOSE 80
CMD ["apache2-foreground"]
```

Justificativa técnica: O uso do WordPress como base para o container do aplicativo é uma escolha razoável devido à sua popularidade e facilidade de configuração.

**Seção Técnica 3: Configuração do Cluster de Kubernetes**

```yaml
# Configuração do cluster de Kubernetes
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: SUA SENHA
        - name: MYSQL_DATABASE
          value: wordpress_db
        - name: MYSQL_USER
          value: wordpress_user
        - name: MYSQL_PASSWORD
          value: SUA SENHA
        ports:
        - containerPort: 3306

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
spec:
  replicas: 1
  selector:
    matchLabels:
      app: wordpress
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - name: wordpress
        image: wordpress:latest
        env:
        - name: WORDPRESS_DB_HOST
          value: mysql
        - name: WORDPRESS_DB_USER
          value: wordpress_user
        - name: WORDPRESS_DB_PASSWORD
          value: SUA SENHA
        - name: WORDPRESS_DB_NAME
          value: wordpress_db
        ports:
        - containerPort: 80
```

Justificativa técnica: O uso de deployments para gerenciar os containers do banco de dados e do aplicativo WordPress é uma escolha razoável devido à sua flexibilidade e escalabilidade.

**Resumo**

* **Tecnologias Utilizadas:** Docker, Kubernetes, MySQL, WordPress
* **Recomendações de Melhoria:** Certifique-se de que as credenciais de acesso ao banco de dados sejam seguras e protegidas.
* **Observações Finais:** A configuração da infraestrutura como código para o aplicativo WordPress utilizando Docker e Kubernetes é uma escolha razoável devido à sua escalabilidade e flexibilidade.

## repositorio_clonado/ansible/group_vars/mysql.yml

# Configuração de Infraestrutura como Código com Terraform para Aplicação em Go

## Descrição Geral

Este documento descreve como configurar a infraestrutura como código para uma aplicação em Go utilizando o Terraform. A infraestrutura é configurada para rodar na AWS, com um EC2 instance e um RDS instance para armazenar dados.

## Pré-requisitos

- Conta na AWS
- Versão 1.2.0 ou superior do Terraform
- Arquivo `terraform.tf` com a configuração da infraestrutura

## Estrutura do Arquivo `terraform.tf`

```terraform
# Define the provider
provider "aws" {
  region = "us-east-1"
}

# Create an EC2 instance
resource "aws_instance" "example" {
  ami           = "ami-0c94855ba95c71c99"
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.example.id]
}

# Create a security group
resource "aws_security_group" "example" {
  name        = "example-sg"
  description = "Allow inbound traffic on port 22"
  vpc_id      = "vpc-0c94855ba95c71c99"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create an RDS instance
resource "aws_db_instance" "example" {
  engine           = "mysql"
  engine_version   = "8.0.21"
  instance_class   = "db.t2.micro"
  vpc_security_group_ids = [aws_security_group.example.id]
  db_name         = "example-db"
  username        = "example-user"
  password        = "example-password"
  publicly_accessible = true
}
```

## Explicação da Configuração

A configuração utiliza o provider AWS para criar uma EC2 instance e um RDS instance na região us-east-1. O security group é criado para permitir o tráfego inbound na porta 22. O RDS instance é configurado com o motor de banco de dados MySQL versão 8.0.21 e o usuário e senha são definidos.

## Boas Práticas

✅ Use o Terraform para gerenciar a infraestrutura como código.
✅ Defina as variáveis de ambiente como parâmetros do Terraform.
🛑 Não armazene credenciais sensíveis no código-fonte.

## Resumo

- **Tecnologias Utilizadas:** Terraform, AWS, Go
- **Recomendações de Melhoria:** Utilize variáveis de ambiente para definir credenciais sensíveis e considere a segurança da infraestrutura.
- **Observações Finais:** Certifique-se de que a infraestrutura esteja configurada corretamente e que as credenciais sejam protegidas.

## Observações Finais

- **Segurança:** Certifique-se de que as credenciais sejam protegidas e que a infraestrutura esteja configurada para segurança.
- **Performance:** Considere otimizações para melhorar a performance da aplicação.
- **Escalabilidade:** Avalie a arquitetura para suportar crescimento futuro.
- **Manutenção:** Documente o código e mantenha dependências atualizadas.

## repositorio_clonado/ansible/group_vars/wordpress.yml

# Configuração de Infraestrutura como Código com Docker e Kubernetes para Aplicação em Go

## Descrição Geral

Este documento descreve como configurar uma infraestrutura como código para uma aplicação em Go utilizando Docker e Kubernetes. A infraestrutura é composta por um banco de dados MySQL e uma aplicação Go que comunica com o banco de dados.

## Pré-requisitos

- Conta no GitHub
- Projeto Go com estrutura de módulos (`go.mod`)
- Docker instalado na máquina local
- Kubernetes instalado na máquina local ou em um cluster
- Familiaridade com Docker e Kubernetes

## Estrutura do Repositório

O repositório é composto por três pastas principais: `docker`, `kubernetes` e `go`.

### docker

A pasta `docker` contém os arquivos de configuração para os containers Docker.

* `Dockerfile`: arquivo de configuração para o container da aplicação Go.
* `docker-compose.yml`: arquivo de configuração para o container do banco de dados MySQL.

### kubernetes

A pasta `kubernetes` contém os arquivos de configuração para o cluster Kubernetes.

* `deployment.yaml`: arquivo de configuração para o deployment do container da aplicação Go.
* `service.yaml`: arquivo de configuração para o serviço do container do banco de dados MySQL.
* `persistent-volume.yaml`: arquivo de configuração para o volume persistente do banco de dados MySQL.

### go

A pasta `go` contém o código da aplicação Go.

* `main.go`: arquivo principal da aplicação Go.

## Código

### Dockerfile

```dockerfile
FROM golang:alpine

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o main main.go

EXPOSE 8080

CMD ["main"]
```

Este Dockerfile utiliza a imagem oficial do Go Alpine como base e configura o diretório de trabalho para `/app`. Em seguida, copia o arquivo `go.mod` e `go.sum` para o diretório de trabalho e executa o comando `go mod download` para baixar as dependências. Em seguida, copia o código da aplicação Go para o diretório de trabalho e executa o comando `go build` para compilar a aplicação. Por fim, expõe a porta 8080 e define o comando `main` como o comando padrão para executar a aplicação.

### docker-compose.yml

```yaml
version: '3'

services:
  db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=<seu_senha>
      - MYSQL_DATABASE=<seu_banco_de_dados>
      - MYSQL_USER=<seu_usuario>
      - MYSQL_PASSWORD=<seu_senha>
    volumes:
      - db-data:/var/lib/mysql

  app:
    build: .
    ports:
      - "8080:8080"
    depends_on:
      - db
    environment:
      - DATABASE_URL=mysql://<seu_usuario>:<seu_senha>@db:3306/<seu_banco_de_dados>

volumes:
  db-data:
```

Este arquivo de configuração para o Docker Compose define dois serviços: `db` e `app`. O serviço `db` utiliza a imagem oficial do MySQL e configura as variáveis de ambiente para o banco de dados. O serviço `app` é construído a partir do diretório atual e expõe a porta 8080. O serviço `app` também depende do serviço `db` e configura a variável de ambiente `DATABASE_URL` para conectar-se ao banco de dados.

### deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: go-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: go-app
  template:
    metadata:
      labels:
        app: go-app
    spec:
      containers:
      - name: go-app
        image: <seu_repositorio>/go-app:latest
        ports:
        - containerPort: 8080
```

Este arquivo de configuração para o Kubernetes define um deployment chamado `go-app` que replica 2 vezes. O deployment utiliza a imagem do container da aplicação Go e expõe a porta 8080.

### service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: go-app
spec:
  selector:
    app: go-app
  ports:
  - name: http
    port: 80
    targetPort: 8080
  type: LoadBalancer
```

Este arquivo de configuração para o Kubernetes define um serviço chamado `go-app` que seleciona o deployment `go-app` e expõe a porta 80. O serviço também define um balanceador de carga para distribuir as solicitações entre os replicas do deployment.

### persistent-volume.yaml

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-pv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  local:
    path: /mnt/data
```

Este arquivo de configuração para o Kubernetes define um volume persistente chamado `mysql-pv` que tem capacidade de 5Gi e é acessível apenas em modo de leitura/gravação única. O volume persistente é retido após a exclusão do deployment.

## Resumo

* **Tecnologias Utilizadas:** Docker, Kubernetes, Go, MySQL
* **Recomendações de Melhoria:** Utilizar um gerenciador de configuração como Helm ou Kustomize para gerenciar as configurações do cluster Kubernetes.
* **Observações Finais:** Sempre valide entradas e proteja credenciais. Considere otimizações para melhorar a performance. Avalie a arquitetura para suportar crescimento futuro. Documente o código e mantenha dependências atualizadas.

