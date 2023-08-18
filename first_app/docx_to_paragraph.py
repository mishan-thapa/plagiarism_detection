import docx

def get_paragraphs_from_word_file(file_path):
    doc = docx.Document(file_path)
    paragraphs = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text)
    return paragraphs

def count_total_words(paragraphs):
    total_words = 0
    for paragraph in paragraphs:
        total_words += len(paragraph.split())
    return total_words

