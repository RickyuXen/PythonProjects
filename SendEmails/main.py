import os
from pathlib import Path
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import ssl
import smtplib
import random

from dotenv import load_dotenv

# Python project to send a 'fun' email package consisting of: a joke, an inspirational quote, and a picture of a cute animal.
# Open to extension;

# Taken from https://www.eslkidsgames.com/jokes-bot-random-joke-generator (I can't come up with good jokes)
jokes = {1:"I was just looking at my ceiling. Not sure if it's the best ceiling in the world, but it's definitely up there.", 
    2:"what do you call a dog that can do magic tricks? a labracadabrador", 
    3:"Why did the burglar hang his mugshot on the wall? To prove that he was framed!", 
    4:"Two guys walked into a bar, the third one ducked.", 
    5:"I cut my finger chopping cheese, but I think that I may have grater problems.", 
    6:"I'd like to start a diet, but I've got too much on my plate right now.", 
    7:"I finally bought the limited edition Thesaurus that I've always wanted. When I opened it, all the pages were blank. I have no words to describe how angry I am."}

quotes = {1:"\"I didn't fail the test. I just found 100 ways to do it wrong.\" - Benjamin Franklin", 
    2:"\"Winning isn't everything, but wanting to win is.\" - Vince Lombardi", 
    3:"\"When you give up, that's when the game ends.\" - Mitsuyoshi Anzai", 
    4:"\"Whatever you lose, you'll find it again. But what you throw away you'll never get back.\" - Kenshin Himura ", 
    5:"\"Never put off till tomorrow what you can do the day after tomorrow just as well.\" - Mark Twain", 
    6:"\"The greatest glory in living lies not in never falling, but in rising every time we fall.\" - Nelson Mandela", 
    7:"\"Love the life you live. Live the life you love.\" - Bob Marley"}

# image names in image folder
randomImages = ["penguin.jpg",
                "otter.jpg",
                "hehecat.jpg",
                "pompuppy.jpg",
                "panda.jpg"]

# environmental variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

email_sender = os.getenv("EMAIL")
email_password = os.getenv("APP_PASSWORD")

# list of email recipients 
email_receiver = []

def main():
    for receiver in email_receiver: # send to each recipient
        joke_int = random.randint(1,len(jokes))
        quote_int = random.randint(1,len(quotes))

        jokeStr = jokes[joke_int]
        quoteStr = quotes[quote_int]

        subject = 'Uplifting Package'

        body = f"""PACKAGE DELIVERY (not an actual package)\n
        """

        # Initalization
        em = EmailMessage()  # to send with images/HTML

        em['From'] = email_sender
        em['To'] = receiver
        em['Subject'] = subject

        em.set_content(body)

        image_cid = make_msgid()
        em.add_alternative(f"""
        <html>
            <body>
            Joke of the day:<br> {jokeStr}<br><br>

            Quote of the day:<br> {quoteStr}<br><br>

            Here's a cute picture: 
            <img src = "cid: {image_cid}">
            <body>
        <html>
        """.format(image_cid=image_cid[1:-1]), subtype='html')
        
        # obtain random image
        random_image = randomImages[random.randint(0,len(randomImages) - 1)]

        # images\file\path\here
        imageFile = f"C:\Important Files\TestCS\PythonProjects\SendEmails\images\{random_image}"

        with open(imageFile, 'rb') as img:
            maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
            em.get_payload()[1].add_related(img.read(), maintype=maintype,subtype=subtype,cid=image_cid)

        context = ssl.create_default_context()

        # Send email smtp = Simple Mail Transfer Protocol
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, receiver, em.as_string())

if __name__ == "__main__":
    main()
