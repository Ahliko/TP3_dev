import logging
from _socket import gethostbyname
from sys import argv

try:
    print(gethostbyname(argv[1]))
except IndexError:
    logging.error("Veuillez entrez un Nom de Domaine Valide")
