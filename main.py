
from langchain_openai import ChatOpenAI
import httpx

client = httpx.Client(verify=False)

llm = ChatOpenAI(
    base_url="https://genailab.tcs.in",
    model="azure_ai/genailab-maas-DeepSeek-V3-0324",
    api_key="sk-w3MhAThbauXLizR2r8cnug",
    http_client=client
)

response = llm.invoke("Hi what is llm")
print(response)
