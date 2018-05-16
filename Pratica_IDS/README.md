<img src="img/index.png" style="width: 200px;"/>


# Tema:  IDS (Intrusion Detection System)
## Prática: Capturando simulação de ataque com Snort
### Professor: David Senna
 Alunos: <br>
 [Esdras Emanuel Mariano Moreira](https://github.com/esdrasemanuel/) <br>
 [Jefferson Costa Severo](https://github.com/jefferson/)
 
 
## Objetivos
Esse trabalho tem como principal objetivo explicar os conceitos e variantes sobre os mecanismos de 
detecção de intrusão, suas aplicações dentro do ambiente de segurança da informação, e por fim mostrar uma pequena prática de simulação de ataque e captura com um software de IDS (Snort)


## O que é um IDS?
Um IDS (Intrusion Detection System) é um mecanismo que ouve o tráfego da rede de maneira furtiva , para localizar atividades anormais ou suspeitas , permitindo assim previnir os riscos da invasão.


## Por que usar um IDS?
Com o aumento e evolução das redes, empresas começaram a colocar suas informações em rede, no entanto, essas informações não existem mais só internamente, também vão estar externamente por meio da internet. Com isso ouve uma necessidade de maior segurança, e o IDS permite monitorar a rede e receber notificações conforme regras específicas.


## Tipos de IDS
-Existem dois tipos de IDS: O de rede (N-IDS) esse tipo monitora toda a rede a partir da pespectiva do local em que a ferramenta foi instalada, e o de host (H-IDS) esse por sua vez monitora apenas atividade anormais no que tange o funcionamento da máquina.

## O SNORT
O snort é um IDS baseado em rede(N-IDS) desenvolvido por Martin Roesch capaz de  desenvolver análise de tráfego em tempo real e registro de pacotes em rede. O Snort é essencial para a sua rede de computadores , pois ele ajuda a controlá-la e a gerenciar melhor todos os dados.
Executa análise de protocolo, busca e associa padrões de conteúdo e pode ser usado para detectar uma variedade de ataques , tais como buffer overflow, stealth port scans , ataques CGI, SMB probes, OS fingerprinting, entre outras. Esta ferramenta é suportada em arquiteturas RISC e CISC e em plataformas das mais diversas.

### Comunidade
Existem diversas comunidades Snort, incluindo a comunidade snort-BR no Brasil, cujo site é www.snort.com.br. Atualmente, existem mais de 400 milhões de usuários registrados na comunidade americana com mais de 4 milhões de downloads.

### Vantagens
- Muito flexível
- Possui metodologias de detecção multidimensional
- Suporte open-source

### Desvantagens
- Perfomaçe de até 30 mpbs
- Interface gráfica limitada
- Implementação lenta e pouco suporte comercial

### Empresas que utilizam Snort
- Desde 2003 , o Serpro utiliza essa ferramenta devido a sua grande flexibilidade
- Outras empresas também utilizam, tais como: Tigra, Sebrae, Submarino dentre outras.


## PRATICA

Detecção de simulação de ataque com snort

### Recursos utilizados
1 máquina virtual em modo bridge com linux onde será instalado o snort
1 máquina virtual em modo bridge com windows onde será instalado o software de simulação de ataque(LOIC)

## Passo-a-passo (Máquina linux)
1 – Antes de instalar o snort certifique-se de atualizar seu sistema.
```
sudo apt update && sudo apt upgrade
```
2 – Instale o snort.
```
	sudo apt install snort
 ```
3 – Na instalação vai pedir para você definir sua rede, coloque o ip da máquina virtual.

4 – Restart o serviço.
```
	service snort restart
 ```
5 – Para monitar a rede basta dar o comando:
```
snort -v
```
6 – Vá ao arquivo de configuração do snort:
```
nano /etc/snort/snort.conf
 ```
7 – Usar ^W para habilitar modo de escrita e escrever a palavra “HOME”

8 – Trocar “any” pelo ip a ser monitorado (IP da máquina virtual linux)

9 – Restart no serviço:
```
	service snort restart
```
10 – Deixando o snort em modo de detecção de ataques:
```
	snort -q -A console -i (interface do IP) -c /etc/snort/snort.conf
```

11 – Nessa forma o snort está esperando algum tipo de anomalia acontecer.

## Passo-a-passo	(Máquina Windows)

1 – Baixar o simular de ataque (LOIC) no seguinte link:
	https://sourceforge.net/projects/loic/
 
 
2 – Executar o programa, colocar método como TCP e no compo de URL colocar o IP da vítima (IP máquina linux)


3 – O snort vai capturar o ataque na máquina linux e mostrar informações como data, hora IP do atacante e IP do atacado,

