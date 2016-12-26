# PythonIntrospection
Using introspection of Python(3) to know more about an object.

# Usage
AnalyzeObj(obj)
AnalyzeObj(obj, exclRgEx=["__doc__", "__builtins__"])

obj: Name of the object. If suppose I want to know about details inside package sklearn (and I have already done import sklearn). I can simply do: AnalyzeObj(sklearn)

exclRgEx: The attributes of object which matches the regex list provided here would be ignored. It has some default value, thus passing an empty list would display all the attributes.

On execution it first display help(obj), user can skip it by typing q + Enter
