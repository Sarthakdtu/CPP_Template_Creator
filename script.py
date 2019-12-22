import os
import sys
args = sys.argv
file_name = None
function_type = None

if len(args)<2:
    print("ERROR: File name not provided.")
    exit()
else:
    file_name = args[1]
if len(args)>2:
    function_type = args[2]

file_name += ".cpp"

print("Creating file",file_name)

f = open(file_name, "wt")
f.write("#include<bits/stdc++.h>\r\n" )
f.write("using namespace std;\r\n")

if function_type:
    print("Creating function of type", function_type)
    f.write(function_type + " function_name(){\r\n\n\n}\n\n")

f.write("int main(){\r\n\n\n")
f.write("return 0;\n")
f.write("}")

print("File created.")
f.close()
