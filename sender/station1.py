# import socket
# import sys
# import os
# import time

# MC_PORT = 5433
# BUF_SIZE = 64000

# def main():
#     if len(sys.argv) != 2:
#         print("usage: python sender.py multicast_address")
#         sys.exit(1)

#     mcast_addr = sys.argv[1]

#     # Create socket
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#     # Build address data structure
#     sin = (mcast_addr, MC_PORT)

#     print("Connected in first station\n\n")

#     video_dir = os.path.join('/home/mininet/ECE 671/sender', 'videos')
#     video_files = ["vid2.mp4", "vid4.mp4", "vid1.mp4", "vid3.mp4"]
#     videos = [os.path.join(video_dir, vid) for vid in video_files]

#     while True:
#         for vid in videos:
#             fp = open(vid, 'rb')

#             if not fp:
#                 print("File not found")
#             else:
#                 fsize = os.path.getsize(vid)
#                 tot_frame = fsize // BUF_SIZE + 1 if fsize % BUF_SIZE != 0 else fsize // BUF_SIZE

#                 print("Total number of packets are:", tot_frame)
#                 print("Sending frames...\n")

#                 for i in range(tot_frame):
#                     string = fp.read(BUF_SIZE)
#                     s.sendto(string, sin)
#                     print("Sent frame", i + 1)
#                     time.sleep(0.4)  # Simulate delay for video stream

#                 fp.close()

#     s.close()

# if __name__ == "__main__":
#     main()
import socket
import sys
import os
import time
from moviepy import editor
from moviepy.editor import concatenate_videoclips, VideoFileClip

MC_PORT = 5433
BUF_SIZE = 64000

def concatenate_videos(video_files, output_path):
    clips = [VideoFileClip(video) for video in video_files]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path, codec='libx264')
    print(f"Concatenated video saved to {output_path}")
    return output_path

def main():
    if len(sys.argv) != 2:
        print("usage: python sender.py multicast_address")
        sys.exit(1)

    mcast_addr = sys.argv[1]

    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Build address data structure
    sin = (mcast_addr, MC_PORT)

    print("Connected in first station\n\n")

    video_dir = os.path.join('/home/mininet/ECE 671/sender', 'videos')
    video_files = ["vid2.mp4", "vid4.mp4", "vid1.mp4", "vid3.mp4"]
    videos = [os.path.join(video_dir, vid) for vid in video_files]

    # Concatenate videos into a single file
    output_path = os.path.join(video_dir, "concatenated_video.mp4")
    concatenated_video_path = concatenate_videos(videos, output_path)

    # Open the concatenated video file
    with open(concatenated_video_path, 'rb') as fp:
        fsize = os.path.getsize(concatenated_video_path)
        tot_frame = fsize // BUF_SIZE + 1 if fsize % BUF_SIZE != 0 else fsize // BUF_SIZE

        print("Total number of packets are:", tot_frame)
        print("Sending frames...\n")

        for i in range(tot_frame):
            string = fp.read(BUF_SIZE)
            s.sendto(string, sin)
            print("Sent frame", i + 1)
            time.sleep(0.4)  # Simulate delay for video stream

    s.close()

if __name__ == "__main__":
    main()

