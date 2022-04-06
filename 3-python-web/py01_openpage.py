import webbrowser
import sys


if len(sys.argv) > 1:
    endereco = ' '.join(sys.argv[1:])
    webbrowser.open(f'https://www.google.com/maps/place/{endereco}')
else:
    print('Digite, por favor, um endereço!')

