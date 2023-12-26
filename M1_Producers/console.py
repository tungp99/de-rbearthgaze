from argparse import ArgumentParser


def shoot():
    parser = ArgumentParser(usage="boom M1_Producers.Aircraft:run")
    parser.add_argument("PATH", type=str, help="M1_Producers.Aircraft:run")
    args = parser.parse_args()

    mod, funcname = args.PATH.split(":")
    module = __import__(mod, fromlist=mod.split("."))
    func = getattr(module, funcname)
    func()


if __name__ == "__main__":
    shoot()
