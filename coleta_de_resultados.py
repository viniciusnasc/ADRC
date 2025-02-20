import os

def merge_results(output_file="merged_results.txt"):
    base_dir = os.getcwd()  # Diretório atual
    protocols = ["aodv", "dsdv"]
    nums = [25, 50, 100]
    
    with open(output_file, "w", encoding="utf-8") as out_file:
        for proto in protocols:
            for num in nums:
                file_path = os.path.join(base_dir, f"{proto}{num}/results/{proto}_{num}.txt")
                
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as in_file:
                        out_file.write(f"# Dados de {proto}_{num}\n")
                        out_file.write(in_file.read() + "\n")
                else:
                    print(f"Arquivo não encontrado: {file_path}")

    print(f"Dados mesclados em {output_file}")

# Executar a função
merge_results()