#!/usr/bin/python3
from __future__ import absolute_import, print_function
#print("A")
import sys
#print("B")
import _thread
#print("C")
import gi
#print("D")
gi.require_version('Gtk', '3.0')
#print("E")
from gi.repository import Gtk, GLib, GdkPixbuf, Gdk
#print("F")
import subprocess as s
#print("G")
name = ""
class EntryWindow(Gtk.Window):

    def __init__(self,param):
        Gtk.Window.__init__(self, title="InstaTweet",name="default")

        self.set_keep_above(True) 
        self.shift=False
        screen = self.get_screen()
        self.set_decorated(False)
        self.set_size_request(screen.get_width(), 0)
        self.move(0,screen.get_height()-10)
        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.add(vbox)


        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
        filename="/home/eduardi/Proyectos/003-TwitterAppLinux-Python/.iconcache", 
        width=24, 
        height=24, 
        preserve_aspect_ratio=True)

        self.image = Gtk.Image.new_from_pixbuf(pixbuf)
        vbox.pack_start(self.image,False,True,6)

        self.label = Gtk.Label(name)
        self.label.set_markup("<span style=\"EmojiOne Color\">"+name+"</span>"+"")
        vbox.pack_start(self.label, False, True, 10)




        # self.len = Gtk.Label("0")
        # self.len.set_markup("<b>("+"0"+")</b>"+"")
        # self.len.set_justify(Gtk.Justification.LEFT)


        # vbox.pack_start(self.len, False, False, 10)

        self.entry = Gtk.Entry()
        self.entry.set_text("")

        if len(param)>=1:
            if param[0]=="-h":
                self.entry.set_visibility(False)
        self.entry.connect("key-release-event", self.postFromUi)
        self.entry.connect("key-press-event", self.shiftpress)
        # Gtk_signal_connect (GTK_OBJECT(self.entry), "activate",
        #               GTK_SIGNAL_FUNC(self.on_editable_toggled),
        #               NULL);
        vbox.pack_end(self.entry, True, True, 10)


    # def loadapi(self):
    #     global apiready
    #     global api
    #     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #     auth.set_access_token(access_token, access_token_secret)

    #     api = tweepy.API(auth)
    #     apiready = True
    #     self.label.set_markup("<b>"+getname()+"</b>"+"")


    def shiftpress(self, widget, ev, data=None):        
        if ev.keyval == Gdk.KEY_Shift_L or ev.keyval == Gdk.KEY_Control_L: #If Escape pressed, reset text
            self.shift=True


    def postFromUi(self, widget, ev, data=None):
        #self.len.set_markup("<b>("+str(len(self.entry.get_text()))+")</b>"+"")
        if ev.keyval == Gdk.KEY_Shift_L or ev.keyval == Gdk.KEY_Control_L:
            self.shift=False
            return
        if ev.keyval == Gdk.KEY_Escape: #If Escape pressed, reset text
            Gtk.main_quit()
        if ev.keyval == Gdk.KEY_KP_Enter: #If Escape pressed, reset text
            if self.shift == True:
                self.entry.set_text(self.entry.get_text()+"\n")
                self.entry.set_position(len(self.entry.get_text()))
            else:
                text = self.entry.get_text()
                #postTweet(text)
                s.call(['./Tweet.py','-t',text])
                Gtk.main_quit()
name = sys.argv[2]
win = EntryWindow(sys.argv[1:])

#_thread.start_new_thread( win.loadapi ,())
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()



# if existe carpeta cache
#   cargar from cache y auth on thread
# else:
#   cargar default
#   descargar y crear cache en thread aparte
