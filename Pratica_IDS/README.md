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

