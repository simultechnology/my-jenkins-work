from my_jenkins_work.greeting import Greeting
import time


def main():
    start_time = time.time()

    print("start")
    g = Greeting()
    g.japanese()
    g.english()

    elapsed_time = time.time() - start_time
    print(elapsed_time)

main()