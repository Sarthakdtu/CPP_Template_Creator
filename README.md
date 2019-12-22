# CPP_Template_Creator
A python script for creating a template cpp file with function for instant file creation and coding.

This script creates a kind of default template of cpp files with main(), bits/stdc++.h header file and a function with type of your choice.

To run the script you must have Python3.

# How To Use

In your current directory simply type the following on terminal ->

Command 1:
 ``
 python3 script.py file_name function_type
 ``
 
 
 or
 
 
 Command 2:
 ``
 python3 script.py file_name 
 ``
 
 file_name must be without ".cpp" extension and function_type can be anything (string, int, vector<int>, map<int, bool>).
 
 
 
 A simple file looks like this after running: 
 ``
 python3 script.py file_name vector<int>
 ``
 
 file_name.cpp
 
 
 ```C++
 #include<bits/stdc++.h>

using namespace std;

vector<int> function_name(){

}

int main(){

  return 0;
}
 ```
 
