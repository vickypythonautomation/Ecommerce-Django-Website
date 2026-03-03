
from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

r'''
(virt) PS C:\Users\surface\Documents\GitHub\Ecommerce-Django-Website\ecom> python .\manage.py shell
16 objects imported automatically (use -v 2 for details).

Ctrl click to launch VS Code Native REPL
Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> from django.contrib.sessions.models import Session
>>> session_k = Session.objects.get(pk='3z318fvx9vq8zck0asqw3l31ophicq69')
>>> session_k.get_decoded()
{
    '_auth_user_id': '1', 
    '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend', 
    '_auth_user_hash': 'e2e06845b48e9accbbcd7b9e91a7cf0b69fc8477c7ddb99088349d12dc9dd12a', 
    'session_key': {}
}

>>> 
'''
