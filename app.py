# app.py

from textblob import TextBlob
import gradio as gr

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    result = f"Polarity: {polarity:.3f}\nSubjectivity: {subjectivity:.3f}\nSentiment: {sentiment}"
    return result

# Gradio UI
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=4, placeholder="Enter your review here..."),
    outputs="text",
    title="Sentiment Analyzer",
    description="Enter a review or any sentence to analyze its sentiment using TextBlob."
)

# Launch the app
if __name__ == "__main__":
    iface.launch()
