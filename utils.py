def remove_repeated_sentences(text):
    """반복된 문장을 제거"""
    sentences = text.split(". ")
    seen = set()
    unique_sentences = []
    for sentence in sentences:
        if sentence not in seen:
            seen.add(sentence)
            unique_sentences.append(sentence)
    return ". ".join(unique_sentences)
