import socket

# Caminho do arquivo com os IPs
file_path = 'endereco.txt'
output_file = 'hostnames.txt'

# Função para obter o hostname a partir do IP
def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Hostname não encontrado"

# Ler o arquivo e processar cada IP
with open(file_path, 'r') as file:
    ips = file.readlines()

# Remover quebras de linha e espaços em branco
ips = [ip.strip() for ip in ips]

# Abrir arquivo para escrever os resultados
with open(output_file, 'w') as out_file:
    for ip in ips:
        hostname = get_hostname(ip)
        # Escrever no formato: "endereço ip (TAB) hostname"
        out_file.write(f"{ip}\t{hostname}\n")

print("Arquivo 'hostnames.txt' gerado com sucesso.")