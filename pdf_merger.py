import PyPDF2
import sys

inputs = sys.argv[2:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(sys.argv[1] + '.pdf')


pdf_combiner(inputs)
#
# with open('pdf.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)  # Need to open a page before we can manipulate it
#     page.rotateClockwise(90)  # rotates the page 90 degrees.
#     print(reader.numPages)  # will tell us the number of pages
#     writer = PyPDF2.PdfFileWriter()  # needs to be created to write.
#     # gives the page we are working with above, adds the page to the writer object.
#     writer.addPage(page)
#     with open('crooked.pdf', 'wb') as new_file:
#         writer.write(new_file)
# # .getPage(n) hwere n is the page number, it will return that page.
# #
