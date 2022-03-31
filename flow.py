#!/usr/bin/python3
import multiprocessing
import progressbar
from multiprocessing import Process
import numpy as np
import sources.create_dist as create_dist
import sources.chisel_flow as chisel
import sources.openlane_flow as openlane
import sources.data_storage as data
import sources.set_env as env
import sources.bar as bar

# Create Arrays

manager = multiprocessing.Manager()
NMED_N = manager.dict()
NMED_T = manager.dict()
NMED_D = manager.dict()
AREA = manager.dict()
POWER = manager.dict()

count = [0,0,0,0]
sum = [0,0,0,0]
sum_array = []
jobs = []


# Functions


def main():

    sum_type_array = ["F0", "A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7",
                      "A8", "A9", "L0", "T0", "T1", "T2", "T3", "T4", "T5", "T6"]
    end = len(sum_type_array)
    n_iter = end*end*end*end*end
    l_num = 0
    bar = progressbar.ProgressBar(maxval=n_iter, \
	widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()

    path = env.define_dir_path()
    data.clean_database(path)
    env.create_chisel_copy(path)
    #env.create_openlane_copy(path)

    for a in range(len(sum_type_array)):
        for b in range(len(sum_type_array)):
            for c in range(len(sum_type_array)):
                for d in range(len(sum_type_array)):
                    for e in range(0,end,4):

                        for n in range(4):
                            bar.update(l_num+1)
                            try:
                                sum[n] = sum_type_array[e+n]+","+sum_type_array[d]+","+sum_type_array[c] + \
                                    ","+sum_type_array[b]+"," + sum_type_array[a]+",F0,F0,F0"
                                count[n] = 8 - sum[n].count("F0")
                                #sum_array.append(sum[n])
                            except:
                                print('the whatever error occurred.')
                        #clean openlane
                        for n in range(4):
                            try:
                                p = Process(target=openlane.clean_openlane_runs, args=(path,str(n+1), ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        #prepare chisel
                        for n in range(4):
                            try:
                                p = Process(target=chisel.prepare_chissel, args=(path,str(n+1),str(count[n]), sum[n], ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        #run chisel
                        for n in range(4):
                            try:
                                p = Process(target=chisel.run_chissel, args=(path,str(n+1), ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        #extract nmed_n
                        for n in range(4):
                            try:
                                p = Process(target=chisel.extract_approx_error_normal_dist, args=(path,str(n+1),NMED_N, ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        #extract nmed_t
                        for n in range(4):
                            try:
                                p = Process(target=chisel.extract_approx_error_triangular_dist, args=(path,str(n+1),NMED_T, ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        #extract nmed_d
                        for n in range(4):
                            try:
                                p = Process(target=chisel.extract_approx_error_discrete_dist, args=(path,str(n+1),NMED_D, ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        #Prepare openlane
                        for n in range(4):
                            try:
                                p = Process(target=openlane.prepare_openlane, args=(path,str(n+1), ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        #run openlane
                        for n in range(4):
                            try:
                                p = Process(target=openlane.run_openlane, args=(path,str(n+1), ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        #extraxt area
                        for n in range(4):
                            try:
                                p = Process(target=openlane.extract_area, args=(path,str(n+1),AREA, ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        #extraxt power
                        for n in range(4):
                            try:
                                p = Process(target=openlane.extract_power, args=(path,str(n+1),POWER, ))
                                jobs.append(p)
                                p.start()
                            except:
                                print('the whatever error occurred.')
                        for proc in jobs:
                            try:
                                proc.join()
                            except:
                                print('the whatever error occurred.')

                        data.database_output(path,count,sum,AREA,POWER,NMED_N,NMED_T,NMED_D)
    # plot_data()


if __name__ == "__main__":
    main()
