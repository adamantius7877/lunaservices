"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .luna.luna import lunanode
from .models import NodeModel
from .forms import LunaMessageForm

def home(request):
    """Renders the home page."""
    if request.method == 'POST':
        # Form was submitted
        textbox_value = request.POST.get('textToSpeakBox')
        lunanode.Speak(textbox_value)
    else:
        textbox_value = ''

    node =  NodeModel()
    node.HostName = lunanode.Name
    node.NodeId = lunanode.NodeId
    node.IPAddress = lunanode.GetIp()
    message = LunaMessageForm()
    # Example: Pass the textbox value back to the template in the context
    context = {
        'message': message,
        'node': node,
        'text': textbox_value,
        'title':'LUNA Control Panel',
        'year':datetime.now().year,
    }
    return render(
        request,
        'app/index.html',
        context
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
