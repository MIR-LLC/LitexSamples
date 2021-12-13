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
    # J5
    ("gpio", 56, Pins("j5:0"), IOStandard("LVCMOS33")),   
    ("gpio", 57, Pins("j5:1"), IOStandard("LVCMOS33")),   
    ("gpio", 58, Pins("j5:2"), IOStandard("LVCMOS33")),   
    # GND
    ("gpio", 59, Pins("j5:4"), IOStandard("LVCMOS33")),
    ("gpio", 60, Pins("j5:5"), IOStandard("LVCMOS33")),
    ("gpio", 61, Pins("j5:6"), IOStandard("LVCMOS33")),
    ("gpio", 62, Pins("j5:7"), IOStandard("LVCMOS33")),
    ("gpio", 63, Pins("j5:8"), IOStandard("LVCMOS33")),
    ("gpio", 64, Pins("j5:9"), IOStandard("LVCMOS33")),
    ("gpio", 65, Pins("j5:10"), IOStandard("LVCMOS33")),
    ("gpio", 66, Pins("j5:11"), IOStandard("LVCMOS33")),
    ("gpio", 67, Pins("j5:12"), IOStandard("LVCMOS33")),
    ("gpio", 68, Pins("j5:13"), IOStandard("LVCMOS33")),
    ("gpio", 69, Pins("j5:14"), IOStandard("LVCMOS33")),
    # GND

    # J6
    ("gpio", 70, Pins("j6:0"), IOStandard("LVCMOS33")),   
    ("gpio", 71, Pins("j6:1"), IOStandard("LVCMOS33")),   
    ("gpio", 72, Pins("j6:2"), IOStandard("LVCMOS33")),   
    # GND
    ("gpio", 73, Pins("j6:4"), IOStandard("LVCMOS33")),
    ("gpio", 74, Pins("j6:5"), IOStandard("LVCMOS33")),
    ("gpio", 75, Pins("j6:6"), IOStandard("LVCMOS33")),
    ("gpio", 76, Pins("j6:7"), IOStandard("LVCMOS33")),
    ("gpio", 77, Pins("j6:8"), IOStandard("LVCMOS33")),
    ("gpio", 78, Pins("j6:9"), IOStandard("LVCMOS33")),
    ("gpio", 79, Pins("j6:10"), IOStandard("LVCMOS33")),
    ("gpio", 80, Pins("j6:11"), IOStandard("LVCMOS33")),
    ("gpio", 81, Pins("j6:12"), IOStandard("LVCMOS33")),
    ("gpio", 82, Pins("j6:13"), IOStandard("LVCMOS33")),
    ("gpio", 83, Pins("j6:14"), IOStandard("LVCMOS33")),
    # GND

    # J7
    ("gpio", 84, Pins("j7:0"), IOStandard("LVCMOS33")),   
    ("gpio", 85, Pins("j7:1"), IOStandard("LVCMOS33")),   
    ("gpio", 86, Pins("j7:2"), IOStandard("LVCMOS33")),   
    # GND
    ("gpio", 87, Pins("j7:4"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 88, Pins("j7:5"), IOStandard("LVCMOS33")),
    ("gpio", 89, Pins("j7:6"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 90, Pins("j7:7"), IOStandard("LVCMOS33")),
    ("gpio", 91, Pins("j7:8"), IOStandard("LVCMOS33")),
    ("gpio", 92, Pins("j7:9"), IOStandard("LVCMOS33")),
    ("gpio", 93, Pins("j7:10"), IOStandard("LVCMOS33")),
    ("gpio", 94, Pins("j7:11"), IOStandard("LVCMOS33")),
    ("gpio", 95, Pins("j7:12"), IOStandard("LVCMOS33")),
    ("gpio", 96, Pins("j7:13"), IOStandard("LVCMOS33")),
    ("gpio", 97, Pins("j7:14"), IOStandard("LVCMOS33")),
    # GND

    # J8
    ("gpio", 98, Pins("j8:0"), IOStandard("LVCMOS33")), # Input now   
    ("gpio", 99, Pins("j8:1"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 100, Pins("j8:2"), IOStandard("LVCMOS33")), # Input now   
    # GND
    ("gpio", 101, Pins("j8:4"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 102, Pins("j8:5"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 103, Pins("j8:6"), IOStandard("LVCMOS33")), # Input now
    ("gpio", 104, Pins("j8:7"), IOStandard("LVCMOS33")),
    ("gpio", 105, Pins("j8:8"), IOStandard("LVCMOS33")),
    ("gpio", 106, Pins("j8:9"), IOStandard("LVCMOS33")),
    ("gpio", 107, Pins("j8:10"), IOStandard("LVCMOS33")),
    ("gpio", 108, Pins("j8:11"), IOStandard("LVCMOS33")),
    ("gpio", 109, Pins("j8:12"), IOStandard("LVCMOS33")),
    ("gpio", 110, Pins("j8:13"), IOStandard("LVCMOS33")),
    ("gpio", 111, Pins("j8:14"), IOStandard("LVCMOS33")),
    # GND
]

from litex.soc.interconnect.csr import AutoCSR, CSRStatus, CSRStorage
class GPU(Module, AutoCSR):
    def __init__(self, pins, clk):
        self.x0 = CSRStorage(16, reset=100)
        self.x1 = CSRStorage(16, reset=150)
        self.y0 = CSRStorage(16, reset=100)
        self.y1 = CSRStorage(16, reset=200)
        self.comb += [
            pins[1].eq(0),
        ]
        self.specials += Instance(
            'gpu',
            i_clk=clk,
            i_x0=self.x0.storage,
            i_x1=self.x1.storage,
            i_y0=self.y0.storage,
            i_y1=self.y1.storage,
            o_hsync=pins[2],
            o_vsync=pins[3],
            o_color=pins[0]
        )


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

    soc.platform.add_extension(_gpios) # General LED outputs        
    touch_pins = [
           soc.platform.request("gpio", 0),
           soc.platform.request("gpio", 1),
           soc.platform.request("gpio", 2),
           soc.platform.request("gpio", 3)
       ]
#    clk = soc.crg.cd_sys.clk
    clk = soc.crg.pll.clkin

    soc.submodules.gpu = GPU(touch_pins, clk)
    soc.add_csr("gpu")
    
    soc.platform.add_source("hvsync_generator.v")
    soc.platform.add_source("gpu.v")

    args.csr_csv = "scripts/csr.csv"
    builder = Builder(soc, **builder_argdict(args))
    builder.build(**trellis_argdict(args), run=args.build)

    if args.load:
        prog = soc.platform.create_programmer()
        prog.load_bitstream(os.path.join(builder.gateware_dir, soc.build_name + ".svf"))

if __name__ == "__main__":
    main()

