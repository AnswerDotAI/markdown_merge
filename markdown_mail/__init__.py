from django.core.mail import *
from django.conf import *
from markdown import markdown
from email.headerregistry import Address
from time import sleep

__all__ = ['get_addr', 'md2email', 'MarkdownMail']

def get_addr(email, name=None): return Address(email if name is None else name, addr_spec=email)

def md2email(subj, from_addr, to_addrs, md, conn=None, attach=None):
    if not isinstance(to_addrs, (list,tuple)): to_addrs = [to_addrs]
    msg = EmailMultiAlternatives(subj, md, str(from_addr), [str(o) for o in to_addrs], connection=conn)
    msg.attach_alternative(markdown(md), "text/html")
    if attach is not None:
        if not isinstance(attach, (list,tuple)): attach = [attach]
        for att in attach: msg.attach_file(att)
    return msg

class MarkdownMail:
    def __init__(self, addrs, from_addr, subj, msg, server_settings=None, inserts=None):
        if server_settings is not None:
            settings._wrapped=empty
            settings.configure(SECRET_KEY='XXX', **server_settings)
        self.addrs,self.from_addr,self.subj,self.msg,self.i = addrs,from_addr,subj,msg,0
        self.inserts = [{}]*len(addrs) if inserts is None else inserts

    def send_msgs(self, pause=0.5):
        with get_connection() as conn:
            while self.i < len(self.addrs):
                addr,insert = self.addrs[self.i],self.inserts[self.i]
                msg = self.msg.format(**insert)
                md2email(self.subj, self.from_addr, addr, md=msg, conn=conn).send()
                sleep(pause)
                self.i += 1
                if self.i%100==0: print(self.i)

    def set_test(self, test=True):
        backend = ('smtp','console')[test]
        settings.EMAIL_BACKEND = f'django.core.mail.backends.{backend}.EmailBackend'

    def reset(self): self.i=0

