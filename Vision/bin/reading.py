def read(filename, pageno):
    import pyttsx3
    import PyPDF2
    book = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print (pages)
    page = pdfReader.getPage(pageno)
    text = page.extractText()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

read("dbms.pdf", 10)