from app.io.input import Input
from app.io.output import Output


def main():
    inp = Input("example.txt")
    outp = Output(inp.filename)
    outp.output_text_to_console()
    outp.write_to_file()
    inp0 = Input("example.csv")
    outp0 = Output(inp0.filename)
    outp0.output_pandas()

if __name__ == '__main__':
    main()
