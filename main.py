import streamlit as st
from langdetect import detect
from io import BytesIO
from mtranslate import translate
import chardet
import docx
import fitz  # PyMuPDF library for PDF handling

# Streamlit configuration
st.set_page_config(
    page_title="Language Translation App",
    page_icon="🌐",
    layout="wide",
)

def identify_language(text):
    try:
        language = detect(text)
        return language
    except:
        return None

def translate_text(text, target_language):
    try:
        translated_text = translate(text, target_language)
        return translated_text
    except:
        return None

def read_docx(file):
    doc = docx.Document(file)
    text = [paragraph.text for paragraph in doc.paragraphs]
    return '\n'.join(text)

def read_pdf(file):
    pdf_content = BytesIO(file.read())
    doc = fitz.open(pdf_content)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text

def main():
    st.title("Language Translation App")

    # Input text area
    input_text = st.text_area("Enter the text you want to translate:")

    # Language detection
    identified_language = identify_language(input_text)

    if identified_language:
        st.info(f"Identified Language: {identified_language}")
    else:
        st.warning("Language detection failed. Please provide valid text.")

    # Target language selection
    target_language = st.selectbox("Select the target language:", ["en", "es", "fr", "hi", "sanskrit"])

    # Translation
    if st.button("Translate"):
        if identified_language and input_text:
            translated_text = translate_text(input_text, target_language)
            if translated_text is not None:
                st.success(f"Translation to {target_language}: {translated_text}")
            else:
                st.warning("Translation failed. Make sure you have valid input text and target language.")
        else:
            st.warning("Unable to perform translation. Make sure you have valid input text.")

    # File upload for translation
    st.subheader("Upload a Document for Translation:")
    uploaded_file = st.file_uploader("Choose a document (.docx or .pdf)", type=["docx", "pdf"])

    if uploaded_file is not None:
        file_type = uploaded_file.type.split('/')[1]
        st.info(f"File Uploaded Successfully! File Type: {file_type.upper()}")

        # Perform translation on the document content
        try:
            if file_type == "docx":
                doc_text = read_docx(uploaded_file)
            elif file_type == "pdf":
                doc_text = read_pdf(uploaded_file)
            else:
                st.warning("Unsupported file type. Please upload a valid document.")
                return

            identified_language_doc = identify_language(doc_text)

            if identified_language_doc:
                st.info(f"Identified Language in Document: {identified_language_doc}")
            else:
                st.warning("Language detection failed for the document.")

            if st.button("Translate Document"):
                if identified_language_doc:
                    translated_doc = translate_text(doc_text, target_language)
                    if translated_doc is not None:
                        st.success(f"Translation to {target_language}:\n{translated_doc}")
                    else:
                        st.warning("Translation failed. Make sure the document has valid text.")
                else:
                    st.warning("Unable to perform translation. Make sure the document has valid text.")
        except Exception as e:
            st.error(f"Error processing the document: {e}")

if __name__ == "__main__":
    main()
