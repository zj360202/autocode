# 自动编码系统测试案例

### 样例

1. examper1.py 生成一个测试项目test, 只包含一个文件test.py, 包含一个打印hello word的方法
```shell script
autocode pc -n test -l python -p "d:/" -m qwen --project_subject "生成一个测试项目test, 只包含一个文件test.py, 包含一个打印hello word的方法" --check_desc "执行项目文件，输出hello world"
```