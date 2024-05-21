## Pré Requisitos Pytest

- [Python 3](https://www.python.org/)  

- [Pytest](https://pypi.org/project/pytest/)  
```
pip install pytest
```

- [Pytest-bdd](https://pypi.org/project/pytest-bdd/)  
```
pip install pytest-bdd
```

### class CarrinhoCompras  
Funções a serem testado.  

```
class CarrinhoCompras:
    def __init__(self):
        self.itens = []

    
    def adicionar_item(self, item, preco):
        self.itens.append({"item": item, "preco": preco})

    def remover_item(self):
        if self.itens:
            self.itens.pop()

    def total(self):
        return sum(item['preco'] for item in self.itens)

    def esta_vazio(self):
        return len(self.itens) == 0
```

## Features
Aqui estamos testando 2 cenários.  

```
Feature: Carrinho de compras
  Como usuário
  Eu quero adicionar e remover itens do meu carrinho de compras
  Para gerenciar minhas compras

Scenario: Adicionar itens ao carrinho
  Given que tenho um carrinho de compras com item "Camiseta" e preço R$ 29.99
  When eu adiciono o item "Calca" com o preço R$ 49.99
  Then o total do carrinho de compras deve ser R$ 79.98

Scenario: Remover item do carrinho
  Given que tenho um carrinho de compras com item "Camiseta" e preço R$ 29.99
  When eu removo o item do carrinho
  Then o carrinho de compras deve estar vazio
```

- Com a class e feature criado, no terminal rode o comando  
isso criarar um arquivo na pasta tests com o nome de test_carrinho_compras.py   
```
pytest-bdd generate features/carrinho.feature > tests/test_carrinho_compras.py
```
