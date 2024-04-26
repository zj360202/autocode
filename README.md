<div align='center'>
  <img src='./images/autocode.png' width=500>
</div>

# AutoCode

自动编码系统。主要通过特定格式的描述，完成用户需求收集，自动完成**可实现完整功能系统**的自动编码系统。

### 🚀 快速开始

#### 🔧 前期准备
- 注册或登录千问官网https://tongyi.aliyun.com/qianwen/, 在项目运作中，会自动打开千问，必须保证已经登录
- git clone https://github.com/zj360202/autocode.git
- cd autocode
- pip install -e .

<font color ="red">*在使用过程中, 有可能会失败，这个主要可能是模型回复的样式不太理想，目前测试中几乎都成功，有失败的，可以提交issue</font>

#### ✨️ 命令参数
```shell script
autocode pc -n test -l python -p "d:/" --model qwen-o --project_subject "生成一个测试项目test, 只包含一个文件test.py, 包含一个打印hello word的方法" --check_desc "执行项目文件，输出hello world"
```
- `pc`: create_project, 创建目录，子命令，后续参数都和这个子命令进行绑定
- `-n`: --name, 项目名称
- `-m`: --mode, 项目创建模式 conti(延续)|cover(重建)，默认conti
- `-s`: --strategy, 项目创建策略 c(完成优先)|e(效果优先) 默认c
- `-l`: --language, 主要编码语言, 暂时只支持python
- `-p`: --project_dir, 项目目录
- `--model`: 支持的模型，qwen-o(qwen官方网站), qwen-i(千问接口，暂不支持)
- `--project_subject`: 项目需求描述
- `--check_desc`: 项目创建完成后的验证内容描述

#### 📜 任务清单

- [x] 生成一个测试项目test, 只包含一个文件test.py, 包含一个打印hello word的方法
- [ ] 轻度重构代码和完成验证中无法自动流转的部分，存在如下部分细节问题
  - [x] 千问是手动打开的，优化到完全自动打开，如果已经打开会复用
  - [ ] 效果验证的地方，prompt没有要模型返回匹配shell执行的结果需要和预期结果进行对比，这个是跨agent参数传递的功能，在后续开发
- [ ] 中型python项目的自动编码
  - [ ] 多个python, python文件直接相互调用
  - [ ] 跨agent参数传递
  - [ ] 项目、文件、函数的描述管理，以便在项目生产中断，可以继续完善项目
  - [ ] 添加两种模式：
    - 完成优先(适合开发, 时间快，但是部分bug可能修复不了，项目就会停止，等待人工修复)
    - 效果优先(适合小白, 时间长，且需要消耗大量的token)


#### 🔨自定义agent

- code doc: 必须包含函数描述，参数类型，参数描述，返回信息描述(如果有返回), 参考
  ```python
  def test(a: int, b: str, c: list = None):
    """
    获取函数的描述内容
        
    Args:
        a (int): param a
        b (str): param b
        c (list, optional): param c. Defaults to None.

    Returns:
        d: result d
    """
    return d
  ```
- 返回类型: 目前只支持简单数据类型，str|int|bool|float, 可以不返回
- 必须放在src/dispatcher/agents下面
- 必须在src/dispatcher/agents/\_\_init__.py中进行注册
- 如果需要设计到项目路径或其他全局变量的，参数src/dispatcher/global_params.py被应用的信息

#### 📌更多内容

- [ ] 添加新的agent，每一个fun必须有详细的doc注释，包含函数说明，参数名称(参数类型): 参数说明，这些内容会被格式化到prompt中进行使用
- [ ] 等第一个项目效果完成，后续开启更新迭代计划

### 💟 特别鸣谢

此项目参考诸多优质开源项目，特此感谢开源项目作者的贡献；以下列出部分参考项目：

- [auto-coder 自动编码项目](https://github.com/allwefantasy/auto-coder)
- [AutoGPT 人工智能+用户需求=产出 人人可用的人工智能产品](https://github.com/Significant-Gravitas/AutoGPT)
- [opencompass 模型评估](https://github.com/open-compass/opencompass)
- [openai-style-api 多模型接口统一封装](https://github.com/tian-minghui/openai-style-api)
