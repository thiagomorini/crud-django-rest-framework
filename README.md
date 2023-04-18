# CRUD with Django REST Framework

Este projeto é um CRUD simples construído com Django REST Framework para demonstrar o uso básico do framework. O projeto possui dois aplicativos, sendo o "backend" (API) e o "frontend", que permitem a listagem, cadastro, alteração e exclusão de módulos, e os testes do model, das views e serializers.

## Tecnologias utilizadas

- Python 3.11
- Django 4.2
- Django CORS 3.14.0
- Django REST Framework 3.14.0

## Instalação e execução

Para executar o projeto localmente, siga os seguintes passos:

1. Clone o repositório para o seu computador:

```
git clone https://github.com/thiagomorini/crud-django-rest-framework.git
```

2. Instale as dependências do projeto.

3. Execute as migrações do banco de dados:

```
python manage.py migrate
```

4. Execute o servidor:

```
python manage.py runserver
```

5. Acesse a API do projeto em seu navegador através do endereço http://127.0.0.1:8000/api/modules/

6. Acesse o projeto em seu navegador através do endereço http://127.0.0.1:8000/modules/

7. Se precisar executar os testes do modelo, das views e do serializer, basta rodar o comando:

```
python manage.py test backend
```

## Contribuição

Você pode contribuir com o projeto de várias formas:

1. Reportando bugs e problemas no Github.
2. Fazendo pull requests com correções e novas funcionalidades.
3. Compartilhando o projeto e incentivando outros desenvolvedores a usá-lo.

## Licença
Este projeto é distribuído sob a licença MIT.

## Contato
Você pode entrar em contato comigo sempre que tiver alguma dúvida ou sugestão de melhorias.
