#
# Automaticly approving RDWorks dialogs when uploading a file to the laser cut machine.
# arad.rgb@gmail.com 02/05/2021
#
import time
import winsound
import pywinauto


__import__('warnings').simplefilter('ignore') # don't print 32/64bit application warning


def main(rdworks_path='RDWorks', is_debug=False):
    app = pywinauto.Application(backend='win32')
    app.process = 1 # hack so next line won't rais AppNotConnected
    dialog = app.window(title_re='^(Name document|Prompt|RDWorks)$')

    while True:
        try:
            if not app.is_process_running():
                app.connect(path=rdworks_path, timeout=10, retry_interval=5)
                [winsound.Beep(i, 100) for i in range(2000, 5000, 1000)]
            dialog.wait('enabled', timeout=1, retry_interval=2)
            text = dialog.static.window_text()
            if text == 'File download success!':
                winsound.Beep(3000, 1200)
            elif text not in ('Document', 'Duplicate file!Cover the old one?'):
                text = ''
            if text:
                dialog.send_keystrokes('{ENTER}')
            else:
                time.sleep(1)
        except Exception:
            if is_debug:
                raise


if __name__ == '__main__':
    main(*__import__('sys').argv[1:])
