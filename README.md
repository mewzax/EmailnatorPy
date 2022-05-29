# GmailnatorPy
 📮 A simple wrapper for Smartnator (old. Gmailnator) to get unlimited gmail written in Python

### Install
`pip install https://github.com/Mewzax/GmailnatorPy`


### Usage
```py
from SmartnatorPy import Smartnator
if __name__ == "__main__":
    sn = Smartnator()
    email = sn.getEmail("dot")
    print("Your email:", email)
    message = sn.waitForMessage(email, sender_address="info@service-mail.zalando.fr")
    print("Your message:" message) # {"sender": sender, "sender_address": sender_address, "subject": subject, "url": url, "content": content }
```

### Options
To filter your mails, you can use options

* sender="`sender_username`"
* sender_address="`sender_email`"
* subject="`message_subject`"