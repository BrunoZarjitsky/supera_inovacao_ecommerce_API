# Teste processo seletivo Supera Inovação em tecnologia
### **Bruno Zarjitsky - Desenvolvedor Backend**
### **brunozar@poli.ufrj.br**
### **[LinkedIn](https://www.linkedin.com/in/brunozar "linkedin.com/in/brunozar")**
### **[GitHub](https://github.com/BrunoZarjitsky)**
---
### **Objetivo**: Desenvolver uma API para um pseudo e-commerce de games contendo os seguintes requisitos
 #### **Requisitos funcionais**
 - **O usuáriodeverá fazer login**
 - **O usuário poderá adicionar e remover produtos do carrinho.**
 - **O usuário poderá ordenar os produtos por preço, popularidade (score) e ordem alfabética. A filtragem deve ser realizada pela API.**
 - **Os valores exibidos no checkout (frete, subtotal e total) devem ser calculados dinamicamente conforme o usuário seleciona ou remove produtos.**
 - **A cada produto adicionado, deve-se somar R$ 10,00 ao frete.**
 - **Quando o valor dos produtos adicionados ao carrinho for igual ou superior a R$ 250,00, o frete é grátis.**
 - **O usuário pode realizar checkout de seu carrinho de compras.**
 - **O usuário pode consultar os pedidos feitos.**
 #### **Requisitos não funcionais**
 - **Deverá ser documentado no README.md como executar/compilar/empacotar o projeto e quais os endpoints solicitados nos requisitos acima. Para esse fim podem ser utilizadas ferramentas de containerização e automatização de builds.**
 - **Utilizar o banco de dados Postgres.**
 - **Para CRUD das entidades no banco de dados, utilizar preferencialmente migrations.**


## **Requisitos do sistema**
 - Python 3.10 (sudo apt-get install python3.10 )
 - venv (sudo apt-get install python3-venv)

## Como rodar o projeto
Criando o ambiente virtual:

    python -m virtualenv .venv

Ativando o ambiente virtual:

    source .venv/bin/activate

Instalando os requisitos da aplicação

    pip install -r requirements.txt

Aplicando as migrações

    ./manage.py migrate

Rodando as fixtures

    ./manage.py loaddata fixtures/product_fixture.json --app ecommerce/Product
    
Iniciando o servidor

    ./manage.py runserver

## Lista de endpoints
 - 127.0.0.1:8000/register/ -> Para registrar um novo usuario
 - 127.0.0.1:8000/login/ -> Para logar um usuario
 - 127.0.0.1:8000/logout/ -> Para deslogar um usuario
 - 127.0.0.1:8000/product/list/ -> Para buscar a lista de produtos
 - 127.0.0.1:8000/cart/active_cart/ -> Para buscar as informações do carrinho ativo do usuario
 - 127.0.0.1:8000/cart/add_prod/ -> Para adicionar um produto ao carrinho do usuario
 - 127.0.0.1:8000/cart/remove_prod/ -> Para remover um produto do carrinho do usuario
 - 127.0.0.1:8000/cart/checkout/ -> Para realizar o checkout no carrinho do usuario
 - 127.0.0.1:8000/order/list/ -> Para buscar os pedidos do usuario

obs: Deixarei uma collection do postman para facilitar o teste dos endpoints

## Detalhamento dos endpoints
Para os endpoints que requerem autenticação, é esperado nos headers o campo:
 - Authorization: Token \<token_de_autenticação\>

### /register/
Campos esperados no body:
 - username: Contem o nome de usuario
 - email: Contem o email do usuario
 - password1: Contem a senha
 - password2: Contem a repetição da senha 
Response esperado no caso de sucesso:
 - key: Token de autenticação do usuario

obs: Esse endpoint não requer autenticação
### /login/
Campos esperados no body:
 - username: Contem o nome de usuario
 - email: Contem o email do usuario
 - password: Contem a senha
 - obs: Só é preciso username ou email, não há nescessidade de enviar os dois campos.

Response esperado no caso de sucesso:
 - key: Token de autenticação do usuario

obs: Esse endpoint não requer autenticação

### /logout/
Não é esperado nenhum campo no body

Response esperado no caso de sucesso:
 - Mensagem de sucesso

### /product/list/
Campos esperados no body:
 - filter_by: Tipo de filtragem dos produtos, caso esse campo não seja passado é usado o filtro score como default

Response esperado no caso de sucesso:
 - Lista de produtos cadastrados

obs: Os filtros permitidos são:
 - name
 - name_rev
 - price
 - price_rev
 - score
 - score_rev

### /cart/active_cart/
Não é esperado nenhum campo no body

Response esperado no caso de sucesso:
 - id: Id do carrinho
 - user: Usuario dono do carrinho
 - products_at_cart: Lista com produtos no carrinho
 - products_amount: Valor dos produtos no carrinho
 - delivery_amount: Valor do frete
 - total_amount: Valor total do carrinho (produtos + frete)
 - active: Indicador de se o carrinho está ativo

### /cart/add_prod/
Campos esperados no body:
 - product_id: Id do produto para ser adicionado ao carrinho

Response esperado no caso de sucesso:
 - id: Id do carrinho
 - user: Usuario dono do carrinho
 - products_at_cart: Lista com produtos no carrinho
 - products_amount: Valor dos produtos no carrinho
 - delivery_amount: Valor do frete
 - total_amount: Valor total do carrinho (produtos + frete)
 - active: Indicador de se o carrinho está ativo

### /cart/remove_prod/
Campos esperados no body:
 - product_id: Id do produto para ser removido do carrinho

Response esperado no caso de sucesso:
 - id: Id do carrinho
 - user: Usuario dono do carrinho
 - products_at_cart: Lista com produtos no carrinho
 - products_amount: Valor dos produtos no carrinho
 - delivery_amount: Valor do frete
 - total_amount: Valor total do carrinho (produtos + frete)
 - active: Indicador de se o carrinho está ativo

### /cart/checkout/
Não é esperado nenhum campo no body

Response esperado no caso de sucesso:
 - id: Id do pedido do usuario
 - user: Usuario dono do pedido
 - cart: Id do carrinho referente ao pedido
 - date_checkout: Data de checkout do carrinho

### /order/list/
Não é esperado nenhum campo no body

Response esperado no caso de sucesso:
 - Lista contendo todos os pedidos do usuario