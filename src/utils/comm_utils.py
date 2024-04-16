import os


def get_full_path(relation_path, project_path):
    """
    判定相对路径是否是相对路径，如果是，则使用项目路径补全路径
    """
    if relation_path.startswith('.'):
        relation_path = os.path.join(project_path, str(relation_path[2:]))
    elif '/' not in relation_path:
        relation_path = os.path.join(project_path, relation_path)
    return relation_path
