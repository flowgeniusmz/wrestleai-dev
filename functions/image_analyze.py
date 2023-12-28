import streamlit as st
from openai import OpenAI
from functions import image_frame_description as fd

client = OpenAI(api_key=st.secrets.openai.api_key)
model = st.secrets.openai.model_vision

def AnalyzeImage(full_analysis, base64_image, user_prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[
                     {
                         "role": "system",
                         "content": """
                Response should be a sentence max, maybe 2. You are a coach of someone who in a collegiate wrestling match..
                They are asking you questions about what is happening in the wrestling match. They will ask you for advice following the wrestling match. Talk to them naturally like a coaching conversation. Be very confident, detailed and precice about the match. Ensure any scoring moves are labeled as Move: {{Move Name}} Points: {{Number Points}} Improvements: {{Improvements}}. 
                """,
                     },
                 ]
                 + full_analysis
                 + fd.FrameDescription(base64_image, user_prompt),
        max_tokens=500,
    )
    response_text = response.choices[0].message.content
    return response_text