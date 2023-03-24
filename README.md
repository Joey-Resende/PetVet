# <img src="file:///PetVet/PetVet/static/img/favicon-III.png" title="" alt="icon" width="50">  **PetVet**

<img title="" src="file:///home/joey/Documents/Back%20up%20notebook/coding/PetVet/PetVet/static/img/cat_yellow.png" alt="" data-align="center">

## **Ideia do projeto**

Trabalho atualmente como porteiro em uma clínica veterinária universitária e nela os registros são manuais, não existe um sistema para gerenciar os cadastros de pacientes, de atendimentos e etc. Isso me fez pensar em criar o meu próprio sistema para resolver esse problema. Dai surge o **PetVet** com a ideia de estudar **Python** com o framework **Django**. Pensei em usar Django por querer a minha aplicação na web e ele ser o framework web python mais usado.

## **Dependências**

O **PetVet** requer os sequintes componentes:

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/) 
- [Django](https://www.djangoproject.com/) 
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5) 
- [django-braces](https://django-braces.readthedocs.io/en/latest/)

Para todos os detalhes das dependências confira o [pyproject.toml](https://github.com/Joey-Resende/PetVet/blob/main/pyproject.toml)

## **Instalação e utilização**

E recomendado o uso de um ambiente virtual para que as dependências fiquem isoladas e para essa função utilizo o poetry, que tambem cria o arquivo **pyproject.toml** que lista, instala e gerencia as dependências.

### **Passo a passo**

- Clonar o repositório do [PetVet](https://github.com/Joey-Resende/PetVet.git) para sua maquina.

- Instalar o [Poetry](https://python-poetry.org/docs/) . A instalação do **poetry** não será coberta aqui mas deixo o link para a Docs dele com o processo.

- Criar um **ambiente virtual** com o poetry
  
  1. ```
     poetry shell         
     ```

- Instala as dependências com o **poetry**
  
  1. ```
     poetry install
     ```

- Se tudo deu certo ja poderemos iniciar o servidor e testar a aplicação, para isso precisamos do arquivo **manage.py** que se encontra no proximo nivel dos diretórios
  
  - ```
    cd PetVet/
    ```

- O arquivo **manage.py** nos fornece alguns comandos, entre eles o de iniciar o servidor.
  
  - ```
    python3 manage.py runserver
    ```

- Depois de iniciar o servidor só e necessário criar **um usuário** para acessar o sistema. O usuário padrão que e criado tem todas as permissões exceto a de excluir registros.

## **Funcionalidades**

Atualmente o sistema possui as seguintes funcionalidades:

- **Atendimentos**

- **Cadastros**
  
  - Pets (Pacientes)
  
  - Tutores
  
  - Veterinários

- **Exames**
  
  - Clínico
  
  - Físico
  
  - Dermatológico

- **Criar usuário**

- E possível visualizar os cadastros por lista e também ver os detalhes, além de editar ou excluir os mesmos. 

## **Licença**

O **PetVet** está disponivel sobre os termos do MIT License. Para os termos completos veja [licença](https://github.com/Joey-Resende/PetVet/blob/main/LICENSE).



<img title="" src="file:///home/joey/Documents/Back%20up%20notebook/coding/PetVet/PetVet/static/img/login_screen.png" alt="tela_login" data-align="center">
