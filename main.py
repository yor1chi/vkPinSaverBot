from Menu import Menu
import os

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    menu = Menu()
    menu.Menu()


