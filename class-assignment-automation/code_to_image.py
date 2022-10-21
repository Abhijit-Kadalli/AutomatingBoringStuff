from fileinput import filename
import os
from pickle import TRUE
from pygments import highlight
from pygments.lexers.c_cpp import CLexer
from pygments.formatters import HtmlFormatter
import imgkit

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROGRAMS_FILE_PATH = os.path.join(
    BASE_DIR, "class-assignment-automation", "programs")
os.chdir(PROGRAMS_FILE_PATH)

code = """
int binary_search(int *arr, int l, int r, int target)
{
    if (r >= l)
    {
        int mid = l + (r - l) / 2;
        if (arr[mid] == target)
            return mid;

        if (arr[mid] > target)
            return binary_search(arr, l, mid - 1, target);
        return binary_search(arr, mid + 1, r, target);
    }
    return -1;
}
"""

styling = "<style> " + """
*{
    margin: 0;
    padding: 0;
}
tbody {
            background-color: #272822;
        }

        .linenodiv {
            color: white
        }
        .container {
            width: 700px;
            display: flex;
            justify-content: center;
        }
        .highlighttable {
            margin : auto;
        }
""" + \
    HtmlFormatter(style="monokai", linenos=True).get_style_defs(
        '.highlight') + " </style>"


for file in os.listdir():
    if os.path.isfile(file):
        with open(file, "r") as readFile:
            filename, extension = os.path.splitext(file)
            codeDiv = highlight(str(readFile.read()),
                                CLexer(), HtmlFormatter(linenos=True))
            htmlFile = open(os.path.join(
                BASE_DIR, "class-assignment-automation", "html", f"{filename}.html"), 'w')
            htmlFile.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Snippet</title>
                {styling}
            </head>
            <body>
            <div class="container">
                {codeDiv} </div>
            </body>
            </html>
            """)
            htmlFile.close()
            imgkit.from_file(os.path.join(
                BASE_DIR, "class-assignment-automation", "html", f"{filename}.html"),
                os.path.join(
                BASE_DIR, "class-assignment-automation", "images", f"{filename}.png"), options={
                'crop-w': '700',
                'format': 'png',
            })
