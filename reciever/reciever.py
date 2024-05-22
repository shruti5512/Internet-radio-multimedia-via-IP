# # # import socket
# # # import sys
# # # import os
# # # import threading
# # # import struct
# # # import time
# # # import PySimpleGUI as sg

# # # MC_PORT = 5433
# # # BUF_SIZE = 64000
# # # done = threading.Event()
# # # done.set()  # Initially allow data fetching

# # # def thread_function(mcast_addr, window):
# # #     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # #     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# # #     s.bind(('', MC_PORT))

# # #     group = socket.inet_aton(mcast_addr)
# # #     mreq = struct.pack('4sL', group, socket.INADDR_ANY)
# # #     s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# # #     file = window['file'].get()

# # #     sg.vprint('Playing file:', file)
# # #     player = sg.Video(file)
# # #     player.play()

# # #     # try:
# # #     #     os.remove("live_data.mp4")
# # #     # except PermissionError as e:
# # #     #     print(f"Error: {e}. File is in use.")
# # #     # except FileNotFoundError:
# # #     #     print("File not found. Creating a new file.")

# # #     # with open("live_data.mp4", "wb") as fp:
# # #     while True:
# # #             if not done.is_set():
# # #                 time.sleep(1)  # Sleep if paused
# # #                 continue
# # #             data, addr = s.recvfrom(BUF_SIZE)
# # #             if not data:
# # #                 break
# # #             file.write(data)
# # #             # Update GUI about data fetch
# # #             window.write_event_value('-THREAD-', 'Data Received')

# # #     s.close()

# # # def main():
# # #     if len(sys.argv) != 2:
# # #         print("Usage: python receiver.py <multicast_address>")
# # #         sys.exit(1)

# # #     mcast_addr = sys.argv[1]

# # #     layout = [
# # #         [sg.Text("Control Panel")],
# # #         [sg.Button("Pause", key='-PAUSE-'), sg.Button("Resume", key='-RESUME-')],
# # #         [sg.Button("Change Station", key='-CHANGE-'), sg.Button("Terminate", key='-TERMINATE-')],
# # #         [sg.Text(size=(40, 1), key='-OUTPUT-')]
# # #     ]

# # #     window = sg.Window("Television App", layout, finalize=True)

# # #     threading.Thread(target=thread_function, args=(mcast_addr, window), daemon=True).start()

# # #     while True:
# # #         event, values = window.read()
# # #         if event == sg.WINDOW_CLOSED or event == '-TERMINATE-':
# # #             done.clear()  # Stop the thread
# # #             if os.path.exists("live_data.mp4"):
# # #                 try:
# # #                     os.remove("live_data.mp4")
# # #                 except PermissionError:
# # #                     print("Failed to delete live_data.mp4: file is in use.")
# # #             break
# # #         elif event == '-PAUSE-':
# # #             done.clear()  # Signal the thread to pause
# # #             window['-OUTPUT-'].update('Video paused...')
# # #         elif event == '-RESUME-':
# # #             done.set()  # Signal the thread to resume
# # #             window['-OUTPUT-'].update('Video resumed...')
# # #         elif event == '-CHANGE-':
# # #             done.clear()  # Stop the thread to change station
# # #             os.system("taskkill /IM ffplay.exe /F")  # Adjusted for Windows compatibility
# # #             if os.path.exists("live_data.mp4"):
# # #                 os.remove("live_data.mp4")
# # #             window['-OUTPUT-'].update('Changing station...')

# # #     window.close()

# # # if __name__ == "__main__":
# # #     main()
# # import socket
# # import sys
# # import os
# # import threading
# # import struct
# # import time
# # import PySimpleGUI as sg
# # import logging

# # MC_PORT = 5433
# # BUF_SIZE = 64000
# # done = threading.Event()
# # done.set()  # Initially allow data fetching

# # def thread_function(mcast_addr, window):
# #     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# #     s.bind(('', MC_PORT))

# #     group = socket.inet_aton(mcast_addr)
# #     mreq = struct.pack('4sL', group, socket.INADDR_ANY)
# #     s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# #     file_path = "live_data.mp4"

# #     try:
# #         if os.path.exists(file_path):
# #             os.remove(file_path)
# #         logging.info(f"Removed existing file: {file_path}")
# #     except PermissionError as e:
# #         logging.error(f"Error removing file {file_path}: {e}")
# #         return

# #     with open(file_path, "wb") as fp:
# #         while True:
# #             if not done.is_set():
# #                 time.sleep(1)
# #                 continue
# #             data, addr = s.recvfrom(BUF_SIZE)
# #             if not data:
# #                 break
# #             fp.write(data)
# #             window.write_event_value('-THREAD-', 'Data Received')

# #     s.close()

# # def main():
# #     logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# #     if len(sys.argv) != 2:
# #         print("Usage: python receiver.py <multicast_address>")
# #         sys.exit(1)

# #     mcast_addr = sys.argv[1]

# #     layout = [
# #         [sg.Text("Control Panel")],
# #         [sg.Button("Pause", key='-PAUSE-'), sg.Button("Resume", key='-RESUME-')],
# #         [sg.Button("Change Station", key='-CHANGE-'), sg.Button("Terminate", key='-TERMINATE-')],
# #         [sg.Text(size=(40, 1), key='-OUTPUT-')]
# #     ]

