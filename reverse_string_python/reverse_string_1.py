# calculating fibonacci sequence depending on count of strings in file
def fibonacci(count_of_strings):
    seq = [0, 1]
    if count_of_strings == 0:
        return 0
    elif count_of_strings == 1:
        return 1
    else:
        # recording max values of sequence
        for i in range(2, count_of_strings):
            # calculating will stop when number in sequence will be higher then count of strings
            if seq[i - 1] <= count_of_strings:
                seq.append(seq[i - 1] + seq[i - 2])
            else:
                return seq


def reading_file(counter, storage):
    for line in open('source.txt', 'r'):
        # reverse string
        storage[counter] = line[::-1]
        counter += 1
    return counter, storage


def writing_to_file(storage, sequence):
    file_to_write = open('output.txt', 'w')
    for line in storage:
        if line in sequence:  #  Saving right line
            file_to_write.write(storage.get(line))
    print('Stored to file "output.txt"')
    file_to_write.close()


if __name__ == "__main__":
    lines = {}  # storage for raws in file
    counter_base = 1  # future number of strings
    counter_base, lines = reading_file(counter_base, lines)  # multireturning in python
    writing_to_file(lines, fibonacci(counter_base))
