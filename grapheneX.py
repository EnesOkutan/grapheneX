#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header, check_privileges
from core.cli.shell import Shell
from core.utils.logcl import GraphenexLogger

def main():
    parse_cli_args()
    print_header()
    check_privileges()
    shell = Shell()
    try:
        shell.cmdloop()
    except KeyboardInterrupt:
        shell.do_EOF(None)

if __name__ == "__main__":
    main()