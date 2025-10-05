import re
import string
from collections import Counter

def analyze_text(text):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()

    words = clean_text.split()
    word_count = len(words)

    temp_sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in temp_sentences if s.strip()]
    if not sentences:
        sentences = text.split('\n')
    sentence_count = len(sentences)

    paragraphs = [p for p in text.split('\n') if p.strip()]
    paragraph_count = len(paragraphs)

    avg_word_len = sum(len(word) for word in words) / word_count if word_count else 0

    freq = Counter(words)
    most_common = freq.most_common(5)

    print("\n--- Text Analysis ---")
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Paragraphs: {paragraph_count}")
    print(f"Average word length: {avg_word_len:.2f} characters")
    print("Most common words:")
    for word, count in most_common:
        print(f"  {word}: {count} times")


if __name__ == "__main__":
    print("=== Text Analyzer ===")
    print("Paste your text below (end with an empty line):")

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    
    text = "\n".join(lines)
    analyze_text(text)
