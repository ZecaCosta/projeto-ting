from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    duplicate_file = False
    instance_length = instance.__len__()
    for item in range(instance_length):
        searched_dic = instance.search(item)
        if path_file == searched_dic['nome_do_arquivo']:
            duplicate_file = True

    if not duplicate_file:
        lines_list = txt_importer(path_file)
        insert_dic = {
                'nome_do_arquivo': path_file,
                'qtd_linhas': len(lines_list),
                'linhas_do_arquivo': lines_list
        }
        instance.enqueue(insert_dic)
        sys.stdout.write(f'{insert_dic}\n')


def remove(instance):
    instance_length = instance.__len__()
    if instance_length == 0:
        return sys.stdout.write('Não há elementos\n')

    removed_dic = instance.dequeue()
    path_file = removed_dic['nome_do_arquivo']
    sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        searched_dic = instance.search(position)
        sys.stdout.write(str(searched_dic))

    except IndexError:
        sys.stderr.write('Posição inválida\n')
