# User config
set ::env(DESIGN_NAME) TO_REPLACE

# Change if needed
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/*.v]

# Fill this
set ::env(CLOCK_PERIOD) "10.0"
set ::env(CLOCK_PORT) "clk"
set ::env(PL_TARGET_DENSITY) 0.70
set ::env(CELL_PAD) 1
set ::env(DESIGN_IS_CORE) 0
set ::env(RT_MAX_LAYER) met4

set filename $::env(DESIGN_DIR)/$::env(PDK)_$::env(STD_CELL_LIBRARY)_config.tcl
if { [file exists $filename] == 1} {
	source $filename
}

