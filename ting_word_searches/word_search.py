def exists_word(word, instance):
    list_to_return = []

    for position in range(instance.__len__()):
        dict_to_return = {
            'palavra': word,
            'arquivo': '',
            'ocorrencias': []
        }
        instance_dict = instance.search(position)
        list_with_lines = instance_dict.get('linhas_do_arquivo')
        file_path = instance_dict.get('nome_do_arquivo')
        dict_to_return['arquivo'] = file_path

        for count, line_content in enumerate(list_with_lines, 1):
            if word.upper() in line_content.upper():
                ocurrence_dict = {'linha': count}
                dict_to_return['ocorrencias'].append(ocurrence_dict)

    ocurrence_list = dict_to_return.get('ocorrencias')

    if ocurrence_list:
        list_to_return.append(dict_to_return)
    return list_to_return


def search_by_word(word, instance):
    list_to_return = []

    for position in range(instance.__len__()):
        dict_to_return = {
            'palavra': word,
            'arquivo': '',
            'ocorrencias': []
        }
        instance_dict = instance.search(position)
        list_with_lines = instance_dict.get('linhas_do_arquivo')
        file_path = instance_dict.get('nome_do_arquivo')
        dict_to_return['arquivo'] = file_path

        for count, line_content in enumerate(list_with_lines, 1):
            if word.upper() in line_content.upper():
                ocurrence_dict = {'linha': count, 'conteudo': line_content}
                dict_to_return['ocorrencias'].append(ocurrence_dict)

    ocurrence_list = dict_to_return.get('ocorrencias')

    if ocurrence_list:
        list_to_return.append(dict_to_return)
    return list_to_return
