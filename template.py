#!/usr/bin/env python3

import os
import sys


class SomeClass:
    def __init__(self, some_var=None):
        """
        Class for doing something

        :keyword some_var: This is a var (Mandatory)
        """
        if some_var is None:
            raise Exception("Keyword some_var required")

        self.some_var = some_var 


    def _internal_function(self):
        """
        Does something

        :return: string
        :rtype: string
        """

        return


    def some_function(self):
        """
        Does something
        
        :return: string
        :rtype: string
        """

        return self.some_var
   

    def some_other_function(self):
        """
        Does something
        
        :return: string
        :rtype: string
        """
        
        return self.some_var.upper()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("some_var", help="some var")
    parser.add_argument("-u", "--upper", help="Return Upper", action="store_true")
    args = parser.parse_args()

    x = SomeClass(some_var=args.some_var)

    if args.upper:
        print(x.some_other_function())
    else:
        print(x.some_function())
