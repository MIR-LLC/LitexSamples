GPU
===

Register Listing for GPU
------------------------

+------------------------------+-------------------------------+
| Register                     | Address                       |
+==============================+===============================+
| :ref:`GPU_X <GPU_X>`         | :ref:`0x00000000 <GPU_X>`     |
+------------------------------+-------------------------------+
| :ref:`GPU_Y <GPU_Y>`         | :ref:`0x00000004 <GPU_Y>`     |
+------------------------------+-------------------------------+
| :ref:`GPU_FRAME <GPU_FRAME>` | :ref:`0x00000008 <GPU_FRAME>` |
+------------------------------+-------------------------------+

GPU_X
^^^^^

`Address: 0x00000000 + 0x0 = 0x00000000`

    X Coordinates

    .. wavedrom::
        :caption: GPU_X

        {
            "reg": [
                {"name": "x0",  "attr": '100', "bits": 16},
                {"name": "x1",  "attr": '150', "bits": 16}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+---------+------+-------------+
| Field   | Name | Description |
+=========+======+=============+
| [15:0]  | X0   | Left        |
+---------+------+-------------+
| [31:16] | X1   | Right       |
+---------+------+-------------+

GPU_Y
^^^^^

`Address: 0x00000000 + 0x4 = 0x00000004`

    Y Coordinates

    .. wavedrom::
        :caption: GPU_Y

        {
            "reg": [
                {"name": "y0",  "attr": '100', "bits": 16},
                {"name": "y1",  "attr": '200', "bits": 16}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


+---------+------+-------------+
| Field   | Name | Description |
+=========+======+=============+
| [15:0]  | Y0   | Top         |
+---------+------+-------------+
| [31:16] | Y1   | Bottom      |
+---------+------+-------------+

GPU_FRAME
^^^^^^^^^

`Address: 0x00000000 + 0x8 = 0x00000008`

    Current Video Frame Number

    .. wavedrom::
        :caption: GPU_FRAME

        {
            "reg": [
                {"name": "frame[15:0]", "bits": 16},
                {"bits": 16},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 1 }, "options": {"hspace": 400, "bits": 32, "lanes": 1}
        }


