# # import socket
# # import sys
# # import subprocess
# # import PySimpleGUI as sg

# # MC_PORT = 5432
# # BUF_SIZE = 64000

# # def main():
# #     sg.theme('Dark Blue 3')  # Add some color to the window

# #     # Define the window's contents
# #     layout = [
# #         [sg.Text("Welcome to Television!")],
# #         [sg.Button("TAYLOR SWIFT", key='-TAYLOR-'), sg.Button("ARIANA GRANDE", key='-ARIANA-')],
# #         [sg.Text(size=(40, 1), key='-OUTPUT-')],
# #         [sg.Button('Exit')]
# #     ]

# #     # Create the window
# #     window = sg.Window('PLAY APP', layout)

# #     host = "localhost"
# #     s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #     sin_t = (host, MC_PORT)
    
# #     try:
# #         s_tcp.connect(sin_t)
# #     except Exception as e:
# #         sg.Popup("TCP connection failed:", e)
# #         sys.exit(1)

# #     print("Client connected in TCP.")
# #     if s_tcp.sendall(b"Start\n") is None:
# #         print("\nStart sent successfully.")
# #     else:
# #         print("\nClient not ready to receive.")

# #     # Display and interact with the Window
# #     while True:
# #         event, values = window.read()
# #         if event == sg.WINDOW_CLOSED or event == 'Exit':
# #             break
# #         elif event == '-TAYLOR-':
# #             display = "Connected to Station 1!"
# #             window['-OUTPUT-'].update(display)
# #             mcast_addr = "239.192.4.2"
# #             subprocess.Popen(["python", "reciever.py", mcast_addr])  # Make sure receiver.py is configured correctly
# #         elif event == '-ARIANA-':
# #             display = "Connected to Station 2!"
# #             window['-OUTPUT-'].update(display)
# #             mcast_addr = "239.192.4.1"
# #             subprocess.Popen(["python", "receiver.py", mcast_addr])  # Make sure receiver.py is configured correctly

# #     # Finish up by removing from the screen
# #     window.close()
# #     s_tcp.close()

# # if __name__ == "__main__":
# #     main()

# import socket
# import struct
# import os
# import threading
# import time
# import sys
# import PySimpleGUI as sg
# import subprocess

# MC_PORT = 5433
# BUF_SIZE = 64000
# done = threading.Event()
# done.set()  # Initially allow data fetching

# def thread_function(mcast_addr, window):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     s.bind(('', MC_PORT))

#     group = socket.inet_aton(mcast_addr)
#     mreq = struct.pack('4sL', group, socket.INADDR_ANY)
#     s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

#     file_path = "live_data.mp4"
#     if os.path.exists(file_path):
#         try:
#             os.remove(file_path)
#             print("File removed successfully.")
#         except PermissionError as e:
#             print(f"Error removing file {file_path}: {e}")
#     else:
#         print("No file to remove, proceeding with file creation.")

#     with open(file_path, "wb") as fp:
#         while True:
#             if not done.is_set():
#                 time.sleep(1)  # Sleep if paused
#                 continue
#             data, addr = s.recvfrom(BUF_SIZE)
#             if not data:
#                 break
#             fp.write(data)
#             window.write_event_value('-THREAD-', 'Data Received')

#     s.close()

# def play_video(file_path):
#     # Check if the file exists and has content
#     if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
#         try:
#             subprocess.Popen(['vlc', file_path])
#         except FileNotFoundError:
#             print("VLC is not installed or not found in system PATH")
#     else:
#         print("Video file does not exist or is empty.")

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: python receiver.py <multicast_address>")
#         sys.exit(1)

#     mcast_addr = sys.argv[1]

#     layout = [
#         [sg.Text("Control Panel")],
#         [sg.Button("Play Video", key='-PLAY-')],
#         [sg.Button("Pause", key='-PAUSE-'), sg.Button("Resume", key='-RESUME-')],
#         [sg.Button("Change Station", key='-CHANGE-'), sg.Button("Terminate", key='-TERMINATE-')],
#         [sg.Text(size=(40, 1), key='-OUTPUT-')]
#     ]

