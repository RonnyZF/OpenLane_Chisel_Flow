import os
import subprocess
import re
import sources.replace as replace_lib


def clean_openlane_runs():
    print("Cleaning Openlane Runs \n \n")
    os.chdir('/home/prj/OpenLane/designs/RcaAdder_A_1/runs/')
    subprocess.run("rm -rfv RUN*", shell=True)


def prepare_openlane():
    print(" \n \n Prepare for OpenLane \n \n")
    # Copy the .v generated file from chisel to OpenLane
    os.chdir('/home/prj/chisel-test/test_run_dir/RCA/RCA_A/src')
    src = "RcaAdder_A_1.v"
    dst_folder = "/home/prj/OpenLane/designs/"+src[:-2]
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
    srcConfig = "/home/prj/design-flow/sources/config.tcl"
    dst_folderConfig = "/home/prj/OpenLane/designs/"+src[:-2]+"/"
    dst_fileConfig = "config.tcl"
    dstConfig = dst_folderConfig+dst_fileConfig
    cmdConfig = 'cp "%s" "%s"' % (srcConfig, dstConfig)
    subprocess.call(cmdConfig, shell=True)
    replace_lib.replace(dstConfig, "TO_REPLACE", src[:-2])


def run_openlane():  # CAMBIAR EL DOCKER ID
    print(" \n \n Run OpenLane \n \n")
    # Copy the .v generated file from chisel to OpenLane
    os.chdir('/home/prj/OpenLane')
    #subprocess.run("make mount", shell=True)
    # automatizaro la obtencion del nombre
    subprocess.run(
        "docker exec -it clever_hellman ./flow.tcl -design RcaAdder_A_1 -to synthesis", shell=True)


def extract_area():
    print(" \n \n Extract Area \n \n")

    os.chdir('/home/prj/OpenLane/designs/RcaAdder_A_1/runs/')
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
    area = float(parse[2])
    return area
    ##print("tesing area array", area_array)


def extract_power():
    print(" \n \n Extract power \n \n")
    os.chdir('/home/prj/OpenLane/designs/RcaAdder_A_1/runs/')
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
    power = float(parse[27])
    return power
    # print(power_array)
