# Requirements for Web Application

To run this application, you need:

- **Python 3.10+**
- **Java 11 or 21** (Required for Pyserini/Lucene)
- **Dependencies:**
    - `flask`: Web framework
    - `pyserini`: Search engine interface
    - `scispacy`: For biomedical entity extraction
    - `en_core_sci_sm`: scispaCy model (or other biomedical models)
    - `pandas`: Data handling

## Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_sci_sm
```  
