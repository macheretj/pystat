import os
import logging
import threading
import time

measures_commands = ["iostat -xt 1 2", "mpstat 1 2", "vmstat 1 2"]


def mkdir(dirs):

    for dir in dirs:
        if not os.path.isdir(dir):
            try:
                os.makedirs(dir)
            except OSError:
                print ("Creation of the directory %s failed" % dir)
            else:
                print ("Successfully created the directory %s " % dir)


def thread_function(command):
    logging.info("Thread %s: starting", command)
    os.system(command)
    logging.info("Thread %s: finishing", command)



def startCapture(snap_number,snap_duration):


    message_format = "%(asctime)s: %(message)s"
    print("Format: {}".format(message_format))
    logging.basicConfig(format=message_format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(measures_commands[0],))
    y = threading.Thread(target=thread_function, args=(measures_commands[1],))
    z = threading.Thread(target=thread_function, args=(measures_commands[2],))


    logging.info("Main    : before running thread")
    x.start()
    y.start()
    z.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")


def main():
    base_temp_data_dir = "/tmp/perfcollector/"
    temp_data_dirs = [ base_temp_data_dir+"iostat", base_temp_data_dir+"mpstat", base_temp_data_dir+"vmstat"]

    mkdir(temp_data_dirs)

    startCapture(1,1)

main()