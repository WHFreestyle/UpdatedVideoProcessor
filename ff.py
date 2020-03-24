import os
import subprocess
import time
import random
#from moviepy.editor import VideoFileClip
import time

mytext = open("mytext.txt","w")
mytext.close()

num_of_cuts = int(input("How many cuts: "))
len = int(input("Lenght(S): "))

f_list = os.listdir("VideoClips")
print(f_list)


def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)


mytext = open("mytext.txt","r+")

for list in f_list:
    mytext.write("file" + " 'VideoClips/" + list + "'" + "\n")

mytext.close()

subprocess.call('ffmpeg -f concat -safe 0 -i mytext.txt -c copy -an output.mp4', shell=True)
lenght = get_length('output.mp4')
print(lenght)

video_Cut_time = lenght/num_of_cuts
mytext = open("mytext.txt","w")
mytext.close()

for x in range(num_of_cuts):
    new_len = random.uniform(len-0.5,len+0.5)
    time = random.uniform(0, int(video_Cut_time) - new_len)
    subprocess.call('ffmpeg -ss {} -i output.mp4 -c copy -t {} cutVids/output{}.mp4'.format(x * video_Cut_time + time,new_len, str(x) + "smile"), shell=True)


t_list = os.listdir("cutVids")

mytext = open("mytext.txt","r+")
for list in t_list:
    mytext.write("file" + " 'cutVids/" + list + "'" + "\n")
mytext.close()
subprocess.call('ffmpeg -f concat -safe 0 -i mytext.txt -c copy -an outputfinal.mp4', shell=True)


subprocess.call('ffmpeg -i outputfinal.mp4 -i moth.mp3 -codec copy -shortest outputfinalfinal.mp4')

os.remove('output.mp4')
os.remove('outputfinal.mp4')
import os, shutil
folder = 'cutVids'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

