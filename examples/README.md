# 自动编码系统测试案例

### 样例

1. examper1.py 生成一个测试项目test, 只包含一个文件test.py, 包含一个打印hello word的方法
```shell script
# 一期版本脚本，后续参数定义会进行变更
autocode pc -n test -l python -p "d:/" --model qwen-o --project_subject "生成一个测试项目test, 只包含一个文件test.py, 包含一个打印hello word的方法" --check_desc "执行项目文件，输出hello world"
```

2. 完成两个python文件，两个文件存在依赖关系，