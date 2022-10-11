#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import uncurl

def testOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    in_str = fdp.ConsumeUnicodeNoSurrogates(64)
    uncurl.parse(in_str)
        
def main():
    atheris.Setup(sys.argv, testOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()