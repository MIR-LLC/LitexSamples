from migen import *
from litex_boards.targets.colorlight_5a_75x import *
from litex_boards.platforms.colorlight_5a_75b import *

_gpios = [
    # Attn. Jx/pin descriptions are 1-based, but zero based defs. used!

    # J1
    ("gpio", 0, Pins("j1:0"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 1, Pins("j1:1"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 2, Pins("j1:2"), IOStandard("LVCMOS33")), # Input now   
    # GND
    ("gpio", 3, Pins("j1:4"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 4, Pins("j1:5"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 5, Pins("j1:6"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 6, Pins("j1:7"), IOStandard("LVCMOS33")),
    ("gpio", 7, Pins("j1:8"), IOStandard("LVCMOS33")),
    ("gpio", 8, Pins("j1:9"), IOStandard("LVCMOS33")),
    ("gpio", 9, Pins("j1:10"), IOStandard("LVCMOS33")),
    ("gpio", 10, Pins("j1:11"), IOStandard("LVCMOS33")),
    ("gpio", 11, Pins("j1:12"), IOStandard("LVCMOS33")),
    ("gpio", 12, Pins("j1:13"), IOStandard("LVCMOS33")),
    ("gpio", 13, Pins("j1:14"), IOStandard("LVCMOS33")),
    # GND

    # J2
    ("gpio", 14, Pins("j2:0"), IOStandard("LVCMOS33")), # Input now   
    ("gpio", 15, Pins("j2:1"), IOStandard("LVCMOS33")), # Input now  
    ("gpio", 16, Pins("j2:2"), IOStandard("LVCMOS33")),   
    # GND
    ("gpio", 17, Pins("j2:4"), IOStandard("LVCMOS33")),
    ("gpio", 18, Pins("j2:5"), IOStandard("LVCMOS33")),
    ("gpio", 19, Pins("j2:6"), IOStandard("LVCMOS33")),
    ("gpio", 20, Pins("j2:7"), IOStandard("LVCMOS33")),
    ("gpio", 21, Pins("j2:8"), IOStandard("LVCMOS33")),
    ("gpio", 22, Pins("j2:9"), IOStandard("LVCMOS33")),
    ("gpio", 23, Pins("j2:10"), IOStandard("LVCMOS33")),
    ("gpio", 24, Pins("j2:11"), IOStandard("LVCMOS33")),
    ("gpio", 25, Pins("j2:12"), IOStandard("LVCMOS33")),
    ("gpio", 26, Pins("j2:13"), IOStandard("LVCMOS33")),
    ("gpio", 27, Pins("j2:14"), IOStandard("LVCMOS33")),
    # GND

    # J3
    ("gpio", 28, Pins("j3:0"), IOStandard("LVCMOS33")),   
    ("gpio", 29, Pins("j3:1"), IOStandard("LVCMOS33")),   
    ("gpio", 30, Pins("j3:2"), IOStandard("LVCMOS33")),   
    # GND
    ("gpio", 31, Pins("j3:4"), IOStandard("LVCMOS33")),
    ("gpio", 32, Pins("j3:5"), IOStandard("LVCMOS33")),
    ("gpio", 33, Pins("j3:6"), IOStandard("LVCMOS33")),
    ("gpio", 34, Pins("j3:7"), IOStandard("LVCMOS33")),
    ("gpio", 35, Pins("j3:8"), IOStandard("LVCMOS33")),
    ("gpio", 36, Pins("j3:9"), IOStandard("LVCMOS33")),
    ("gpio", 37, Pins("j3:10"), IOStandard("LVCMOS33")),
    ("gpio", 38, Pins("j3:11"), IOStandard("LVCMOS33")),
    ("gpio", 39, Pins("j3:12"), IOStandard("LVCMOS33")),
    ("gpio", 40, Pins("j3:13"), IOStandard("LVCMOS33")),
    ("gpio", 41, Pins("j3:14"), IOStandard("LVCMOS33")),
    # GND

    # J4
    ("gpio", 42, Pins("j4:0"), IOStandard("LVCMOS33")),  # j4 pin 1
    ("gpio", 43, Pins("j4:1"), IOStandard("LVCMOS33")),  # j4 pin 2
    ("gpio", 44, Pins("j4:2"), IOStandard("LVCMOS33")),  # j4 pin 3
                                                         # j4 pin 4, GND
    ("gpio", 45, Pins("j4:4"), IOStandard("LVCMOS33")),  # j4 pin 5                                                       
    ("gpio", 46, Pins("j4:5"), IOStandard("LVCMOS33")),  # j4 pin 6
    ("gpio", 47, Pins("j4:6"), IOStandard("LVCMOS33")),  # j4 pin 7
    ("gpio", 48, Pins("j4:7"), IOStandard("LVCMOS33")),  # j4 pin 8
    ("gpio", 49, Pins("j4:8"), IOStandard("LVCMOS33")),  # j4 pin 9
    ("gpio", 50, Pins("j4:9"), IOStandard("LVCMOS33")),  # j4 pin 10
    ("gpio", 51, Pins("j4:10"), IOStandard("LVCMOS33")), # j4 pin 11
    ("gpio", 52, Pins("j4:11"), IOStandard("LVCMOS33")), # j4 pin 12
    ("gpio", 53, Pins("j4:12"), IOStandard("LVCMOS33")), # j4 pin 13
    ("gpio", 54, Pins("j4:13"), IOStandard("LVCMOS33")), # j4 pin 14
    ("gpio", 55, Pins("j4:14"), IOStandard("LVCMOS33")), # j4 pin 15
                                                         # j4 pin 16, GND
    ("sram_pins",0,
       Subsignal ("cen", Pins("j8:14")),
       Subsignal ("wen", Pins("j8:13")),
       Subsignal ("oen", Pins("j8:12")),
       Subsignal ("addr", Pins("j8:11 j8:10 j8:9 j8:8 j8:7 j8:6",
                             "j8:5 j8:4 j8:2 j8:1 j8:0 j7:6 j5:0",
                             "j7:4 j7:2 j7:1 j7:0 j6:6 j4:6")),

       Subsignal ("data", Pins("j6:4 j6:2 j6:1 j6:0 j5:6 j5:4",
                             "j5:2 j5:1"))
    )
]

from litex.soc.interconnect.csr import AutoCSR, CSRStatus, CSRStorage, CSRField
from litex.soc.integration.doc import AutoDoc, ModuleDoc

class GPU(Module, AutoCSR, AutoDoc):
    def __init__(self, pins, clk):
        self.x = CSRStorage(
            description="X Coordinates",
            fields=[
                CSRField("x0", size=16, reset=100,description="Left"),
                CSRField("x1", size=16, reset=150,description="Right"),
            ]
            )
        self.y = CSRStorage(
            description="Y Coordinates",
            fields=[
            CSRField("y0", size=16, reset=100,description="Top"),
            CSRField("y1", size=16, reset=200,description="Bottom"),
            ])
        self.frame = CSRStatus (
            description="Current Video Frame Number",
            size=16
            )
        self.comb += [
            pins['Zero'].eq(0),
        ]
        self.specials += Instance(
            'gpu',
            i_clk=clk,
            i_x0=self.x.fields.x0,
            i_x1=self.x.fields.x1,
            i_y0=self.y.fields.y0,
            i_y1=self.y.fields.y1,
            o_curFrame = self.frame.status,
            o_hsync=pins['HSync'],
            o_vsync=pins['VSync'],
            o_color=pins['Color']
        )


class ISSIRam(Module):

   def __init__(self, clk, rst, wishbone, pins):

      self.bus = wishbone
      self.data_width = 32
      self.size = 524288

      self.specials += Instance("issiram",
         i_clk = clk,
         i_rst = rst,
         i_wbs_stb_i = wishbone.stb,
         i_wbs_cyc_i = wishbone.cyc,
         i_wbs_adr_i = wishbone.adr,
         i_wbs_we_i = wishbone.we,
         i_wbs_sel_i = wishbone.sel,
         i_wbs_dat_i = wishbone.dat_w,
         o_wbs_ack_o = wishbone.ack,
         o_wbs_dat_o = wishbone.dat_r,
         o_mem_ce_n = pins['ce'],
         o_mem_oe_n = pins['oe'],
         o_mem_we_n = pins['we'],
         o_mem_adr = pins['adr'],
         io_mem_dat = pins['dat']
      )

class WBRam(Module):

   def __init__(self, clk, rst, wishbone):

      self.bus = wishbone
      self.data_width = 32
      self.size = 512*4

      self.specials += Instance("wb_ram",
         i_clk = clk,
         i_rst = rst,
         i_stb_i = wishbone.stb,
         i_cyc_i = wishbone.cyc,
         i_adr_i = wishbone.adr,
         i_we_i = wishbone.we,
         i_sel_i = wishbone.sel,
         i_dat_i = wishbone.dat_w,
         o_ack_o = wishbone.ack,
         o_dat_o = wishbone.dat_r
      )


from litex.soc.doc import generate_docs, generate_svd
from litex.soc.interconnect import wishbone
from litex.soc.integration.soc import SoCRegion

def main():
    parser = argparse.ArgumentParser(description="LiteX SoC on Colorlight 5A-75X")
    parser.add_argument("--build",             action="store_true",              help="Build bitstream")
    parser.add_argument("--load",              action="store_true",              help="Load bitstream")
    parser.add_argument("--board",             default="5a-75b",                 help="Board type: 5a-75b (default) or 5a-75e")
    parser.add_argument("--revision",          default="7.0", type=str,          help="Board revision: 7.0 (default), 6.0 or 6.1")
    parser.add_argument("--sys-clk-freq",      default=60e6,                     help="System clock frequency (default: 60MHz)")
    ethopts = parser.add_mutually_exclusive_group()
    ethopts.add_argument("--with-ethernet",    action="store_true",              help="Enable Ethernet support")
    ethopts.add_argument("--with-etherbone",   action="store_true",              help="Enable Etherbone support")
    parser.add_argument("--eth-ip",            default="192.168.1.50", type=str, help="Ethernet/Etherbone IP address")
    parser.add_argument("--eth-phy",           default=0, type=int,              help="Ethernet PHY: 0 (default) or 1")
    parser.add_argument("--use-internal-osc",  action="store_true",              help="Use internal oscillator")
    parser.add_argument("--sdram-rate",        default="1:1",                    help="SDRAM Rate: 1:1 Full Rate (default), 1:2 Half Rate")
    builder_args(parser)
    soc_core_args(parser)
    trellis_args(parser)
    args = parser.parse_args()

    soc = BaseSoC(board=args.board, revision=args.revision,
        sys_clk_freq     = int(float(args.sys_clk_freq)),
        with_ethernet    = args.with_ethernet,
        with_etherbone   = args.with_etherbone,
        eth_ip           = args.eth_ip,
        eth_phy          = args.eth_phy,
        use_internal_osc = args.use_internal_osc,
        sdram_rate       = args.sdram_rate,
        cpu_type         = None,
        cpu              = None,
        **soc_core_argdict(args)
    )

    soc.mem_map["csr"] = 0xf0000000;

    soc.platform.add_extension(_gpios) # General LED outputs        
    touch_pins = {
           'Color' : soc.platform.request("gpio", 0),
           'Zero' : soc.platform.request("gpio", 1),
           'HSync' : soc.platform.request("gpio", 2),
           'VSync' : soc.platform.request("gpio", 3)
       }
#    clk = soc.crg.cd_sys.clk
    clk = soc.crg.pll.clkin

    soc.submodules.gpu = GPU(touch_pins, clk)
    soc.add_csr("gpu")
    
    soc.platform.add_source("hvsync_generator.v")
    soc.platform.add_source("gpu.v")


    clk_ram = soc.crg.cd_sys.clk
    rst = ResetSignal()

    issiram = soc.platform.request('sram_pins')
    pins = {
      'ce': issiram.cen,
      'oe': issiram.oen,
      'we': issiram.wen,
      'adr': issiram.addr,
      'dat': issiram.data
    }

    extmem_bus = wishbone.Interface()
    extmem = ISSIRam(clk_ram, rst, extmem_bus, pins)
    soc.submodules.extmem = extmem
    soc.bus.add_slave(name="extmem", slave=extmem_bus,region=SoCRegion(size=extmem.size,cached=True))
    soc.platform.add_source("issiram.v")

    wbram_bus = wishbone.Interface()
    wbram = WBRam(clk_ram, rst, wbram_bus)
    soc.submodules.wbram = wbram
    soc.bus.add_slave(name="wbram", slave=wbram_bus,region=SoCRegion(size=wbram.size,cached=True))
    soc.platform.add_source("wb_ram.v")

    args.csr_csv = "scripts/csr.csv"
    builder = Builder(soc, **builder_argdict(args))
    builder.build(**trellis_argdict(args), run=args.build)

    generate_docs(soc, "build/documentation")
    generate_svd(soc, "build")

    if args.load:
        prog = soc.platform.create_programmer()
        prog.load_bitstream(os.path.join(builder.gateware_dir, soc.build_name + ".svf"))

if __name__ == "__main__":
    main()

