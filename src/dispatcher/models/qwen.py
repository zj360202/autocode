import time
import copy
from DrissionPage import ChromiumPage
from DrissionPage.errors import ElementLostError
from loguru import logger
import pyperclip

class ModelQWen:
    """
    通过浏览器访问qwen
    在浏览器图标上右键，在属性中的目标位置，在最后面添加" --explicitly-allowed-ports=6666"(前面有空格)
    请用户自行登录qwen后，再运行
    """
    def __init__(self) -> None:
        self.page = ChromiumPage(6666)
        # 这个地方需要替换成自己千问的会话session
        self.page.get('https://tongyi.aliyun.com/qianwen/')
        time.sleep(1)
        self.new_page = self.page.get_tab(self.page.latest_tab).page
        
    def model(self, question):
        textarea_ele = self.new_page.ele('tag:textarea@@class:ant-input')
        textarea_ele.input(question)
        try:
            self.new_page.ele('css:div.chatBtn--RFpkrgo_ > span.anticon').click()
        except ElementLostError:
            logger.warning('模型发送按钮无效, 请替换自己的会话session在开始')
        time.sleep(10)
        
        answers = self.new_page.eles('css:div.answerItem--U4_Uv3iw')
        answer_ele = answers[-1]
        
        parse = answer_ele.ele('css:div.rightArea--waHL0DVo > div:nth-child(3)')
        # print(f'parse:{parse}')
        while True:
            try:
                parse.click()
                logger.info('复制模型返回的内容')
                break
            except Exception as e:
                logger.info('等待5s')
                time.sleep(5)
                parse = answer_ele.ele('css:div.rightArea--waHL0DVo > div:nth-child(3)')
        time.sleep(1)
        answer = pyperclip.paste()
        # logger.debug(f'千问模型问答: question:{question} answer:{answer}')
        return answer
