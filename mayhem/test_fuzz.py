#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import uncurl

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    in_str = fdp.ConsumeUnicodeNoSurrogates(2048)

    try:
        uncurl.parse(in_str)
    except:
        pass
    
        
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()