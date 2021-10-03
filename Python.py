# Python3 program to demonstrate

# SCAN Disk Scheduling algorithm

size = 8

disk_size = 200

 

def SCAN(arr, head, direction):

 

    seek_count = 0

    distance, cur_track = 0, 0

    left = []

    right = []

    seek_sequence = []

 

    # Appending end values

    # which has to be visited

    # before reversing the direction

    if (direction == "left"):

        left.append(0)

    elif (direction == "right"):

        right.append(disk_size - 1)

 

    for i in range(size):

        if (arr
