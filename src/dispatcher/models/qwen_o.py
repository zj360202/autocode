import os
import time
import copy
from DrissionPage import ChromiumPage
from DrissionPage.errors import ElementLostError, ElementNotFoundError
from loguru import logger
import pyperclip

class ModelQWenOffice:
    """
    通过浏览器访问qwen
    在浏览器图标上右键，在属性中的目标位置，在最后面添加" --explicitly-allowed-ports=6666"(前面有空格)
    请用户自行登录qwen后，再运行
    """
    def __init__(self) -> None:
        self.page = ChromiumPage(6666)
        # 获取chrome的最后一个tab
        self.new_page = self.page.get_tab(self.page.latest_tab).page
        # 判定页面是否已经打开
        tongyi_url = os.environ.get('QWEN_OFFICAL_URL' ,'https://tongyi.aliyun.com/qianwen/')
        if self.new_page.url.startswith(tongyi_url):
            time.sleep(1)
        else:
            # 打开千问页面
            self.page.get(tongyi_url)
            self.new_page = self.page.get_tab(self.page.latest_tab).page
            time.sleep(1)
            # 打开新的会话
            new_chat = os.environ.get('QWEN_NEW_CHAT_BUTTON_CSS' ,'#chat-content > div.flex.mt-4 > div.side--ZR10Ab5M > button')
            self.new_page.ele(f'css:{new_chat}').click()
            time.sleep(3)
        
        
        
    def model(self, question):
        # chat_input = os.environ.get('QWEN_CHAT_INPUT_TAG' ,'textarea@@class:ant-input')
        # textarea_ele = self.new_page.ele(f'tag:{chat_input}')
        # textarea_ele.input(question)
        # try:
        #     chat_submit = os.environ.get('QWEN_CHAT_SUBMIT_CSS' ,'div.chatBtn--RFpkrgo_ > span.anticon')
        #     self.new_page.ele(f'css:{chat_submit}').click()
        # except (ElementLostError, ElementNotFoundError):
        #     logger.warning('模型发送按钮无效, 请替换自己的会话session在开始')
        # time.sleep(10)
        
        answer_css = os.environ.get('QWEN_CHAT_ANSWER_CSS' ,'div.answerItem--U4_Uv3iw')
        answers = self.new_page.eles(f'css:{answer_css}')
        answer_ele = answers[-1]
        
        answer_copy = os.environ.get('QWEN_CHAT_ANSWER_COPY_CSS' ,'div.rightArea--waHL0DVo > div:nth-child(3)')
        parse = answer_ele.ele(f'css:{answer_copy}')
        # print(f'parse:{parse}')
        while True:
            try:
                parse.click()
                logger.info('复制模型返回的内容')
                break
            except Exception as e:
                logger.info('等待5s')
                time.sleep(5)
                parse = answer_ele.ele(f'css:{answer_copy}')
        time.sleep(1)
        answer = pyperclip.paste()
        # logger.debug(f'千问模型问答: question:{question} answer:{answer}')
        return answer
