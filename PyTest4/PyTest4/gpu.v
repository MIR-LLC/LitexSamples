module gpu(
    input        clk, 
    output       hsync, 
    output       vsync, 
    output       color, 
    input signed [15:0] x0, 
    input signed [15:0] x1, 
    input signed [15:0] y0, 
    input signed [15:0] y1,
    output reg [15:0] curFrame = 0
);
  wire pclk;
  wire display_on;
  wire signed [15:0] hpos;
  wire signed [15:0] vpos;

  reg vsync_d;
  always @(posedge clk)
  begin
     vsync_d <= vsync;
     if ((!vsync_d) & (vsync))
     begin
        curFrame <= curFrame + 1;  
     end
  end
  
  // VGA 640x480 @60Hz needs a 25.175MHz pixel clock
  // but the PLL is already in use
  // I split the horizontal resolution in half and use the existing 12MHz clock instead
  // front and back porch are manually adjusted until VSYNC reaches the expected 60Hz
  hvsync_generator hvsync_gen (
    .clk(clk),
    .reset(0),
    .hsync(hsync),
    .vsync(vsync),
    .display_on(display_on),
    .hpos(hpos),
    .vpos(vpos),
  );
    
  assign color = display_on && (hpos >= x0 && hpos < x1 && vpos >= y0 && vpos < y1);

endmodule
