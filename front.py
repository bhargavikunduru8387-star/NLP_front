
import gradio as gr
import requests
API_URL = "https://nlp-back-1.onrender.com"
def analyze(description):
    response = requests.post(
        API_URL,
        json={"description": description}
    )
    if response.status_code == 200:
        return response.json()["analysis"]
    return "Error"
demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(
        lines=12,
        label="Enter Product Description"
    ),
    outputs=gr.Textbox(
        lines=20,
        label="Analysis"
    ),
    title="AI Product Description Analyzer",
    description="Analyze product descriptions using Gemini AI"
)
demo.launch()
