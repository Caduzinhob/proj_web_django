# Projeto Blog Django

Este projeto é uma aplicação web de um Blog desenvolvida com Django e Django REST Framework, permitindo o cadastro de usuários e a criação de posts, assim como deletá-los.

## Diagrama do Projeto

![Diagrama Relacional](C:\Users\caduz\OneDrive\Documentos\GitHub\proj_web_django)

---

# Instalação e configuração

## Pré-requisitos

- Python 3.10 ou superior
- Git (opcional, para clonar o repositório)
- Django 5.2+
- Django REST Framework

---

## Configuração do Ambiente

1. **Clone o repositório (opcional):**
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd proj_web_django
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python -m venv venv
   .source venv/Scripts/activate
   ```

---

## Instalação das Dependências

```sh
pip install django djangorestframework
```

---

## Migrações do Banco de Dados

Crie as migrações e aplique-as ao banco de dados:

```sh
python manage.py makemigrations
python manage.py migrate
```

---

## Executando o Servidor

Inicie o servidor de desenvolvimento:

```sh
python manage.py runserver
```

Acesse [http://127.0.0.1:8000/]no navegador.
---

## Descrição

O sistema permite:
- Criação de usuários
- Deletar usuários
- Criação, listagem, edição e exclusão de posts

A API foi construída utilizando Django REST Framework.

---


## Funcionalidades

- Cadastro de usuários
- CRUD de posts
- API RESTful para usuários e posts

---

## Observações

- Para acessar o admin do Django, criei um superusuário(nome: admin):
  ```sh
  python manage.py createsuperuser
  ```

---