class Similarity():
    """Differents similarity measures functions."""

    def overlap_similarity(data, umbral, generate_matrix=False, generate_file=False, file_name='default-ov'):
        """
        Extrae las arista entre dos vertices basado en n atributos en común.

        -----------
        Parameters:
        data: df
            Conjunto de datos.
        umbral: int
            Umbral para decidir si existe arista entre dos registros.
        generate_matrix: bool
            Calcular la matriz de distancias.
        generate_file: bool
            Generar o no archivo con aristas (Usar para Gephi)
        name_file: str
            Nombre del archivo.

        -----------
        Return:
        matrix_overlap_metric: df
            Dataframe con la matriz de distancia.
        Archivo csv con las aristas
        """

        print("*"*20)
        print("Iniciando construcción de aristas por OVERLAP")

        size_data = len(data)
        n_atributos = len(data.columns)  # Número de atributos Columnas
        # Lista donde se almacena todas las aristas (Sirve pal Netowrkx)
        lista_edges = []

        if generate_matrix:
            matrix_list = []  # Creación de la lista que ira en la matriz
            for i in range(size_data):
                fila_matrix = []  # Fila donde se metera a la matrix
                for j in range(size_data):
                    a = data.iloc[i].to_list()
                    b = data.iloc[j].to_list()
                    inter = [value for value in a if value in b]
                    # Convertir a umbral
                    inter = len(inter) / n_atributos
                    fila_matrix.append(inter)  # Matrix
                    # if inter >= umbral and i!=j:
                    # f.write(str(i)+";"+str(j)+"\n")
                matrix_list.append(fila_matrix)  # Matrix
            matrix_jaccard_metric = pd.DataFrame(matrix_list)

        #################################################
        # En esta parte se construye la lista de aristas
        # Se realiza otro ciclo para eliminar las aristas iguales

        if generate_file:
            # Archivo donde se guardan aristas
            f = open("grafo-"+file_name+".csv", "w")
            f.write("Source;Target;Weight\n")
            for i in range(size_data):
                for j in range(i+1, size_data):
                    a = data.iloc[i].to_list()
                    b = data.iloc[j].to_list()
                    inter = [value for value in a if value in b]
                    # Convertir a umbral
                    inter = len(inter) / n_atributos
                    if inter >= umbral:
                        f.write(str(i)+";"+str(j)+";" +
                                str(round(inter, 2))+"\n")
                        lista_edges.append((i, j, inter))
        else:
            for i in range(size_data):
                for j in range(i+1, size_data):
                    a = data.iloc[i].to_list()
                    b = data.iloc[j].to_list()
                    inter = [value for value in a if value in b]
                    # Convertir a umbral
                    inter = len(inter) / n_atributos
                    if inter >= umbral:
                        lista_edges.append((i, j, inter))

        print("Finalizado")
        print("*"*20)
        # Imprimir la configuración utilizada
        print("### Finalizado ###")
        print("# Configuración utilizada #")
        print("Umbral: ", umbral)
        print("Generación de Matriz: ", generate_matrix)
        print("Generación de Archivo: ", generate_file)
        if generate_file:
            print("Nombre de archivo: ", file_name)
        print("*"*20)
        # Retornar la matrix y la lista de aristas
        if generate_matrix:
            return matrix_jaccard_metric, lista_edges
        else:
            return lista_edges
