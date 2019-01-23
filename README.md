# Hamburgueria

Instruções para copiar o projeto e executar em sua máquina local para desenvolvimento ou para testes.

## Pré-requisitos

Você precisa de python 3 (a versão utilizada foi a 3.6.7) instalada em seu sistema e pip ou pip3 para instalar as extenções.

### Instalação

Após isso, crie um novo ambiente python para instalar as extensões com:

```
python3 -m venv env`
```

Depois que for criado o ambiente, você deverá ativá-lo com:

```
source /<path>/<para>/<env>/activate
```

Após o ambiente estar ativo, você pode simplesmente executar o comando

```
pip install -r requirements.txt
```

para instalar todas as dependências necessárias

Após a instalação das dependências deve setar a aplicação para o flask com

```
export FLASK_APP=restaurante.py
```


>Caso queira executar no modo de desenvolvimento deve-se setar o flask para rodar com o comando
>```
>export FLASK_ENV=development
>```
>antes de executá-lo

Agora está tudo setado para rodar a aplicação em sua máquina local com:

```
flask run
```

## Rodando os testes

Deve-se estar na raiz do projeto, com isso apenas rode o arquivo `test_function.py` com:

```
python3 test_function.py
```

Ele te derá um output de todos os testes e os status finais.

## Construído com

* [Flask](http://flask.pocoo.org/) - O python framework utilizado

* [Tailwind](https://tailwindcss.com/) - O CSS framework utilizado

## Design de código

Foi-se utilizado o design de código **Orientado a Objeto**
por ser um dos mais utilizados e mais simples de se trabalhar, pois pode-se apenas fazer uma instância do objeto e trabalhar com as informações contidas neste objeto.

Assim, conforme algo é mudado, mudamos os dados da instância do objeto que esteja na memória.