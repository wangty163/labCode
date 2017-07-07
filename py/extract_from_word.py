import win32com.client as client
import re, glob
from tqdm import tqdm

regex = re.compile("^(\+?defcategory\\b[^:]*)")
line_break = "\n"

def solve(word, file_path):
    print("solve file:", file_path)
    
    # 打开一个已存在的文件
    try:
        doc = word.Documents.Open(file_path)
    except Exception as e:
        print(e)
        return []
        
    ret = list()

    for parNo in tqdm(range(1, doc.Paragraphs.Count)):
        paragraph = doc.Paragraphs(parNo)
        # Get the text of the paragraph.
        current_text = paragraph.Range.Text
        #print(current_text)
        match = regex.search(current_text)
        if match:
            ret.append(match.group(1) + line_break)
    doc.Close()
    return ret

def start(folder_path):
    # 链接word应用进程
    word = client.DispatchEx('Word.Application')

    # 可视化1（可以看见该word进程），不可视0（后台运行word进程）.
    word.Visible = 0

    ret = [line for file_path in glob.iglob(folder_path + "/**/*.docx", recursive=True) for line in solve(word, file_path)]
    
    word.Quit()
    return ret

def write_result(folder_path, lines, file_name = "res.txt"):
    with open(folder_path + "/" + file_name, "w") as fw:
        fw.writelines(lines)

if __name__ == "__main__":
    folder_path = r"C:\Users\wuyuming\Desktop\G0 - 刘雯旻修改"
    ret = start(folder_path)
    write_result(folder_path, ret)
    #print(ret)
