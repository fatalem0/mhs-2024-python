import argparse

from latex_generator_fatalem0 import generate_latex_table


def main(output_file):
    data = [
        ["Header1", "Header2", "Header3"],
        ["Row1Col1", "Row1Col2", "Row1Col3"],
        ["Row2Col1", "Row2Col2", "Row2Col3"]
    ]

    latex_code = generate_latex_table(data)

    with open(output_file, "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\usepackage{graphicx}\n")
        f.write("\\begin{document}\n")
        f.write(latex_code)
        f.write("\n\\end{document}")

    print(f"LaTeX файл успешно сохранён в {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="1.tex")
    args = parser.parse_args()

    main(output_file=args.output)
