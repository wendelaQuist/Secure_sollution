import sys
from itertools import product
import copy

dob0_0 = dict()
dob0_1 = dict()
dob0_2 = dict()
dob0_3 = dict()

dob1_0 = dict()
dob1_1 = dict()
dob1_2 = dict()
dob1_3 = dict()
dob1_4 = dict()

dob2_0 = dict()
dob2_1 = dict()
dob2_2 = dict()
dob2_3 = dict()
dob2_4 = dict()
dob2_5 = dict()

dob3_0 = dict()
dob3_1 = dict()
dob3_2 = dict()
dob3_3 = dict()
dob3_4 = dict()
dob3_5 = dict()
dob3_6 = dict()

dob4_0 = dict()
dob4_1 = dict()
dob4_2 = dict()
dob4_3 = dict()
dob4_4 = dict()
dob4_5 = dict()

dob5_0 = dict()
dob5_1 = dict()
dob5_2 = dict()
dob5_3 = dict()
dob5_4 = dict()

dob6_0 = dict()
dob6_1 = dict()
dob6_2 = dict()
dob6_3 = dict()

allOptions = [
    "412",
    "213",
    "315",
    "514",
    "124",
    "426",
    "623",
    "321",
    "132",
    "236",
    "635",
    "531",
    "145",
    "546",
    "642",
    "241",
    "153",
    "356",
    "654",
    "451",
    "264",
    "465",
    "563",
    "362",
]

the456Options = [
    "514",
    "426",
    "635",
    "546",
    "654",
    "465",
]

dob0_0["options"] = ["153"]  
dob0_1["options"] = ["213"]  
dob0_2["options"] = ["654"]  
dob0_3["options"] = ["465"]  

dob1_0_val = "563"  
dob1_1["options"] = ["315", "465", "145", "635"]  
dob1_2_val = "124"  
dob1_3["options"] = ["451", "654", "356", "153"]  
dob1_4["options"] = ["635", "642"]  

dob2_0["options"] = ["213", "124"]
dob2_1["options"] = allOptions 
dob2_2["options"] = allOptions 
dob2_3["options"] = ["264", "213"]  
dob2_4["options"] = allOptions 
dob2_5_val = "153"

dob3_0_val = "635"  
dob3_1["options"] = the456Options  
dob3_2_val = "145"  
dob3_3["options"] = the456Options  
dob3_4["options"] = the456Options  
dob3_5_val = "264"  
dob3_6_val = "264"  

dob4_0["options"] = allOptions 
dob4_1["options"] = ["623", "153"]  
dob4_2["options"] = allOptions 
dob4_3_val = "213"  
dob4_4["options"] = ["145", "315", "635", "465"]  
dob4_5["options"] = [
    "132",
    "315",
    "236",
    "321",
    "145",
    "412",
    "514",
    "153",
    "241",
    "426",
]  

dob5_0["options"] = ["412", "426", "465", "451"]  
dob5_1["options"] = ["635", "642"]  
dob5_2["options"] = allOptions 
dob5_3["options"] = allOptions 
dob5_4_val = "153"

dob6_0["options"] = ["623", "654"]  
dob6_1["options"] = ["145", "465", "635", "315"]  
dob6_2_val = "654"  
dob6_3["options"] = ["514", "145", "412", "426", "315", "236"]  

lookup = [-1, 1, 2, 3, 4, 5, 6]


def SumLR(ar):
    tot = 0
    for s in ar:
        tot += int(s[0]) + int(s[2])
    return tot


def SumLT(ar):
    tot = 0
    for s in ar:
        tot += int(s[0]) + int(s[1])
    return tot


def SumTR(ar):
    tot = 0
    for s in ar:
        tot += int(s[1]) + int(s[2])
    return tot


progressTotal = len(dob3_1["options"]) * len(dob3_3["options"]) * len(dob3_4["options"])

