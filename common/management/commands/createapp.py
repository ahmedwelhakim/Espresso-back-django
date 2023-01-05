from django.core.management import CommandError
from django.core.management.templates import TemplateCommand
import ast
import os
from django.conf import settings

SLASH = '\\' if os.name == 'nt' else '/'


class Command(TemplateCommand):
    help = (
        "Creates a Django app directory structure for the given app name in "
        "the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide an application name."

    def handle(self, **options):
        try:
            app_name = options.pop("name")
            target = options.pop("directory")
            print(app_name,target)
            super().handle("app", app_name, target, **options)
            self.controller(app_name=app_name)
        except CommandError as e:
            raise e

    @staticmethod
    def controller(app_name: str):
        settings_abs_path = _get_settings_abs_path()
        print(settings_abs_path)
        file = _file_reader(settings_abs_path)
        prefix = _get_app_prefix()
        app_name = _get_app_prefix() + "." + app_name
        target_name = getattr(settings, "CREATE_APP_LOCATION", "INSTALLED_APPS")
        node = _find_target_node(code=file, target_name=target_name)
        assert isinstance(node, ast.Assign), "Node must be of type assign"
        lineno, end_lineno, col_offset, end_col_offset, flag = _get_target_info(node)
        insert_text = _get_insert_text(col_no=col_offset, app_name=app_name, flag=flag)
        at_line = end_lineno - 1
        updated_file = _get_updated_file(
            original_file=file, insert=insert_text, at_line=at_line, flag=flag
        )
        _file_writer(settings_abs_path, updated_file)


def _file_reader(path: str) -> str:
    f = open(path, "r")
    return f.read()


def _file_writer(path: str, code: str):
    f = open(path, "w")
    f.write(code)
    f.close()


def _find_target_node(
        *, code: str, target_name="INSTALLED_APPS"
) -> ast.Assign | None:
    ast_tree = ast.parse(code)
    for node in ast.walk(ast_tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == target_name:
                    return node
                else:
                    continue
    return None


def _get_target_info(node: ast.Assign) -> (int, int, int, int, bool):
    """
    :param node: ast node
    :return: (
        node_lineno, node_end_lineo,
        last_const_col_offset,
        last_const_end_col_offset,
        is_array_end_bracket_same_line_of_last_string
    )
    """
    assert isinstance(node.value, ast.List), "Node value must be ast.List"
    last_const = node.value.elts[-1]
    lc_lineno, lc_end_lineno, lc_col_offset, lc_end_col_offset = (
        last_const.lineno,
        last_const.end_lineno,
        last_const.col_offset,
        last_const.end_col_offset,
    )
    n_lineno, n_end_lineno, n_col_offset, n_end_col_offset = (
        node.lineno,
        node.end_lineno,
        node.col_offset,
        node.end_col_offset,
    )

    return (
        n_lineno,
        n_end_lineno,
        lc_col_offset,
        lc_end_col_offset,
        n_end_lineno == lc_end_lineno,
    )


def _get_insert_text(col_no: int, app_name: str, flag:bool):
    text = " " * col_no if not flag else ''
    text += f'"{app_name}"'
    return text


def _get_updated_file(original_file: str, insert: str, at_line: int, flag=False):
    lines_list = original_file.split("\n")
    if not flag:
        lines_list[at_line-1].rstrip().removesuffix(',')
        lines_list[at_line-1] +=','
        lines_list.insert(at_line, f'{insert},')
    else:
        line = lines_list[at_line].rstrip()
        line = line.removesuffix(']').rstrip()
        line = line.removesuffix(',')
        line += f', {insert}, ]'
        lines_list[at_line] = line
    updated_file = "\n".join(lines_list)
    return updated_file


def _get_settings_abs_path() -> str:
    project_root = str(settings.BASE_DIR.absolute())
    assert (
            project_root != ""
    ), "project root is unknown from os.path.abspath(os.path.dirname(__name__))"
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE", "")
    assert (
            settings_module != ""
    ), 'setting module is unknown from os.environ.get("DJANGO_SETTINGS_MODULE")'
    settings_rel_path = SLASH.join(settings_module.split(".")) + ".py"
    abs_path = project_root + SLASH + settings_rel_path
    return abs_path


def _get_app_prefix() -> str:
    project_root = str(settings.BASE_DIR.absolute())
    cwd = os.getcwd()
    prefix = cwd.removeprefix(project_root)
    prefix = prefix.removeprefix(SLASH)
    prefix.replace(SLASH, ".")
    return prefix
