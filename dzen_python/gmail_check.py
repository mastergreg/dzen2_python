from time import sleep
from threading import Thread
from config_mod import GMAIL_NOTIFIER,GMAIL_BACKGROUND_COLOR,GMAIL_COLOR,GMAIL_UNREAD_COLOR,GMAIL_MAILBOXES,GMAIL_USERNAME,GMAIL_PASSWORD
from colors import set_colors,set_normal_color
from imaplib import IMAP4_SSL
from icons import set_icon
UNREAD=""

from gi.repository import Notify, GLib, Gtk
def unread():
    return UNREAD
def set_unread(un="n/a"):
    global UNREAD
    UNREAD = "{0}{1}{2} {3}{4}".format(set_colors(GMAIL_UNREAD_COLOR,GMAIL_BACKGROUND_COLOR), 
            un,
            set_colors(GMAIL_COLOR,GMAIL_BACKGROUND_COLOR),
            set_icon("envelope.xbm"),
            set_normal_color())

set_unread()

class gmail_notifier(object):
    def __init__(self):
        self._unread = 0
        Notify.init("Gmail Notifier")
    def check(self, unread):
        if GMAIL_NOTIFIER == "ON" and self._unread < unread:
            self.notifyme(unread)
            self._unread = unread
    def notifyme(self, unread, icon="mail", transient=True, urgency=Notify.Urgency.NORMAL):
        summary = "You got mail"
        body = "You got {0} unread emails :)".format(unread)
        #im-message-new is not a standard icon name, neither is user-*, but they are present
        #in many themes that support empathy. lookup the supplied icon and fallback to skype
        #if missing
        if not Gtk.IconTheme.get_default().has_icon(icon):
            icon = "mail"
        n = Notify.Notification.new(summary, body, icon)
        n.set_hint("transient", GLib.Variant.new_boolean(transient))
        n.set_urgency(urgency)
        n.show()

class get_gmail_check(Thread):
    def run(self):
        global UNREAD
        notifier = gmail_notifier()
        while True:
            try:
                srv = IMAP4_SSL("imap.gmail.com")
                count=[]
                srv.login(GMAIL_USERNAME,GMAIL_PASSWORD)
                unseen = 0
                for i in GMAIL_MAILBOXES.split(','):
                    srv.select(i)
                    status,count=srv.search(None,'UnSeen')
                    #unseen= len(c.get_inbox_conversations(is_unread=True))
                    unseen += len(count[0][1:].split())

                notifier.check(unseen)
                set_unread(unseen)
                srv.close()
                srv.logout()
                sleep(60)
            except:
                sleep(60)

