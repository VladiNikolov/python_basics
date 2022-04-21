volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
worker_no_work = float(input())

time_pipe_1 = pipe_1 * worker_no_work
time_pipe_2 = pipe_2 * worker_no_work
all_pipe1_pipe2 = time_pipe_1 + time_pipe_2
procent = 0
procent = (all_pipe1_pipe2 * 100)/ volume
procent_pipe1 = (time_pipe_1 / all_pipe1_pipe2) * 100
procent_pipe2 = (time_pipe_2 / all_pipe1_pipe2) * 100
prelqla_voda = abs(all_pipe1_pipe2 - volume)
if all_pipe1_pipe2 <= volume:
    print(f"The pool is {procent:.2f}% full. Pipe 1: {procent_pipe1:.2f}%. Pipe 2: {procent_pipe2:.2f}%.")
else:
    print(f"For {worker_no_work} hours the pool overflows with {prelqla_voda} liters.")
