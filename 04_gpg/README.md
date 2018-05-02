

Foi feito a chave com o nome "Esdras" e exporada para o http://keyserver.ubuntu.com/ , Depois, Luzia importou minha chave e fez a criptografia e me enviou para testar. recebi o documento e consegui ver a mensagem. depois foi revogada a chave.

- 04_gpg
Cria a chave: <br>
```
gpg --gen-key
```
- colocar foto <br>
```
gpg --edit-key XXXXXXX
```
> addphoto <br>
- Em seguida adicionar o caminho para sua foto: <br>
```
/home/user/dir/dir/foto.jpg
```
- importar a chave:

```
gpg --import arnaldo.gpg

```
- enviar mensagem de texto criptografada e assinar com a chave do colega:
```
gpg -e -r [chave] documento.doc
```
- revogar a sua chave no servidor remoto utilizando o certificado em:
```
gpg --edit-key
```

> revkey 

Depois so escolher as opções de revogação e salvar!

