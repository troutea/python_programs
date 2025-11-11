import os
import subprocess

def run_add(args):
    #result_ls = subprocess.run(['dir/w'],capture_output=True,text=True)
    
    cmd = ['add.exe'] + [str(args)]
    #result = subprocess.run(['add.exe' ,'2'], capture_output=True, text=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    #print(result_ls.stdout)
    #print(result)
    output=result.stdout
    print(f"output: {output}")
    print(output)

    
print("hello")
#run_add(['2'])
run_add(2)