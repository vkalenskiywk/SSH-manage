def createpath(link_all_cl, filename):

    link_all_cl = link_all_cl.replace("\\", "/")  # корректировка пути

    if link_all_cl[-1] != "/":  # Установка слеша перед именем файла
        link_all_cl = link_all_cl + "/"
    fullpath = link_all_cl + filename
    return fullpath