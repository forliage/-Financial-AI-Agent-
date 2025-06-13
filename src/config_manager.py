import os
from dotenv import load_dotenv

# 在模块加载时，自动从.env文件加载环境变量
load_dotenv()

def get_api_key(provider: str) -> str | None:
    """
    根据提供商名称获取API密钥。

    Args:
        provider(str): LLM提供商的名称('openai', 'gemini', 'qwen')

    Returns:
        str | None: 如果找到，返回API密钥字符串,否则返回None
    """
    provider = provider.lower()
    if provider == 'openai':
        return os.getenv("OPENAI_API_KEY")
    elif provider == 'gemini':
        return os.getenv("GOOGLE_API_KEY")
    elif provider == 'qwen':
        return os.getenv("DASHSCOPE_API_KEY")
    else:
        print(f"错误:不支持的提供商'{provider}'。")
        return None

# 在这里测试一下
if __name__ == '__main__':
    # 在运行此文件进行测试前，请确保你已经创建了 .env 文件并填入了密钥
    gemini_key = get_api_key('gemini')
    if gemini_key:
        print(f"成功获取到Gemini API密钥的前5位: {gemini_key[:5]}...")
    else:
        print("未找到Gemini API密钥。")

    openai_key = get_api_key('openai')
    if openai_key:
        print(f"成功获取到OpenAI API密钥的前8位: {openai_key[:8]}...")
    else:
        print("未找到OpenAI API密钥。")