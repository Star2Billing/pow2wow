#!/usr/bin/env python
# vim: set expandtab shiftwidth=4:

__author__ = "Belaid Arezqui (areski@gmail.com)"
__copyright__ = "Copyright (C) 2010 - Belaid Arezqui"
__version__ = "1.0"


# Load Python modules
import sys, os

sys.path.append( os.path.dirname(os.path.abspath( __file__ )) + '/py-asterisk')

from Asterisk.Config import Config
from Asterisk.Manager import Manager
import random



sample = True
#sample = False

#
# ------------------------------ CLASS -----------------------------
#

class conference(object):
    
    
    def conference_list(self):

        if (sample) :
            obj_list = []

            obj_conf_list = dict()
            obj_conf_list['confno'] = '400'
            obj_conf_list['member'] = str(random.randrange(1, 10))
            obj_conf_list['activity'] = '1'
            obj_list.append(obj_conf_list)

            obj_conf_list = dict()
            obj_conf_list['confno'] = '5000'
            obj_conf_list['member'] = str(random.randrange(1, 10))
            obj_conf_list['activity'] = '1'
            obj_list.append(obj_conf_list)

            return obj_list


        try :
            manager = Manager(*Config().get_connection())
            conflist = manager.Command("meetme list concise")
        except:
            #print "There is an error!"
            return None
        else:

            obj_list = []
            for x, val in enumerate(conflist) :
                if (val.find('!') <> -1) :
                    sp_list = val.split( '!')
                    obj_conf_list = dict()
                    obj_conf_list['confno'] = sp_list[0]
                    obj_conf_list['member'] = sp_list[1]
                    obj_conf_list['activity'] = sp_list[1]

                    obj_list.append(obj_conf_list)


            return obj_list

    def create_member(self, no):
        obj_conf_list = dict()
        obj_conf_list['callerno']       = no
        obj_conf_list['cid_number']     = str(random.randrange(800120000, 809000000))
        obj_conf_list['cid_name']       = 'name' + str(random.randrange(100, 999))
        obj_conf_list['channel']        = 'mychannel'
        obj_conf_list['user_type']      = '1'
        obj_conf_list['monitor']        = ''
        obj_conf_list['muted']          = ''
        obj_conf_list['floor']          = ''
        obj_conf_list['istalking']      = str(random.randrange(0, 2))
        obj_conf_list['callduration']   = str(random.randrange(10, 15)) + ':' + str(random.randrange(0, 59))

        return obj_conf_list

    """
    Concise MeetMe List output
    [0] => Caller #
    [1] => Callerid Number
    [2] => Callerid Name
    [3] => Channel:
    [4] => 1 for Admin, NULL for User
    [5] => 1 for Monitor, Null otherwise
    [6] => 1 for Muted, NULL for UnMuted
    [7] => 1 for Resquests Floor, 0 otherwise
    [8] => 1 for 'Is Talking', 0 otherwise
    [9] => Call duration
    """
    def conference_member(self, confno):

        if (sample) :
            obj_list = []

            for i in range(1, random.randrange(9, 10)):
                obj_conf_list = self.create_member(i)
                obj_list.append(obj_conf_list)
                
            return obj_list
        
        if not (IsInt(confno)):
            return None
        
        try :
            manager = Manager(*Config().get_connection())
            conflist = manager.Command("meetme list " + str(confno) + " concise")
        except:
            #print "There is an error!"
            return None
        else:

            obj_list = []
            for x, val in enumerate(conflist) :
                if (val.find('!') <> -1) :
                    sp_list = val.split( '!')
                    obj_conf_list = dict()
                    obj_conf_list['callerno']       = sp_list[0]
                    obj_conf_list['cid_number']     = sp_list[1]
                    obj_conf_list['cid_name']       = sp_list[2]
                    obj_conf_list['channel']        = sp_list[3]
                    obj_conf_list['user_type']      = sp_list[4]
                    obj_conf_list['monitor']        = sp_list[5]
                    obj_conf_list['muted']          = sp_list[6]
                    obj_conf_list['floor']          = sp_list[7]
                    obj_conf_list['istalking']      = sp_list[8]
                    obj_conf_list['callduration']   = sp_list[9]

                    obj_list.append(obj_conf_list)
            

            return obj_list

    def mute_member(self, confno, usernumber):

        if not (IsInt(confno)):
            return None

        if not (IsInt(usernumber)):
            return None

        try :
            manager = Manager(*Config().get_connection())
            action_result = manager.Command("meetme mute " + str(confno) + " " + str(usernumber))
        except:
            return None

    def unmute_member(self, confno, usernumber):

        if not (IsInt(confno)):
            return None

        if not (IsInt(usernumber)):
            return None

        try :
            manager = Manager(*Config().get_connection())
            action_result = manager.Command("meetme unmute " + str(confno) + " " + str(usernumber))
        except:
            return None

    def kick_member(self, confno, usernumber):

        if not (IsInt(confno)):
            return None
        
        try :
            manager = Manager(*Config().get_connection())
            print "meetme kick " + str(confno) + " " + str(usernumber)
            action_result = manager.Command("meetme kick " + str(confno) + " " + str(usernumber))
        except:
            return None

    def invite_member(self, invite_callerid, invite_route, confno, phonenumber):
        
        if not (IsInt(confno)):
            return None

        if not (IsInt(phonenumber)):
            return None

        channel = invite_route + phonenumber;
        context = "meetme_context";
        extension = confno;
        priority = "1";
        application = None;
        data = None;
        #application = "MeetMe";
        #data = confno+",dT";
        timeout = "30000";
        variable = "";
        account = "";
        async = True;
        
        try :
            manager = Manager(*Config().get_connection())
            action_result = manager.Originate(channel, context, extension, priority, application, data, timeout, invite_callerid, variable, account, async);
        except:
            raise


# ------------------------------ FUNCTION ------------------------------

def IsInt( str ):
    """ Is the given string an integer?    """
    ok = 1
    try:
        num = int(str)
    except ValueError:
        ok = 0
    except TypeError:
        ok = 0
    return ok



# ------------------------------ MAIN ------------------------------  
if __name__ == '__main__':

    import pprint
    pp = pprint.PrettyPrinter(depth=6)


    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"

    inst_conference = conference()
    obj_conf_list = inst_conference.conference_list()
    pp.pprint(obj_conf_list)

    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"

    inst_conference = conference()
    obj_conf_list = inst_conference.conference_member("5000")
    pp.pprint(obj_conf_list)

    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"

    #print "KICK user 1 in room 5000"
#res = inst_conference.kick_member("5000", "1")

    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    invite_route = "SIP/aresksip/";
    confno = "5000";
    phonenumber = "6503909212";
    res = inst_conference.invite_member(phonenumber, invite_route, confno, phonenumber)
