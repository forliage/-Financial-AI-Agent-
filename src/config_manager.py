import os
from dotenv import load_dotenv

# 在模块加载时，自动从 .env 文件加载环境变量
load_dotenv()

def get_tushare_token() -> str | None:
    """获取Tushare的API Token。"""
    return os.getenv("TUSHARE_TOKEN")

def get_llm_api_key(provider: str) -> str | None:
    """
    根据提供商名称获取LLM的API密钥。
    (函数名修改得更清晰)

    Args:
        provider (str): LLM提供商的名称 ('openai', 'gemini', 'qwen').

    Returns:
        str | None: 如果找到，返回API密钥字符串，否则返回None。
    """
    provider = provider.lower()
    if provider == 'openai':
        return os.getenv("OPENAI_API_KEY")
    elif provider == 'gemini':
        return os.getenv("GOOGLE_API_KEY")
    elif provider == 'qwen':
        return os.getenv("DASHSCOPE_API_KEY")
    else:
        print(f"错误：不支持的LLM提供商 '{provider}'。")
        return None

# 测试代码
if __name__ == '__main__':
    # 测试 Tushare token
    tushare_token = get_tushare_token()
    if tushare_token:
        print(f"成功获取到Tushare Token: {tushare_token[:8]}...")
    else:
        print("未在 .env 文件中找到 TUSHARE_TOKEN。")

    # 测试 LLM key
    gemini_key = get_llm_api_key('gemini')
    if gemini_key:
        print(f"成功获取到Gemini API密钥的前5位: {gemini_key[:5]}...")
    else:
        print("未找到Gemini API密钥。")