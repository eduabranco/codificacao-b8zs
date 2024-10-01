import matplotlib.pyplot as plt  

# Função para aplicar a codificação Bipolar com Substituição de 8 Zeros (B8ZS)
def b8zs_encoding(bit_sequence):
    last_pulse = -1
    encoded_sequence = []
    
    i = 0
    while i < len(bit_sequence):
        # Verifica se há uma sequência de 8 zeros
        if bit_sequence[i:i+8] == '00000000':
            # Verifica qual foi o último pulso bipolar (positivo ou negativo)
            if last_pulse == 1:
                # Substituição para o último pulso positivo (+)
                encoded_sequence.extend([0, 0, 0, 0.5, -0.5, 0, -0.5, 0.5])
            else:
                # Substituição para o último pulso negativo (-)
                encoded_sequence.extend([0, 0, 0, -0.5, 0.5, 0, 0.5, -0.5])
            
            # Avança 8 posições, pois substituímos uma sequência de 8 zeros
            i += 8
        else:
            # Se o bit for 1, alterna o pulso bipolar
            if bit_sequence[i] == '1':
                last_pulse *= -1
                encoded_sequence.append(last_pulse)
            else:
                encoded_sequence.append(0)
            i += 1

    return encoded_sequence

# Função para desenhar a sequência original e codificada
def plot_sequences(original_sequence, encoded_sequence, title):
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))

    # Adiciona um ponto extra ao final para o gráfico de degraus
    original_sequence = original_sequence + [original_sequence[-1]]
    encoded_sequence = encoded_sequence + [encoded_sequence[-1]]

    # Plot da sequência original (ajustando para gráfico de degraus)
    ax[0].step(range(len(original_sequence)), original_sequence, where='post', label='Sequência Original', color='blue')
    ax[0].set_title('Sequência Original')
    ax[0].set_ylim(-0.1, 1.1)
    ax[0].set_xlim(0, len(original_sequence)-1)
    ax[0].grid(True)

    # Plot da sequência codificada (mantendo step para codificação)
    ax[1].step(range(len(encoded_sequence)), encoded_sequence, where='post', label='Sequência Codificada (B8ZS)', color='orange')
    ax[1].set_title('Sequência Codificada (B8ZS)')
    ax[1].set_ylim(-1.1, 1.1)
    ax[1].set_xlim(0, len(encoded_sequence)-1)
    ax[1].grid(True)

    # Títulos e exibição
    plt.suptitle(title)
    plt.show()


# Sequências de bits fornecidas
bit_sequence_1 = "1000000001010011"
bit_sequence_2 = "1110100101000010"

# Converte as sequências de string para listas de inteiros
bit_sequence_1_list = [int(bit) for bit in bit_sequence_1]
bit_sequence_2_list = [int(bit) for bit in bit_sequence_2]

# Codifica as sequências usando B8ZS
encoded_sequence_1 = b8zs_encoding(bit_sequence_1)
encoded_sequence_2 = b8zs_encoding(bit_sequence_2)

# Exibe os gráficos
plot_sequences(bit_sequence_1_list, encoded_sequence_1, 'Codificação B8ZS - Sequência 1')
plot_sequences(bit_sequence_2_list, encoded_sequence_2, 'Codificação B8ZS - Sequência 2')
