//`include "/home/prj/chisel-test/RcaAdder_A.v"

module testbench ();  // Testbench

    reg   clk;
    reg   reset;
    reg   [7:0] io_a;
    reg   [7:0] io_b;
    reg   io_cin;
    wire  [7:0] io_sum;
    wire  io_cout;

    RcaAdder_A_1 dut_adder(
        .clock(clock),
        .reset(reset),
        .io_a(io_a),
        .io_b(io_b),
        .io_cin(io_cin),
        .io_sum(io_sum),
        .io_cout(io_cout)
    );

reg [7:0] A;
integer outfile0, outfile1, outfile2, outfile3;
int status;

initial begin

    outfile0=$fopen("/home/prj/chisel-test/test.txt","r");   //"r" means reading and "w" means writing
    //read line by line.
    while(!$feof(outfile0)) begin //read until an "end of file" is reached.
        status = $fscanf(outfile0,"%d\n",A); //scan each line and get the value as an hexadecimal, use %b for binary and %d for decimal.
        $display("%d",A);
        #10; //wait some time as needed.
    end 
    //once reading and writing is finished, close the file.
    $fclose(outfile0);
end




  //  initial #End_of_Test $finish;
  initial #800 $finish();

  initial begin
    #5 clk = 1;
    forever #5 clk = ~clk;
  end

  //SPC inputs
  initial begin
    reset_t();
    repeat (5) @(posedge clk);
  end

  /************************************** FUNCT *************************************/
  //function automatic logic addr_parity_gen;
    
  //endfunction
  /************************************** TASKS *************************************/

  task reset_t;
    begin
        reset = 1'b1;
        io_a = 8'd0;
        io_b = 8'd0;
        io_cin = 8'd0;
    end
  endtask


endmodule
