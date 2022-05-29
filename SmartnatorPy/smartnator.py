import httpx, random, html, time
from ssl import create_default_context
from bs4 import BeautifulSoup


class CertVerifyFixAdapter(httpx.HTTPTransport):
    def init_poolmanager(self, *args, **kwargs):
        context = create_default_context()
        kwargs["ssl_context"] = context
        return super(CertVerifyFixAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_default_context()
        kwargs["ssl_context"] = context
        return super(CertVerifyFixAdapter, self).proxy_manager_for(*args, **kwargs)


class Smartnator:
    def __init__(self):
        self.session = httpx.Client(transport=CertVerifyFixAdapter())
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
            }
        )

        self.url = "https://www.smartnator.com"
        self.token = self.session.get(self.url).cookies["csrf_gmailnator_cookie"]

    def getEmail(self, option):
        options = []
        if option == "domain":
            options.append(1)
        elif option == "plus":
            options.append(2)
        elif option == "dot":
            options.append(3)
        elif option == "random":
            options.append(random.choice([1, 2, 3]))

        return self.session.post(
            self.url + "/index/indexquery",
            data={
                "csrf_gmailnator_token": self.token,
                "action": "GenerateEmail",
                "data[]": options,
            },
        ).json()["email"]

    def getInbox(self, email):
        res = self.session.post(
            self.url + "/mailbox/mailboxquery",
            data={
                "csrf_gmailnator_token": self.token,
                "action": "LoadMailList",
                "Email_address": email,
            },
        )

        messages = []
        for message in res.json():
            if "https://fastestvpn.com/lifetime-special-deal" in message["content"]:
                continue
            else:
                messages.append(self.getMessageInfos(message))

        return messages

    def getMessageInfos(self, message):
        page = message["content"].strip()

        # -- GET URL --
        url, page = page.split('<a href="', 1)[1].split('"', 1)
        url = html.unescape(url)

        # -- GET SENDER --
        sender, page = page.split("<td>", 1)[1].split("</td>", 1)
        sender = html.unescape(sender)

        sender, _, sender_address = sender.partition("<")
        if sender_address:
            sender = sender.rstrip()
            sender_address = sender_address.split(">", 1)[0]

        # -- GET SUBJECT --
        subject, page = page.split("<td>", 1)[1].split("</td>", 1)
        subject = html.unescape(subject)

        content = self.getMessageContent(url)

        return {
            "sender": sender,
            "sender_address": sender_address,
            "subject": subject,
            "url": url,
            "content": content,
        }

    def getMessageContent(self, url):
        page = self.session.get(url)
        page = page.text.split('<iframe srcdoc="', 1)[1].split('"', 1)[0]
        soup = BeautifulSoup(page, features="html.parser")

        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        text = soup.get_text()

        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # -- REMOVE HTML TAGS --
        text = html.unescape(text)

        with open("test.txt", "w", encoding="utf-8") as f:
            f.write(text)

        return text

    def waitForMessage(self, email, **user_options):

        options = {
            "sender": None,
            "sender_address": None,
            "subject": None
        }
        options.update(user_options)

        while True:
            time.sleep(3)
            messages = self.getInbox(email)
            for message in messages:
                if options["sender"] and options["sender"] != message["sender"]:
                    continue
                if options["sender_address"] and options["sender_address"] != message["sender_address"]:
                    continue
                if options["subject"] and options["subject"] != message["subject"]:
                    continue
                return message