# # # import socket
# # # import sys
# # # import struct

# # # SERVER_PORT = 5432
# # # MAX_PENDING = 5
# # # MAX_LINE = 512000

# # # # Structure of site info
# # # class SiteInfo:
# # #     def __init__(self, site_name, site_desc):
# # #         self.site_name = site_name
# # #         self.site_desc = site_desc
# # #         self.site_name_size = len(site_name)
# # #         self.site_desc_size = len(site_desc)

# # # # Structure of station info
# # # class StationInfo:
# # #     def __init__(self, station_number, multicast_address, data_port, info_port, bit_rate, station_name):
# # #         self.station_number = station_number
# # #         self.multicast_address = multicast_address
# # #         self.data_port = data_port
# # #         self.info_port = info_port
# # #         self.bit_rate = bit_rate
# # #         self.station_name = station_name

# # # def main():
# # #     # Build address data structure
# # #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # #     s.bind(('localhost', SERVER_PORT))
# # #     s.listen(MAX_PENDING)

# # #     print(f"Server is using address 'localhost' and port {SERVER_PORT}.")
# # #     print("Waiting for client connections...")

# # #     try:
# # #         while True:
# # #             # Accept a new connection
# # #             new_s, addr = s.accept()
# # #             print(f"Accepted connection from {addr}.")

# # #             # Assuming the client sends "Start" to trigger info transmission
# # #             start_signal = new_s.recv(5)
# # #             if start_signal.decode() != "Start":
# # #                 print("Expected start signal not received.")
# # #                 continue

# # #             # Declaration of site info for stations
# # #             site1 = SiteInfo("www.taylor.com", "TAYLOR SWIFT")
# # #             site2 = SiteInfo("www.ariana.com", "ARIANA GRANDE")

# # #             # Declaration of station info for stations
# # #             stat1 = StationInfo(1, "239.192.4.2", 5433, 5432, 1087, "TAYLOR SWIFT")
# # #             stat2 = StationInfo(2, "239.192.4.1", 5433, 5432, 891, "ARIANA GRANDE")

# # #             # Sending structure of site info
# # #             new_s.send(struct.pack('!I20sI100s', site1.site_name_size, site1.site_name.encode(), site1.site_desc_size, site1.site_desc.encode()))
# # #             new_s.send(struct.pack('!I20sI100s', site2.site_name_size, site2.site_name.encode(), site2.site_desc_size, site2.site_desc.encode()))

# # #             # Sending structure of station info
# # #             new_s.send(struct.pack('!I32sHHII50s', stat1.station_number, stat1.multicast_address.encode(), stat1.data_port, stat1.info_port, stat1.bit_rate, stat1.station_name.encode()))
# # #             new_s.send(struct.pack('!I32sHHII50s', stat2.station_number, stat2.multicast_address.encode(), stat2.data_port, stat2.info_port, stat2.bit_rate, stat2.station_name.encode()))

# # #             # Close client socket after sending data
# # #             new_s.close()
    
# # #     except KeyboardInterrupt:
# # #         print("Server is shutting down.")
# # #         s.close()
# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")
# # #         s.close()

# # # if __name__ == "__main__":
# # #     main()

# # import socket
# # import sys
# # import struct

# # SERVER_PORT = 5432
# # MAX_PENDING = 5
# # MAX_LINE = 512000

# # # Structure of site info
# # class SiteInfo:
# #     def __init__(self, site_name, site_desc):
# #         self.site_name = site_name
# #         self.site_desc = site_desc
# #         self.site_name_size = len(site_name)
# #         self.site_desc_size = len(site_desc)

# # # Structure of station info
# # class StationInfo:
# #     def __init__(self, station_number, multicast_address, data_port, info_port, bit_rate, station_name):
# #         self.station_number = station_number
# #         self.multicast_address = multicast_address
# #         self.data_port = data_port
# #         self.info_port = info_port
# #         self.bit_rate = bit_rate
# #         self.station_name = station_name

# # def main():
# #     # Build address data structure
# #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #     s.bind(('localhost', SERVER_PORT))
# #     s.listen(MAX_PENDING)

# #     print(f"Server is using address 'localhost' and port {SERVER_PORT}.")
# #     print("Waiting for client connections...")

# #     try:
# #         while True:
# #             # Accept a new connection
# #             new_s, addr = s.accept()
# #             print(f"Accepted connection from {addr}.")

# #             # Assuming the client sends "Start" to trigger info transmission
# #             start_signal = new_s.recv(5)
# #             if start_signal.decode() != "Start":
# #                 print("Expected start signal not received.")
# #                 new_s.close()
# #                 continue

