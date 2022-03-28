module testbench_tap ();  // Testbench

  import jkr_cport_dpkt_mem_csrs_pkg::*;
  import jkr_cport_dpkt_mem_param_pkg::*;

  typedef reg [INGRESS_ADDR_WIDTH-1:0] reg_ingress_addr_t;
  typedef reg [INGRESS_DATA_WIDTH-1:0] reg_ingress_data_t;
  typedef reg [INGRESS_DATA_WIDTH/32-1:0] reg_ingress_data_parity_t;
  typedef reg [RISC_ADDR_WIDTH-1:0] reg_risc_addr_t;
  typedef struct packed {
    reg        addr_parity_check_en;
    reg [15:0] data_parity_check_en;
  } reg_cp_dpkt_in_parity_en_pt;
  typedef struct packed {reg valid;} reg_cp_dpkt_err_info_addr_in_pt;
  typedef struct packed {reg valid;} reg_cp_dpkt_err_info_data_out_pt;

  reg i_core_clk;
  reg i_cport_clk;
  reg i_reset;

  // Interface from the ingress path
  reg i_wr_valid;
  reg_ingress_addr_t i_spc_addr;
  reg_ingress_data_t i_data;
  reg_ingress_data_parity_t i_data_parity;
  reg i_addr_parity;
  wire o_wr_ack;

  // Interface with RISC core
  reg i_rd_en;
  reg_risc_addr_t i_cport_addr;
  wire jkr_cport_dpkt_mem_param_pkg::risc_data_t o_data;
  wire jkr_cport_dpkt_mem_param_pkg::risc_ecc_t o_chk_rd_data;
  wire o_rd_valid;

  // Interface from the central CSR block
  reg_cp_dpkt_in_parity_en_pt i_cp_parity_en_csr;
  reg_cp_dpkt_err_info_addr_in_pt i_clr_err_info_addr_in_valid;
  wire jkr_cport_dpkt_mem_csrs_pkg::cp_dpkt_err_info_addr_in_pti o_new_err_info_addr_in;
  wire jkr_cport_dpkt_mem_csrs_pkg::cp_dpkt_err_info_addr_in_we o_we_err_info_addr_in;
  reg_cp_dpkt_err_info_data_out_pt i_clr_err_info_data_out_valid;
  wire jkr_cport_dpkt_mem_csrs_pkg::cp_dpkt_err_info_data_out_pti o_new_err_info_data_out;
  wire jkr_cport_dpkt_mem_csrs_pkg::cp_dpkt_err_info_data_out_we o_we_err_info_data_out;
  wire jkr_cport_dpkt_mem_csrs_pkg::cp_dpkt_err_info_data_out_data0_pti o_new_err_info_data_out_data0;
  wire jkr_cport_dpkt_mem_csrs_pkg::cp_dpkt_err_info_data_out_data1_pti o_new_err_info_data_out_data1;

  jkr_cport_dpkt_mem_top dpm (
      // System
      .i_core_clk(i_core_clk),
      .i_cport_clk(i_cport_clk),
      .i_reset(i_reset),

      // Interface from the ingress path
      .i_wr_valid(i_wr_valid),
      .i_core_addr(i_spc_addr),
      .i_data(i_data),
      .i_data_parity(i_data_parity),
      .i_addr_parity(i_addr_parity),
      .o_wr_ack(o_wr_ack),

      // Interface with RISC core
      .i_rd_en(i_rd_en),
      .i_cport_addr(i_cport_addr),
      .o_data(o_data),
      .o_chk_rd_data(o_chk_rd_data),
      .o_rd_valid(o_rd_valid),

      // Interface from the central CSR block
      .i_cp_parity_en_csr(i_cp_parity_en_csr),
      .i_clr_err_info_addr_in_valid(i_clr_err_info_addr_in_valid),
      .o_new_err_info_addr_in(o_new_err_info_addr_in),
      .o_we_err_info_addr_in(o_we_err_info_addr_in),
      .i_clr_err_info_data_out_valid(i_clr_err_info_data_out_valid),
      .o_new_err_info_data_out(o_new_err_info_data_out),
      .o_we_err_info_data_out(o_we_err_info_data_out),
      .o_new_err_info_data_out_data0(o_new_err_info_data_out_data0),
      .o_new_err_info_data_out_data1(o_new_err_info_data_out_data1)
  );

  reg_ingress_addr_t spc_addr_q[$];
  reg_ingress_addr_t spc_addr_tmp;
  logic [2:0] sel;

  //  initial #End_of_Test $finish;
  initial #800 $finish();

  initial begin
    #5 i_core_clk = 1;
    forever #5 i_core_clk = ~i_core_clk;
  end

  initial begin
    #5 i_cport_clk = 1;
    forever #10 i_cport_clk = ~i_cport_clk;
  end

  //SPC inputs
  initial begin
    reset();
    repeat (5) @(posedge i_core_clk);

    ingress_transaction_bad_addr_parity();
    wr_valid_zero();
    repeat (10) @(posedge i_core_clk);
    ingress_transaction_good_parity();
    ingress_transaction_good_parity();
    ingress_transaction_good_parity();
    ingress_transaction_bad_data_parity();
    ingress_transaction_good_parity();
    ingress_transaction_bad_addr_parity();
    ingress_transaction_good_parity();
    wr_valid_zero();
    //wr_valid_zero();
    //ingress_transaction_bad_data_parity();
    //ingress_transaction_bad_addr_parity();
    //ingress_transaction_good_parity();

  end

  //RISC inputs
  initial begin
    repeat (3) @(posedge i_cport_clk);
    set_csrs_addr_parity_chk_en();
    set_csrs_data_parity_chk_en();
    repeat (5) @(posedge i_cport_clk);
    risc_read_addr();
    risc_no_rd_en();
    repeat (5) @(posedge i_cport_clk);
    risc_read_addr();
    risc_read_addr();
    risc_read_addr();
    risc_read_addr();
    risc_read_addr();
    risc_no_rd_en();

    //risc_no_rd_en();
    //set_i_clr_err_info_addr_in_valid();
    //reset_i_clr_err_info_addr_in_valid();


  end
  //



  /************************************** FUNCT *************************************/
  function automatic logic [15:0] data_parity_gen;
    input [511:0] data;
    logic [31:0] chunk_array[16];
    {<<32{chunk_array}} = data;
    begin
      for (int a = 0; a < 16; a++) begin
        logic data_parity_chk = 1'b1;
        logic [31:0] data_chunk;
        data_chunk = chunk_array[a];

        for (int i = 0; i < 32; i++) begin
          if (data_chunk[i]) begin
            data_parity_chk = ~data_parity_chk;
          end
        end
        //$display("hex chunk %d = %b prty = %d\n", a, data_chunk, data_parity_chk);
        data_parity_gen[a] = data_parity_chk;
      end
    end
  endfunction

  function automatic logic addr_parity_gen;
    input jkr_cport_dpkt_mem_param_pkg::ingress_addr_t addr;
    addr_parity_gen = ~^addr;
  endfunction

  /************************************** TASKS *************************************/

  task reset;
    begin
      i_reset = 1'b1;

      i_wr_valid = '0;
      i_spc_addr = '0;
      i_data = '0;
      i_data_parity = '0;
      i_addr_parity = '0;
      i_rd_en = '0;
      i_cport_addr = '0;
      i_cp_parity_en_csr = '0;
      i_clr_err_info_addr_in_valid.valid = '0;
      i_clr_err_info_data_out_valid.valid = '0;
      repeat (2) @(posedge i_cport_clk);
      i_reset = 0;
    end
  endtask

  task wr_valid_zero;
    begin
      @(posedge i_core_clk) begin
        i_wr_valid = 1'b0;
        i_spc_addr = $urandom();
        i_data = {
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom()
        };
        i_data_parity = data_parity_gen(i_data);
        i_addr_parity = addr_parity_gen(i_spc_addr);
      end
    end
  endtask

  task ingress_transaction_bad_addr_parity;
    begin
      @(posedge i_core_clk) begin
        i_wr_valid = 1'b1;
        i_spc_addr = $urandom();
        i_data = {
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom()
        };
        i_data_parity = data_parity_gen(i_data);
        i_addr_parity = ~addr_parity_gen(i_spc_addr);
        //spc_addr_q.push_front(i_spc_addr);
      end
    end
  endtask

  task ingress_transaction_bad_data_parity;
    begin
      @(posedge i_core_clk) begin
        $display("error data parity %0t", $time);
        i_wr_valid = 1'b1;
        i_spc_addr = $urandom();
        i_data = {
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom()
        };
        i_data_parity = ~data_parity_gen(i_data);
        i_addr_parity = addr_parity_gen(i_spc_addr);
        spc_addr_q.push_front(i_spc_addr);
      end
    end
  endtask

  task ingress_transaction_good_parity;
    begin
      @(posedge i_core_clk) begin
        i_wr_valid = 1'b1;
        i_spc_addr = $urandom();
        i_data = {
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom(),
          $urandom()
        };
        i_data_parity = data_parity_gen(i_data);
        i_addr_parity = addr_parity_gen(i_spc_addr);
        spc_addr_q.push_front(i_spc_addr);
      end
    end
  endtask

  task risc_read_addr;
    begin
      spc_addr_tmp = spc_addr_q.pop_back();
      @(posedge i_cport_clk) begin
        sel =  'd7;//$urandom();
        i_cport_addr  = {spc_addr_tmp,sel};
        i_rd_en    = 1'b1;

      end
    end
  endtask

  task risc_no_rd_en;
    begin
      @(posedge i_cport_clk) begin
        //i_cport_addr  = $urandom();
        i_rd_en = 1'b0;

      end
    end
  endtask

  task set_csrs_addr_parity_chk_en;
    begin
      i_cp_parity_en_csr.addr_parity_check_en = 1'b1;
    end
  endtask

  task set_csrs_data_parity_chk_en;
    begin
      i_cp_parity_en_csr.data_parity_check_en = 'hFFFF;
      //i_cp_parity_en_csr.data_parity_check_en = 'd3;
    end
  endtask

  task reset_csrs_addr_parity_chk_en;
    begin
      i_cp_parity_en_csr.addr_parity_check_en = 1'b0;
    end
  endtask

  task reset_csrs_data_parity_chk_en;
    begin
      i_cp_parity_en_csr.data_parity_check_en = 'd0;
    end
  endtask

  task set_i_clr_err_info_addr_in_valid;
    begin
      i_clr_err_info_addr_in_valid.valid = 1'b1;
    end
  endtask

  task reset_i_clr_err_info_addr_in_valid;
    begin
      i_clr_err_info_addr_in_valid.valid = 1'b0;
    end
  endtask

endmodule
