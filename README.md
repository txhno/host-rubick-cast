# Rubick CAST Streamlit Hosting

This repository hosts the Rubick CAST HTML documentation in Streamlit and includes a downloadable DOCX version.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

Use these fields:

- Repository: `txhno/host-rubick-cast`
- Branch: `main`
- Main file path: `app.py`

Keep `app.py`, `cast.html`, `rubick_cast_documentation.docx`, and `requirements.txt` in the repository root.
