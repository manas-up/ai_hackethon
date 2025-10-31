from langchain_openai import ChatOpenAI
import httpx
import streamlit as st

client = httpx.Client(verify=False)

llm = ChatOpenAI(
    base_url="https://genailab.tcs.in",
    model="azure_ai/genailab-maas-DeepSeek-V3-0324",
    api_key="sk-w3MhAThbauXLizR2r8cnug",
    http_client=client
)

# Streamlit UI for AI Trip Planner
st.title("AI Trip Planner")
source = st.text_input("Enter Source:")
destination = st.text_input("Enter Destination:")

if st.button("Get Travel Options"):
    if source and destination:
        prompt = f"Suggest travel options from {source} to {destination}. List the best ways to travel, including flights, trains, buses, and any other relevant options. Format the response as a numbered list."
        response = llm.invoke(prompt)
        # Parse the output to display as a list
        if hasattr(response, 'content'):
            output = response.content
        else:
            output = str(response)
        # Try to split into lines for better display
        options = [line for line in output.split('\n') if line.strip()]
        st.subheader("Travel Options:")
        for option in options:
            st.write(option)
    else:
        st.warning("Please enter both source and destination.")
