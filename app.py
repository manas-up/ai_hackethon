from flask import Flask, render_template, request
from langchain_openai import ChatOpenAI
import httpx

app = Flask(__name__)

# Disable SSL verification for httpx (since you're using self-signed internal cert)
client = httpx.Client(verify=False)

# Initialize LLM
llm = ChatOpenAI(
    base_url="https://genailab.tcs.in",
    model="azure_ai/genailab-maas-DeepSeek-V3-0324",
    api_key="sk-w3MhAThbauXLizR2r8cnug",
    http_client=client
)

@app.route("/", methods=["GET", "POST"])
def index():
    options = None
    if request.method == "POST":
        source = request.form["source"]
        destination = request.form["destination"]

        if source and destination:
            prompt = (
                f"Suggest travel options from {source} to {destination}. "
                "List the best ways to travel, including flights, trains, buses, "
                "and any other relevant options. Format the response as a numbered list."
            )
            response = llm.invoke(prompt)
            output = getattr(response, 'content', str(response))
            options = [line for line in output.split('\n') if line.strip()]
    return render_template("index.html", options=options)

if __name__ == "__main__":
    app.run(debug=True)