#     window = sg.Window("Television App", layout, finalize=True)
#     threading.Thread(target=thread_function, args=(mcast_addr, window), daemon=True).start()

#     player = None
#     while True:
#         event, values = window.read()
#         if event == sg.WINDOW_CLOSED or event == '-TERMINATE-':
#             done.clear()
#             break
#         elif event == '-PLAY-':
#             play_video('live_data.mp4')
#         elif event == '-PAUSE-' and player:
#             player.pause()
#             window['-OUTPUT-'].update('Video paused...')
#         elif event == '-RESUME-' and player:
#             player.unpause()
#             window['-OUTPUT-'].update('Video resumed...')
#         elif event == '-CHANGE-':
#             done.clear()
#             if player:
#                 player.stop()
#             # logic to change station or video source

#     window.close()

# if __name__ == "__main__":
#     main()

# # import socket
# # import sys
# # import subprocess
# # import PySimpleGUI as sg
# # import struct

# # def receive_station_info(s_tcp):
# #     """Receive station information from the server."""
# #     try:
# #         # Expecting two stations' information
# #         data = s_tcp.recv(1024)  # Adjust buffer size as needed
# #         # Unpack data received from the server (modify as per server's sending structure)
# #         station1_info = struct.unpack('50s 15s', data[:65])
# #         station2_info = struct.unpack('50s 15s', data[65:])
# #         return station1_info, station2_info
# #     except struct.error as e:
# #         print("Failed to unpack received data:", e)
# #         return None



# # def main():
# #     sg.theme('Dark Blue 3')  # Add some color to the window

# #     # Define the window's contents
# #     layout = [
# #         [sg.Text("Welcome to Television!")],
# #         [sg.Button("Station 1", key='-STATION1-'), sg.Button("Station 2", key='-STATION2-')],
# #         [sg.Text(size=(40, 1), key='-OUTPUT-')],
# #         [sg.Button('Exit')]
# #     ]

# #     # Create the window
# #     window = sg.Window('PLAY APP', layout)

# #     # Setup TCP Connection
# #     host = "localhost"
# #     MC_PORT = 5432
# #     s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #     sin_t = (host, MC_PORT)

# #     try:
# #         s_tcp.connect(sin_t)
# #     except Exception as e:
# #         sg.Popup("TCP connection failed:", e)
# #         sys.exit(1)

# #     print("Client connected in TCP.")
# #     # Send start signal to receive station info
# #     if s_tcp.sendall(b"Start\n") is None:
# #         print("\nStart sent successfully.")
# #         station1_info, station2_info = receive_station_info(s_tcp)
# #         if not station1_info or not station2_info:
# #             sg.Popup("Failed to receive station information.")
# #             sys.exit(1)
# #     else:
# #         print("\nClient not ready to receive.")

# #     # Display and interact with the Window
# #     while True:
# #         event, values = window.read()
# #         if event == sg.WINDOW_CLOSED or event == 'Exit':
# #             break
# #         elif event == '-STATION1-':
# #             display = f"Connected to {station1_info[0].decode().strip()}!"
# #             window['-OUTPUT-'].update(display)
# #             subprocess.Popen(["python", "reciever.py", station1_info[1].decode().strip()])
# #         elif event == '-STATION2-':
# #             display = f"Connected to {station2_info[0].decode().strip()}!"
# #             window['-OUTPUT-'].update(display)
# #             subprocess.Popen(["python", "reciever.py", station2_info[1].decode().strip()])

# #     # Finish up by removing from the screen
# #     window.close()
# #     s_tcp.close()

# # if __name__ == "__main__":
# #     main()

# import socket
# import sys
# import struct
# import subprocess
# import PySimpleGUI as sg

# MC_PORT = 5432
# BUF_SIZE = 64000

# class SiteInfo:
#     def __init__(self, site_name, site_desc):
#         self.site_name = site_name
#         self.site_desc = site_desc

# class StationInfo:
#     def __init__(self, station_number, multicast_address, data_port, info_port, bit_rate, station_name):
#         self.station_number = station_number
#         self.multicast_address = multicast_address
#         self.data_port = data_port
#         self.info_port = info_port
#         self.bit_rate = bit_rate
#         self.station_name = station_name



