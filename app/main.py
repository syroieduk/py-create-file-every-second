from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        d = datetime.now()
        s = d.strftime("%Y-%m-%d %H:%M:%S")
        name = f"app-{d.hour}_{d.minute}_{d.second}.log"
        with open(name, "w") as x:
            x.write(f"{s}")
            print(f"{s} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
