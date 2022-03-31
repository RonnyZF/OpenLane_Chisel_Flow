import os
import subprocess
import re
import sources.replace as replace_lib


def clean_openlane_runs(path, indx):
    print("Cleaning Openlane Runs for process "+indx+" \n")
    os.chdir(path+'/target/OpenLane_'+indx+'/designs/RcaAdder_A_1/runs/')
    subprocess.run("rm -rfv RUN*", shell=True)


def prepare_openlane(path, indx):
    print("Prepare for OpenLane for process "+indx+" \n")
    # Copy the .v generated file from chisel to OpenLane
    os.chdir(path+'/target/chisel-test_'+indx+'/test_run_dir/RCA/RCA_A/src')
    src = "RcaAdder_A_1.v"
    dst_folder = path+"/target/OpenLane_"+indx+"/designs/"+src[:-2]
    dst_file = src
    dst = dst_folder+"/src/"+dst_file
    cmd = 'cp "%s" "%s"' % (src, dst)
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
    # generate config.tcl file
    srcConfig = path+"/sources/config.tcl"
    dst_folderConfig = path+"/target/OpenLane_"+indx+"/designs/"+src[:-2]+"/"
    dst_fileConfig = "config.tcl"
    dstConfig = dst_folderConfig+dst_fileConfig
    cmdConfig = 'cp "%s" "%s"' % (srcConfig, dstConfig)
    subprocess.call(cmdConfig, shell=True)
    replace_lib.replace(dstConfig, "TO_REPLACE", src[:-2])


def run_openlane(path, indx):  # CAMBIAR EL DOCKER ID
    print("Run OpenLane for process "+indx+" \n")
    # Copy the .v generated file from chisel to OpenLane
    os.chdir(path+"/target/OpenLane_"+indx)
    #subprocess.run("make mount", shell=True)
    # automatizaro la obtencion del nombre
    if(int(indx) == 1):
        # subprocess.run(
        #    "docker exec -it tender_shaw ./flow.tcl -design RcaAdder_A_1 -init_design_config", shell=True)
        subprocess.run(
            "docker exec -it tender_shaw ./flow.tcl -design RcaAdder_A_1 -to synthesis", shell=True)
    elif(int(indx) == 2):
        # subprocess.run(
        #    "docker exec -it frosty_merkle ./flow.tcl -design RcaAdder_A_1 -init_design_config", shell=True)
        subprocess.run(
            "docker exec -it frosty_merkle ./flow.tcl -design RcaAdder_A_1 -to synthesis", shell=True)
    elif(int(indx) == 3):
        # subprocess.run(
        #    "docker exec -it hungry_babbage ./flow.tcl -design RcaAdder_A_1 -init_design_config", shell=True)
        subprocess.run(
            "docker exec -it hungry_babbage ./flow.tcl -design RcaAdder_A_1 -to synthesis", shell=True)
    elif(int(indx) == 4):
        # subprocess.run(
        #    "docker exec -it compassionate_moser ./flow.tcl -design RcaAdder_A_1 -init_design_config", shell=True)
        subprocess.run(
            "docker exec -it compassionate_moser ./flow.tcl -design RcaAdder_A_1 -to synthesis", shell=True)


def extract_area(path, indx, AREA):
    #print("Extract Area for process "+indx+" \n")

    os.chdir(path+"/target/OpenLane_"+indx+"/designs/RcaAdder_A_1/runs/")
    proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
    run_name = proc.stdout.read()
    os.chdir(str(run_name)[2:-3]+'/logs/synthesis')

    pattern = re.compile("Design area")
    cnt = 0
    for i, line in enumerate(open('2-sta.log')):
        for match in re.finditer(pattern, line):
            cnt = i+1

    extlines = []
    file = open("2-sta.log", "rt")
    for lines in file:
        extlines.append(lines.rstrip('\n'))
    file.close()
    parse = extlines[cnt-1].split(" ")
    AREA[int(indx)-1] = float(parse[2])
    # print(AREA)
    ##print("tesing area array", area_array)


def extract_power(path, indx, POWER):
    #print("Extract power for process "+indx+" \n")
    os.chdir(path+"/target/OpenLane_"+indx+"/designs/RcaAdder_A_1/runs/")
    proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
    run_name = proc.stdout.read()
    os.chdir(str(run_name)[2:-3]+'/logs/synthesis')
    #subprocess.run("pwd", shell=True)
    pattern = re.compile("report_power")
    cnt = 0
    for i, line in enumerate(open('2-sta.log')):
        for match in re.finditer(pattern, line):
            cnt = i+1
            # print(cnt)

    extlines = []
    file = open("2-sta.log", "rt")
    for lines in file:
        extlines.append(lines.rstrip('\n'))
    file.close()
    parse = extlines[cnt+9].split(" ")
    POWER[int(indx)-1] = float(parse[27])
    # print(POWER)
    # print(power_array)
