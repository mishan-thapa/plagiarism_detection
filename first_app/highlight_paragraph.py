import docx
from docx.enum.text import WD_COLOR_INDEX

def highlight_paragraph(paragraph_text,doc):

    # Search for the target paragraph and highlight it
    for paragraph in doc.paragraphs:
        if paragraph_text in paragraph.text:
            for run in paragraph.runs:
                run.font.highlight_color = WD_COLOR_INDEX.YELLOW  # Highlight the text
            break  # Stop searching after finding the paragraph

    return doc
def process_plagiarized_paragraphs(doc, output_file_path,paragraph_list):

    for item in paragraph_list:
        source_file = item['source']
        target_paragraph = item['paragraph']


        doc = highlight_paragraph(target_paragraph,doc)

    doc.save(output_file_path)