# def receive_site_info(s):
#     try:
#         site_infos = []
#         for _ in range(2):  # Assuming there are 2 sites to receive
#             data = s.recv(struct.calcsize('!I20sI100s'))
#             site_name_size, site_name, site_desc_size, site_desc = struct.unpack('!I20sI100s', data)
#             site_infos.append(SiteInfo(site_name[:site_name_size].decode().strip('\x00'), site_desc[:site_desc_size].decode().strip('\x00')))
#         return site_infos
#     except Exception as e:
#         sg.Popup("Error receiving site info:", e)
#         sys.exit(1)

# def receive_station_info(s):
#     try:
#         station_infos = []
#         for _ in range(2):  # Assuming there are 2 stations to receive
#             data = s.recv(struct.calcsize('!I32sHHI50s'))
#             station_number, multicast_address, data_port, info_port, bit_rate, station_name = struct.unpack('!I32sHHI50s', data)
#             station_infos.append(StationInfo(station_number, multicast_address[:15].decode().strip('\x00'), data_port, info_port, bit_rate, station_name[:50].decode().strip('\x00')))
#         return station_infos
#     except Exception as e:
#         sg.Popup("Error receiving station info:", e)
#         sys.exit(1)

# def send_acknowledgment(s_tcp):
#     try:
#         # Example ACK message
#         ack_message = b'ACK\n'
#         s_tcp.sendall(ack_message)
#         print("Acknowledgment sent successfully.")
#     except socket.error as e:
#         print(f"Failed to send acknowledgment: {e}")

# # Assuming s_tcp is your connected TCP socket
#     data = s_tcp.recv(1024)  # Receive data from the server
#     if data:
#         print("Data received from the server:", data)
#         send_acknowledgment(s_tcp)

# def main():
#     sg.theme('Dark Blue 3')  # Add some color to the window

#     # Define the window's contents
#     layout = [
#         [sg.Text("Welcome to Television!")],
#         [sg.Button("TAYLOR SWIFT", key='-TAYLOR-'), sg.Button("ARIANA GRANDE", key='-ARIANA-')],
#         [sg.Text(size=(40, 1), key='-OUTPUT-')],
#         [sg.Button('Exit')]
#     ]

#     # Create the window
#     window = sg.Window('PLAY APP', layout)

#     host = "localhost"
#     s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sin_t = (host, MC_PORT)
    
#     try:
#         s_tcp.connect(sin_t)
#     except Exception as e:
#         sg.Popup("TCP connection failed:", e)
#         sys.exit(1)

#     print("Client connected in TCP.")
#     if s_tcp.sendall(b"Start\n") is None:
#         print("\nStart sent successfully.")
#     else:
#         print("\nClient not ready to receive.")

#     # Receive site info
#     sites = receive_site_info(s_tcp)
#     for site in sites:
#         print(f"Site Name: {site.site_name}, Site Description: {site.site_desc}")

#     # Receive station info
#     stations = receive_station_info(s_tcp)
#     for station in stations:
#         print(f"Station Name: {station.station_name}, Multicast Address: {station.multicast_address}")

#     acknowledgment = send_acknowledgment(s_tcp)
#     for acknowledge in acknowledgment:
#         print(f"Acknowledgement Sent:{acknowledge.acknowledge_name}")

#     # Display and interact with the Window
#     while True:
#         event, values = window.read()
#         if event == sg.WINDOW_CLOSED or event == 'Exit':
#             break
#         elif event == '-TAYLOR-':
#             display = "Connected to Station 1!"
#             window['-OUTPUT-'].update(display)
#             mcast_addr = "239.192.4.2"
#             subprocess.Popen(["python", "reciever.py", mcast_addr])  # Make sure receiver.py is configured correctly
#         elif event == '-ARIANA-':
#             display = "Connected to Station 2!"
#             window['-OUTPUT-'].update(display)
#             mcast_addr = "239.192.4.1"
#             subprocess.Popen(["python", "reciever.py", mcast_addr])  # Make sure receiver.py is configured correctly

