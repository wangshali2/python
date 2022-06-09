import sys
import importlib

importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter #解释器
from pdfminer.converter import PDFPageAggregator #转换器
from pdfminer.layout import LTTextBoxHorizontal, LAParams #布局
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed #是否允许pdf和text转换


# pdf->txt
def readPDF(path, toPath):
    #以二进制形式打开pdf文件
    f = open(path, "rb")

    #创建一个pdf文档分析器
    parser = PDFParser(f)
    #创建pdf文档
    pdfFile = PDFDocument()
    #链接分析器与文档对象
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    #提供初始化密码
    pdfFile.initialize()
    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据
        #数据管理器
        manager = PDFResourceManager()
        #创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manager, device)
        #开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(toPath, "a") as f:
                        str = x.get_text()
                        #print(str)
                        f.write(str+"\n")

path = r"../out/test.pdf"
toPath = r"../out/n.txt"
readPDF(path, toPath)