# #             # Declaration of site info for stations
# #             site1 = SiteInfo("www.taylor.com", "TAYLOR SWIFT")
# #             site2 = SiteInfo("www.ariana.com", "ARIANA GRANDE")

# #             # Declaration of station info for stations
# #             stat1 = StationInfo(1, "239.192.4.2", 5433, 5432, 1087, "TAYLOR SWIFT")
# #             stat2 = StationInfo(2, "239.192.4.1", 5433, 5432, 891, "ARIANA GRANDE")

# #             # Sending structure of site info
# #             new_s.send(struct.pack('!I20sI100s', site1.site_name_size, site1.site_name.encode(), site1.site_desc_size, site1.site_desc.encode()))
# #             new_s.send(struct.pack('!I20sI100s', site2.site_name_size, site2.site_name.encode(), site2.site_desc_size, site2.site_desc.encode()))

# #             # Sending structure of station info
# #             new_s.send(struct.pack('!I32sHHI50s', stat1.station_number, stat1.multicast_address.encode(), stat1.data_port, stat1.info_port, stat1.bit_rate, stat1.station_name.encode()))
# #             new_s.send(struct.pack('!I32sHHI50s', stat2.station_number, stat2.multicast_address.encode(), stat2.data_port, stat2.info_port, stat2.bit_rate, stat2.station_name.encode()))

# #             # Close client socket after sending data
# #             new_s.close()
    
# #     except KeyboardInterrupt:
# #         print("Server is shutting down.")
# #         s.close()
# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         s.close()

# # if __name__ == "__main__":
# #     main()

# import socket
# import sys
# import struct
# import logging

# # Setup logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# SERVER_PORT = 5432
# MAX_PENDING = 5

# class SiteInfo:
#     def __init__(self, site_name, site_desc):
#         self.site_name = site_name
#         self.site_desc = site_desc
#         self.site_name_size = len(site_name.encode('utf-8'))
#         self.site_desc_size = len(site_desc.encode('utf-8'))

# class StationInfo:
#     def __init__(self, station_number, multicast_address, data_port, info_port, bit_rate, station_name):
#         self.station_number = station_number
#         self.multicast_address = multicast_address
#         self.data_port = data_port
#         self.info_port = info_port
#         self.bit_rate = bit_rate
#         self.station_name = station_name

# def send_station_info(client_socket, stations):
#     for station in stations:
#         # Pack and send each station's info
#         packed_data = struct.pack('!I32sHHI50s',
#                                   station.station_number,
#                                   station.multicast_address.encode(),
#                                   station.data_port,
#                                   station.info_port,
#                                   station.bit_rate,
#                                   station.station_name.encode())
#         client_socket.sendall(packed_data)
#         logging.info(f"Sent data for {station.station_name}")

# def main():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind(('localhost', SERVER_PORT))
#         s.listen(MAX_PENDING)
#         logging.info(f"Server is running on localhost and port {SERVER_PORT}")

#         try:
#             while True:
#                 client_socket, addr = s.accept()
#                 with client_socket:
#                     logging.info(f"Accepted connection from {addr}")
#                     start_signal = client_socket.recv(5)
                    
#                     if start_signal.decode().strip() != "Start":
#                         logging.warning("Expected start signal not received.")
#                         continue

#                     # Define the stations
#                     stations = [
#                         StationInfo(1, "239.192.4.2", 5433, 5432, 1087, "TAYLOR SWIFT"),
#                         StationInfo(2, "239.192.4.1", 5433, 5432, 891, "ARIANA GRANDE")
#                     ]
                    
#                     # Send station info to the client
#                     send_station_info(client_socket, stations)
        
#         except KeyboardInterrupt:
#             logging.info("Server shutdown requested.")
#         except Exception as e:
#             logging.error(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()

# import socket
# import struct
# import logging
# import sys

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# SERVER_PORT = 5432
# MAX_PENDING = 5

# class SiteInfo:
#     def __init__(self, site_name, site_desc):
#         self.site_name = site_name
#         self.site_desc = site_desc
#         self.site_name_size = len(site_name.encode('utf-8'))
#         self.site_desc_size = len(site_desc.encode('utf-8'))

# class StationInfo:
#     def __init__(self, station_number, multicast_address, data_port, info_port, bit_rate, station_name):
#         self.station_number = station_number
#         self.multicast_address = multicast_address
#         self.data_port = data_port
#         self.info_port = info_port
#         self.bit_rate = bit_rate
#         self.station_name = station_name

