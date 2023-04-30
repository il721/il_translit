from pathlib import Path
import os


def all_ui_grc_to_py(path_in: str, extension: str) -> None:
    path = Path(path_in)
    ext = f"*.{extension}"
    if extension == 'ui':
        command = 'pyside6-uic'
    else:
        command = 'pyside6-rcc'
    out_list = list(path.glob(ext))
    for item in out_list:
        cmd = f"{command} {item.absolute()} -o {item.name.split('.')[0]}.py"
        os.popen(cmd)


# def all_ui_to_py(path: str):
#     files = os.listdir(path)
#     ui_list = []
#     pattern = re.compile(r'.*\.ui')
#     for it in files:
#         if pattern.match(it):
#             ui_list.append(it)
#
#     for it in ui_list:
#         file_path = os.path.join(path, it)
#         file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
#         cmd = f'pyside6-uic {file_path} > {path}{os.sep}{file_name_without_extension}.py'
#         os.popen(cmd)


if __name__ == '__main__':
    ui_grc_path = '.'
    all_ui_grc_to_py(ui_grc_path, 'ui')
    all_ui_grc_to_py(ui_grc_path, 'qrc')
    # print(*list(path.glob('*.ui')), sep='\n')
    # all_ui_to_py(os.path.dirname((os.path.abspath(__file__))))
    # print(*[x for x in path.iterdir()], sep='\n')
    # print(*list(path.glob('*.qrc')), sep='\n')
