<div align='center'>
  <img src='./images/autocode.png' width=500>
</div>

# AutoCode

自动编码系统。主要通过特定格式的描述，完成用户需求收集，自动完成**可实现完整功能系统**的自动编码系统。

### 🚀 快速开始

#### 📜 任务清单

- [x] 生成一个测试项目test, 只包含一个文件test.py, 包含一个打印hello word的方法
- [ ] 轻度重构代码和完成验证中无法自动流转的部分，存在如下部分细节问题
  - [ ] 千问是手动打开的，也可以自动打开，需要自己先登录，然后获取包含session_id的Url
  - [ ] 效果验证的地方，prompt没有要模型返回匹配shell执行的结果需要和预期结果进行对比，这个是跨agent参数传递的功能，在后续开发
- [ ] 中型python项目的自动编码
  - [ ] 多个python, python文件直接相互调用
  - [ ] 跨agent参数传递
  - [ ] 项目、文件、函数的描述管理，以便在项目生产中断，可以继续完善项目

#### 📌更多内容

- [ ] 添加新的agent，每一个fun必须有详细的doc注释，包含函数说明，参数名称(参数类型): 参数说明，这些内容会被格式化到prompt中进行使用
- [ ] 等第一个项目效果完成，后续开启更新迭代计划

### 💟 特别鸣谢

此项目参考诸多优质开源项目，特此感谢开源项目作者的贡献；以下列出部分参考项目：

- [auto-coder 自动编码项目](https://github.com/allwefantasy/auto-coder)
- [AutoGPT 人工智能+用户需求=产出 人人可用的人工智能产品](https://github.com/Significant-Gravitas/AutoGPT)
- [opencompass 模型评估](https://github.com/open-compass/opencompass)
- [openai-style-api 多模型接口统一封装](https://github.com/tian-minghui/openai-style-api)
