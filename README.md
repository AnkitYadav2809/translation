# Language Translation App

This project is a language translation application built with Streamlit. It allows users to input text or upload documents (.docx or .pdf) for translation into various languages. The application detects the language of the input text and translates it into the selected target language.

## Features

- Language detection for input text and documents.
- Translation of text and documents to multiple languages.
- Support for .docx and .pdf document formats.
- User-friendly interface with Streamlit.

## Installation

To run this project, ensure you have Python installed on your machine. Then, follow these steps:

1. Clone this repository:

    ```bash
    git clone <repository-url>
    ```

2. Change into the project directory:

    ```bash
    cd translation-app
    ```

3. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Requirements

- streamlit
- langdetect
- mtranslate
- chardet
- docx
- PyMuPDF

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the text you want to translate in the input text area or upload a document (.docx or .pdf) for translation.

4. Select the target language from the dropdown menu.

5. Click on the "Translate" button to get the translated text.

## Code Overview

### Streamlit Configuration

```python
st.set_page_config(
    page_title="Language Translation App",
    page_icon="🌐",
    layout="wide",
)
```

### Functions

#### `identify_language(text)`

Detects the language of the input text.

#### `translate_text(text, target_language)`

Translates the input text into the specified target language.

#### `read_docx(file)`

Reads the content of a .docx file and returns the text.

#### `read_pdf(file)`

Reads the content of a .pdf file and returns the text.

### Main Application

The main function sets up the Streamlit interface, handles user inputs, detects the language of the input text, and translates it. It also allows users to upload .docx and .pdf files for translation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features or improvements you would like to see.

## License

This project is licensed under the MIT License.

---

Replace `<repository-url>` with the actual URL of your repository. Save this content in a file named `README.md` in the root of your project directory.
