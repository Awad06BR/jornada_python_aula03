### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

import time

pagina = 1

paginas = 1

while pagina <= paginas:

    print(f"Processando paginas. Atual:{pagina} Total:{paginas}")
    time.sleep(5)
    pagina+=1

print(f"Procesamento concluido! Total:{paginas}")
