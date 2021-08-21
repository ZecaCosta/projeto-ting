from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    duplicate_file = False
    instance_length = instance.__len__()
    for item in range(instance_length):
        searched_dic = instance.search(item)
        if path_file == searched_dic["nome_do_arquivo"]:
            duplicate_file = True

    if not duplicate_file:
        lines_list = txt_importer(path_file)
        insert_dic = {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(lines_list),
                "linhas_do_arquivo": lines_list
        }
        instance.enqueue(insert_dic)
        sys.stdout.write(f'{insert_dic}\n')


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
