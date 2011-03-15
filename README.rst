

.. image:: https://github.com/Star2Billing/cdr-stats/raw/master/cdr_stats/resources/logo/icon_600.png

Pow2Wow is a Conference Monitoring tool for Asterisk/Freeswitch. It allows you to 
interrogate the conferencing server and see who is actually present into the conference room.
Some basics features, such as Mute, UnMute, Kick, Invite or Talk, are available.

It is based on the Django Python Framework which enables the building 
of clean, maintainable web applications, and encourages rapid 
development with clean and pragmatic design.

Star2Billing S.L. is the company behind the development of Pow2Wow, and 
was originally formed to replace the project WebMeetMe with a more flexible and suitable solution. 
Professional support for  installation and consultancy services are available


Applications
------------

Monitor all the active conference room
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Usage : http://localhost:8000/conf/

    - Login option is available to become an Admin (Moderator)


Add your conf number to the url to monitor a conference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-

    Usage : http://localhost:8000/conf/5000/    

    - Action :
        http://localhost:8000/conf/5000/kickall
        
    - Mute an user :
        http://localhost:8000/conf/5000/mute/1
    
    - Unmute an user :
        http://localhost:8000/conf/5000/unmute/1
    
    - Kick an user :
        http://localhost:8000/conf/5000/kick/1


Admin interface
~~~~~~~~~~~~~~~

    This interface allow you to create new moderator :
    http://localhost:8000/admin/


2 type of users
~~~~~~~~~~~~~~-

    - Admin : Have rights to any action : Kick, Mute, Unmute, stop conference, Invite User.
    
    - Visitor : Visitor won't be able to run any action and the options won't be displayer.
    

Configure the Invite Route to use, SIP / IAX and the trunk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Edit /usr/share/django_app/pow2wow/settings.py

    # INVITE SETTINGS
    # Set how Asterisk will invite new members
    INVITE_ROUTE = "SIP/areski/";


Coding Conventions
------------------

Please refer to those sources for the Coding Conventions :

    - http://docs.djangoproject.com/en/dev/internals/contributing/#coding-style

    - http://www.python.org/dev/peps/pep-0008/
    
    
Support 
-------

Star2Billing S.L. offers consultancy including installation, training and customisation 

Please email us at sales@star2billing.com for more information
    

