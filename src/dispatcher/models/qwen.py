import time
import copy
from DrissionPage import ChromiumPage

from logs.logger import log


class ModelQWen:
    """
    通过浏览器访问qwen
    在浏览器图标上右键，在属性中的目标位置，在最后面添加" --explicitly-allowed-ports=6666"(前面有空格)
    请用户自行登录qwen后，再运行
    """
    def __init__(self) -> None:
        self.page = ChromiumPage(6666)
        # page.get('https://tongyi.aliyun.com/qianwen/')
        self.new_page = self.page.get_tab(self.page.latest_tab).page
        
    def qa(self, question):
        textarea_ele = self.new_page.ele('tag:textarea@@class:ant-input')
        # a = 'Interim Dividend 与以下分类及分类说明，最相关的三个分类是哪些 Banking: 与银行相关的业务 Commercial & Operations:
        # 公司IT硬件、软件、授权，场地租聘，固定资产和虚拟资产相关 Corporate Governance: 规定公司审计、授权、人员职责、评价政策、风险管理、费用管理等相关内容 Corporate Matters:
        # 公司注册、重组、注销、法人、驻地、子公司、公司章程等相关内容 CSR: 企业社会责任相关 Directors & Offices: 董事会、监事、高级管理人员的任命、变更、续约内容 Finance:
        # 对公司现金、抵押物、股票相关的说明、计划、政策、管理和审计人员 Financial Reports: 以报告、政策、公告、代表函等书面形式描述公司财务相关的内容 HKEX ‐ Listed Entity:
        # 与上市公司上市文件、股东大会、关联交易、内幕交易监管、审计、证监会豁免相关内容 HKEX Products & Services:
        # 与香港交易所推出的产品相关，包含产品上市，终止，更新，优化；现有产品：对上市公司的薪酬变更、人力变更、激励计划、员工培训、公积金、审查等提供服务 HR Investment & Treasury:
        # 与公司投资基金、托管银行、基金经理的管理、投资策略的相关内容 Legal: 与公司人员纠纷、法律顾问、诉讼、商标等相关的内容 Listing Matters: 与上市公司报告、审计政策、上市规则相关的内容
        # Projects & Transactions: 与公司融资、增资，对子公司、合资公司及公司相关相关的操作内容 Regulatory: 公司费用、交易等受政府、监管机构、证监会监管的内容，并包含与与之对应的回复内容
        # Risk Management: 公司风险管理相关内容 Share Capital & Securities: 公司股票发行、股权结构、上市、配售等相关内容 Strategy & Updates:
        # 公司战略计划、投资计划、行业报告、市场分析、投资政策等相关内容'
        textarea_ele.input(question)
        self.new_page.ele('css:div.chatBtn--RFpkrgo_ > span.anticon').click()
        time.sleep(10)
        answers = self.new_page.eles('css:div.stream--brXJQIKe > div.contentBox--WIsVhFWg > div.tongyi-ui-markdown')
        last_answer = ''
        answer = answers[-1].text if answers is not None and len(answers) > 0 else ''
        # flex_ele = new_page.ele('tag:div@@class=flexCon')
        while answer == '' or answer != last_answer:
            last_answer = copy.deepcopy(answer)
            time.sleep(5)
            answers = self.new_page.eles('css:div.stream--brXJQIKe > div.contentBox--WIsVhFWg > div.tongyi-ui-markdown')
            answer = answers[-1].text
        log.debug(f'千问模型问答: question:{question} answer:{answer}')
        return answer
