# # app/services/report_generator.py

# from langchain.agents import initialize_agent, Tool
# from langchain_openai import ChatOpenAI

# # ✅ Import functions from other services
# from app.services.csv_analyzer import generate_csv_insights
# from app.services.vision_analyzer import analyze_image

# # ✅ Define LLM in THIS file
# llm = ChatOpenAI(temperature=0.2)

# tools = [
#     Tool(
#         name="CSV Analyzer",
#         func=generate_csv_insights,
#         description="Generates business insights from CSV statistics"
#     ),
#     Tool(
#         name="Image Analyzer",
#         func=analyze_image,
#         description="Extracts insights from charts, graphs, and business images"
#     ),
# ]

# agent = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent="zero-shot-react-description",
#     verbose=True
# )

# def generate_report(csv_data: dict, image_data: list[str]) -> str:
#     """
#     Generate a structured business report
#     """
#     prompt = f"""
#     Create a structured business analytics report using:

#     CSV Insights:
#     {csv_data}

#     Image Insights:
#     {image_data}

#     Include:
#     - Executive summary
#     - Key metrics
#     - Trends
#     - Recommendations
#     """

#     return agent.run(prompt)
