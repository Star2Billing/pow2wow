#!/usr/bin/env python
# vim: set expandtab shiftwidth=4:

__author__ = "Belaid Arezqui (areski@gmail.com)"
__copyright__ = "Copyright (C) 2010 - Belaid Arezqui"
__version__ = "0.1"

# Load Python modules
import os
import datetime
import random
import manager


voipserver_host     = "localhost"
voipserver_login    = "meetmeuser"
voipserver_passw    = "meetmepw"
voipserver_port     = 5038
voipserver_server_type = 1


#
# ------------------------------ CLASS -----------------------------
#

class meetme(object):

    inst_voipserver = None
    
    def conference_list(self):

        self.inst_voipserver = voipserver()
        # Connect to Asterisk AMI
        self.inst_voipserver.connect(voipserver_host, voipserver_login, voipserver_passw, voipserver_port, voipserver_server_type)

        command = "meetme list concise"
        result = self.inst_voipserver.command(command)
        
        print result 

        self.inst_voipserver.disconnect()

    def conference_member(self, confno):

        inst_voipserver = voipserver()



class voipserver(object):
    _voipserver             = None
    _voipserver_host        = None
    _voipserver_login       = None
    _voipserver_passw       = None
    _voipserver_port        = 5038      # Asterisk Default port
    _voipserver_server_type = 1         # 1 = Asterisk
    
    def connect (self, host, login, password, port, server_type):
        
        if (self._voipserver_host != host or
            self._voipserver_login != login or
            self._voipserver_passw != password or
            self._voipserver_port != port or
            self._voipserver_server_type != server_type or
            self._voipserver == None) :
            
            # we have different outbound server parameter so let s connect
            if self._voipserver != None:
                self.disconnect()
            
            self._voipserver_host         = host
            self._voipserver_login        = login
            self._voipserver_passw        = password
            self._voipserver_port         = port
            self._voipserver_server_type  = server_type
            
            try :
                res_try_connect = self.try_connect()
            except :
                raise
            
            return res_try_connect
        
        return True
        
    def try_connect (self):
        
        # logging.debug("OutBound Server try_connect : "+self._voipserver_host+" - server_type : "+str(self._voipserver_server_type))

        # Asterisk
        if (self._voipserver_server_type == 1) :
            
            # instance Manager
            self._voipserver = manager.Manager()
            
            # connect & login with Asterisk
            try :
                self._voipserver.connect(self._voipserver_host);
                self._voipserver.login(self._voipserver_login, self._voipserver_passw);
                
            except manager.ManagerSocketException, (errno, reason):
                #logging.info("Error connecting to the manager: %s" % reason);
                raise
            except manager.ManagerAuthException, reason:
                #logging.info("Error logging in to the manager: %s" % reason);
                raise
            except manager.ManagerException, reason:
                #logging.info("Error: %s" % reason);
                raise
        
    def try_originate (self, server_type = None, channel = None, exten = None, context = None, priority = None, timeout = None, caller_id = None, async = True, account = None, application = None, data = None, variables = None, actionid = None, retry = None, retry_time = None):
        
        # server_type :  1 = Asterisk  
        if (self._voipserver_server_type == 1):
            # Asterisk
            try: 
                self.try_originate_manager (channel, exten, context, priority, timeout, caller_id, async, account, application, data, variables, actionid);
            except OriginateException, reason:
                raise OriginateException(reason)
        

    def try_originate_manager (self, channel = None, exten = None, context = None, priority = None, timeout = None, caller_id = None, async = True, account = None, application = None, data = None, variables = None, actionid = None):
        
        try : 
            response = self._voipserver.originate(channel, exten, context, priority, timeout, caller_id, async, account, application, data, variables, actionid)
            return response
        except manager.ManagerException, reason:
            # Second attempt
            self.disconnect()
            self.try_connect()
            try :
                response = self._voipserver.originate(channel, exten, context, priority, timeout, caller_id, async, account, application, data, variables, actionid)
                return response
            except manager.ManagerException, reason:
                logging.info("ManagerException : error Connection on second attempt = "+ str(reason))
                raise OriginateException(reason)
        
        return None

    def command (self, command):

        response = self._voipserver.command(command)
        return response
     
    def disconnect (self):
        
        self._voipserver.close()
        self._voipserver = None








# ------------------------------ MAIN ------------------------------  
if __name__ == '__main__':
    
    inst_meetme = meetme()
    inst_meetme.conference_list()

    
