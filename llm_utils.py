import ollama

# -------- detect outfit-related question --------
def is_outfit_query(question):
    keywords = [
        "outfit", "look", "wear", "dress",
        "style", "clothes", "fit", "appearance"
    ]
    question = question.lower()
    return any(word in question for word in keywords)


# -------- main response function --------
def generate_response(question, outfit_analysis, history):

    outfit_related = is_outfit_query(question)

    # -------- CASE 1: Outfit question + image available --------
    if outfit_related and outfit_analysis:
        prompt = f"""
        You are a friendly best friend giving outfit advice.

        Rules:
        - Start with something positive
        - Give 1 suggestion max
        - Be casual and natural

        Outfit:
        {outfit_analysis}

        Conversation:
        {history}

        User: {question}
        """

    # -------- CASE 2: Normal chat OR no image --------
    else:
        prompt = f"""
        You are a fun, friendly best friend.

        - Talk casually like a real human
        - Be engaging, chill, slightly playful
        - DO NOT ask for outfit image unless user asks

        Conversation:
        {history}

        User: {question}
        """

    # -------- call Ollama --------
    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']