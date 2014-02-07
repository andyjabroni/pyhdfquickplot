from lib.mod_main import MainUI

# Import Qt modules
from PyQt4 import QtGui

from sys import exit, argv

def main():    
    # Load browser window and show it:
    app = QtGui.QApplication(argv)
    window = MainUI()
    window.show()
    
    # It's exec_ because exec is a reserved word in Python
    exit(app.exec_())


if __name__ == "__main__":
    main()
