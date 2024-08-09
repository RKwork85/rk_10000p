'''
复制文件或目录：
python
shutil.copy(src, dst)  # 复制文件或目录到目标路径
shutil.copy2(src, dst)  # 复制文件或目录到目标路径，并保留元数据
shutil.copytree(src, dst)  # 递归地复制整个目录树

移动文件或目录：
shutil.move(src, dst)  # 移动文件或目录到目标路径
删除文件或目录：
shutil.rmtree(path)  # 递归地删除整个目录树
shutil.unlink(path)  # 删除指定文件

压缩和解压缩文件：
shutil.make_archive(base_name, format, root_dir)  # 创建压缩文件
shutil.unpack_archive(filename, extract_dir)  # 解压缩文件
获取文件信息：
python
复制
shutil.disk_usage(path)  # 获取指定路径的磁盘使用情况
shutil.which(cmd)  # 在系统的PATH中查找可执行文件的路径

'''
import os
import shutil
import tempfile


# print(tempfile.gettempdir())    

BASE_TEMP_DIR = os.path.join(tempfile.gettempdir(), "rkwork_temp")

# print(os.path.isdir(BASE_TEMP_DIR))
try:
    shutil.rmtree(BASE_TEMP_DIR)    # 使用shutil.rmtree(BASE_TEMP_DIR)尝试删除BASE_TEMP_DIR目录及其内容
except Exception:
    pass
os.makedirs(BASE_TEMP_DIR, exist_ok=True)     # 如果路径存在，不爆错  