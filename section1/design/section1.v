module section1(
    input clk,
    input [7:0] a,
    input [7:0] b,
    output reg [7:0] out
);


always @(posedge clk) begin
    out <= a & b;
end

endmodule