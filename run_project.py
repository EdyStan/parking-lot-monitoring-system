from task_solutions import task1, task2
import os


PROJECT_PATH = '/home/edstan/Desktop/master_AI/sem2/computer_vision/project2'

TASK1_PATH = os.path.join(PROJECT_PATH, 'train/Task1')
TASK1_OUTPUT_PATH = os.path.join(PROJECT_PATH, 'output_train/Task1')

TASK2_PATH = os.path.join(PROJECT_PATH, 'train/Task2')
TASK2_OUTPUT_PATH = os.path.join(PROJECT_PATH, 'output_train/Task2')


if not os.path.exists(TASK1_OUTPUT_PATH):
    os.makedirs(TASK1_OUTPUT_PATH)

if not os.path.exists(TASK2_OUTPUT_PATH):
    os.makedirs(TASK2_OUTPUT_PATH)

# task1.solve_task1(TASK1_PATH, TASK1_OUTPUT_PATH)
task2.solve_task2(TASK2_PATH, TASK2_OUTPUT_PATH)