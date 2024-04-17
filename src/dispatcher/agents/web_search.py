from typing import Any
from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import urllib.request

from dispatcher.agents import Agents, AgentFactory

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
bing_url = 'https://cn.bing.com/search?q='
baidu_url = 'https://www.baidu.com/s?wd='
google_url = 'https://www.google.com/search?q='


# https://github.com/langchain-ai/langchain/blob/master/libs/langchain/langchain/utilities/bing_search.py
def bing_search(param: str, num_results: int = 8) -> list:
    """获取搜索标题和内容"""
    page = urllib.request.urlopen('https://www.bing.com/search?q=%s' % param)

    soup = BeautifulSoup(page.read(), 'lxml')
    links = soup.select("li h2")

    for link in links:
        print(link.text)
    result = {
        'title': None,      # 标题
        'link': None,       # 链接
        'snippet': None     # 描述或片段内容
    }


def baidu_search(param: str, num_results: int = 8) -> list:
    pass


def google_search(param: str, num_results: int = 8) -> list:
    pass


class WebSearchAgents(Agents):
    @property
    def name(self):
        return 'web_search'

    def _run(self,
             search_content: str,
             web_type: str = 'bing'):
        if web_type == 'bing':
            return bing_search(search_content)
        elif web_type == 'baidu':
            return baidu_search(search_content)
        elif web_type == 'google':
            return google_search(search_content)
        return []

    async def _arun(self,
                    search_content: str,
                    web_type: str = 'bing'):
        if web_type == 'bing':
            return bing_search(search_content)
        elif web_type == 'baidu':
            return baidu_search(search_content)
        elif web_type == 'google':
            return google_search(search_content)
        return []