progress = 0
tot = 0
# Middle
for (dob3_1_val, dob3_3_val, dob3_4_val,) in product(
    dob3_1["options"],
    dob3_3["options"],
    dob3_4["options"],
):
    progress += 1
    print(dob3_1_val, dob3_3_val, dob3_4_val, (progress / progressTotal) * 100, "%")
    if (
        SumLR(
            [
                dob3_0_val,
                dob3_1_val,
                dob3_2_val,
                dob3_3_val,
                dob3_4_val,
                dob3_5_val,
                dob3_6_val,
            ]
        )
        == 61
    ):
        # Bottom
        for (dob6_0_val, dob6_1_val, dob6_3_val) in product(
            dob6_0["options"], dob6_1["options"], dob6_3["options"]
        ):

            if SumLR([dob6_0_val, dob6_1_val, dob6_2_val, dob6_3_val]) == 35:
                # Right vertical
                for dob4_5_val in dob4_5["options"]:
                    if SumLT([dob3_6_val, dob4_5_val, dob5_4_val, dob6_3_val]) == 24:
                        # Right vertical -1
                        for dob4_4_val in dob4_4["options"]:
                            for dob5_3_val in dob5_3["options"]:
                                if (
                                    SumLT(
                                        [
                                            dob2_5_val,
                                            dob3_5_val,
                                            dob4_4_val,
                                            dob5_3_val,
                                            dob6_2_val,
                                        ]
                                    )
                                    == 33
                                ):
                                    # Fifth horizontal 
                                    for (
                                        dob4_0_val,
                                        dob4_1_val,
                                        dob4_2_val,
                                    ) in product(
                                        dob4_0["options"],
                                        dob4_1["options"],
                                        dob4_2["options"],
                                    ):
                                        if (
                                            SumLR(
                                                [
                                                    dob4_0_val,
                                                    dob4_1_val,
                                                    dob4_2_val,
                                                    dob4_3_val,
                                                    dob4_4_val,
                                                    dob4_5_val,
                                                ]
                                            )
                                            == 46
                                        ):
                                            # Secondlast
                                            for (
                                                dob5_0_val,
                                                dob5_1_val,
                                                dob5_2_val,
                                            ) in product(
                                                dob5_0["options"],
                                                dob5_1["options"],
                                                dob5_2["options"],
                                            ):
                                                if (
                                                    SumLR(
                                                        [
                                                            dob5_0_val,
                                                            dob5_1_val,
                                                            dob5_2_val,
                                                            dob5_3_val,
                                                            dob5_4_val,
                                                        ]
                                                    )
                                                    == 38
                                                ):
                                                    # 5 vertical
                                                    for dob1_4_val in dob1_4["options"]:
                                                        for dob2_4_val in dob2_4[
                                                            "options"
                                                        ]:
                                                            if (
                                                                SumLT(
                                                                    [
                                                                        dob1_4_val,
                                                                        dob2_4_val,
                                                                        dob3_4_val,
                                                                        dob4_3_val,
                                                                        dob5_2_val,
                                                                        dob6_1_val,
                                                                    ]
                                                                )
                                                                == 47
                                                            ):
                                                                for (
                                                                    dob0_3_val
                                                                ) in dob0_3["options"]:
                                                                    # vertical middle
                                                                    for (
                                                                        dob1_3_val
                                                                    ) in dob1_3[
                                                                        "options"
                                                                    ]:
                                                                        for (
                                                                            dob2_3_val
                                                                        ) in dob2_3[
                                                                            "options"
                                                                        ]:
                                                                            if (
                                                                                SumLT(
                                                                                    [
                                                                                        dob0_3_val,
                                                                                        dob1_3_val,
                                                                                        dob2_3_val,
                                                                                        dob3_3_val,
                                                                                        dob4_2_val,
                                                                                        dob5_1_val,
                                                                                        dob6_0_val,
                                                                                    ]
                                                                                )
                                                                                == 65
                                                                            ):
                                                                                # vertical third
                                                                                for dob0_2_val in dob0_2[
                                                                                    "options"
                                                                                ]:
                                                                                    for dob2_2_val in dob2_2[
                                                                                        "options"
                                                                                    ]:
                                                                                        if (
                                                                                            SumLT(
                                                                                                [
                                                                                                    dob0_2_val,
                                                                                                    dob1_2_val,
                                                                                                    dob2_2_val,
                                                                                                    dob3_2_val,
                                                                                                    dob4_1_val,
                                                                                                    dob5_0_val,
                                                                                                ]
                                                                                            )
                                                                                            == 45
                                                                                        ):
                                                                                            # Top row
                                                                                            for (
                                                                                                dob0_0_val,
                                                                                                dob0_1_val,
                                                                                            ) in product(
                                                                                                dob0_0[
                                                                                                    "options"
                                                                                                ],
                                                                                                dob0_1[
                                                                                                    "options"
                                                                                                ],
                                                                                            ):
                                                                                                if (
                                                                                                    SumLR(
                                                                                                        [
                                                                                                            dob0_0_val,
                                                                                                            dob0_1_val,
                                                                                                            dob0_2_val,
                                                                                                            dob0_3_val,
                                                                                                        ]
                                                                                                    )
                                                                                                    == 28
                                                                                                ):
                                                                                                    # Second row
                                                                                                    for dob1_1_val in dob1_1[
                                                                                                        "options"
                                                                                                    ]:
                                                                                                        if (
                                                                                                            SumLR(
                                                                                                                [
                                                                                                                    dob1_0_val,
                                                                                                                    dob1_1_val,
                                                                                                                    dob1_2_val,
                                                                                                                    dob1_3_val,
                                                                                                                    dob1_4_val,
                                                                                                                ]
                                                                                                            )
                                                                                                            == 39
                                                                                                        ):
                                                                                                            for dob2_0_val in dob2_0[
                                                                                                                "options"
                                                                                                            ]:
                                                                                                                for dob2_1_val in dob2_1[
                                                                                                                    "options"
                                                                                                                ]:

                                                                                                                    if (
                                                                                                                        SumLR(
                                                                                                                            [
                                                                                                                                dob2_0_val,
                                                                                                                                dob2_1_val,
                                                                                                                                dob2_2_val,
                                                                                                                                dob2_3_val,
                                                                                                                                dob2_4_val,
                                                                                                                                dob2_5_val,
                                                                                                                            ]
                                                                                                                        )
                                                                                                                        == 36
                                                                                                                    ):
                                                                                                                        # All done, just checks now
                                                                                                                        # Second vetical
                                                                                                                        if (
                                                                                                                            SumLT(
                                                                                                                                [
                                                                                                                                    dob0_1_val,
                                                                                                                                    dob1_1_val,
                                                                                                                                    dob2_1_val,
                                                                                                                                    dob3_1_val,
                                                                                                                                    dob4_0_val,
                                                                                                                                ]
                                                                                                                            )
                                                                                                                            == 30
                                                                                                                        ) and (
                                                                                                                            SumLT(  # first vertical
                                                                                                                                [
                                                                                                                                    dob0_0_val,
                                                                                                                                    dob1_0_val,
                                                                                                                                    dob2_0_val,
                                                                                                                                    dob3_0_val,
                                                                                                                                ]
                                                                                                                            )
                                                                                                                            == 29
                                                                                                                        ):
                                                                                                                            if (
                                                                                                                                SumTR(  # tr 0
                                                                                                                                    [
                                                                                                                                        dob3_0_val,
                                                                                                                                        dob4_0_val,
                                                                                                                                        dob5_0_val,
                                                                                                                                        dob6_0_val,
                                                                                                                                    ]
                                                                                                                                )
                                                                                                                                == 39
                                                                                                                                and (
                                                                                                                                    SumTR(  # tr 1
                                                                                                                                        [
                                                                                                                                            dob2_0_val,
                                                                                                                                            dob3_1_val,
                                                                                                                                            dob4_1_val,
                                                                                                                                            dob5_1_val,
                                                                                                                                            dob6_1_val,
                                                                                                                                        ]
                                                                                                                                    )
                                                                                                                                    == 38
                                                                                                                                )
                                                                                                                                and (
                                                                                                                                    SumTR(  # tr 2
                                                                                                                                        [
                                                                                                                                            dob1_0_val,
                                                                                                                                            dob2_1_val,
                                                                                                                                            dob3_2_val,
                                                                                                                                            dob4_2_val,
                                                                                                                                            dob5_2_val,
                                                                                                                                            dob6_2_val,
                                                                                                                                        ]
                                                                                                                                    )
                                                                                                                                    == 60
                                                                                                                                )
                                                                                                                                and (
                                                                                                                                    SumTR(  # tr 3
                                                                                                                                        [
                                                                                                                                            dob0_0_val,
                                                                                                                                            dob1_1_val,
                                                                                                                                            dob2_2_val,
                                                                                                                                            dob3_3_val,
                                                                                                                                            dob4_3_val,
                                                                                                                                            dob5_3_val,
                                                                                                                                            dob6_3_val,
                                                                                                                                        ]
                                                                                                                                    )
                                                                                                                                    == 52
                                                                                                                                )
                                                                                                                                and (
                                                                                                                                    SumTR(  # tr 4
                                                                                                                                        [
                                                                                                                                            dob0_1_val,
                                                                                                                                            dob1_2_val,
                                                                                                                                            dob2_3_val,
                                                                                                                                            dob3_4_val,
                                                                                                                                            dob4_4_val,
                                                                                                                                            dob5_4_val,
                                                                                                                                        ]
                                                                                                                                    )
                                                                                                                                    == 47
                                                                                                                                )
                                                                                                                                and (
                                                                                                                                    SumTR(  # tr 5
                                                                                                                                        [
                                                                                                                                            dob0_2_val,
                                                                                                                                            dob1_3_val,
                                                                                                                                            dob2_4_val,
                                                                                                                                            dob3_5_val,
                                                                                                                                            dob4_5_val,
                                                                                                                                        ]
                                                                                                                                    )
                                                                                                                                    == 43
                                                                                                                                )
                                                                                                                                and (
                                                                                                                                    SumTR(  # tr 6
                                                                                                                                        [
                                                                                                                                            dob0_3_val,
                                                                                                                                            dob1_4_val,
                                                                                                                                            dob2_5_val,
                                                                                                                                            dob3_6_val,
                                                                                                                                        ]
                                                                                                                                    )
                                                                                                                                    == 37
                                                                                                                                )
                                                                                                                            ):

                                                                                                                                tot += 1
                                                                                                                                print(
                                                                                                                                    "FOUND",
                                                                                                                                    tot,
                                                                                                                                )
                                                                                                                                print(
                                                                                                                                    "h:",
                                                                                                                                    dob0_0_val,
                                                                                                                                    dob0_1_val,
                                                                                                                                    dob0_2_val,
                                                                                                                                    dob0_3_val,
                                                                                                                                    "v:",
                                                                                                                                    dob0_0_val,
                                                                                                                                    dob1_0_val,
                                                                                                                                    dob2_0_val,
                                                                                                                                    dob3_0_val,
                                                                                                                                )

                                                                                                                                print(
                                                                                                                                    "-----------------"
                                                                                                                                )
                                                                                                                                print(
                                                                                                                                    dob0_0_val,
                                                                                                                                    dob0_1_val,
                                                                                                                                    dob0_2_val,
                                                                                                                                    dob0_3_val,
                                                                                                                                )
                                                                                                                                print(
                                                                                                                                    dob1_0_val,
                                                                                                                                    dob1_1_val,
                                                                                                                                    dob1_2_val,
                                                                                                                                    dob1_3_val,
                                                                                                                                    dob1_4_val,
                                                                                                                                )
                                                                                                                                print(
                                                                                                                                    dob2_0_val,
                                                                                                                                    dob2_1_val,
                                                                                                                                    dob2_2_val,
                                                                                                                                    dob2_3_val,
                                                                                                                                    dob2_4_val,
                                                                                                                                    dob2_5_val,
                                                                                                                                )
                                                                                                                                print(
                                                                                                                                    dob3_0_val,
                                                                                                                                    dob3_1_val,
                                                                                                                                    dob3_2_val,
                                                                                                                                    dob3_3_val,
                                                                                                                                    dob3_4_val,
                                                                                                                                    dob3_5_val,
                                                                                                                                    dob3_6_val,
                                                                                                                                )
                                                                                                                                print(
                                                                                                                                    dob4_0_val,
                                                                                                                                    dob4_1_val,
                                                                                                                                    dob4_2_val,
                                                                                                                                    dob4_3_val,
                                                                                                                                    dob4_4_val,
                                                                                                                                    dob4_5_val,
                                                                                                                                )
                                                                                                                                print(
                                                                                                                                    dob5_0_val,
                                                                                                                                    dob5_1_val,
                                                                                                                                    dob5_2_val,
                                                                                                                                    dob5_3_val,
                                                                                                                                    dob5_4_val,
                                                                                                                                )
                                                                                                                                print(
                                                                                                                                    dob6_0_val,
                                                                                                                                    dob6_1_val,
                                                                                                                                    dob6_2_val,
                                                                                                                                    dob6_3_val,
                                                                                                                                )
                                                                                                                                print(
                                                                                                                                    "-----------------"
                                                                                                                                )




