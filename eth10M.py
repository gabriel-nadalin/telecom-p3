def decode(sig):
    # TODO: processe o sinal sig (uma lista de inteiros 0 ou 1) e retorne
    # o quadro Ethernet como um valor do tipo bytes, contendo desde o
    # endereço MAC de destino até o FCS.
    manchester_dec = []
    counter = 0
    for i in range(len(sig)):
        counter += 1
        if sig[i-1] != sig[i] and counter >= 7:
            manchester_dec.append(sig[i])
            counter = 0

    preamble = True
    byte_reset = 0b1_0000_0000
    byte = byte_reset
    frame = []
    for i in range(len(manchester_dec)):
        if preamble:
            if manchester_dec[i-1:i+1] == [1, 1]:
                preamble = False
        else:
            byte = byte >> 1 | manchester_dec[i] << 8
            if byte & 1 == 1:
                frame.append(byte >> 1)
                byte = byte_reset

    return bytes(frame)
