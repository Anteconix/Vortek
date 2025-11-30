# Plataforma Vortek – Sistema Integrado de Consultoria Financeira, TI e Produções

## PAC
**Projeto de Aprendizagem Colaborativa Extensionista do Curso de Engenharia de Software da Católica de Santa Catarina.**

### Autores
- **Bryann Lucas Locatelli**
- **Carlos Magno Dutra Filho**

### Professores Orientadores
- **Luiz Carlos Camargo**
- **Claudinei Dias**

---

## Justificativa do PAC perante a entidade beneficiada — Vortek
A empresa **Vortek** atua em três áreas distintas: **consultoria e gestão de criptomoedas**, **serviços de infraestrutura e suporte técnico de TI**, e **produções audiovisuais, incluindo fotografia e filmagem profissional**.

Atualmente, os serviços são oferecidos de forma descentralizada e manual, dificultando a comunicação com os clientes, a gestão das solicitações e a apresentação dos produtos. Essa fragmentação gera gargalos operacionais e cria uma experiência inconsistente para o usuário final.

O presente projeto busca solucionar esse problema por meio da construção de uma **plataforma digital unificada**, que centralize todos os serviços da Vortek em um único ambiente de fácil uso e responsivo. Assim, o PAC contribui diretamente para a **modernização da entidade beneficiada**, promovendo eficiência, escalabilidade e melhor atendimento aos clientes.

---

## Descrição do Aplicativo
A plataforma será um sistema web desenvolvido em **Vue.js (frontend)** e **Django (backend)**, utilizando **SQLite** como banco de dados local.

O sistema permitirá que os usuários:
- Criem e gerenciem contas de forma segura
- Acessem e gerenciem seus ativos de criptomoedas
- Simulem transações financeiras
- Busquem informações sobre criptomoedas
- Realizem contatos P2P com outros investidores
- Solicitem suporte técnico de TI
- Visualizem o portfólio da Vortek Produções
- Solicitem cotações de serviços de fotografia, filmagem e suporte de informática
- Consultem postagens e anúncios do administrador
- Atualizem dados da conta

O objetivo central é integrar os três setores da empresa em uma experiência unificada, intuitiva e eficiente.

---

# Requisitos Funcionais

### **RF001 - Registro do usuário (CRUD)**
O sistema deve permitir o registro do usuário no sistema de criptomoedas para ter acesso às funcionalidades.  
Dados: nome, email, senha.

### **RF002 - Autenticação**
O sistema deve permitir autenticação do usuário na página de login.  
Dados: nome de usuário, senha.

### **RF003 - Recuperar senha**
O sistema deve possuir uma função por onde o usuário pode recuperar sua senha.

### **RF004 - Acesso aos ativos**
O sistema deve permitir que o usuário possa acessar seus ativos digitais para gerenciá-los.

### **RF005 - Busca**
O sistema deve permitir a busca de criptomoedas.

### **RF006 - Atualizar conta (CRUD)**
O sistema deve possuir uma tela por onde o usuário poderá atualizar sua conta.

### **RF007 - Adicionar postagens/anúncios (CRUD)**
O sistema deve permitir que o admin adicione postagens/anúncios a respeito de notícias e novidades sobre seus serviços e modificações no sistema.

### **RF008 - Simular**
O sistema deve permitir que o usuário simule transações com suas criptomoedas.

### **RF009 - Compra P2P**
O sistema deve permitir que o usuário faça contato com outros investidores interessados em fazer a venda de seus ativos da forma P2P (Person To Person).

### **RF010 - Suporte ao sistema**
O sistema deve disponibilizar ao usuário suporte para os problemas que possam vir a ocorrer no uso do sistema de criptomoedas.

### **RF011 - Produções**
O sistema deve permitir que o usuário veja as fotos publicadas pela Vortek Produções e solicite cotações.

### **RF012 - Suporte de TI**
O sistema deve permitir que o usuário solicite cotações sobre os serviços da Vortek Consultoria.

---

# Requisitos Não Funcionais

### **RNF001**
O sistema deverá se comunicar com o banco de dados das criptomoedas para visualização em tempo real.

### **RNF002**
O sistema deverá funcionar nos principais navegadores.

### **RNF003**
O sistema deverá notificar o usuário caso a sua senha esteja incorreta.

### **RNF004**
Quando o usuário estiver logado, o sistema deverá mostrar uma página inicial, uma para a área de produções, criptomoedas, consultoria de TI e gerenciamento de conta.

### **RNF005**
O sistema deve enviar o usuário para a página do serviço referente ao ícone clicado na página principal.

### **RNF006**
O sistema deverá ser feito em Vue.js e Django.

### **RNF007**
O sistema deverá ser otimizado e responsivo para computadores e celulares.

---

# Tecnologias Utilizadas
- **Frontend:** Vue.js  
- **Backend:** Python + Django  
- **Banco de Dados:** SQLite

---

# Requisitos para preparar o ambiente de desenvolvimento

## Backend (Django)

### 1. Instale o Python 3.10+.
Verifique a instalação e rode o projeto:
```bash
python --version

python manage.py runserver
```
## Frontend (Vue.JS)

```bash
npm run dev
```


