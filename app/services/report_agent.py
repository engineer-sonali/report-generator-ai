from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

prompt = PromptTemplate(
    input_variables=["context"],
    template="""
You are a senior business analyst.

Using ONLY the information below, generate a structured business report.

Context:
{context}

Return valid JSON with:
- key_metrics
- trends_and_correlations
- recommendations
- summary
"""
)

# Runnable chain (LangChain 1.x)
report_chain = prompt | llm

def generate_report(context: str):
    response = report_chain.invoke({"context": context})
    return response.content
