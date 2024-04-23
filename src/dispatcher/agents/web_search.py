import requests
from loguru import logger

from dispatcher.agents.agent import format_agent_result


# Search engine related. You don't really need to change this.
BING_SEARCH_V7_ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"
BING_MKT = "en-US"
GOOGLE_SEARCH_ENDPOINT = "https://customsearch.googleapis.com/customsearch/v1"

# Specify the number of references from the search engine you want to use.
# 8 is usually a good number.
REFERENCE_COUNT = 8

# Specify the default timeout for the search engine. If the search engine
# does not respond within this time, we will return an error.
DEFAULT_SEARCH_ENGINE_TIMEOUT = 5


# https://github.com/langchain-ai/langchain/blob/master/libs/langchain/langchain/utilities/bing_search.py
@format_agent_result
def bing_search(query: str, subscription_key: str) -> list:
    """
    bing搜索
    Args:
        query: 搜索内容
        subscription_key: 订阅密钥
    Returns:
        list: 搜索结果
    """
    params = {
        "q": query, 
        "mkt": BING_MKT, 
        'count': REFERENCE_COUNT, 
        "textDecorations": True, 
        "textFormat": "HTML"
    }        
    response = requests.get(
        BING_SEARCH_V7_ENDPOINT,
        headers={"Ocp-Apim-Subscription-Key": subscription_key},
        params=params,
        timeout=DEFAULT_SEARCH_ENGINE_TIMEOUT,
    )
    if not response.ok:
        logger.error(f"{response.status_code} {response.text}")
        raise Exception(response.status_code, "Search engine error.")
    json_content = response.json()
    contexts = json_content["webPages"]["value"]
    return contexts


def baidu_search(query: str, subscription_key: str) -> list:
    pass


@format_agent_result
def google_search(query: str, subscription_key: str, cx: str) -> list:
    """
    Search with google and return the contexts.
    """
    params = {
        "key": subscription_key,
        "cx": cx,
        "q": query,
        "num": REFERENCE_COUNT,
    }
    response = requests.get(
        GOOGLE_SEARCH_ENDPOINT, params=params, timeout=DEFAULT_SEARCH_ENGINE_TIMEOUT
    )
    if not response.ok:
        logger.error(f"{response.status_code} {response.text}")
        raise Exception(response.status_code, "Search engine error.")
    json_content = response.json()
    try:
        contexts = json_content["items"][:REFERENCE_COUNT]
    except KeyError:
        logger.error(f"Error encountered: {json_content}")
        return []
    return contexts

