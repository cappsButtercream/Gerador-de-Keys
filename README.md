# [random-keys]
## gerador de tokens para as NFT's do [Capps] e [Mr.leonard]
### ele tem que analisar os tokens armazenados na pasta "token criados"
### se um token recem criado for igual a outro, ele será refeito até que não seja mais igual
```
Se o token (token: ekltdba) for igual a outro que já estega
no arquivo "tokens criados" ele será refeito até ser diferente
e a mensagem "[*COLISÃO_DE_DADOS*]" vai aparecer

|========================================================|
        while True:
            if 'ekltdba' in tokens:
                print('[*COLISÃO_DE_DADOS*]')
                break
            else:
                file.write(f'ekltdba\n')
                sleep(1)
                print('\nToken criado!')
                sleep(0.5)
                print(f'Token: ekltdba')
                autenticaton = False
                break
|========================================================|
```
## o sistema está pronto para testes
