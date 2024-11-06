import os

from dotenv import load_dotenv, find_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI

def main():
    load_dotenv(find_dotenv())
    print(os.environ["AZURE_OPENAI_ENDPOINT"])
    # Azure OpenAIのGPT-4oモデルを使用してAzureChatOpenAIインスタンスを作成します。
    model = AzureChatOpenAI(
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    )

    # 翻訳指示とユーザーからのメッセージを定義します。
    messages = [
        SystemMessage(content="Translate the following from English into Japanese"),
        HumanMessage(content="Hi!"),
    ]

    # # モデルにメッセージを渡して翻訳を実行します。
    response = model.invoke(messages)
    print(response)

if __name__ == "__main__":
    main()