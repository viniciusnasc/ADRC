Avaliação de Desempenho e Escalabilidade da Rede em Redes Ad-hoc (AODV vs DSDV)
Professor: Arthur de Castro Callado, professor da Universidade Federal do Ceará no campus de Quixadá.

Simulador: OmNet++ v6.1 IDE (baseada em Eclipse IDE)
Área de simulação: 600m X 600m
Alcance do sinal: 50m
Área de detecção e interferência: 100m
Tamanho do pacote de dados 1024 bytes
Intervalo de envio dos dados 1s
Número de nós 25, 50 e 100
Velocidade de movimentação 5m/s
Modelo de movimentação Random Waypoint
Tempo de pausa 1s (constante)
MAC layer 802.11
Largura de banda 10Mbps

Cada cenário possui um projeto individual para uma execução isolada sem alteração do script manualmente. No diretório results de cada cenário possui um script Python que lê os arquivos Scalars,
Vectorials e de RoutingTable e coleta as métricas automaticamente após rodar a simulação executando o arquivo omnetpp.ini de cada cenário. No diretório raiz, também há um script que lê todos os
arquivos de texto coletado através dos scripts individuais, concatenam e gera a saída para um arquivo de texto na raiz do diretório para facilitar uma possível análise geral.

OBS: Os arquivos HighMobility-#0.vec dos cenários de 100 nós em ambos os protocolos foram removidos devido ao limite de tamanho para upload de arquivos excedidos (25MB).

Equipe: Vinícius gabriel (501154) e Fernanda Pessoa (493982)
Data: 20/02/2025
