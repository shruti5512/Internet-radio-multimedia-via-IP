import socket
import sys
import os
import time

MC_PORT = 5432
BUF_SIZE = 64000

def main():
    if len(sys.argv) != 2:
        print("usage: python sender.py multicast_address")
        sys.exit(1)

    mcast_addr = sys.argv[1]

    # TCP socket setup
    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_tcp.bind(('', MC_PORT))
    s_tcp.listen(5)

    print("TCP Socket created and bound\n")

    # Accept TCP connection
    tcp_ac, addr = s_tcp.accept()
    print("TCP Connection accepted from:", addr, "\n")

    # Receive station number from TCP connection
    num = tcp_ac.recv(1024).decode()
    print("Station number is:", num, "\n")

    # UDP socket setup
    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sin = (mcast_addr, MC_PORT)

    # Open video file
    filenames = ["vid1.mp4", "vid2.mp4", "vid3.mp4"]

    for filename in filenames:
        print("Current Stream:", filename, "\n")
        next_stream = filenames[(filenames.index(filename) + 1) % len(filenames)]
        print("Next Stream:", next_stream, "\n")

        try:
            with open(filename, 'rb') as fp:
                fsize = os.path.getsize(filename)
                tot_frame = fsize // BUF_SIZE + 1 if fsize % BUF_SIZE != 0 else fsize // BUF_SIZE
                print("Total number of packets are:", tot_frame, "\n")
                print("Sending frames...\n")

                # Send total frame count
                s_udp.sendto(tot_frame.to_bytes(4, byteorder='big'), sin)

                # Send frames
                for i in range(tot_frame):
                    string = fp.read(BUF_SIZE)
                    s_udp.sendto(string, sin)
                    print("Sent frame", i+1)
                    time.sleep(0.01)  # Simulate delay for video stream
        except FileNotFoundError:
            s_udp.sendto(b"File Not Found\n", sin)

    s_udp.close()
    s_tcp.close()

if __name__ == "__main__":
    main()