# #     window = sg.Window("Television App", layout, finalize=True)

# #     threading.Thread(target=thread_function, args=(mcast_addr, window), daemon=True).start()

# #     while True:
# #         event, values = window.read()
# #         if event == sg.WINDOW_CLOSED or event == '-TERMINATE-':
# #             done.clear()
# #             break
# #         elif event == '-PAUSE-':
# #             done.clear()
# #             window['-OUTPUT-'].update('Video paused...')
# #         elif event == '-RESUME-':
# #             done.set()
# #             window['-OUTPUT-'].update('Video resumed...')
# #         elif event == '-CHANGE-':
# #             done.clear()
# #             # Add any logic needed to handle station changing
# #             window['-OUTPUT-'].update('Changing station...')

# #     window.close()

# # if __name__ == "__main__":
# #     main()

# import socket
# import sys
# import os
# import threading
# import struct
# import time
# import PySimpleGUI as sg
# import logging

# MC_PORT = 5433
# BUF_SIZE = 64000
# done = threading.Event()
# done.set()  # Initially allow data fetching

# def thread_function(mcast_addr, window):
#     logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     s.bind(('', MC_PORT))
#     group = socket.inet_aton(mcast_addr)
#     mreq = struct.pack('4sL', group, socket.INADDR_ANY)
#     s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

#     file_path = "live_data.mp4"
#     try:
#         os.remove(file_path)
#         logging.info("File removed successfully.")
#     except FileNotFoundError:
#         logging.warning("File not found, creating a new file.")
#     except PermissionError as e:
#         logging.error(f"Error removing file: {e}")

#     with open(file_path, "wb") as fp:
#         while True:
#             if not done.is_set():
#                 time.sleep(1)
#                 continue
#             data, addr = s.recvfrom(BUF_SIZE)
#             if not data:
#                 break
#             fp.write(data)
#             window.write_event_value('-THREAD-', 'Data Received')
    
#     s.close()

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: python receiver.py <multicast_address>")
#         sys.exit(1)

#     mcast_addr = sys.argv[1]
#     layout = [
#         [sg.Text("Control Panel")],
#         [sg.Button("Pause", key='-PAUSE-'), sg.Button("Resume", key='-RESUME-')],
#         [sg.Button("Change Station", key='-CHANGE-'), sg.Button("Terminate", key='-TERMINATE-')],
#         [sg.Text(size=(40, 1), key='-OUTPUT-')]
#     ]

#     window = sg.Window("Television App", layout, finalize=True)
#     threading.Thread(target=thread_function, args=(mcast_addr, window), daemon=True).start()

#     while True:
#         event, values = window.read()
#         if event == sg.WINDOW_CLOSED or event == '-TERMINATE-':
#             done.clear()
#             break
#         elif event == '-PAUSE-':
#             done.clear()
#             window['-OUTPUT-'].update('Video paused...')
#         elif event == '-RESUME-':
#             done.set()
#             window['-OUTPUT-'].update('Video resumed...')
#         elif event == '-CHANGE-':
#             done.clear()
#             window['-OUTPUT-'].update('Changing station...')

#     window.close()

# if __name__ == "__main__":
#     main()
import os
import vlc
import PySimpleGUI as sg

def create_window():
    sg.theme('DarkBlue3')

    layout = [
        [sg.Text('Station Video Player', size=(20, 1), justification='center')],
        [sg.Button('Play video 1', key='-PLAY1-'), sg.Button('Play video 2', key='-PLAY2-')],
        [sg.Button('Play video 3', key='-PLAY3-'), sg.Button('Play video 4', key='-PLAY4-')],
        [sg.Button('Pause'), sg.Button('Resume'), sg.Button('Stop')],
        [sg.Text(size=(40, 1), key='-OUTPUT-')]
    ]

    return sg.Window('Station Video Player', layout, finalize=True)

def main():
    window = create_window()
    player = vlc.MediaPlayer()
    import os

    file_path = r'C:\\Users\\pshru\\OneDrive\\Desktop\\ECE 671\\sender\\videos\\vid1.mp4'
    print("Does the file exist?", os.path.exists(file_path))


    video_files = {
        '-PLAY1-': 'vid1.mp4',
        '-PLAY2-': 'vid3.mp4',
        '-PLAY3-': 'vid7.mp4',
        '-PLAY4-': 'vid8.mp4'
    }

    while True:
        event, values = window.read(timeout=100)

        if event == sg.WIN_CLOSED:
            break
        elif event in ['-PLAY1-', '-PLAY2-','-PLAY3-','-PLAY4-']:
            if player.is_playing():
                player.stop()
            video_path = video_files[event]
            player.set_media(vlc.Media(video_path))
            player.play()
            window['-OUTPUT-'].update(f'Playing: {os.path.basename(video_path)}')
        elif event == 'Pause':
            player.pause()
            window['-OUTPUT-'].update('Video paused')
        elif event == 'Resume':
            player.play()
            window['-OUTPUT-'].update('Video resumed')
        elif event == 'Stop':
            player.stop()
            window['-OUTPUT-'].update('Video stopped')

    player.stop()
    window.close()

if __name__ == '__main__':
    main()
