/*

Copyright (c) 2015-2016 Alex Forencich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

*/

// Language: Verilog 2001

`timescale 1ns / 1ps

/*
 * Wishbone RAM
 */
module wb_ram #
(
    parameter DATA_WIDTH = 32,              // width of data bus in bits (8, 16, 32, or 64)
    parameter ADDR_WIDTH = 9,              // width of address bus in bits
    parameter SELECT_WIDTH = (DATA_WIDTH/8) // width of word select bus (1, 2, 4, or 8)
)
(
    input  wire                    clk,
    input  wire                    rst,

    input  wire [ADDR_WIDTH-1:0]   adr_i,   // ADR_I() address
    input  wire [DATA_WIDTH-1:0]   dat_i,   // DAT_I() data in
    output wire [DATA_WIDTH-1:0]   dat_o,   // DAT_O() data out
    input  wire                    we_i,    // WE_I write enable input
    input  wire [SELECT_WIDTH-1:0] sel_i,   // SEL_I() select input
    input  wire                    stb_i,   // STB_I strobe input
    output wire                    ack_o,   // ACK_O acknowledge output
    input  wire                    cyc_i    // CYC_I cycle input
);

// width of data port in words (1, 2, 4, or 8)
parameter WORD_WIDTH = SELECT_WIDTH;
// size of words (8, 16, 32, or 64 bits)
parameter WORD_SIZE = DATA_WIDTH/WORD_WIDTH;

reg [DATA_WIDTH-1:0] dat_o_reg = {DATA_WIDTH{1'b0}};
reg ack_o_reg = 1'b0;

// (* RAM_STYLE="BLOCK" *)
reg [7:0] mem0[(2**ADDR_WIDTH)-1:0];
reg [7:0] mem1[(2**ADDR_WIDTH)-1:0];
reg [7:0] mem2[(2**ADDR_WIDTH)-1:0];
reg [7:0] mem3[(2**ADDR_WIDTH)-1:0];

assign dat_o = dat_o_reg;
assign ack_o = ack_o_reg;

integer i, j;

always @(posedge clk) begin
    if (rst)
    begin
        ack_o_reg <= 1'b0;
    end else
    begin
        ack_o_reg <= 1'b0;
        if (cyc_i & stb_i & ~ack_o) 
	begin
            if (we_i & sel_i[0]) begin
                mem0[adr_i] <= dat_i[7:0];
            end
            if (we_i & sel_i[1]) begin
                mem1[adr_i] <= dat_i[15:8];
            end
            if (we_i & sel_i[2]) begin
                mem2[adr_i] <= dat_i[23:16];
            end
            if (we_i & sel_i[3]) begin
                mem3[adr_i] <= dat_i[31:24];
            end
            dat_o_reg[7:0] <= mem0[adr_i];
            dat_o_reg[15:8] <= mem1[adr_i];
            dat_o_reg[23:16] <= mem2[adr_i];
            dat_o_reg[31:24] <= mem3[adr_i];
            ack_o_reg <= 1'b1;
        end
     end
end

endmodule
