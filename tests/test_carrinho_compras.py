"""Carrinho de compras feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
from app.carrinho_compras import CarrinhoCompras
from pytest import fixture

@fixture
def contexto():
    return CarrinhoCompras()

@scenario('../features/carrinho.feature', 'Adicionar itens ao carrinho')
def test_adicionar_itens_ao_carrinho():
    """Adicionar itens ao carrinho."""


@given(parsers.parse('que tenho um carrinho de compras com item "{item}" e preço R$ {preco:f}'))
def adicionar_item(contexto, item, preco):
    contexto.adicionar_item(item, preco)


@when(parsers.parse('eu adiciono o item "{item}" com o preço R$ {preco:f}'))
def adicionar_novo_item(contexto, item, preco):
    contexto.adicionar_item(item, preco)


@then(parsers.parse('o total do carrinho de compras deve ser R$ {total:f}'))
def verificar_valor_total(contexto, total):
    assert contexto.total() == total


@scenario('../features/carrinho.feature', 'Remover item do carrinho')
def test_remover_item_do_carrinho():
    """Remover item do carrinho."""


@given(parsers.parse('que tenho um carrinho de compras com item "{item}" e preço R$ {preco:f}'))
def adicionar_item(contexto, item, preco):
    contexto.adicionar_item(item, preco)



@when('eu removo o item do carrinho')
def remover_item_carrinho(contexto):
    contexto.remover_item()
    


@then('o carrinho de compras deve estar vazio')
def carrinho_vazio(contexto):
   assert contexto.esta_vazio()

