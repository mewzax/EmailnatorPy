# GmailnatorPy
 📮 A simple wrapper for Smartnator (old. Gmailnator) to get unlimited gmail written in Python

### Hello World
[Gmailnator](smartnator.com) changed their name to Smartnator and their private API so this is a package to continue using it

### Install
`pip install git+https://github.com/Mewzax/GmailnatorPy`

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

### Docs

#### .getEmail(email_type)
PARAMETER | TYPE | DESCRIPTION
--- | --- | ---
email_type | [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) | Can be domain, plus, dot or random
#### .waitForMessage(email, **options)

PARAMETER | TYPE | DESCRIPTION
--- | --- | ---
email | [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) | The email wich will receive the message
sender | Optional [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) | The message's sender name
sender_address | Optional [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) | The message's sender email
subject | Optional [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) | The message's subject

### Credits
Repository inpired by [h0nda](https://github.com/h0nde)