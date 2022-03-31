import os
import subprocess
import re
import sources.replace as replace_lib


def prepare_chissel(path, indx, apr_num, sum_type):
    print("Preparing Chissel for process "+indx+"\n")
    os.chdir(path+'/target/chisel-test_'+indx+'/src/test/scala/RCA')
    subprocess.run(
        "cp /home/prj/design-flow/sources/Launcher.scala Launcher.scala", shell=True)
    replace_lib.replace("Launcher.scala", "APR_NUM_SUB", apr_num)
    replace_lib.replace("Launcher.scala", "TYPE_SUB", sum_type)
    # Run Chisel test


def run_chissel(path, indx):
    print("Run Chissel for process "+indx+"\n")
    os.chdir(path+'/target/chisel-test_'+indx)
    subprocess.run(
        "sbt 'test:runMain RCA.Launcher RCA_A' --> "+path+"/target/chisel-test_"+indx+"/test_run_dir/RCA/RCA_A/test.txt", shell=True)
    # Extract NMED from Normal Distribution


def extract_approx_error_normal_dist(path, indx, NMED_N):
    print("Extract normal dist approximation error for process "+indx+"\n")
    os.chdir(path+'/target/chisel-test_'+indx+'/test_run_dir/RCA/RCA_A/')
    pattern = re.compile("NORMAL DIST")
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
        parse = extlines[found_lines[n]].split(" ")
        got_array.append(float(parse[10]))
        expected_array.append(float(parse[12]))
    tmp_a = []
    ed_s = 0
    ed_i = 0.0
    for j in range(len(got_array)):
        nmed_scalar = abs(expected_array[j] - got_array[j])
        tmp_a.append(nmed_scalar)
    for z in range(len(tmp_a)):
        ed_s = ed_s + tmp_a[z]
    if len(got_array) > 0:
        ed_i = ((1/len(tmp_a)) * ed_s)
    else:
        ed_i = 0
    print(int(indx)+5)
    print(ed_i)
    NMED_N[int(indx)-1] = ed_i
    print(NMED_N)
    # Extract NMED from Triangular Distribution


def extract_approx_error_triangular_dist(path, indx, NMED_T):
    print("Extract triangular dist approximation error for process "+indx+"\n")
    os.chdir(path+'/target/chisel-test_'+indx+'/test_run_dir/RCA/RCA_A/')
    pattern = re.compile("TRIANGULAR DIST")
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
        parse = extlines[found_lines[n]].split(" ")
        got_array.append(float(parse[10]))
        expected_array.append(float(parse[12]))
    tmp_a = []
    ed_s = 0
    ed_i = 0.0
    for j in range(len(got_array)):
        nmed_scalar = abs(expected_array[j] - got_array[j])
        tmp_a.append(nmed_scalar)
    for z in range(len(tmp_a)):
        ed_s = ed_s + tmp_a[z]
    if len(got_array) > 0:
        ed_i = ((1/len(tmp_a)) * ed_s)
    else:
        ed_i = 0
    NMED_T[int(indx)-1] = ed_i
    print(NMED_T)
    # Extract NMED from Discrete Distribution


def extract_approx_error_discrete_dist(path, indx, NMED_D):
    print("Extract discrete approximation error for process "+indx+"\n")
    os.chdir(path+'/target/chisel-test_'+indx+'/test_run_dir/RCA/RCA_A/')
    pattern = re.compile("DISCRETE DIST")
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
        parse = extlines[found_lines[n]].split(" ")
        got_array.append(float(parse[10]))
        expected_array.append(float(parse[12]))
    tmp_a = []
    ed_s = 0
    ed_i = 0.0
    for j in range(len(got_array)):
        nmed_scalar = abs(expected_array[j] - got_array[j])
        tmp_a.append(nmed_scalar)
    for z in range(len(tmp_a)):
        ed_s = ed_s + tmp_a[z]
    if len(got_array) > 0:
        ed_i = ((1/len(tmp_a)) * ed_s)
    else:
        ed_i = 0
    NMED_D[int(indx)-1] = ed_i
    print(NMED_D)

