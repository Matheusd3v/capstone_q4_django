# capstone_q4_django

### Instalar o poetry
```shell
  https://python-poetry.org/docs/
```

para ativar o ambiente virtual

```shell
  poetry shell
```

adicionar as dependências com o requirements.txt

```shell
  poetry add `cat requirements.txt`
```

criar banco de dados
```shell
  ./manage.py makemigrations && ./manage.py migrate
```

criar um super usuário
```shell
  ./manage.py createsuperuser
```