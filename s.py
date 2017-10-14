# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(token="XXX")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="XXX")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="XXX")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="XXX")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="XXX")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="XXX")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="XXX")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="XXX")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="XXX")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="XXX")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="XXX")
ki10.loginResult()
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""✯==== ꧁ ⋆🐯हईທຮຮๅજईह🐯⋆ ꧂ ====✯
✯====⋆⋆[Softbot Thailand]⋆⋆ =====✯
___________________________________

✪[Id]
✪[Mid]
✪[Me] [Mee]
✪[Mic: 'mid']
✪[TL: "Text"]
✪[Renama:"Text"]
✪[Contact on\off]
✪[Join on\off]
✪[Leave on\off]
✪[Share on\off]
✪[Invite cancel:"number of people"]
✪[Add on\off]
✪[Massage add change: "text"]
✪[Com][Comm1]
✪[Clock on\off]
✪[Name clock:'Text']
✪[Refresh]
✪[Cancell]["Delete all self invitations"]
✪[Commet on\off]

      [Commands only for groups]
___________________________________
✪[Gift]
✪[#kicker] [#PHET]
✪[Bot [@1=@10]]
✪[#bye]
✪[#Phet!!]=[คำสั่งอันตราย!!]
✪[Ban on]+["Contact"]
✪Unban on]+["Contact"]
✪[Ban check]
✪[Me ban][Me chack]
✪[whitelist]
✪[P: '@']=[KN]
✪[Bl: '@']
✪[Wl: '@']
✪[BP: '@'/BNK:"name"
✪[Link on/off]
✪[url]
✪[Cancel]
✪[Gn: "Group name"]
___________________________________
✯==== ꧁ Creator ꧂ ====✯

⋆[❦〖Ǥµ ✍Ŧ€₳MжĦ₳ʗҜ฿❂Ŧ✈​✓]⋆

⋆[❦〖Pђëŧ〗☞ᵀËÄMທஇລ❂قB❂T✓]⋆

✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯
"""

mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':True,
    "lang":"JP",
    "comment":"Phet hack bot",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"™Phetㄨ ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "atjointicket":True,
}
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u0c8779ca416157866099d62a8b583706":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error❗")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already❗")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"decided not to comment")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already❗")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted❗")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list〄1�7")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","คำสั่ง","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group❗")
            elif ("Title: "in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Title: ","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Not for use less than group")
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links=[]
                for l in links:
                    if l not in n_links:
                        n_links.append(l)
                for ticket_id in n_links:
                    if wait["atjointicket"] == True:
                        group=cl.findGroupByTicket(ticket_id)
                        cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "Mee" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif "Bot1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':kimid}
                cl.sendMessage(msg)
                ki.sendMessage(msg)
            elif "Bot2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki2mid}
                cl.sendMessage(msg)
                ki2.sendMessage(msg)
            elif "Bot3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki3mid}
                cl.sendMessage(msg)
                ki3.sendMessage(msg)
            elif "Bot4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki4mid}
                cl.sendMessage(msg)
                ki4.sendMessage(msg)
            elif "Bot5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki5mid}
                cl.sendMessage(msg)
                ki5.sendMessage(msg)
            elif "Bot6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki6mid}
                cl.sendMessage(msg)
                ki6.sendMessage(msg)
            elif "Bot7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki7mid}
                cl.sendMessage(msg)
                ki7.sendMessage(msg)
            elif "Bot8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki8mid}
                cl.sendMessage(msg)
                ki8.sendMessage(msg)
            elif "Bot9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki9mid}
                cl.sendMessage(msg)
                ki9.sendMessage(msg)
            elif "Bot10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki10mid}
                cl.sendMessage(msg)
                ki10.sendMessage(msg)
#            elif "Bot11" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki11mid}
                cl.sendMessage(msg)
                ki11.sendMessage(msg)
 #           elif "Bot12" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki12mid}
                cl.sendMessage(msg)
                ki12.sendMessage(msg)
#            elif "Bot13" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki13mid}
                cl.sendMessage(msg)
                ki13.sendMessage(msg)
#            elif "Bot14" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki14mid}
                cl.sendMessage(msg)
                ki14.sendMessage(msg)
            elif "Bot15" == msg.text:
 #               msg.contentType = 13
                msg.contentMetadata = {'mid':ki15mid}
                cl.sendMessage(msg)
                ki15.sendMessage(msg)
#            elif "Bot16" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki16mid}
                cl.sendMessage(msg)
                ki16.sendMessage(msg)
#            elif "Bot17" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki17mid}
                cl.sendMessage(msg)
                ki17.sendMessage(msg)
 #           elif "Bot18" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki18mid}
                cl.sendMessage(msg)
                ki18.sendMessage(msg)
#            elif "Bot19" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki19mid}
                cl.sendMessage(msg)
                ki19.sendMessage(msg)
  #          elif "Bot20" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki20mid}
                cl.sendMessage(msg)
                ki20.sendMessage(msg)
  #          elif "Bot121" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki21mid}
                cl.sendMessage(msg)
                ki21.sendMessage(msg)
#            elif "Bot22" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki22mid}
                cl.sendMessage(msg)
                ki22.sendMessage(msg)
 #           elif "Bot23" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki23mid}
                cl.sendMessage(msg)
                ki23.sendMessage(msg)
  #          elif "Bot24" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki24mid}
                cl.sendMessage(msg)
                ki24.sendMessage(msg)
#            elif "Bot25" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki25mid}
                cl.sendMessage(msg)
                ki25.sendMessage(msg)
 #           elif "Bot26" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki26mid}
                cl.sendMessage(msg)
                ki26.sendMessage(msg)
   #         elif "Bot27" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki27mid}
                cl.sendMessage(msg)
                ki27.sendMessage(msg)
  #          elif "Bot28" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki28mid}
                cl.sendMessage(msg)
                ki28.sendMessage(msg)
  #          elif "Bot29" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki29mid}
                cl.sendMessage(msg)
                ki29.sendMessage(msg)
#            elif "Bot30" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid':ki30mid}
                cl.sendMessage(msg)
                ki30.sendMessage(msg)
            elif msg.text in ["Me bot","Me me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid':mid}
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '9d56d8a2-1190-48f3-944d-5e9da31922a2',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
            elif msg.text in ["Gift gift","Gift you"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '9d56d8a2-1190-48f3-944d-5e9da31922a2',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
            elif msg.text in ["Bot1 gift",]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '5335f8bb-b871-4ff4-a02e-39a519806c36',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Bot2 gift",]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '7ec65c67-d3f8-4c07-b8db-3ba562d12e6b',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ki2.sendMessage(msg)
            elif msg.text in ["Bot3 gift",]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '5335f8bb-b871-4ff4-a02e-39a519806c36',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                kl3.sendMessage(msg)
            elif msg.text in ["ยกเลิก","Cancel","cancal","00"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting❗")
                            cl.sendText(msg.to,"ไม่มีค้างเชิญที่จะยกเลิก❗")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent❗")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group〄1�7")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Cancel","ลบเชิญ","000"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting❗")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent❗")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group。")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"already URL。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group。")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"already off URL。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group。")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "ไม่พบผู้สร้างกลุ่ม"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                          u = "ปิด"
                        else:
                            u = "เปิด"
                        cl.sendText(msg.to,"[ชื่อของกลุ่ม]:\n" + str(ginfo.name) + "\n[Gid]:\n" + msg.to + "\n[ผู้สร้างกลุ่ม:]\n" + gCreator + "\n[ลิ้งค์รูปกลุ่ม]:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n[จำนวนสมาชิก]:" + str(len(ginfo.members)) + "คน\n[จำนวนค้างเชิญ]:" + sinvitee + "คน\n[สถานะลิ้งค์]:" + u + "URL [By: เพชร ทีมทดลองบอท]")
                    else:
                        cl.sendText(msg.to,"Nama Gourp:\n" + str(ginfo.name) + "\nGid:\n" + msg.to + "\nCreator:\n" + gCreator + "\nProfile:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else: 
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group。")
                    else:
                         cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Bot1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki.sendText(msg.to,kimid)
                ki.sendText(msg.to,kimid)
            elif "Bot2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
                ki2.sendText(msg.to,ki2mid)
                ki2.sendText(msg.to,ki2mid)
            elif "Bot3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
                ki3.sendText(msg.to,ki3mid)
                ki3.sendText(msg.to,ki3mid)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki5mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                ki10.sendText(msg.to,ki10mid)
#            elif "Me mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                ki.sendText(msg.to,kimid)
                ki.sendText(msg.to,kimid)
                ki.sendText(msg.to,kimid)
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki2.sendText(msg.to,ki2mid)
                ki2.sendText(msg.to,ki2mid)
                ki2.sendText(msg.to,ki2mid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki3.sendText(msg.to,ki3mid)
                ki3.sendText(msg.to,ki3mid)
                ki3.sendText(msg.to,ki3mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki4.sendText(msg.to,ki4mid)
                ki4.sendText(msg.to,ki4mid)
                ki4.sendText(msg.to,kl4mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,kl5mid)
                ki5.sendText(msg.to,ki5mid)
                ki5.sendText(msg.to,ki5mid)
                ki5.sendText(msg.to,kl5mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki6.sendText(msg.to,ki6mid)
                ki6.sendText(msg.to,ki6mid)
                ki6.sendText(msg.to,ki6mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki7.sendText(msg.to,ki7mid)
                ki7.sendText(msg.to,ki7mid)
                ki7.sendText(msg.to,ki7mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki8.sendText(msg.to,ki8mid)
                ki8.sendText(msg.to,ki8mid)
                ki8.sendText(msg.to,ki8mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                ki9.sendText(msg.to,ki9mid)
                ki9.sendText(msg.to,ki9mid)
                ki9.sendText(msg.to,ki9mid)
                ki9.sendText(msg.to,ki9mid)
                ki10.sendText(msg.to,ki10mid)
                ki10.sendText(msg.to,ki10mid)
                ki10.sendText(msg.to,ki10mid)
                ki10.sendText(msg.to,ki10mid)
                ki10.sendText(msg.to,ki10mid)
                ki11.sendText(msg.to,ki11mid)
                ki11.sendText(msg.to,ki11mid)
                ki11.sendText(msg.to,ki11mid)
                ki11.sendText(msg.to,ki11mid)
                ki11.sendText(msg.to,ki11mid)
                ki12.sendText(msg.to,ki12mid)
                ki12.sendText(msg.to,ki12mid)
                ki12.sendText(msg.to,ki12mid)
                ki12.sendText(msg.to,ki12mid)
                ki12.sendText(msg.to,ki12mid)
                ki13.sendText(msg.to,ki13mid)
                ki13.sendText(msg.to,ki13mid)
                ki13.sendText(msg.to,ki13mid)
                ki13.sendText(msg.to,ki13mid)
                ki13.sendText(msg.to,ki13mid)
                ki14.sendText(msg.to,ki14mid)
                ki14.sendText(msg.to,ki14mid)
                ki14.sendText(msg.to,ki14mid)
                ki14.sendText(msg.to,kl14mid)
                ki14.sendText(msg.to,ki14mid)
                ki15.sendText(msg.to,kl15mid)
                ki15.sendText(msg.to,ki15mid)
                ki15.sendText(msg.to,ki15mid)
                ki15.sendText(msg.to,kl15mid)
                ki15.sendText(msg.to,ki15mid)
                ki16.sendText(msg.to,ki16mid)
                ki16.sendText(msg.to,ki16mid)
                ki16.sendText(msg.to,ki16mid)
                ki16.sendText(msg.to,ki16mid)
                ki16.sendText(msg.to,ki16mid)
                ki17.sendText(msg.to,ki17mid)
                ki17.sendText(msg.to,ki17mid)
                ki17.sendText(msg.to,ki17mid)
                ki17.sendText(msg.to,ki17mid)
                ki17.sendText(msg.to,ki17mid)
                ki18.sendText(msg.to,ki18mid)
                ki18.sendText(msg.to,ki18mid)
                ki18.sendText(msg.to,ki18mid)
                ki18.sendText(msg.to,ki18mid)
                ki18.sendText(msg.to,ki18mid)
                ki19.sendText(msg.to,ki19mid)
                ki19.sendText(msg.to,ki19mid)
                ki19.sendText(msg.to,ki19mid)
                ki19.sendText(msg.to,ki19mid)
                ki19.sendText(msg.to,ki19mid)
                ki20.sendText(msg.to,ki20mid)
                ki20.sendText(msg.to,ki20mid)
                ki20.sendText(msg.to,ki20mid)
                ki20.sendText(msg.to,ki20mid)
                ki20.sendText(msg.to,ki20mid)
            elif "Ps1" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
#            elif "Ps3" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata ={
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" } 
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki11.sendMessage(msg)
                ki12.sendMessage(msg)
                ki13.sendMessage(msg)
                ki14.sendMessage(msg)
                ki15.sendMessage(msg)
                ki16.sendMessage(msg)
                ki17.sendMessage(msg)
                ki18.sendMessage(msg)
                ki19.sendMessage(msg)
                ki20.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki11.sendMessage(msg)
                ki12.sendMessage(msg)
                ki13.sendMessage(msg)
                ki14.sendMessage(msg)
                ki15.sendMessage(msg)
                ki16.sendMessage(msg)
                ki17.sendMessage(msg)
                ki18.sendMessage(msg)
                ki19.sendMessage(msg)
                ki20.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki11.sendMessage(msg)
                ki12.sendMessage(msg)
                ki13.sendMessage(msg)
                ki14.sendMessage(msg)
                ki15.sendMessage(msg)
                ki16.sendMessage(msg)
                ki17.sendMessage(msg)
                ki18.sendMessage(msg)
                ki19.sendMessage(msg)
                ki20.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki11.sendMessage(msg)
                ki12.sendMessage(msg)
                ki13.sendMessage(msg)
                ki14.sendMessage(msg)
                ki15.sendMessage(msg)
                ki16.sendMessage(msg)
                ki17.sendMessage(msg)
                ki18.sendMessage(msg)
                ki19.sendMessage(msg)
                ki20.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki11.sendMessage(msg)
                ki12.sendMessage(msg)
                ki13.sendMessage(msg)
                ki14.sendMessage(msg)
                ki15.sendMessage(msg)
                ki16.sendMessage(msg)
                ki17.sendMessage(msg)
                ki18.sendMessage(msg)
                ki19.sendMessage(msg)
                ki20.sendMessage(msg)
                ki21.sendMessage(msg)
                ki22.sendMessage(msg)
                ki23.sendMessage(msg)
                ki24.sendMessage(msg)
                ki25.sendMessage(msg)
                ki21.sendMessage(msg)
                ki22.sendMessage(msg)
                ki23.sendMessage(msg)
                ki24.sendMessage(msg)
                ki25.sendMessage(msg)
                ki26.sendMessage(msg)
                ki27.sendMessage(msg)
                ki28.sendMessage(msg)
                ki29.sendMessage(msg)
                ki30.sendMessage(msg)
                ki26.sendMessage(msg)
                ki27.sendMessage(msg)
                ki28.sendMessage(msg)
                ki29.sendMessage(msg)
                ki30.sendMessage(msg)
                ki26.sendMessage(msg)
                ki27.sendMessage(msg)
                ki28.sendMessage(msg)
                ki29.sendMessage(msg)
                ki30.sendMessage(msg)
                ki31.sendMessage(msg)
                ki32.sendMessage(msg)
                ki33.sendMessage(msg)
                ki34.sendMessage(msg)
                ki35.sendMessage(msg)
                ki31.sendMessage(msg)
                ki32.sendMessage(msg)
                ki33.sendMessage(msg)
                ki34.sendMessage(msg)
                ki35.sendMessage(msg)
                ki31.sendMessage(msg)
                ki32.sendMessage(msg)
                ki33.sendMessage(msg)
                ki34.sendMessage(msg)
                ki35.sendMessage(msg)
            elif "Ps2" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
            elif "Ps3" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata ={
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" } 
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
            elif "TL: " in msg.text:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Renama: " in msg.text:
                string = msg.text.replace("Renama: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Change name " + string + "is ready。")
            elif "ชื่อ:" in msg.text:
                string = msg.text.replace("ชื่อ:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"name " + string + " done..❗")
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"name " + string + " done..❗")
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"name " + string + " done..❗")
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"name " + string + " done..❗")
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"name " + string + " done..❗")
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"name " + string + " done..❗")
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"name " + string + " done..❗")
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"name " + string + " done..❗")
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"name " + string + " done..❗")
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"name " + string + " done..❗")
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"name " + string + " done..❗")
#---------------------------------------------------------
            elif "Mic:" in msg.text:
                mmid = msg.text.replace("Mic:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
            elif msg.text in ["Contact on","K on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact on already❗")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
            elif msg.text in ["Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off。")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact off already❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
            elif msg.text in ["Join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join on already❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join on already❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
            elif msg.text in ["Join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off❗")
                    else:
                        cl.sendText(msg.to,"")
            elif msg.text in ["Contact off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
            elif "Invite cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Invite cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"The group of people canceled off.❗")
                        else:
                            cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["leaveRoom"]["on"] = True
                        if wait["lang"] == "JP":
                             cl.sendText(msg.to,"done..❗")
                        else:
                            cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"al ready on。")
                    else:
                        cl.sendText(msg.to,"价值奇怪。")
            elif msg.text in ["Leave on","เเชทรวมปิด"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave on already❗")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
            elif msg.text in ["Leave off","เเชทรวมเปิด"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"leave off already❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done..❗")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif "Set" == msg.text:
                md = ""
                if wait["contact"] == True: md+="✪⌠ Contact on ⌡\n"
                else: md+="✪⌠ Contact off ⌡\n"
                if wait["autoJoin"] == True: md+="✪⌠ Join on ⌡\n"
                else: md +="✪⌠ Join off ⌡\n"
                if wait["autoCancel"]["on"] == True:md+="✪⌠ Invite cancel:" + str(wait["autoCancel"]["members"]) + "⌡\n"
                else: md+= "✪⌠ Invite cancel off ⌡\n"
                if wait["leaveRoom"] == True: md+="✪⌠ Leave on ⌡\n"
                else: md+="✪⌠ Leave off ⌡\n"
                if wait["timeline"] == True: md+="✪⌠ Share on ⌡\n"
                else:md+="✪⌠ Share off ⌡\n"
                if wait["autoAdd"] == True: md+="✪⌠ Add on ⌡\n"
                else:md+="✪⌠ Add off ⌡\n"
                if wait["commentOn"] == True: md+="✪⌠ Comment on ⌡\n"
                else:md+="✪⌠ Comment off ⌡"
                cl.sendText(msg.to,md)
            elif "Me check:" in msg.text:
                gid = msg.text.replace("Me check:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album❗")
                    else:
                        cl.sendText(msg.to,"done❗")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album❗"
                    else:
                        mg = "以下是对象的相册"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0枚\n"
                    cl.sendText(msg.to,mg)
            elif "Check1:" in msg.text:
                gid = msg.text.replace("Check1:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album❗")
                    else:
                        cl.sendText(msg.to,"Done..❗")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album❗"
                    else:
                        mg = "no album❗"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "枚\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "AR:" in msg.text:
                gid = msg.text.replace("AR:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums❗")
                else:
                    cl.sendText(msg.to,str(i) + "Deleted albums❗")
            elif msg.text in ["Pid"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)
            elif msg.text in ["Cancell"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Done..❗")
                else:
                    cl.sendText(msg.to,"All invitations have been refused❗")
                    cl.sendText(msg.to,"คำเชิญทั้งหมดถูกปฏิเสธ..❗")
            elif "Hapus album:" in msg.text:
                gid = msg.text.replace("Hapus album:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted❗")
                else:
                    cl.sendText(msg.to,str(i) + "删除了事的相册。")
            elif msg.text in ["Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on..❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif "Comm:" in msg.text:
                wait["message"] = msg.text.replace("Massage add change:","")
                cl.sendText(msg.to,"The message was changed❗")
            elif "Massage add:" in msg.text:
                wait["message"] = msg.text.replace("Massage add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"done..❗")
                else:
                    cl.sendText(msg.to,"变更了信息。")
            elif msg.text in ["Check add","Com"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"It is Massage auto add:" + wait["message"])
                else:
                    cl.sendText(msg.to,"Bot Phet hack bot\n\n" + wait["message"])
            elif msg.text in ["言語変更","言語變更"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"切換中國語。")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"言語を日本語にしました。")
            elif "Comm1:" in msg.text:
                c = msg.text.replace("Comm1:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"The character string which can't be changed❗")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"I changed it\n\n" + c)
            elif "Add comm:" in msg.text:
                c = msg.text.replace("Add comm:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed❗")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed..\n\n" + c)
            elif msg.text in ["Comment on","Com on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"already on❗")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
            elif msg.text in ["Comment off","Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"already off❗")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done..❗")
                    else:
                        cl.sendText(msg.to,"done..❗")
            elif msg.text in ["Comment","Com Com"]:
                cl.sendText(msg.to,"message changed to\n\n。" + str(wait["comment"]))
            elif msg.text in ["url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group❗")
                    else:
                        cl.sendText(msg.to,"Not for use less than group❗")
            elif "Purl:" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Purl:","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Can not be used outside the group❗")
            
            elif "aurl:" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("aurl:","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif "Gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl得到→","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"以小组以外不能使用")
            elif msg.text in ["Blacklist"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl❗")
            elif msg.text in ["Whitelist"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"White to comment bl❗")
            elif msg.text in ["Cblacklist"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed❗")
                else:
                    cl.sendText(msg.to,"It is a black list")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Clock on","Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on❗")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done..❗")
            elif msg.text in ["Clock off","Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already on❗")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done..❗")
            elif "Name clock:" in msg.text:
                n = msg.text.replace("Name clock:","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"Last name clock❗")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Name clock change done.\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update to refresh❗")
            
            elif "PP: @" in msg.text:
                if msg.toType == 2:
                    print "[NK:]ok"
                    _name = msg.text.replace("PP: @","")
                    _kicktarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Error❗")
#-----------------------------------------------------------
            elif "P: @" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("P: @","")
                    _kicktarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _kicktarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found..❗")
                    else:
                        for target in targets:
                            try:
                                cl.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
           
#-----------------------------------------------------------
            elif "NK:" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("NK:","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found❗")
                    else:
                        for target in targets:
                            try:
                                cl.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
#-----------------------------------------------------------
            elif "BP: @" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("BP: @","")
                    _kicktarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _kicktarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found..❗")
                    else:
                        for target in targets:
                            try:
                                ki.kickoutFromGroup(msg.to,[target])
                                ki2.kickoutFromGroup(msg.to,[target])
                                ki3.kickoutFromGroup(msg.to,[target])
                                ki4.kickoutFromGroup(msg.to,[target])
                                ki5.kickoutFromGroup(msg.to,[target])
                                ki6.kickoutFromGroup(msg.to,[target])
                                ki7.kickoutFromGroup(msg.to,[target])
                                ki8.kickoutFromGroup(msg.to,[target])
                                ki9.kickoutFromGroup(msg.to,[target])
                                ki10.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
           
#-----------------------------------------------------------
            elif "BNK:" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("BNK:","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found❗")
                    else:
                        for target in targets:
                            try:
                                ki.kickoutFromGroup(msg.to,[target])
                                ki2.kickoutFromGroup(msg.to,[target])
                                ki3.kickoutFromGroup(msg.to,[target])
                                ki4.kickoutFromGroup(msg.to,[target])
                                ki5.kickoutFromGroup(msg.to,[target])
                                ki6.kickoutFromGroup(msg.to,[target])
                                ki7.kickoutFromGroup(msg.to,[target])
                                ki8.kickoutFromGroup(msg.to,[target])
                                ki9.kickoutFromGroup(msg.to,[target])
                                ki10.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
#-----------------------------------------------------------
            elif "Kick:" in msg.text:
                _name = msg.text.replace("Kick:","")
                _kicktarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"not found..❗")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"error❗")
#-----------------------------------------------------------
#statusMessage
            elif "#Phet!!" in msg.text:
                if msg.toType == 2:
                    print "[#Phet]ok"
                    _name = msg.text.replace("#Phet!!","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    cl.sendText(msg.to,"􂀁􀄃explosion􏿿 Just some casual cleansing 􂀁􀄃explosion􏿿")
                    for g in gs.members:
                        if _name in g.statusMessage:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.❗")
                    else:
                        for target in targets:
                            try:
                                cl.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"Error❗")
#-----------------------------------------------------------
            elif "Bl: @" in msg.text:
                _name = msg.text.replace("Bl: @","")
                _kicktarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    cl.sendText(msg.to,"Succes...❗")
                                except:
                                    cl.sendText(msg.to,"error❗")
            elif "Wl: @" in msg.text:
                _name = msg.text.replace("Wl: @","")
                _kicktarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"not found❗")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    cl.sendText(msg.to,"Succes...❗")
                                except:
                                    cl.sendText(msg.to,"error❗")                         
#-----------------------------------------------------------
            elif "Midb:" in msg.text:
                midd = msg.text.replace("Midb:","")
                wait["blacklist"][midd] = True
#-----------------------------------------------------------
            elif "Kill1" in msg.text:
                if msg.toType == 2:
                    print "[Kick b]ok"
                    _name = msg.text.replace("Kill1","")
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found❗")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                            except:
                                ki.sendText(msg.to,"Error❗")
#-----------------------------------------------------------
            elif "#終了" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------

#-----------------------------------------------------------
            elif "Bot?" in msg.text:
                ki.sendText(msg.to,"Bot 1🔥")
                ki2.sendText(msg.to,"Bot 2🔥")
                ki3.sendText(msg.to,"Bot 3🔥")
                ki4.sendText(msg.to,"Bot 4🔥")
                ki5.sendText(msg.to,"Bot 5🔥")
                ki6.sendText(msg.to,"Bot 6🔥")
                ki7.sendText(msg.to,"Bot 7🔥")
                ki8.sendText(msg.to,"Bot 8🔥")
                ki9.sendText(msg.to,"Bot 9🔥")
                ki10.sendText(msg.to,"Bot 10🔥")
#-----------------------------------------------------------speed
            elif msg.text in ["Ban on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Phet contact to blacklist...❗")
            elif msg.text in ["Unban on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Phet contact to whitelist...❗")
            elif msg.text in ["Me ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing..❗")
                else:
                    cl.sendText(msg.to,"It is a black list❗")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Me ban1"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "It is banlist❗")
            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["Ban"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"There was no blacklist user❗")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif msg.text in ["ยกเลิก1"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled..")
            elif msg.text in ["ยกเลิก11"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ki.cancelGroupInvitation(msg.to,[_mid])
                        ki2.cancelGroupInvitation(msg.to,[_mid])
                        ki3.cancelGroupInvitation(msg.to,[_mid])
                        ki4.cancelGroupInvitation(msg.to,[_mid])
                        ki5.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled..")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "MM:" in msg.text:
                try:
                    albumtags = msg.text.replace("MM:","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "oh good..😁")
                except:
                    cl.sendText(msg.to,"Error❗")
            elif "MMM:" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("MMM:","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass

#-----------------------------------------------

#-----------------------------------------------
            elif msg.text in ["#kicker","!มาบอท!","*+*","คิง10"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki4.sendText(msg.to,"hello")
                        ki5.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "[By.🐯हईທຮຮๅજईह🐯]")
                        ki6.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "[By.BF``บั้ม.BOT]")
                        ki7.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "[By.Gυ Tєʌм HʌcκBoт]")
                        ki8.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "[By.เพชรทีมทดลองบอท]")
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)

            elif "@1" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki.sendText(msg.to,"Hello...")
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)

            elif "@2" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki2.sendText(msg.to,"Hello..")
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)                                 

            elif "@3" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki3.sendText(msg.to,"Hello..")
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)                                 

            elif "@4" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki4.sendText(msg.to,"Hello..")
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)                                 

            elif "@5" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki5.sendText(msg.to,"Hello..")
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)                                 
#-----------------------------------------------
            elif "#PHET" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["#bye","Bye","#ออก"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    ki4.sendText(msg.to,"bye")
                    ki5.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "[Good bye]")
                    ki6.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "[Good bye]")
                    ki7.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "[Good bye]")
                    ki8.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "[Good bye]")
                    print "kicker ok"
                    try:
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    ki.sendText(msg.to,"Bye~Bye")
                    print "kicker ok"
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    ki2.sendText(msg.to,"Bye~Bye")
                    print "kicker ok"
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    ki3.sendText(msg.to,"Bye~Bye")
                    print "kicker ok"
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
#            elif "#Test" in msg.text:
                ki.sendText(msg.to,"Test..🔥")
                ki2.sendText(msg.to,"Test..🔥")
                ki3.sendText(msg.to,"Test..🔥")
                ki4.sendText(msg.to,"Test..🔥")
                ki5.sendText(msg.to,"Test..🔥")
                ki6.sendText(msg.to,"Test..🔥")
                ki7.sendText(msg.to,"Test..🔥")
                ki8.sendText(msg.to,"Test..🔥")
                ki9.sendText(msg.to,"Test..🔥")
                ki10.sendText(msg.to,"Test..🔥")
                ki11.sendText(msg.to,"Test..🔥")
                ki12.sendText(msg.to,"Test..🔥")
                ki13.sendText(msg.to,"Test..🔥")
                ki14.sendText(msg.to,"Test..🔥")
                ki15.sendText(msg.to,"Test..🔥")
                ki16.sendText(msg.to,"Test..🔥")
                ki17.sendText(msg.to,"Test..🔥")
                ki18.sendText(msg.to,"Test..🔥")
                ki19.sendText(msg.to,"Test..🔥")
                ki20.sendText(msg.to,"Test..🔥")
                ki21.sendText(msg.to,"Test..🔥")
                ki22.sendText(msg.to,"Test..🔥")
                ki23.sendText(msg.to,"Test..🔥")
                ki24.sendText(msg.to,"Test..🔥")
                ki25.sendText(msg.to,"Test..🔥")
                ki26.sendText(msg.to,"Test..🔥")
                ki27.sendText(msg.to,"Test..🔥")
                ki28.sendText(msg.to,"Test..🔥")
                ki29.sendText(msg.to,"Test..🔥")
                ki30.sendText(msg.to,"Test..🔥")
                ki31.sendText(msg.to,"Test..🔥")
                ki32.sendText(msg.to,"Test..🔥")
                ki33.sendText(msg.to,"Test..🔥")
                ki34.sendText(msg.to,"Test..🔥")
                ki35.sendText(msg.to,"OK..Phet....🔥")

#-----------------------------------------------
            elif "Hi bot" in msg.text:
                ki.sendText(msg.to,"Hi Phet 😁")
                ki.sendText(msg.to,"Hi Gu  😁")
                ki.sendText(msg.to,"Hi Phet 😁")
                ki.sendText(msg.to,"Hi Gu  😁")
                ki.sendText(msg.to,"Hi Phet 😁")
                ki2.sendText(msg.to,"Hi Gu  😁")
                ki2.sendText(msg.to,"Hi Phet 😁")
                ki2.sendText(msg.to,"Hi Gu  😁")
                ki2.sendText(msg.to,"Hi Phet 😁")
                ki2.sendText(msg.to,"Hi Gu  😁")
                ki3.sendText(msg.to,"Hi Phet 😁")
                ki3.sendText(msg.to,"Hi Gu  😁")
                ki3.sendText(msg.to,"Hi Phet 😁")
                ki3.sendText(msg.to,"Hi Gu  😁")
                ki4.sendText(msg.to,"Hi Phet 😁")
                ki4.sendText(msg.to,"Hi Gu  😁")
                ki4.sendText(msg.to,"Hi Phet 😁")
                ki4.sendText(msg.to,"Hi Gu  😁")
                ki4.sendText(msg.to,"Hi Phet 😁")
                ki5.sendText(msg.to,"Hi Gu  😁")
                ki5.sendText(msg.to,"Hi Phet 😁")
                ki5.sendText(msg.to,"Hi Gu  😁")
                ki5.sendText(msg.to,"Hi Phet 😁")
                ki5.sendText(msg.to,"Hi Gu  😁")
                ki6.sendText(msg.to,"Hi Gu  😁")
                ki6.sendText(msg.to,"Hi Phet 😁")
                ki6.sendText(msg.to,"Hi Gu  😁")
                ki6.sendText(msg.to,"Hi Phet 😁")
                ki6.sendText(msg.to,"Hi Gu  😁")
                ki7.sendText(msg.to,"Hi Gu  😁")
                ki7.sendText(msg.to,"Hi Phet 😁")
                ki7.sendText(msg.to,"Hi Gu  😁")
                ki7.sendText(msg.to,"Hi Phet 😁")
                ki7.sendText(msg.to,"Hi Gu  😁")
                ki8.sendText(msg.to,"Hi Gu  😁")
                ki8.sendText(msg.to,"Hi Phet 😁")
                ki8.sendText(msg.to,"Hi Gu  😁")
                ki8.sendText(msg.to,"Hi Phet 😁")
                ki8.sendText(msg.to,"Hi Phet  😁")
                ki9.sendText(msg.to,"Hi Gu  😁")
                ki9.sendText(msg.to,"Hi Gu 😁")
                ki9.sendText(msg.to,"Hi Gu  😁")
                ki9.sendText(msg.to,"Hi Gu 😁")
                ki9.sendText(msg.to,"Hi Gu  😁")
                ki10.sendText(msg.to,"Hi Phet  😁")
                ki10.sendText(msg.to,"Hi Phet 😁")
                ki10.sendText(msg.to,"Hi Phet  😁")
                ki10.sendText(msg.to,"Hi Phet ")
                ki10.sendText(msg.to,"Hi Phet  😁")
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","sp"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...\n")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))
                ki.sendText(msg.to, "%s second" % (elapsed_time))
                ki2.sendText(msg.to, "%s second" % (elapsed_time))
                ki3.sendText(msg.to, "%s second" % (elapsed_time))
                ki4.sendText(msg.to, "%s second" % (elapsed_time))
                ki5.sendText(msg.to, "%s second" % (elapsed_time))
                ki6.sendText(msg.to, "%s second" % (elapsed_time))
                ki7.sendText(msg.to, "%s second" % (elapsed_time))
                ki8.sendText(msg.to, "%s second" % (elapsed_time))
                ki9.sendText(msg.to, "%s second" % (elapsed_time))
                ki10.sendText(msg.to, "%s second" % (elapsed_time))
#-------------------------------------------------------------------蹴り返し
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False

                       
                        
                elif op.param3 in ki2mid:
                    if op.param2 in kimid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)


                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
            except:
                pass
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
#----------------------------------------
            if msg.text in["@Me"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, jml = [], [], [], len(nama)
                if jml <= 100:
                   mention(msg.to, nama)
                if jml > 100 and jml < 200:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, len(nama)-1):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2)
                if jml > 200  and jml < 300:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, 199):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2)
                   for k in range(200, len(nama)-1):
                       nm3 += [nama[k]]
                   mention(msg.to, nm3)
                if jml > 300:
                    print "Waow,,300+ Member"
                cnt = Message()
                cnt.text = "Done:"+str(jml)
                cont.to = msg.to
                cl.sendMessage(cnt)
            elif msg.text in ["Me@"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error

#-------------------------------
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
