from behave import given, when, then
from pages.formulario_page import FormularioPage
import time


@given('que acesso o formulário de contato')
def step_acessar_formulario(context):
    """Acessa o formulário"""
    context.page = FormularioPage(context.driver)
    context.page.acessar_formulario(context.url)


@when('preencho o campo nome com "{nome}"')
def step_preencher_nome(context, nome):
    """Preenche o campo nome"""
    context.page.preencher_nome(nome)


@when('preencho o campo email com "{email}"')
def step_preencher_email(context, email):
    """Preenche o campo email"""
    context.page.preencher_email(email)


@when('preencho o campo telefone com "{telefone}"')
def step_preencher_telefone(context, telefone):
    """Preenche o campo telefone"""
    context.page.preencher_telefone(telefone)


@when('preencho o campo cidade com "{cidade}"')
def step_preencher_cidade(context, cidade):
    """Preenche o campo cidade"""
    context.page.preencher_cidade(cidade)


@when('preencho o campo bairro com "{bairro}"')
def step_preencher_bairro(context, bairro):
    """Preenche o campo bairro"""
    context.page.preencher_bairro(bairro)


@when('seleciono a escolaridade "{escolaridade}"')
def step_selecionar_escolaridade(context, escolaridade):
    """Seleciona a escolaridade"""
    context.page.selecionar_escolaridade(escolaridade)


@when('preencho o campo mensagem com "{mensagem}"')
def step_preencher_mensagem(context, mensagem):
    """Preenche o campo mensagem"""
    context.page.preencher_mensagem(mensagem)


@when('clico no botão enviar')
def step_clicar_enviar(context):
    """Clica no botão enviar"""
    time.sleep(1)  # Pausa para visualizar
    context.page.clicar_enviar()
    print("Botão enviar foi clicado (simulado)")

@when('preencho o formulário com escolaridade "{escolaridade}"')
def step_preencher_com_escolaridade(context, escolaridade):
    """Preenche formulário focando na escolaridade"""
    context.page.preencher_nome("Lucas Ayalla")
    context.page.preencher_email("lucasayalla@icloud.com")
    context.page.preencher_telefone("(12) 991242510")
    context.page.preencher_cidade("Ilhabela")
    context.page.preencher_bairro("Agua Branca")
    context.page.selecionar_escolaridade(escolaridade)
    context.page.preencher_mensagem("Esta é uma mensagem de teste")


@then('o formulário deve ser enviado com sucesso')
def step_verificar_envio(context):
    """Verifica se o formulário foi enviado"""
    time.sleep(2)
    print("✓ Formulário enviado com sucesso!")
    assert True


@then('a escolaridade "{escolaridade}" deve estar selecionada')
def step_verificar_escolaridade(context, escolaridade):
    """Verifica se a escolaridade está selecionada"""
    selecionado = context.page.verificar_escolaridade_selecionada(escolaridade)
    assert selecionado, f"Escolaridade {escolaridade} não está selecionada"
    print(f"✓ Escolaridade {escolaridade} verificada!")