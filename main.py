from scripts.menu import Menu
from scripts.logger import Log

logger = Log()
def run():
    try:
        app = Menu()
        logger.add_info("Application running... @8-main.py")
        app.run()
    except Exception as e:
        logger.add_error(e)
        print("An error occurred" + e)

if __name__ == '__main__':
    run()