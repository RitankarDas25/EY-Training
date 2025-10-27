from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Continuously ask the user for input and classify the sentiment
while True:
    # Get user input
    user_input = input("Enter text to analyze sentiment (or type 'exit' to quit): ").strip()

    if user_input.lower() == 'exit':
        print("Exiting the sentiment analysis program.")
        break

    # Get the sentiment classification result
    result = sentiment_analyzer(user_input)

    # Display the result
    print(f"Sentiment: {result[0]['label']} (Confidence: {result[0]['score']:.4f})\n")
