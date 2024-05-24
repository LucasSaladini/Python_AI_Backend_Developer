file = open("teste.txt", "w")
file.write("Escrevendo dados em um novo arquivo.")
file.writelines(['\n', 'escrevendo', '\n', 'um', '\n', 'novo', '\n', 'texto'])
file.close()