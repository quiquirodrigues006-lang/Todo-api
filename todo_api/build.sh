#!/usr/bin/env bash
# Interrompe a execução caso ocorra algum erro
set -o errexit

# Instala as dependências
pip install -r requirements.txt

# Reúne os arquivos do Admin na pasta staticfiles
python manage.py collectstatic --no-input

# Aplica as migrações no banco de dados
python manage.py migrate