import random

def procesar_arp(archivo_entrada, archivo_salida, porcentaje_faltantes=0.05):
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
        lineas = entrada.readlines()
        secuencia_anterior = None
        
        for linea in lineas:
            # Omitir líneas que comienzan con '#'
            if linea.startswith('#'):
                continue
            
            # Si es una línea con secuencia (números)
            if all(caracter in '0123 ' for caracter in linea.strip()):
                # Simular faltantes en la secuencia
                nueva_secuencia = ''.join('?' if (caracter in '0123' and random.random() < porcentaje_faltantes) else caracter for caracter in linea.strip())
                salida.write(nueva_secuencia + '\n')
            else:
                # Si es una línea de etiqueta, copiarla tal cual
                salida.write(linea)

# Uso del script
archivo_entrada = 'depp_completo-temp_1_1.arp'
archivo_salida = 'new_file.txt'
procesar_arp(archivo_entrada, archivo_salida, porcentaje_faltantes=0.026)  # 2.5% de datos faltantes
