def generate_latex():
    # Opening a LaTeX file in write mode
    with open('generated_latex.tex', 'w') as file:
        # Writing the LaTeX document content
        file.write(
'''
\\documentclass{article}
\\begin{document}

\\section*{Generated LaTeX Document}

This is a simple example of generating LaTeX using Python.

\\begin{equation}
    E = mc^2
\\end{equation}

\\begin{itemize}
    \\item Item 1
    \\item Item 2
    \\item Item 3
\\end{itemize}

\\end{document}
'''
        )

if __name__ == "__main__":
    generate_latex()
