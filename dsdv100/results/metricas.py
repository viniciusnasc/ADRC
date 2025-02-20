import re

def calculate_average_delay(input_file_vci, output_file):
    with open(input_file_vci, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    total_delay = 0
    count = 0

    for line in lines:
        if line.strip() and line[0].isdigit():
            fields = line.split()
            if len(fields) >= 7:
                try:
                    time_sent = float(fields[5])
                    time_arrival = float(fields[6])
                    delay = time_arrival - time_sent
                    total_delay += delay
                    count += 1
                except ValueError:
                    continue

    if count > 0:
        average_delay = total_delay / count
        with open(output_file, 'a', encoding='utf-8') as out_file:
            out_file.write(f"\nCenário com 100 nós com mobilidade constante e protocolo DSDV:\n")
            out_file.write(f"\nMédia do atraso: {average_delay:.2f} ms\n")
        print(f"Média do atraso calculada e adicionada ao arquivo {output_file}")
    else:
        print("Nenhuma linha com tempos válidos encontradas no arquivo.")

def process_metrics(file_path, output_file):
    pacotes_recebidos = 0
    recebidos_com_sucesso = 0
    recebidos_com_erro = 0
    retransmissao = 0
    not_addr = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for line in lines:
        if "mac rcvdPkFromLl:count" in line:
            pacotes_recebidos += int(re.findall(r'\d+$', line)[0])
        elif "mac passedUpPk:count" in line:
            recebidos_com_sucesso += int(re.findall(r'\d+$', line)[0])
        elif "mac packetDropIncorrectlyReceived:count" in line or "mac packetDropNotAddressedToUs:count" in line:
            recebidos_com_erro += int(re.findall(r'\d+$', line)[0])
            
    for line in lines:
        if "mac packetDropIncorrectlyReceived:count" in line:
            retransmissao += int(re.findall(r'\d+$', line)[0])
        elif "mac packetDropNotAddressedToUs:count" in line:
            not_addr += int(re.findall(r'\d+$', line)[0])
    
    if pacotes_recebidos > 0:
        sucesso_percent = (recebidos_com_sucesso / pacotes_recebidos) * 100
        erro_percent = (recebidos_com_erro / pacotes_recebidos) * 100
        retransmissao_percent = (retransmissao / pacotes_recebidos) * 100
        not_addr_percent = (not_addr / pacotes_recebidos) * 100
    else:
        sucesso_percent = erro_percent = 0
    
    output = (
        f"\nPacotes Recebidos: {pacotes_recebidos} (100%)\n"
        f"Recebidos com Sucesso: {recebidos_com_sucesso} ({sucesso_percent:.2f}%)\n"
        f"Pacotes Retransmitidos: {retransmissao} ({retransmissao_percent:.2f}%)\n"
        f"Pacotes Não enderçados ao host: {not_addr} ({not_addr_percent:.2f}%)\n"
        f"Recebidos com Erro: {recebidos_com_erro} ({erro_percent:.2f}%)\n"
    )
    
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(output)

def extrair_ultimo_evento(arquivo_entrada, arquivo_saida):
    ultima_linha = None
    
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                ultima_linha = line.strip()
    
    if ultima_linha:
        campos = ultima_linha.split()
        if len(campos) >= 5:
            ultimo_evento = campos[4]
            with open(arquivo_saida, 'a', encoding='utf-8') as out_file:
                out_file.write(f"Último evento válido de simulação: {ultimo_evento}\n")
            print(f"Último evento válido registrado: {ultimo_evento}")
        else:
            print("A linha não contém pelo menos 5 campos.")
    else:
        print("Nenhuma linha válida encontrada no arquivo.")

# Caminhos dos arquivos
input_file_sca = "HighMobility-#0.sca"
input_file_vci = "HighMobility-#0.vci"
output_file = "dsdv_100.txt"

# Executar as funções na ordem desejada
calculate_average_delay(input_file_vci, output_file)
process_metrics(input_file_sca, output_file)
extrair_ultimo_evento(input_file_vci, output_file)