# def send_station_info(client_socket, stations):
#     try:
#         for station in stations:
#             # Pack and send each station's info
#             packed_data = struct.pack('!I32sHHI50s',
#                                       station.station_number,
#                                       station.multicast_address.encode(),
#                                       station.data_port,
#                                       station.info_port,
#                                       station.bit_rate,
#                                       station.station_name.encode())
#             client_socket.sendall(packed_data)
#             logging.info(f"Sent data for {station.station_name}")
#         # Optionally wait for client's acknowledgment
#         ack = client_socket.recv(1024).decode().strip()
#         if ack == "ACK":
#             logging.info("Client acknowledged receipt of all data.")
#         else:
#             logging.warning("No acknowledgment from client.")
#     except Exception as e:
#         logging.error(f"Error sending data: {e}")

# def main():
#     if len(sys.argv) > 1:
#         host = sys.argv[1]
#     else:
#         host = 'localhost'

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((host, SERVER_PORT))
#         s.listen(MAX_PENDING)
#         logging.info(f"Server is running on {host} and port {SERVER_PORT}")

#         while True:
#             try:
#                 client_socket, addr = s.accept()
#                 with client_socket:
#                     logging.info(f"Accepted connection from {addr}")
#                     start_signal = client_socket.recv(5)
                    
#                     if start_signal.decode().strip() != "Start":
#                         logging.warning("Expected start signal not received.")
#                         continue

#                     # Define the stations
#                     stations = [
#                         StationInfo(1, "239.192.4.2", 5433, 5432, 1087, "TAYLOR SWIFT"),
#                         StationInfo(2, "239.192.4.1", 5433, 5432, 891, "ARIANA GRANDE")
#                     ]
                    
#                     # Send station info to the client
#                     send_station_info(client_socket, stations)

#             except Exception as e:
#                 logging.error(f"An error occurred with {addr}: {e}")

#         logging.info("Server shutdown requested.")

# if __name__ == "__main__":
#     main()


# import socket
# import struct
# import logging
# import threading

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# SERVER_PORT = 5432
# MAX_PENDING = 5

# class SiteInfo:
#     def __init__(self, site_name, site_desc):
#         self.site_name = site_name
#         self.site_desc = site_desc
#         self.site_name_size = len(site_name.encode('utf-8'))
#         self.site_desc_size = len(site_desc.encode('utf-8'))

# class StationInfo:
#     def __init__(self, station_number, multicast_address, data_port, info_port, bit_rate, station_name):
#         self.station_number = station_number
#         self.multicast_address = multicast_address
#         self.data_port = data_port
#         self.info_port = info_port
#         self.bit_rate = bit_rate
#         self.station_name = station_name



# def send_site_info(client_socket, sites):
#     try:
#         for site in sites:
#             # Pack and send each site's info
#             packed_data = struct.pack('!I20sI100s',
#                                       site.site_name_size,
#                                       site.site_name.encode(),
#                                       site.site_desc_size,
#                                       site.site_desc.encode())
#             client_socket.sendall(packed_data)
#             logging.info(f"Sent site info for {site.site_name}")
        
#     except Exception as e:
#         logging.error(f"Error sending site info: {e}")
#         raise
# def send_video_file(client_socket, file_path):
#     try:
#         with open(file_path, 'rb') as video_file:
#             while True:
#                 bytes_read = video_file.read(1024)  # Read the file in chunks
#                 if not bytes_read:
#                     break  # File transmission is done
#                 client_socket.sendall(bytes_read)
#         logging.info("Video file sent successfully.")
#     except Exception as e:
#         logging.error(f"Error sending video file: {e}")

# # This function could be called after sending station info,
# # if the client sends a request indicating they've selected a specific station.


# def send_station_info(client_socket, stations):
#     try:
#         for station in stations:
#             # Pack and send each station's info
#             packed_data = struct.pack('!I32sHHI50s',
#                                       station.station_number,
#                                       station.multicast_address.encode(),
#                                       station.data_port,
#                                       station.info_port,
#                                       station.bit_rate,
#                                       station.station_name.encode())
#             client_socket.sendall(packed_data)
#             logging.info(f"Sent station info for {station.station_name}")
        
#         # Optionally wait for client's acknowledgment
#         ack = client_socket.recv(1024).decode().strip()
#         if ack == "ACK":
#             logging.info("Client acknowledged receipt of all data.")
#         else:
#             logging.warning("No acknowledgment from client.")
#     except Exception as e:
#         logging.error(f"Error sending station info: {e}")
#         raise

# def handle_client(client_socket, addr):
#     try:
#         logging.info(f"Accepted connection from {addr}")
#         start_signal = client_socket.recv(5)
        
