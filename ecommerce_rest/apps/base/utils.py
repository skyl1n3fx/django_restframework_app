# Función para validar envio de archivos binarios.
def validate_files(request,field,update = False):
    """
    :params
    :request: request.data
    :field: key of file
    """
    # Hacemos una copia del request.data para poder mutarla.
    request = request.copy()

    if update:
        if type(request[field]) == str: request.__delitem__(field)
    else:    
        if type(request[field]) == str: request.__setitem__(field, None)
    
    return request