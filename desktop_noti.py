from quote_gen import get_quotes
from win10toast import ToastNotifier
import random
import time

def display_quote():
    quote=get_quotes()
    toaster=ToastNotifier()
    toaster.show_toast("Self Help Quote Of The Day", quote, duration=10)

if __name__=='__main__':
    display_quote()
