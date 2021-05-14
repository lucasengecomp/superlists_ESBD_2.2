# superlists_ESBD_2.2
ESBD 2.2 - Teste de Software Aplicado ao Desenvolvimento de Software  
Turma A: 
        Cezar Godinho 
        Cintia Fortes 
        Lucas Castro 
        Rodrigo Bueno
        
        
Comandos para iniciar o projeto

#Comandos uteis para execução do trabalho
#verificar se estes exports estão no .zshrc
export PATH=$HOME/.local/bin:$PATH
export WORKON_HOME="$HOME/tdd"
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
source /usr/local/bin/virtualenvwrapper.sh

#diretório inicial de trabalho
cd $HOME/tdd
pip3 install "django<=3.2" "selenium<4"

mkvirtualenv superlists_ESBD_2.2
cd $HOME/tdd/superlists_ESBD_2.2

$ deactivate 
$ workon superlists

django-admin startproject superlists_ESBD_2

cd superlists_ESBD_2

python manage.py runserver 
