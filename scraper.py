import requests
from bs4 import BeautifulSoup
import smtplib
import time

def priceTracker():
    URL = 'https://www.amazon.in/Fossil-Season-Chronograph-Black-Watch/dp/B0183NW5H6?pf_rd_p=65673e09-07e3-4fb8-83f4-60cbb5447790&pd_rd_wg=RLtmS&pf_rd_r=JG1DMKXAC407RHD5TNJE&ref_=pd_gw_unk&pd_rd_w=qhqeJ&pd_rd_r=51e3dd4d-8138-45ac-b323-63db54062580'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:-1].replace(',', ''))
    # print(type(converted_price))
    print(title.strip())
    print(converted_price)

    desired_price = 7000
    if(converted_price < desired_price):
        send_mail(title, converted_price, desired_price, URL)


def send_mail(title, converted_price, desired_price, URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nirmaldalmia17@gmail.com', 'wywygsfkrvhcpbug')

    subject = 'Price Alert!'
    body = 'The price of the product ' + str(title.strip()) + ' has fallen below your desired price of ' + str(desired_price) + '.The current price is ' + str(converted_price) + '. Check it out at the link: ' + str(URL)
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'nirmaldalmia17@gmail.com',
        'nirmal.dalmia.16cse@bml.edu.in',
        msg
    )
    print("Email successfully sent!")

    server.quit()

while True:
    priceTracker()
    time.sleep(86400)