#!/usr/bin/python3

import xml.sax

class ShanbayHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.word = ""


   # 元素开始调用
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      

   # 元素结束调用
   def endElement(self, tag):
      if self.CurrentData == "word":
         print (self.word) 

   # 读取字符时调用
   def characters(self, content):
      if self.CurrentData == "word":
         #print("1")
         self.word = content 
         #print(self.word)
  
if ( __name__ == "__main__"):
   
   # 创建一个 XMLReader
   parser = xml.sax.make_parser()
   # 关闭命名空间
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # 重写 ContextHandler
   Handler = ShanbayHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("1.xml")
