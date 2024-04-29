import os
import zipfile

def unzip_file(src_file, dest_dir, *password: str):
    """解压zip文件"""
    if password:
        password = password.encode()
    zf = zipfile.ZipFile(src_file)
    try:
        zf.extractall(path=dest_dir, pwd=password)
    except RuntimeError as e:
        print(e)
    zf.close()
    
def del_file(path):
    if os.path.exists(path):
        os.remove(path)

