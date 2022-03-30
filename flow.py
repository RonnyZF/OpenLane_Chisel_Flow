#!/usr/bin/python3
import sources.libraries
import sources.create_dist as create_dist
import sources.chisel_flow as chisel
import sources.openlane_flow as openlane
import sources.data_storage as data

# Create Arrays
area = 0
power = 0
NMED_N = 0
NMED_T = 0
NMED_D = 0

sum_array = []
expected_normal = []
got_normal = []
expected_triangular = []
got_triangular = []
expected_discrete = []
got_discrete = []

# Functions


def main():

    sum_type_array = ["F0", "A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7",
                      "A8", "A9", "L0", "T0", "T1", "T2", "T3", "T4", "T5", "T6"]
    create_dist.create_triangular_dist()
    create_dist.create_discrete_dist()
    for a in range(len(sum_type_array)):
        for b in range(len(sum_type_array)):
            for c in range(len(sum_type_array)):
                for d in range(len(sum_type_array)):
                    for e in range(len(sum_type_array)):
                        sum = sum_type_array[e]+","+sum_type_array[d]+","+sum_type_array[c] + \
                            ","+sum_type_array[b]+"," + \
                            sum_type_array[a]+",F0,F0,F0"
                        count = 8 - sum.count("F0")
                        sum_array.append(sum)
                        print("Testing the device ", sum,
                              " with the aproximation of ", count)
                        openlane.clean_openlane_runs()
                        chisel.prepare_chissel(str(count), sum)
                        chisel.run_chissel()
                        NMED_N = chisel.extract_approx_error_normal_dist()
                        NMED_T = chisel.extract_approx_error_triangular_dist()
                        NMED_D = chisel.extract_approx_error_discrete_dist()
                        openlane.prepare_openlane()
                        openlane.run_openlane()
                        area = openlane.extract_area()
                        power = openlane.extract_power()
                        data.database_output(
                            count, sum, area, power, NMED_N, NMED_T, NMED_D)
    # plot_data()


if __name__ == "__main__":
    main()
