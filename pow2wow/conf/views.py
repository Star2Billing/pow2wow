# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from conf.forms import InviteForm, loginForm
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


import sys, os

sys.path.append( os.path.dirname(os.path.abspath( __file__ ))+ '/../' )
from voip_res.conf import conference



def index(request):
    template = 'index.html'

    inst_conference = conference()
    obj_conf_list = inst_conference.conference_list()
    errorlogin = False

    if request.method == 'POST':
        try:
            action = request.POST['action']
        except (KeyError):
            action = "login"
        
        if action=="logout":
            logout(request)
        else:
            loginform = loginForm(request.POST)
            if loginform.is_valid():
                cd = loginform.cleaned_data
                user = authenticate(username=cd['user'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        # Redirect to a success page.
                    else:
                        # Return a 'disabled account' error message
                        errorlogin = True
                else:
                    # Return an 'invalid login' error message.
                    errorlogin = True

    loginform = loginForm()

    data = {
        'conf_list' : obj_conf_list,
        'loginform' : loginform,
        'errorlogin' : errorlogin,
        #'is_authenticated' : request.user.is_authenticated()
    }
    form = InviteForm()
    return render_to_response(template, data,
           context_instance = RequestContext(request))


def member(request, confno):
    template = 'member.html'
    inst_conference = conference()

    if request.user.is_authenticated():
        if request.method == 'POST':
            form = InviteForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                res = inst_conference.invite_member(cd['phonenumber'], settings.INVITE_ROUTE, confno, cd['phonenumber'])
    
    form = InviteForm()

    
    obj_conf_member = inst_conference.conference_member(confno)
    #print conf_member

    if (obj_conf_member) :
        num_member = len(obj_conf_member)
    else :
        num_member = 0

    data = {
        'confno' : confno,
        'conf_member' : obj_conf_member,
        'number_conf_member' : num_member,
        'form': form,
    }

    return render_to_response(template, data,
           context_instance = RequestContext(request))

def member_refresh(request, confno):
    template = 'member_refresh.html'
    inst_conference = conference()

    obj_conf_member = inst_conference.conference_member(confno)
    #print conf_member

    data = {
        'confno' : confno,
        'conf_member' : obj_conf_member,
    }

    return render_to_response(template, data,
           context_instance = RequestContext(request))

@login_required
def kick(request, confno, usernumber):
    print "kick %s, %s" % (confno, usernumber)
    inst_conference = conference()
    obj_conf_member = inst_conference.kick_member(confno, usernumber)

@login_required
def kickall(request, confno):
    print "kick %s, %s" % (confno, "all")
    inst_conference = conference()
    obj_conf_member = inst_conference.kick_member(confno, "all")

@login_required
def mute(request, confno, usernumber):
    print "mute %s, %s" % (confno, usernumber)
    inst_conference = conference()
    obj_conf_member = inst_conference.mute_member(confno, usernumber)

@login_required
def unmute(request, confno, usernumber):
    print "unmute %s, %s" % (confno, usernumber)
    inst_conference = conference()
    obj_conf_member = inst_conference.unmute_member(confno, usernumber)


