# useful-scripts
Useful scripts for everyday use.

### Contribution Guidelines
- Create scripts that will save people time, make difficult tasks easier, or just fulfill an interesting purpose. If you would use it, chances are others would as well.
- Ensure scripts can be run "as is", inputs should be passed as cli arguments or similar.
- When you add a script, add a brief description to the [Scripts](#scripts) section along with any non-standard libraries.
- If you want to be added as a collaborator, just let me know!

### Scripts
- `archive_files.py` - archive a file or folder using the zip format.
- `convert_currency.py` - convert a the value of a currency to a second currency.
- `pdf_extract.py` - extract text from a PDF file, accuracy depends on the quality and encoding of the PDF. Uses `PyPDF2`, `pyperclip` (for `--copy` only).
- `pdf_join.py` - merge multiple PDFs into a single file. Uses `PyPDF2`.
- `pdf_split.py` - split a PDF file into multiple files. Uses `PyPDF2`.
- `random_pass.py` - generate a secure random password with a mix of uppercase and lowercase characters, digits, and special characters.
- `stock_checker.py` - check and graph the price of a stock across a range. Uses `matplotlib`, `pandas`, `yfinance`.
