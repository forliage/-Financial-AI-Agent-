# 金融智能投顾 (Financial AI Agent) v2.0 

本项目是一个带有**交互式图形用户界面**的金融智能代理。用户无需编写任何代码，即可通过简单的界面操作，配置自己的大语言模型（LLM）API，并获得专业的金融市场分析。

### ✨ 核心功能

*   **图形用户界面 (GUI)**: 基于Gradio构建，提供现代化、响应迅速的用户界面，操作直观便捷。
*   **动态交互**: 用户可随时输入股票代码、选择模型、配置API密钥，并即时获取分析结果。
*   **多模型支持**: 用户可自由选择并配置Google Gemini, OpenAI, 或通义千问（Qwen）作为分析核心。
*   **实时数据分析**: 对接主流财经数据接口，获取准实时的市场动态，并进行自动化分析。
*   **可视化报告**: 自动生成清晰的股价走势图，并将LLM的分析与策略建议以文本形式呈现。

---

### 🖥️ GUI界面预览

(这里可以放一张你的应用截图)


---

### 🛠️ 技术栈 (Tech Stack)

*   **语言**: Python 3.9+
*   **GUI框架**: **Gradio**
*   **核心框架**: Pandas
*   **LLM API**: `google-generativeai`, `openai`, `dashscope` (for Qwen)
*   **金融数据**: `yfinance`, `akshare`
*   **数据可视化**: `Plotly` (用于生成可交互的图表), `Matplotlib`

---

### 📂 项目结构

```
financial-ai-agent/
├── app.py                          # 启动Gradio GUI的主程序
├── notebooks/
│   └── development_notebook.ipynb  # 用于模块开发和测试
├── src/                            # 核心源代码目录
│   ├── config_manager.py           # API密钥和配置管理
│   ├── data_fetcher.py             # 金融数据获取
│   ├── llm_handler.py              # 统一处理不同LLM的API
│   ├── analysis_engine.py          # 核心分析逻辑
│   └── visualizer.py               # 图表生成
├── .env                            # 存储你的API密钥
├── .env.example                    # API密钥配置示例
├── requirements.txt                # Python依赖包
└── README.md                       # 本说明文档
```

---

### 🚀 安装与运行

**1. 克隆项目**
```bash
git clone https://github.com/forliage/-Financial-AI-Agent-.git
cd financial-ai-agent
```

**2. 创建并激活虚拟环境**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. 安装依赖**
```bash
pip install -r requirements.txt
```

**4. 配置API密钥**

我们提供两种配置API密钥的方式：

*   **方式一（推荐）**: 创建 `.env` 文件。将 `.env.example` 复制为 `.env`，并填入你的密钥。程序会优先从这里读取。
    ```ini
    # .env file content
    OPENAI_API_KEY="sk-..."
    GOOGLE_API_KEY="AI..."
    DASHSCOPE_API_KEY="sk-..."
    ```

*   **方式二（临时）**: 直接在GUI界面的API密钥输入框中填入。这种方式的密钥不会被保存，关闭程序后即失效。

**5. 启动应用**

在项目根目录下，运行以下命令：
```bash
python app.py
```

程序启动后，你会在终端看到类似以下的输出：
```
Running on local URL:  http://127.0.0.1:7860
```
在你的浏览器中打开这个URL，即可开始使用本金融智能投顾！

---

### 📝 如何使用GUI

1.  **选择模型**: 在界面顶部的下拉菜单中选择你想使用的LLM（如`Gemini`, `ChatGPT`, `Qwen`）。
2.  **输入API密钥**: 如果你没有配置`.env`文件，请在此处输入对应模型的API密钥。
3.  **输入查询目标**: 在“股票代码/证券名称”输入框中，输入你想要分析的目标，例如 `AAPL` (苹果), `000001.SZ` (平安银行)。
4.  **点击分析**: 点击“开始分析”按钮。
5.  **查看结果**: 等待几秒钟，界面右侧将依次展示：
    *   **价格走势图**: 一个可交互的股票价格图表。
    *   **市场分析**: LLM生成的关于市场情况的详细中文分析。
    *   **投资策略建议**: LLM基于分析结果给出的具体操作建议。

---

### ⚠️ 免责声明

*   **API费用**: 调用大语言模型API会产生费用，请根据您所选API提供商的计费策略合理使用。
*   **数据延迟**: 金融数据源可能存在一定的延迟，请注意风险。
*   **非投资建议**: 本项目提供的所有分析和建议仅供学术研究和技术演示，**不构成任何投资建议**。投资者据此操作，风险自担。