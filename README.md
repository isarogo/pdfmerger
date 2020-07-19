# pdfmerger
a lightweight pdf merger utility in python

## Package Requirements

- PyPDF2
- sys

## Usage

Place the .pdfs you wish to merge into the same directory as `pdf_merger.py`.

Run the following code to merge:

`python pdf_merger.py <desired_name_of_output> <name_of_first_doc.pdf> <name_of_nth_doc.pdf>`

Where

- `desired_name_of_output`: the name you wish the completed merge file to take. The program will automatically add the `.pdf` extension.
- `name_of_first_doc.pdf`: the name of the first document you would like merged. The program will place this pdf first.
- `name_of_nth_doc.pdf`: the name of the next document you would like merged.

You may input more than two pdfs to merge at a time. There is no hard-coded limit.

## Example:
`python pdf_merger.py CombinedPdfs document1.pdf document2.pdf documentN.pdf`
