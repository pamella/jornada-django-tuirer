# [Django] Tuirer
Repositório do projeto Tuirer, feito para o curso de Django da 28ª Jornada de Cursos do [CITi](https://github.com/citi-ufpe).

## Deploy
* Deploy realizado no link abaixo
```bash
https://orange-tuirer.herokuapp.com
```

## Como utilizar
* Clone o projeto para seu computador
  ```bash
  $ git clone https://github.com/pamella/jornada-django-tuirer.git
  ```
* Inicie um ambiente virtual e instale as dependências
  ```bash
  $ python -m virtualenv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  ```
* Rode as migrações
  ```bash
  $ python manage.py migrate
  ```
* Inicie o servidor
  ```bash
  $ python manage.py runserver
  ```
* Antes de commitar, delete as pastas pycache
  ```bash
  $ make clean
  ```