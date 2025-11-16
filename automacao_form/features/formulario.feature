# language: pt

Funcionalidade: Preencher formulário de contato
  Como um usuário do sistema
  Eu quero preencher o formulário de contato
  Para enviar minhas informações

  Cenário: Preencher formulário com dados válidos
  Dado que acesso o formulário de contato
  Quando preencho o campo nome com "Fabio Marques"
  E preencho o campo email com "fabinho_marquez@hotmail.com.br"
  E preencho o campo telefone com "(12) 991251455"
  E preencho o campo cidade com "Ilhabela"
  E preencho o campo bairro com "Agua Branca"
  E seleciono a escolaridade "Superior"
  E preencho o campo mensagem com "Esta é uma mensagem de teste"
  E clico no botão enviar
  Então o formulário deve ser enviado com sucesso
