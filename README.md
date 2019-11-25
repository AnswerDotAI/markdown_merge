## markdownmailmerge

Send templated emails in markdown.

### Install

```bash
pip install git+https://github.com/jph00/markdownmailmerge
```

### How to use

#### Provide your SMTP server settings, e.g. for [fastmail](https://www.fastmail.com)

```
cfg = dict(EMAIL_HOST='smtp.fastmail.com', EMAIL_PORT=465,
    EMAIL_HOST_USER='XXX@fastmail.com', EMAIL_HOST_PASSWORD='XXX', EMAIL_USE_SSL=True)
```

#### Provide your email details

```
from_addr = get_addr('XXX@fastmail.com', 'Jeremy Howard')
to_addrs = [get_addr('douglas@example.com', 'Douglas Adams'),
            get_addr('cleese@example.com', 'John Cleese')]
inserts  = [{'special': "Thanks for all the fish."},
            {'special': "That was a silly walk."}]

msg = """
## Hello there!

This is an exciting message with three parts:

- This bit
- That bit
- The other bit

Here is your special message: *{special}*
"""
```

Your message should be in markdown format. It will be converted into a two part email, containing both a plain text and an HTML part, so recipients will see whatever format they're set as their preference for viewing mail. Note that anything in curly brackets will be replaced with the contents of the `inserts` dictionary for that address. If there are no bracketed variables to replace, then you don't need to pass any `inserts`.

#### Create `MarkdownMailMerge`

```
ml = MarkdownMailMerge(to_addrs, from_addr, subj='A message', msg=msg, server_settings=cfg, inserts=inserts)
```

#### Optional: test send

```
ml.set_test(True)
ml.send_msgs()
ml.reset()
```

This will print all the messages to be sent to the console, and will not actually send them. `MarkdownMail` remembers what emails it was successfully sent so far (including test sends) and won't re-send them when you call `send_msgs` again; therefore you should run `reset` to reset the counter after a test send.

#### Send your messages

```
ml.set_test(False)
ml.send_msgs()
```

### TODO

- Attachments
- Images

PRs welcome.
