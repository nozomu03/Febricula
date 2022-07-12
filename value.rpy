image text1 = ParameterizedText(xalign=0.5, yalign=0.47)
image text2 = ParameterizedText(xalign=0.5, yalign=0.53)
init python:    
    def ShowImage(start=1, end=11):
        global path
        for i in range(start, end):     
            renpy.transition(dissolve)      
            renpy.show("fall_" + str(i))
            renpy.pause(1.0)
        return
    
    def SoundPlayer(fn="", t=2.0, ch="sound"):
        renpy.music.play("/audio/"+ fn, channel=ch)
        renpy.pause(t)
        renpy.music.stop(channel='sound')
        return

    def FaceChange(img="", loc=0 ,t=2.0, org_img=None):
        if loc == 0:
            renpy.show(img, [left])
        elif loc == 1:
            renpy.show(img, [center])
        elif loc == 2:
            renpy.show(img, [right])
        else:
            renpy.show(img, [Position(xalign=loc, yalign=1.0)])
        renpy.transition(Dissolve(t))
        if org_img != None:
            renpy.hide(org_img)
        renpy.pause(t, hard=True)

    def Smoking(img="main", loc=0, rep = 1, first=False):
        count = 0
        if first == True:
            renpy.sound.play("/audio/lighter.ogg")
            renpy.pause(4.0)
            if img + "_lighter" in renpy.get_showing_tags():
                print("문제 발생")
                FaceChange(img + "_taba", loc, 2.0, img + "_lighter")
            else:
                FaceChange(img + "_taba", loc, 2.0, img + "_taba_nof")
            first = False
        while count < rep:
            FaceChange(img + "_taba", loc, 1.0, img + "_tabahand")
            renpy.sound.play("/audio/smoke.ogg")
            FaceChange(img + "_tabahand", loc, 1.0, img + "_taba")
            renpy.pause(2.0)
            count += 1

    class Message:
        def __init__(self, type=0, who="N/A", message = "awa\ngawg"):
            self.type = type
            self.who = who
            self.message = message

    def ImgDisplay(name = "clock", s_in = 0, e_in = 10):
        for i in range(s_in, e_in):
            renpy.show(str(name) + "_" + str(i))
            renpy.pause(.1)
            renpy.hide(str(name) + "_" + str(i))
        renpy.show(str(name) + "_" + str(e_in))
        renpy.music.stop(channel='looping', fadeout=1.0)
        renpy.with_statement(Dissolve(1.0), always=False)
        return

#image 1 = "/fall_anim/1.png"
    renpy.music.register_channel(name = "second", mixer = None, loop = False)
    renpy.music.register_channel(name = "looping", mixer = None, loop = True)

    message_list = []
define narr = Character("목소리", who_color = "#B9E2FA", what_color="#DCFFDC")
define nvlnarr = Character(None, kind=nvl, what_color="#000000")
define chunyul = Character("천율", who_color = "#FAE1AF", what_color = "#FFBB8C")
define ginsetsu = Character("은설", who_color="#C39873", what_color="#b4b4b4")
define yeon = Character("연호", who_color = "#AAFA82", what_color = "#008080")
define eye_open = ImageDissolve("gun_barrel.jpg", 5.0, 8)
define eye_close = ImageDissolve("gun_barrel2.jpg", 5.0, 8)

define left = Position(xalign=.1, yalign=1.0)
define center = Position(xalign=.5, yalign=1.0)
define right = Position(xalign=.9, yalign = 1.0)

screen phone_screen:
    modal True
    add "phone_back.png"
    if message_list != []:
        default y = 180
        default counter = 0
        for i in message_list:        
          #  vbox:
         #   #    hbox:
                   # text "[y]"
            #$print(y)
            $temp_text = Text(i.message)
            if i.type == 0:
                if counter == 0 or past_i.type == 1:
                    fixed:  
                        text "{color=#000000}{size=20}[i.who]{/size}":
                            pos(490, y-13)
                        add "msg_back.png":                                        
                            pos(490, y)                                      
                            size(temp_text.size()[0], temp_text.size()[1] - 5)
                        text "{color=#000000}{size=25}[i.message]":
                            pos(490, y)
                else:
                    $y -= 5
                    fixed:                      
                        add "msg_back.png":                                        
                            pos(490, y)                                      
                            size(temp_text.size()[0], temp_text.size()[1] - 5)
                        text "{color=#000000}{size=25}[i.message]":
                            pos(490, y)            
                if temp_text.size()[1] >= 54:                
                    $y += int(temp_text.size()[1] - 27)
                $counter += 1 
            else:
                $x=790
                $x-=int(temp_text.size()[0])
                #text "{color=#FF0000}"+str(int(x)):
                #    xalign .8
                #    ypos y
                $y -= 5
                #790
                fixed:                      
                    add "msg_back.png":                                        
                        pos(x, y)                                      
                        size(temp_text.size()[0], temp_text.size()[1] - 5)
                    text "{color=#000000}{size=25}[i.message]":
                        pos(x, y)            
                if temp_text.size()[1] >= 54:                
                    $y += int(temp_text.size()[1] - 27)           # else:
            $y += 40
            $past_i = i            
        #$go_messagebox +  
    button action [Return()]#, SetVariable("go_messagebox", go_messagebox + message_list)]
    $message_list = []
        #$time.sleep(2)
