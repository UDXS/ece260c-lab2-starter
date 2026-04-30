module section2(
    input clk,
    input [15:0] a,
    input [15:0] b,
    output reg [15:0] out
);


always @(posedge clk) begin
    out <= a & b;
end

endmodule