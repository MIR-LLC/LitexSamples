setlocal
PATH=C:\cygwin64\bin;%PATH%
PATH=D:\LATICE\yosys-master;%PATH%
PATH=D:\LATICE\nextpnr-master\out\build\x64-Release;%PATH%
PATH=D:\LATICE\nextpnr-master\out\install\x64-Release\lib;%PATH%
PATH=D:\LATICE\OpenOCD-20210729-0.11.0\bin;%PATH%
PATH=D:\LATICE\Litex\riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-w64-mingw32\bin;%PATH%

yosys -l colorlight_5a_75b.rpt colorlight_5a_75b.ys 
nextpnr-ecp5 --json colorlight_5a_75b.json --lpf colorlight_5a_75b.lpf --textcfg colorlight_5a_75b.config      --25k --package CABGA256 --speed 6 --timing-allow-fail  --seed 1
ecppack colorlight_5a_75b.config --svf colorlight_5a_75b.svf --bit colorlight_5a_75b.bit --bootaddr 0   || exit /b
