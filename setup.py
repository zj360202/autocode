import os
from setuptools import setup, find_packages

folder = os.path.dirname(__file__)

install_requires = []
req_path = os.path.join(folder, "requirements.txt")
install_requires = []
if os.path.exists(req_path):
    with open(req_path, encoding='UTF-8') as fp:
        install_requires = [line.strip() for line in fp]

# readme_path = os.path.join(folder, "README.md")
# readme_contents = ""
# if os.path.exists(readme_path):
#     with open(readme_path, encoding='UTF-8') as fp:
#         readme_contents = fp.read().strip()

setup(
    name="autocode",
    version="0.0.1",
    author="zj360202",
    author_email="zj360202@126.com",
    description="自动编码系统",
    long_description="",
    license="Apache License, Version 2.0",
    # url="http://test.com",
    classifiers=[
        # 许可证信息
        'License :: OSI Approved :: MIT License',
        # 属于什么类型
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        # 目标 Python 版本
        "Programming Language :: Python :: 3.9",
    ],

    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'autocode = autocode:main'
        ]
    }
)