#     # Finish up by removing from the screen
#     window.close()
#     s_tcp.close()

# if __name__ == "__main__":
#     main()
import socket
import sys
import struct
import subprocess
import PySimpleGUI as sg

MC_PORT = 5432
BUF_SIZE = 64000

class SiteInfo:
    def __init__(self, site_name, site_desc):
        self.site_name = site_name
        self.site_desc = site_desc

class StationInfo:
    def __init__(self, station_number, multicast_address, data_port, info_port, bit_rate, station_name):
        self.station_number = station_number
        self.multicast_address = multicast_address
        self.data_port = data_port
        self.info_port = info_port
        self.bit_rate = bit_rate
        self.station_name = station_name

def receive_site_info(s):
    site_infos = []
    try:
        for _ in range(2):  # Assume two sites
            data = s.recv(struct.calcsize('!I20sI100s'))
            site_name_size, site_name, site_desc_size, site_desc = struct.unpack('!I20sI100s', data)
            site_infos.append(SiteInfo(site_name[:site_name_size].decode().strip('\x00'), site_desc[:site_desc_size].decode().strip('\x00')))
    except Exception as e:
        sg.Popup("Error receiving site info:", e)
        sys.exit(1)
    return site_infos

def receive_station_info(s):
    station_infos = []
    try:
        for _ in range(2):  # Assume two stations
            data = s.recv(struct.calcsize('!I32sHHI50s'))
            station_number, multicast_address, data_port, info_port, bit_rate, station_name = struct.unpack('!I32sHHI50s', data)
            station_infos.append(StationInfo(station_number, multicast_address.decode().strip('\x00'), data_port, info_port, bit_rate, station_name.decode().strip('\x00')))
    except Exception as e:
        sg.Popup("Error receiving station info:", e)
        sys.exit(1)
    return station_infos

def send_acknowledgment(s):
    try:
        ack_message = b'ACK\n'
        s.sendall(ack_message)
        print("Acknowledgment sent successfully.")
    except Exception as e:
        print(f"Failed to send acknowledgment: {e}")

def receive_video_file(socket, save_path):
    """Function to receive video file from server and save it."""
    try:
        with open(save_path, 'wb') as f:
            while True:
                bytes_read = socket.recv(1024)
                if not bytes_read:
                    # nothing is received
                    # file transmitting is done
                    break
                f.write(bytes_read)
        print("Received video file saved to", save_path)
    except Exception as e:
        print(f"Failed to receive video file: {e}")

# Example usage
# Assuming 'client_socket' is your connected socket and 'server_address' is your server IP and port


def main():
    sg.theme('Dark Blue 3')

    layout = [
        [sg.Text("Welcome to Television!")],
        [sg.Button("TAYLOR SWIFT", key='-TAYLOR-'), sg.Button("ARIANA GRANDE", key='-ARIANA-')],
        [sg.Text(size=(40, 1), key='-OUTPUT-')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('PLAY APP', layout)
    host = "localhost"
    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s_tcp.connect((host, MC_PORT))
        print("Client connected in TCP.")
        s_tcp.sendall(b"Start\n")
        print("Start command sent successfully.")
    except Exception as e:
        sg.Popup("TCP connection failed:", e)
        sys.exit(1)

    sites = receive_site_info(s_tcp)
    stations = receive_station_info(s_tcp)

    send_acknowledgment(s_tcp)  # Send acknowledgment after receiving data

 # Requesting the server to send the Taylor video


    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        elif event == '-TAYLOR-':
            display = "Connected to Station 1: TAYLOR SWIFT"
            window['-OUTPUT-'].update(display)
            subprocess.Popen(["python", "reciever.py", "239.192.4.2"])
        elif event == '-ARIANA-':
            display = "Connected to Station 2: ARIANA GRANDE"
            window['-OUTPUT-'].update(display)
            subprocess.Popen(["python", "reciever.py", "239.192.4.1"])

    window.close()
    s_tcp.close()

if __name__ == "__main__":
    main()
