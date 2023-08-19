def count_total_words(paragraphs):
    total_words = 0
    for paragraph in paragraphs:
        total_words += len(paragraph.split())
    return total_words


def count_total_words_one_paragraph(paragraph):
    total_words = 0
    total_words += len(paragraph.split())
    return total_words