"""
CONSTANTE = "Variáveis" que não vão mudar de valor
"""

velocidade = 61  # Valocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # Velocidade máxima permitida no radar 1
LOCAL_1 = 100  # Local do radar 1
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1

if vel_carro_pass_radar_1:
    print("Você foi multado")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        vel_carro_pass_radar_1:
    print("Você foi multado")
