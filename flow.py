#!/usr/bin/python3

import re
import subprocess, os
import shutil
import docker
import statistics
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

area_array = [1,2]
power_array = [1,2]
NMED_array = [1,2]
sum_array = []

def replace(filename,oldText,newText,flags=0):
	with open(filename,"r+") as file:
		fileContents = file.read()
		textPattern = re.compile( re.escape(oldText),flags)
		fileContents = textPattern.sub(newText,fileContents)
		file.seek(0)
		file.truncate()
		file.write(fileContents)

def prepare_chissel(apr_num,sum_type):
    print("Preparing Chissel \n \n")
    os.chdir('/home/prj/chisel-test/src/test/scala/RCA')
    subprocess.run("cp /home/prj/design-flow/sources/Launcher.scala Launcher.scala", shell=True)
    replace("Launcher.scala","APR_NUM_SUB",apr_num)
    replace("Launcher.scala","TYPE_SUB",sum_type)
    

def run_chissel():
    print("Run Chissel \n \n")
    os.chdir('/home/prj/chisel-test')
    subprocess.run("sbt 'test:runMain RCA.Launcher RCA_A'", shell=True)

def extract_approx_error():
    print(" \n \n Extract approximation error \n \n")
    os.chdir('/home/prj/chisel-test/test_run_dir/RCA/RCA_A/')
    #subprocess.run("pwd", shell=True)
    pattern = re.compile("EXPECT AT")
    found_lines = []
    for i, line in enumerate(open('test.txt')):
        for match in re.finditer(pattern, line):
            found_lines.append(i)

    extlines = []
    file = open("test.txt", "rt")
    for lines in file:
        extlines.append(lines.rstrip('\n'))
    file.close()
    got_array = []
    expected_array = []
    for n in range(len(found_lines)):
        parse=extlines[found_lines[n]].split(" ")
        got_array.append(float(parse[9]))
        expected_array.append(float(parse[11]))
    
    tmp_a = []
    
    for j in range(len(got_array)):
        nmed_scalar = expected_array[j] - got_array[j]
        tmp_a.append(nmed_scalar)
    mean = statistics.mean(tmp_a)
    NMED_array.append(mean)

    #print(NMED_array)

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

def database_output(apr_num):
    print(" \n \n Creating database \n \n")
    os.chdir('/home/prj/design-flow/outputs/')
    subprocess.run("pwd", shell=True)

    with open ("database.csv", "w") as file:
        writer = csv.writer(file, delimiter=',')
        for n in range(len(area_array)):
            writer.writerow([apr_num,sum_array[n],area_array[n],power_array[n],NMED_array[n]])
    
def plot_data():
    os.chdir('/home/prj/design-flow/')
    l = len(area_array)
    index = np.linspace(0, l, l)
    print(index)

    fig,ax=plt.subplots(1,1)
    plt.subplots_adjust(bottom=0.2)
    ax.plot(index, power_array,marker="v",lw=1)
    plt.xlabel('Sum type')
    plt.ylabel('Power (W)')
    plt.title('Power consumed')
    ax.grid(True)
    #plt.tight_layout()
    ax.set_xticks(index)
    ax.set_xticklabels(sum_array, rotation='vertical', fontsize=6)
    ax.legend(loc='upper right')
    plt.savefig("outputs/power.png")
    plt.close()

    fig,ax=plt.subplots(1,1)
    plt.subplots_adjust(bottom=0.2)
    plt.plot(index, area_array,marker="v",lw=1)
    plt.xlabel('Sum type')
    plt.ylabel('Area (u^2)')
    plt.title('Area')
    ax.grid(True)
    #plt.tight_layout()
    ax.set_xticks(index)
    ax.set_xticklabels(sum_array, rotation='vertical', fontsize=6)
    ax.legend(loc='upper right')
    plt.savefig("outputs/area.png")
    plt.close()
    
    fig,ax=plt.subplots(1,1)
    plt.subplots_adjust(bottom=0.2)
    ax.plot(index, power_array,marker="v",lw=1)
    plt.plot(index, NMED_array,marker="v",lw=1)
    plt.xlabel('Sum type')
    plt.ylabel('NMED)')
    plt.title('NMED')
    ax.grid(True)
    #plt.tight_layout()
    ax.set_xticks(index)
    ax.set_xticklabels(sum_array, rotation='vertical', fontsize=6)
    ax.legend(loc='upper right')
    plt.savefig("outputs/NMED.png")
    plt.close()


def main():

    
    sum_type_array = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9","L0","T0","T1","T2","T3","T4","T5","T6"]

    for a in range(len(sum_type_array)):
        for b in range(len(sum_type_array)):
            sum = sum_type_array[b]+","+sum_type_array[1]+",F0,F0,F0"
            sum_array.append(sum)
            clean_openlane_runs()
            prepare_chissel(str(2),sum)
            run_chissel()
            extract_approx_error() # todas las distibuciones
            prepare_openlane()
            
            run_openlane()
            extract_area()
            extract_power()
    
    database_output(2)
    plot_data()

if __name__ == "__main__":
    main()