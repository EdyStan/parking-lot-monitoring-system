from task_solutions import task1, task2, task3
import os


SHOW_DETAILS = True
PROJECT_PATH = '/home/edstan/Desktop/master_AI/sem2/computer_vision/project2'

TASK1_PATH = os.path.join(PROJECT_PATH, 'train/Task1')
TASK1_OUTPUT_PATH = os.path.join(PROJECT_PATH, 'output_train/Task1')

TASK2_PATH = os.path.join(PROJECT_PATH, 'train/Task2')
TASK2_OUTPUT_PATH = os.path.join(PROJECT_PATH, 'output_train/Task2')

TASK3_PATH = os.path.join(PROJECT_PATH, 'train/Task3')
TASK3_OUTPUT_PATH = os.path.join(PROJECT_PATH, 'output_train/Task3')


if not os.path.exists(TASK1_OUTPUT_PATH):
    os.makedirs(TASK1_OUTPUT_PATH)

if not os.path.exists(TASK2_OUTPUT_PATH):
    os.makedirs(TASK2_OUTPUT_PATH)

if not os.path.exists(TASK3_OUTPUT_PATH):
    os.makedirs(TASK3_OUTPUT_PATH)

# task1.solve_task1(TASK1_PATH, TASK1_OUTPUT_PATH, SHOW_DETAILS)
# task2.solve_task2(TASK2_PATH, TASK2_OUTPUT_PATH)
task3.solve_task3(TASK3_PATH, TASK3_OUTPUT_PATH)