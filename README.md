# MarkdownMerge

Send templated emails in markdown.


## Install

`pip install markdown_merge`

## How to use

### Provide your SMTP server settings, e.g. for fastmail
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
cfg = dict(EMAIL_HOST='smtp.fastmail.com', EMAIL_PORT=465,
    EMAIL_HOST_USER='XXX@fastmail.com', EMAIL_HOST_PASSWORD='XXX', EMAIL_USE_SSL=True)
```

</div>

</div>

Alternately you can put your server settings in `mail_settings.py`. There's an example settings file in the repo.

### Provide your email details
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
from_addr = get_addr('XXX@fastmail.com', 'Jeremy Howard')
to_addrs = [get_addr('douglas@example.com', 'Douglas Adams'),
            get_addr('cleese@example.com', 'John Cleese')]
inserts  = [{'special': "Thanks for all the fish."},
            {'special': "That was a silly walk."}]

msg = """## Hello there!

Here is your special message: *{special}*"""
```

</div>

</div>
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
ml = MarkdownMerge(to_addrs, from_addr, 'A message', msg=msg, inserts=inserts)
```

</div>

</div>

Optionally, enable *test* mode to just print the messages, instead of sending them.
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
ml.set_test(True)
```

</div>

</div>

### Send your messages
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
ml.send_msgs()
```

</div>

</div>

## Credits

All the hard work is done by Django mail, python-markdown, and python. So thanks to the authors of those projects!
