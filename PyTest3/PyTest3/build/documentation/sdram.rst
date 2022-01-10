SDRAM
=====

Register Listing for SDRAM
--------------------------

+--------------------------------------------------------------------+--------------------------------------------------+
| Register                                                           | Address                                          |
+====================================================================+==================================================+
| :ref:`SDRAM_DFII_CONTROL <SDRAM_DFII_CONTROL>`                     | :ref:`0x00002000 <SDRAM_DFII_CONTROL>`           |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_COMMAND <SDRAM_DFII_PI0_COMMAND>`             | :ref:`0x00002004 <SDRAM_DFII_PI0_COMMAND>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_COMMAND_ISSUE <SDRAM_DFII_PI0_COMMAND_ISSUE>` | :ref:`0x00002008 <SDRAM_DFII_PI0_COMMAND_ISSUE>` |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_ADDRESS <SDRAM_DFII_PI0_ADDRESS>`             | :ref:`0x0000200c <SDRAM_DFII_PI0_ADDRESS>`       |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_BADDRESS <SDRAM_DFII_PI0_BADDRESS>`           | :ref:`0x00002010 <SDRAM_DFII_PI0_BADDRESS>`      |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_WRDATA <SDRAM_DFII_PI0_WRDATA>`               | :ref:`0x00002014 <SDRAM_DFII_PI0_WRDATA>`        |
+--------------------------------------------------------------------+--------------------------------------------------+
| :ref:`SDRAM_DFII_PI0_RDDATA <SDRAM_DFII_PI0_RDDATA>`               | :ref:`0x00002018 <SDRAM_DFII_PI0_RDDATA>`        |
+--------------------------------------------------------------------+--------------------------------------------------+

SDRAM_DFII_CONTROL
^^^^^^^^^^^^^^^^^^

`Address: 0x00002000 + 0x0 = 0x00002000`


    .. wavedrom::
        :caption: SDRAM_DFII_CONTROL

        {
            "reg": [
                {"name": "sel",  "attr": '1', "bits": 1},
                {"name": "cke",  "bits": 1},
                {"name": "odt",  "bits": 1},
                {"name": "reset_n",  "bits": 1},
                {"bits": 28}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+---------+-------------------------------------------+
| Field | Name    | Description                               |
+=======+=========+===========================================+
| [0]   | SEL     |                                           |
|       |         |                                           |
|       |         | +---------+-----------------------------+ |
|       |         | | Value   | Description                 | |
|       |         | +=========+=============================+ |
|       |         | | ``0b0`` | Software (CPU) control.     | |
|       |         | +---------+-----------------------------+ |
|       |         | | ``0b1`  | Hardware control (default). | |
|       |         | +---------+-----------------------------+ |
+-------+---------+-------------------------------------------+
+-------+---------+-------------------------------------------+
+-------+---------+-------------------------------------------+
+-------+---------+-------------------------------------------+

SDRAM_DFII_PI0_COMMAND
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x00002000 + 0x4 = 0x00002004`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_COMMAND

        {
            "reg": [
                {"name": "dfii_pi0_command[5:0]", "bits": 6},
                {"bits": 26},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


SDRAM_DFII_PI0_COMMAND_ISSUE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x00002000 + 0x8 = 0x00002008`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_COMMAND_ISSUE

        {
            "reg": [
                {"name": "dfii_pi0_command_issue", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


SDRAM_DFII_PI0_ADDRESS
^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x00002000 + 0xc = 0x0000200c`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_ADDRESS

        {
            "reg": [
                {"name": "dfii_pi0_address[10:0]", "bits": 11},
                {"bits": 21},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI0_BADDRESS
^^^^^^^^^^^^^^^^^^^^^^^

`Address: 0x00002000 + 0x10 = 0x00002010`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_BADDRESS

        {
            "reg": [
                {"name": "dfii_pi0_baddress", "bits": 1},
                {"bits": 31},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


SDRAM_DFII_PI0_WRDATA
^^^^^^^^^^^^^^^^^^^^^

`Address: 0x00002000 + 0x14 = 0x00002014`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_WRDATA

        {
            "reg": [
                {"name": "dfii_pi0_wrdata[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


SDRAM_DFII_PI0_RDDATA
^^^^^^^^^^^^^^^^^^^^^

`Address: 0x00002000 + 0x18 = 0x00002018`


    .. wavedrom::
        :caption: SDRAM_DFII_PI0_RDDATA

        {
            "reg": [
                {"name": "dfii_pi0_rddata[31:0]", "bits": 32}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