#         if start_signal.decode().strip() != "Start":
#             logging.warning("Expected start signal not received.")
#             return

#         # Define the sites and stations
#         sites = [
#             SiteInfo("www.taylor.com", "TAYLOR SWIFT"),
#             SiteInfo("www.ariana.com", "ARIANA GRANDE")
#         ]

#         stations = [
#             StationInfo(1, "239.192.4.2", 5433, 5432, 1087, "TAYLOR SWIFT"),
#             StationInfo(2, "239.192.4.1", 5433, 5432, 891, "ARIANA GRANDE")
#         ]
        
#         # Send site info to the client
#         send_site_info(client_socket, sites)
        
#         # Send station info to the client
#         send_station_info(client_socket, stations)
#     except Exception as e:
#         logging.error(f"An error occurred with {addr}: {e}")

# def start_tcp_server():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind(('', SERVER_PORT))
#         s.listen(MAX_PENDING)
#         logging.info(f"Server is running on port {SERVER_PORT}")

#         while True:
#             client_socket, addr = s.accept()
#             client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
#             client_thread.start()

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#     start_tcp_server()


import socket
import struct
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SERVER_PORT = 5432
MAX_PENDING = 5

class SiteInfo:
    def __init__(self, site_name, site_desc):
        self.site_name = site_name
        self.site_desc = site_desc
        self.site_name_size = len(site_name.encode('utf-8'))
        self.site_desc_size = len(site_desc.encode('utf-8'))

class StationInfo:
    def __init__(self, station_number, multicast_address, data_port, info_port, bit_rate, station_name):
        self.station_number = station_number
        self.multicast_address = multicast_address
        self.data_port = data_port
        self.info_port = info_port
        self.bit_rate = bit_rate
        self.station_name = station_name

def send_site_info(client_socket, sites):
    try:
        for site in sites:
            packed_data = struct.pack('!I20sI100s',
                                      site.site_name_size,
                                      site.site_name.encode(),
                                      site.site_desc_size,
                                      site.site_desc.encode())
            client_socket.sendall(packed_data)
            logging.info(f"Sent site info for {site.site_name}")
    except Exception as e:
        logging.error(f"Error sending site info: {e}")

def send_station_info(client_socket, stations):
    try:
        for station in stations:
            packed_data = struct.pack('!I32sHHI50s',
                                      station.station_number,
                                      station.multicast_address.encode(),
                                      station.data_port,
                                      station.info_port,
                                      station.bit_rate,
                                      station.station_name.encode())
            client_socket.sendall(packed_data)
            logging.info(f"Sent station info for {station.station_name}")

        ack = client_socket.recv(1024).decode().strip()
        if ack == "ACK":
            logging.info("Client acknowledged receipt of all data.")
        else:
            logging.warning("No acknowledgment from client.")
    except Exception as e:
        logging.error(f"Error sending station info: {e}")

def send_video_file(client_socket, file_path):
    try:
        with open(file_path, 'rb') as video_file:
            while True:
                bytes_read = video_file.read(1024)  # Read the file in chunks
                if not bytes_read:
                    break  # File transmission is done
                client_socket.sendall(bytes_read)
        logging.info("Video file sent successfully.")
    except Exception as e:
        logging.error(f"Error sending video file: {e}")

def handle_client(client_socket, addr):
    logging.info(f"Accepted connection from {addr}")
    try:
        start_signal = client_socket.recv(5).decode().strip()
        if start_signal != "Start":
            logging.warning("Expected start signal not received.")
            return

        sites = [SiteInfo("www.taylor.com", "TAYLOR SWIFT"), SiteInfo("www.ariana.com", "ARIANA GRANDE")]
        send_site_info(client_socket, sites)

        stations = [
            StationInfo(1, "239.192.4.2", 5433, 5432, 1087, "TAYLOR SWIFT"),
            StationInfo(2, "239.192.4.1", 5433, 5432, 891, "ARIANA GRANDE")
        ]
        send_station_info(client_socket, stations)

        # Wait for a request to send a video file
        video_request = client_socket.recv(1024).decode().strip()
        if video_request == "SEND_TAYLOR":
            send_video_file(client_socket, "taylor_swift_video.mp4")
        elif video_request == "SEND_ARIANA":
            send_video_file(client_socket, "ariana_grande_video.mp4")

    except Exception as e:
        logging.error(f"An error occurred with {addr}: {e}")
    finally:
        client_socket.close()

def start_tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', SERVER_PORT))
        s.listen(MAX_PENDING)
        logging.info(f"Server is running on port {SERVER_PORT}")

        while True:
            client_socket, addr = s.accept()
            threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    start_tcp_server()
