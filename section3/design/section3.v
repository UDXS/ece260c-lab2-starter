module section3(
    input clk,
    input data,
    input [6:0] addr,
    input write,
    output reg match
);

//reg [6:0] mem; 
wire mem [128];
wire cmp [128];



genvar i;
for (i = 0; i < 128; i = i + 1)
begin : cam

    sg13g2_dfrbp_1 mem_cell (
        .Q(mem[i]),
        .D(write ? data : mem[i]),
        .CLK(clk)
    );

    sg13g2_xnor2_1 comparator (
        .A(mem[i]),
        .B(data),
        .Y(cmp[i])
    );
    //assign cmp[i] = ~(mem[i] ^ data);
end

always @(posedge clk) 
        match <= cmp[addr];

endmodule