# Respostas da Atividade 

## EQUIPE:
[Calebe Tavares](https://github.com/calebetaap)<br>
[Esdras Emanuel](https://github.com/esdrasemanuel)<br>
jardel e Mara (Troca de respostas dontpad para agilizar, ps: aula foi corrida)

## 1 - O que são chaves simetrica e assimetrica?

São chaves usadas  para criptografar e deografar dados  provendo segurança na comunicação. Na prática, representa um segredo compartilhado entre duas ou mais partes que pode ser usado para manter uma  informação privada.

## 2 - Quais são as diferenças?

Simétrica: É usada uma única chave que é partilhada entre o emissor e o receptor. Desta forma, a chave que é usada para cifrar é a mesma que é usada para decifrar. Algoritmos que usam criptografia simétrica tendem a ser mais rápidos, no entanto não são tão seguros como os que usam criptografia assimétrica, uma vez que a chave usada 	para cifrar a informação é partilhada entre as várias máquinas.

Assimétrica: Usam um par de chaves distintas (chave privada e chave pública). A chave pública é usada para cifrar (encriptar)
A chave privada é usada para decifrar (desencriptar). A criptografia assimétrica é também conhecida por criptografia de chave pública.

## 3 - Dê exemplos reais de algoritmo:
AES (Advanced Encryption Standard), é uma cifra de bloco: Em criptografia, uma cifra de bloco é um algoritmo determinístico que opera sobre agrupamentos de bits de tamanho fixo, chamados de blocos, com uma transformação invariável que é especificada por uma chave simétrica. Cifras de bloco são componentes elementares importantes na concepção de muitos protocolos de criptografia, e são amplamente utilizados para implementar a encriptação de dados em massa.

RSA - utilizamos duas chaves, uma chave para encriptação e outra para decriptação.
<br>temos também: DES, MD5, SHA, RC4.

## 4 - Dê exemplo de onde elas são usadas em conjunto:
São usadas em conjuntos para melhorar o desempenho e a velocidade de envio de chaves, pois são usadas as chaves simétricas para criptografar as assimétricas.

## 5 - O que é KDC?
O KDC - Centro Distribuidor de Chaves é um servidor centralizado responsável pela autenticação dos usuários. O KDC autentica o usuário, através de um ticket, que será utilizado para provar a identidade do usuário para os serviços disponíveis na rede.

## 6 - Como funciona o GPG?
O GPG usa o método de chaves pública e privada (secreta) para assegurar a transferência de informações entre pares. Sua chave pública é distribuída para as pessoas que deseja trocar dados/mensagens e a chave privada fica em sua máquina (ela não pode ser distribuída). As chaves públicas e privadas são armazenadas nos arquivos pubring.gpg e secring.gpg respectivamente, dentro do subdiretório ~/.gnupg.

## 7 - O que é um ICP?
(Infraestrutura de Chaves Públicas Brasileira)
é um conjunto de tecnologias  que garante às transações e aos documentos eletrônicos a segurança por meio do uso de um par de chaves. Uma delas é pública (de conhecimento geral), e a outra, privada (de conhecimento somente do proprietário), cujos dados estão consolidados em um “certificado digital”.

## 8 - Porque dá erro de cerficifado em alguns site inclusive no site da caixa?
Por não possuir um certificado digital de alguma unidade certificadora para ser verificado pelo navegador.
