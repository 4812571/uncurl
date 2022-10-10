#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import uncurl

def testOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    print(uncurl.parse("curl 'https://pypi.python.org/pypi/uncurl' -H 'Accept-Encoding: gzip,deflate,sdch'"))
        
def main():
    atheris.Setup(sys.argv, testOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()