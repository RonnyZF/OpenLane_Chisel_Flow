#!/usr/bin/python3

import re
import subprocess, os
import shutil
import docker

area_array = []
power_array = []

def replace(filename,oldText,newText,flags=0):
	with open(filename,"r+") as file:
		fileContents = file.read()
		textPattern = re.compile( re.escape(oldText),flags)
		fileContents = textPattern.sub(newText,fileContents)
		file.seek(0)
		file.truncate()
		file.write(fileContents)

def prepare_chissel(apr_num,pri_type,sub_type):
    print("Preparing Chissel \n \n")
    os.chdir('/home/prj/chisel-test/src/test/scala/RCA')
    subprocess.run("cp /home/prj/design-flow/sources/Launcher.scala Launcher.scala", shell=True)
    replace("Launcher.scala","APR_NUM_SUB",apr_num)
    replace("Launcher.scala","PRI_TYPE_SUB",pri_type)
    replace("Launcher.scala","SUB_TYPE_SUB",sub_type)
    

def run_chissel():
    print("Run Chissel \n \n")
    os.chdir('/home/prj/chisel-test')
    subprocess.run("sbt 'test:runMain RCA.Launcher RCA_A'", shell=True)

def clean_openlane_runs():
    print("Cleaning Openlane Runs \n \n")
    os.chdir('/home/prj/OpenLane/designs/RcaAdder_A_1/runs/')
    subprocess.run("rm -rfv RUN*", shell=True)

def prepare_openlane():
    print(" \n \n Prepare for OpenLane \n \n")
    #Copy the .v generated file from chisel to OpenLane
    os.chdir('/home/prj/chisel-test/test_run_dir/RCA/RCA_A/src')
    src="RcaAdder_A_1.v"
    dst_folder="/home/prj/OpenLane/designs/"+src[:-2]
    dst_file=src
    dst=dst_folder+"/src/"+dst_file
    cmd='cp "%s" "%s"' % (src, dst)
    subprocess.call("mkdir "+dst_folder, shell=True)
    subprocess.call("mkdir "+dst_folder+"/src/", shell=True)
    status = subprocess.call(cmd, shell=True)
    if status != 0:
        if status < 0:
            print("Killed by signal", status)
        else:
            print("Command failed with return code - ", status)
    else:
        print('Execution of %s passed!\n' % cmd)
    #generate config.tcl file
    srcConfig="/home/prj/design-flow/sources/config.tcl"
    dst_folderConfig="/home/prj/OpenLane/designs/"+src[:-2]+"/"
    dst_fileConfig="config.tcl"
    dstConfig=dst_folderConfig+dst_fileConfig
    cmdConfig='cp "%s" "%s"' % (srcConfig, dstConfig)
    subprocess.call(cmdConfig, shell=True)
    replace(dstConfig,"TO_REPLACE",src[:-2])

def run_openlane():
    print(" \n \n Run OpenLane \n \n")
    #Copy the .v generated file from chisel to OpenLane
    os.chdir('/home/prj/OpenLane')  
    #subprocess.run("make mount", shell=True)
    subprocess.run("docker exec -it clever_hellman ./flow.tcl -design RcaAdder_A_1 -to synthesis", shell=True) #automatizaro la obtencion del nombre
    
def extract_area():
    print(" \n \n Extract Area \n \n")
    
    os.chdir('/home/prj/OpenLane/designs/RcaAdder_A_1/runs/')
    proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
    run_name = proc.stdout.read()
    os.chdir(str(run_name)[2:-3]+'/logs/synthesis')

    pattern = re.compile("Design area")
    cnt=0
    for i, line in enumerate(open('2-sta.log')):
        for match in re.finditer(pattern, line):
            cnt=i+1

    extlines = []
    file = open("2-sta.log", "rt")
    for lines in file:
        extlines.append(lines.rstrip('\n'))
    file.close()
    parse=extlines[cnt-1].split(" ")
    area_array.append(float(parse[2]))
    print(area_array)

def extract_power():
    print(" \n \n Extract power \n \n")
    os.chdir('/home/prj/OpenLane/designs/RcaAdder_A_1/runs/')
    proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
    run_name = proc.stdout.read()
    os.chdir(str(run_name)[2:-3]+'/logs/synthesis')
    #subprocess.run("pwd", shell=True)
    pattern = re.compile("report_power")
    cnt=0
    for i, line in enumerate(open('2-sta.log')):
        for match in re.finditer(pattern, line):
            cnt=i+1
            print (cnt)

    extlines = []
    file = open("2-sta.log", "rt")
    for lines in file:
        extlines.append(lines.rstrip('\n'))
    file.close()
    parse=extlines[cnt+9].split(" ")
    power_array.append(float(parse[27]))
    print(power_array)
    
    


def main():

    for apr_num in range(5):
        for pri_type in range(3):
            for sub_type in range(9):
                clean_openlane_runs()
                prepare_chissel(str(apr_num),str(pri_type),str(sub_type))
                run_chissel()
                prepare_openlane()
                run_openlane()
                extract_area()
                extract_power()


if __name__ == "__main__":
    main()