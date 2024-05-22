# Projeto Django Exemplo

## Visão Geral

Este projeto é uma aplicação Django criada para demonstrar o uso de Managers e QuerySets personalizados em modelos Django. O projeto também utiliza ferramentas adicionais como `black` para formatação de código, `ipython` para um shell interativo aprimorado, e `django-extensions` para fornecer funcionalidades adicionais ao Django.

## Requisitos

- Python 3.10
- Django 3.2+
- black
- ipython
- django-extensions

## Configuração do Ambiente

1. **Clone o repositório**:
    ```sh
    git clone https://github.com/flaviomouracarvalho/djangomanager.git
    cd djangomanager
    ```

2. **Crie e ative um ambiente virtual**:
    ```sh
    python3.10 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Execute as migrações**:
    ```sh
    python manage.py migrate
    ```

5. **Inicie o servidor de desenvolvimento**:
    ```sh
    python manage.py runserver
    ```

## Uso de Manager e QuerySet Personalizados
