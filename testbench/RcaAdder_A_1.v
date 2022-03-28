module AFA(
  input   io_a,
  input   io_b,
  input   io_cin,
  output  io_sum,
  output  io_cout
);
  wire  _T_1 = io_a ^ io_b; // @[AFA.scala 23:22]
  assign io_sum = _T_1 ^ io_cin; // @[AFA.scala 23:12]
  assign io_cout = io_cin; // @[AFA.scala 24:13]
endmodule
module AFA_1(
  input   io_a,
  input   io_b,
  input   io_cin,
  output  io_sum,
  output  io_cout
);
  wire  _T_1 = io_a ^ io_b; // @[AFA.scala 28:22]
  wire  _T_3 = io_a & io_b; // @[AFA.scala 29:22]
  wire  _T_5 = _T_1 & io_cin; // @[AFA.scala 29:47]
  assign io_sum = _T_1 | io_cin; // @[AFA.scala 28:12]
  assign io_cout = _T_3 | _T_5; // @[AFA.scala 29:13]
endmodule
module FullAdder(
  input   io_a,
  input   io_b,
  input   io_cin,
  output  io_sum,
  output  io_cout
);
  wire [1:0] _T = io_a + io_b; // @[FullAdder.scala 14:20]
  wire [1:0] _GEN_0 = {{1'd0}, io_cin}; // @[FullAdder.scala 14:28]
  wire [2:0] sum = _T + _GEN_0; // @[FullAdder.scala 14:28]
  assign io_sum = sum[0]; // @[FullAdder.scala 15:12]
  assign io_cout = sum[1]; // @[FullAdder.scala 16:13]
endmodule
module RcaAdder_A_1(
  input        clock,
  input        reset,
  input  [7:0] io_a,
  input  [7:0] io_b,
  input        io_cin,
  output [7:0] io_sum,
  output       io_cout
);
  wire  AFA_io_a; // @[RCA_A_1.scala 27:31]
  wire  AFA_io_b; // @[RCA_A_1.scala 27:31]
  wire  AFA_io_cin; // @[RCA_A_1.scala 27:31]
  wire  AFA_io_sum; // @[RCA_A_1.scala 27:31]
  wire  AFA_io_cout; // @[RCA_A_1.scala 27:31]
  wire  AFA_1_io_a; // @[RCA_A_1.scala 27:31]
  wire  AFA_1_io_b; // @[RCA_A_1.scala 27:31]
  wire  AFA_1_io_cin; // @[RCA_A_1.scala 27:31]
  wire  AFA_1_io_sum; // @[RCA_A_1.scala 27:31]
  wire  AFA_1_io_cout; // @[RCA_A_1.scala 27:31]
  wire  AFA_2_io_a; // @[RCA_A_1.scala 27:31]
  wire  AFA_2_io_b; // @[RCA_A_1.scala 27:31]
  wire  AFA_2_io_cin; // @[RCA_A_1.scala 27:31]
  wire  AFA_2_io_sum; // @[RCA_A_1.scala 27:31]
  wire  AFA_2_io_cout; // @[RCA_A_1.scala 27:31]
  wire  FullAdder_io_a; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_io_b; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_io_cin; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_io_sum; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_io_cout; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_1_io_a; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_1_io_b; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_1_io_cin; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_1_io_sum; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_1_io_cout; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_2_io_a; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_2_io_b; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_2_io_cin; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_2_io_sum; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_2_io_cout; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_3_io_a; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_3_io_b; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_3_io_cin; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_3_io_sum; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_3_io_cout; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_4_io_a; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_4_io_b; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_4_io_cin; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_4_io_sum; // @[RCA_A_1.scala 19:27]
  wire  FullAdder_4_io_cout; // @[RCA_A_1.scala 19:27]
  wire  outBits_1 = AFA_1_io_sum; // @[RCA_A_1.scala 15:21 RCA_A_1.scala 31:22]
  wire  outBits_0 = AFA_io_sum; // @[RCA_A_1.scala 15:21 RCA_A_1.scala 31:22]
  wire  outBits_3 = FullAdder_io_sum; // @[RCA_A_1.scala 15:21 RCA_A_1.scala 23:22]
  wire  outBits_2 = AFA_2_io_sum; // @[RCA_A_1.scala 15:21 RCA_A_1.scala 31:22]
  wire [3:0] _T_18 = {outBits_3,outBits_2,outBits_1,outBits_0}; // @[RCA_A_1.scala 35:27]
  wire  outBits_5 = FullAdder_2_io_sum; // @[RCA_A_1.scala 15:21 RCA_A_1.scala 23:22]
  wire  outBits_4 = FullAdder_1_io_sum; // @[RCA_A_1.scala 15:21 RCA_A_1.scala 23:22]
  wire  outBits_7 = FullAdder_4_io_sum; // @[RCA_A_1.scala 15:21 RCA_A_1.scala 23:22]
  wire  outBits_6 = FullAdder_3_io_sum; // @[RCA_A_1.scala 15:21 RCA_A_1.scala 23:22]
  wire [3:0] _T_21 = {outBits_7,outBits_6,outBits_5,outBits_4}; // @[RCA_A_1.scala 35:27]
  AFA AFA ( // @[RCA_A_1.scala 27:31]
    .io_a(AFA_io_a),
    .io_b(AFA_io_b),
    .io_cin(AFA_io_cin),
    .io_sum(AFA_io_sum),
    .io_cout(AFA_io_cout)
  );
  AFA_1 AFA_1 ( // @[RCA_A_1.scala 27:31]
    .io_a(AFA_1_io_a),
    .io_b(AFA_1_io_b),
    .io_cin(AFA_1_io_cin),
    .io_sum(AFA_1_io_sum),
    .io_cout(AFA_1_io_cout)
  );
  AFA AFA_2 ( // @[RCA_A_1.scala 27:31]
    .io_a(AFA_2_io_a),
    .io_b(AFA_2_io_b),
    .io_cin(AFA_2_io_cin),
    .io_sum(AFA_2_io_sum),
    .io_cout(AFA_2_io_cout)
  );
  FullAdder FullAdder ( // @[RCA_A_1.scala 19:27]
    .io_a(FullAdder_io_a),
    .io_b(FullAdder_io_b),
    .io_cin(FullAdder_io_cin),
    .io_sum(FullAdder_io_sum),
    .io_cout(FullAdder_io_cout)
  );
  FullAdder FullAdder_1 ( // @[RCA_A_1.scala 19:27]
    .io_a(FullAdder_1_io_a),
    .io_b(FullAdder_1_io_b),
    .io_cin(FullAdder_1_io_cin),
    .io_sum(FullAdder_1_io_sum),
    .io_cout(FullAdder_1_io_cout)
  );
  FullAdder FullAdder_2 ( // @[RCA_A_1.scala 19:27]
    .io_a(FullAdder_2_io_a),
    .io_b(FullAdder_2_io_b),
    .io_cin(FullAdder_2_io_cin),
    .io_sum(FullAdder_2_io_sum),
    .io_cout(FullAdder_2_io_cout)
  );
  FullAdder FullAdder_3 ( // @[RCA_A_1.scala 19:27]
    .io_a(FullAdder_3_io_a),
    .io_b(FullAdder_3_io_b),
    .io_cin(FullAdder_3_io_cin),
    .io_sum(FullAdder_3_io_sum),
    .io_cout(FullAdder_3_io_cout)
  );
  FullAdder FullAdder_4 ( // @[RCA_A_1.scala 19:27]
    .io_a(FullAdder_4_io_a),
    .io_b(FullAdder_4_io_b),
    .io_cin(FullAdder_4_io_cin),
    .io_sum(FullAdder_4_io_sum),
    .io_cout(FullAdder_4_io_cout)
  );
  assign io_sum = {_T_21,_T_18}; // @[RCA_A_1.scala 35:10]
  assign io_cout = FullAdder_4_io_cout; // @[RCA_A_1.scala 17:11]
  assign AFA_io_a = io_a[0]; // @[RCA_A_1.scala 28:24]
  assign AFA_io_b = io_b[0]; // @[RCA_A_1.scala 29:24]
  assign AFA_io_cin = io_cin; // @[RCA_A_1.scala 30:26]
  assign AFA_1_io_a = io_a[1]; // @[RCA_A_1.scala 28:24]
  assign AFA_1_io_b = io_b[1]; // @[RCA_A_1.scala 29:24]
  assign AFA_1_io_cin = AFA_io_cout; // @[RCA_A_1.scala 30:26]
  assign AFA_2_io_a = io_a[2]; // @[RCA_A_1.scala 28:24]
  assign AFA_2_io_b = io_b[2]; // @[RCA_A_1.scala 29:24]
  assign AFA_2_io_cin = AFA_1_io_cout; // @[RCA_A_1.scala 30:26]
  assign FullAdder_io_a = io_a[3]; // @[RCA_A_1.scala 20:22]
  assign FullAdder_io_b = io_b[3]; // @[RCA_A_1.scala 21:22]
  assign FullAdder_io_cin = AFA_2_io_cout; // @[RCA_A_1.scala 22:24]
  assign FullAdder_1_io_a = io_a[4]; // @[RCA_A_1.scala 20:22]
  assign FullAdder_1_io_b = io_b[4]; // @[RCA_A_1.scala 21:22]
  assign FullAdder_1_io_cin = FullAdder_io_cout; // @[RCA_A_1.scala 22:24]
  assign FullAdder_2_io_a = io_a[5]; // @[RCA_A_1.scala 20:22]
  assign FullAdder_2_io_b = io_b[5]; // @[RCA_A_1.scala 21:22]
  assign FullAdder_2_io_cin = FullAdder_1_io_cout; // @[RCA_A_1.scala 22:24]
  assign FullAdder_3_io_a = io_a[6]; // @[RCA_A_1.scala 20:22]
  assign FullAdder_3_io_b = io_b[6]; // @[RCA_A_1.scala 21:22]
  assign FullAdder_3_io_cin = FullAdder_2_io_cout; // @[RCA_A_1.scala 22:24]
  assign FullAdder_4_io_a = io_a[7]; // @[RCA_A_1.scala 20:22]
  assign FullAdder_4_io_b = io_b[7]; // @[RCA_A_1.scala 21:22]
  assign FullAdder_4_io_cin = FullAdder_3_io_cout; // @[RCA_A_1.scala 22:24]
endmodule
