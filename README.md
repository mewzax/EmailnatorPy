# GmailnatorPy
 📮 A simple wrapper for Smartnator (old. Gmailnator) to get unlimited gmail written in Python

```py
from SmartnatorPy import Smartnator

if __name__ == "__main__":
    sn = Smartnator()
    email = sn.getEmail("dot")
    print("Your email:", email)
    message = sn.waitForMessage(email, sender_address="info@service-mail.zalando.fr") # can be sendern sender_address, subject
    print("Your message:" message) # {"sender": sender, "sender_address": sender_address, "subject": subject, "url": url, "content": content }
```