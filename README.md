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

### Docs

<h2 id="lol">.waitForMessage(email, **options)</h2>
<h3>Wait for the message you want</h3>

PARAMETER | TYPE | DESCRIPTION | EXEMPLE
--- | --- | --- | ---
image | [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) - [Buffer](https://developer.mozilla.org/en-US/docs/Glossary/buffer) - [Canvas.Image](https://www.tabnine.com/code/javascript/functions/canvas/loadImage) | Image to affect | https://someimage.com/image.png
