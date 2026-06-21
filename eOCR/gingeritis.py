import language_tool_python

mytext = """
Dont FORGET TO Cat YOUR LuncH And Make SoMe TRouBLE
"""

def grammarCorrector(text):
    tool = language_tool_python.LanguageTool('en-US')
    result = tool.correct(text)
    return result

output_data = grammarCorrector(mytext)
print(output_data)