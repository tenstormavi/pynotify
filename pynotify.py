import pyinotify
import glob

count = 0
wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_CREATE  # watched events
mask2 = pyinotify.IN_MOVED_TO

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname
        #print "Event: %s" % event
        global wdd2
        if wdd2:
            #print "wdd2: %s" % wdd2
            wm.rm_watch(wdd2.values())
            wdd2 = wm.add_watch(glob.glob('/tmp/*/TODO'), mask2)
            #print "wdd2: %s" % wdd2
            

    def process_IN_MOVED_TO(self, event):
        print "Moved to:", event.pathname
	# run your script


notifier = pyinotify.ThreadedNotifier(wm, EventHandler())
notifier.start()

wdd = wm.add_watch('/tmp', mask)
#print "wdd: %s" % wdd

wdd2 = wm.add_watch(glob.glob('/tmp/*/TODO'), mask2)
#print "wdd2: %s" % wdd2
