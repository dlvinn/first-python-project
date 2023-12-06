import pyttsx3
import PyPDF2

pdfreader = PyPDF2.PdfReader(open('book.pdf','rb'))
speaker = pyttsx3.init()
speaker.setProperty("rate",150)
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace("\n"," ")
    print(clean_text) 




    speaker.save_to_file("sarsam", "sarsam.mp3")


speaker.runAndWait()

speaker.stop()

