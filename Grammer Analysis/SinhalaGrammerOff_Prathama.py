import re

def check_grammar(text, letter_combination):
    # Split the text into sentences
    sentences = re.split(r'[.?]', text)

    #print(sentences)

    results = []

    for sentence in sentences:
        # Split each sentence into words
        words = sentence.split()

        # Check if there are at least two words in the sentence
        if len(words) >= 1:
            last_word = words[-1].strip(".,!?")

            # Check if the last two letters of the last word match the specified letter combination
            if last_word[-4:].lower() == letter_combination.lower():
                results.append("Correct Grammar")
            else:
                results.append("Incorrect Grammar")
        else:
            # If there are no words in the sentence, it's considered incorrect grammar
            results.append("Incorrect Grammar")

    return results


def sinhala_to_english(text):
    # Define a mapping dictionary for Sinhalese to English letters
    sinhala_to_english_mapping = {
        'ම': 'm', 'අ': 'a', 'ද': 'd', 'ග': 'g', 'ෙ': 'e',
        'හ': 'h', 'ප': 'p', 'බ': 'b',
        'ඉ': 'i', 'න': 'n', 'ට': 't', 'ත': 'tha',
        'ච': 'c', 'එ': 'e', 'ය': 'y', 'ල': 'l', 'ව': 'w',
        'ැ': 'ae', 'ළ': 'l', 'ආ': 'aa', 'ං': 'n',
        'ර': 'r', 'ජ': 'j', 'ස': 's', 'ෆ': 'f', 'භ': 'b',
        'ය': 'y', 'ි': 'i', 'ක': 'k',
        'ො': 'o', 'ඩ': 'd', '්': '', ' ': ' ', '.': '.',
        'ා': 'a', 'ැ': 'ae', 'ෑ': 'aee', 'ි': 'i', 'ී': 'ii',
        'ු': 'u', 'ූ': 'uu', 'ෘ': 'u', 'ෙ': 'e', 'ේ': 'ee',
        'ෛ': 'ei', 'ෝ': 'oo', 'ෞ': 'ou',
        'ෟ': 'o', 'ෲ': 'lu', 'ෳ': 'lu'
    }

    # Perform the conversion
    english_text = ""
    for char in text:
        if char in sinhala_to_english_mapping:
            english_text += sinhala_to_english_mapping[char]
        else:
            english_text += char

    return english_text


# Example usage:
input_text = "බල්ලෝ උඩු බුරති. මිනිස්සු ඉක්මනට ගමන් කරති. ඔබ ගමන් ගියහි? තමුන්නාන්සේ කුමක්ද කරන්නේ. කාන්තාවෝ සංචාරය කරති"
letter_comb = "ති"

# Convert Sinhala letters to English
english_text = sinhala_to_english(input_text)
print("Input Text in Sinhala:")
print(input_text)
print("\nConverted to English Letters:")
print(english_text)

start_text = sinhala_to_english(letter_comb)
print("\nConverted Starting Letter:")
print(start_text)


def count_correct_grammar_sentences(english_text, start_text):
    # Check grammar using the previous code
    results = check_grammar(english_text, start_text)

    correct_grammar_count = results.count("Correct Grammar")
    incorrect_grammar_count = results.count("Incorrect Grammar")

    return correct_grammar_count, incorrect_grammar_count


# Check grammar using the previous code
results = check_grammar(english_text, start_text)
print("\nGrammar Check Results:")
sentences = re.split(r'[.?]', english_text)
# sentences = english_text.re.split(r'[.?]')
for i, sentence in enumerate(sentences):
    print(f"Sentence {i + 1}: {sentence.strip()}")
    print(f"Grammar: {results[i]}\n")

# Example usage:
correct_grammar_count, incorrect_grammar_count = count_correct_grammar_sentences(english_text, start_text)

print(f"Number of Correct Grammar Sentences: {correct_grammar_count}")
print(f"Number of Incorrect Grammar Sentences: {incorrect_grammar_count}")
