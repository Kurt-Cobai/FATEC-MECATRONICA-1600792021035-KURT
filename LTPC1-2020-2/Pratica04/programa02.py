#Pede para o usuário uma senha a valida ela com a senha secreta
#Cria uma varíavel para guardar a senha
senha_secreta = '123456'

#Pede para o usuario digitar sua senha
senha = input('informe a senha:')

#Verificar se a senha do usuario esta correta
if senha == senha_secreta:
  print('bem vindo Hackerman')

if senha != senha_secreta:
  print('acesso negado!')
