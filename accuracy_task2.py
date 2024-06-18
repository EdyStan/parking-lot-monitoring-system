import os

dir1 = '/home/edstan/Desktop/master_AI/sem2/computer_vision/project2/output_train/Task2'
dir2 = '/home/edstan/Desktop/master_AI/sem2/computer_vision/project2/train/Task2/ground-truth'
files1 = sorted(os.listdir(dir1))
files2 = sorted(os.listdir(dir2))

i = 0
j = 0
for file1 in files1:
    if not file1.endswith('.txt'):
        continue
    file2 = files2[i]
    i += 1

    with open(os.path.join(dir1, file1), 'r') as f1, open(os.path.join(dir2, file2), 'r') as f2:
        a = f1.read()
        b = f2.read()
        if a == b:
            j += 1
        # print('new')
        # print(a)
        # print(b)

    # if i == 6:
    #     break
# Replace 'dir1' and 'dir2' with your actual directory paths
print(j/i)