'''
下面我们做文本解析,首先已经通过ocr_byzhang这个算法镜像,得到了tmp.jpg这个图片的所有文本信息.

下面进行段落拼接.

https://cloud.tencent.com/act/pro/AI?fromSource=gwzcw.3177853.3177853.3177853&utm_medium=cpc&utm_id=gwzcw.3177853.3177853.3177853
下面给用腾讯的ocr api

在下面试用的框中上传本地图片tmp.jpg, 就会在response里面得到需要的jason文件.
也就是下面的shuru这个字符串.
'''


##


# 超参数
#

jingdu=0.2
jiangexishu=0.5



#下面是解析后的大字典.

shuru={
  "TextDetections": [
    {
      "DetectedText": "100",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 338,
          "Y": 443
        },
        {
          "X": 395,
          "Y": 443
        },
        {
          "X": 395,
          "Y": 485
        },
        {
          "X": 338,
          "Y": 485
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Tem peraure Cycling",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1615,
          "Y": 467
        },
        {
          "X": 1884,
          "Y": 467
        },
        {
          "X": 1884,
          "Y": 498
        },
        {
          "X": 1615,
          "Y": 498
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "Thermal Cycle:",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 434,
          "Y": 494
        },
        {
          "X": 665,
          "Y": 494
        },
        {
          "X": 665,
          "Y": 527
        },
        {
          "X": 434,
          "Y": 527
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "233+ -➢398K",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 455,
          "Y": 532
        },
        {
          "X": 712,
          "Y": 532
        },
        {
          "X": 712,
          "Y": 564
        },
        {
          "X": 455,
          "Y": 564
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":5}}"
    },
    {
      "DetectedText": "Variable",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1967,
          "Y": 534
        },
        {
          "X": 2061,
          "Y": 534
        },
        {
          "X": 2061,
          "Y": 560
        },
        {
          "X": 1967,
          "Y": 560
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "80",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 319,
          "Y": 578
        },
        {
          "X": 407,
          "Y": 578
        },
        {
          "X": 407,
          "Y": 627
        },
        {
          "X": 319,
          "Y": 627
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Sn-xAg-0.5Cu",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 436,
          "Y": 572
        },
        {
          "X": 673,
          "Y": 572
        },
        {
          "X": 673,
          "Y": 610
        },
        {
          "X": 436,
          "Y": 610
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":6}}"
    },
    {
      "DetectedText": "SAC105",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1970,
          "Y": 566
        },
        {
          "X": 2059,
          "Y": 566
        },
        {
          "X": 2059,
          "Y": 593
        },
        {
          "X": 1970,
          "Y": 593
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "-0.5Cu",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 559,
          "Y": 586
        },
        {
          "X": 655,
          "Y": 586
        },
        {
          "X": 655,
          "Y": 630
        },
        {
          "X": 559,
          "Y": 630
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":7}}"
    },
    {
      "DetectedText": "SACO307",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 1981,
          "Y": 599
        },
        {
          "X": 2080,
          "Y": 599
        },
        {
          "X": 2080,
          "Y": 631
        },
        {
          "X": 1981,
          "Y": 631
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "Cu pad",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 426,
          "Y": 619
        },
        {
          "X": 546,
          "Y": 619
        },
        {
          "X": 546,
          "Y": 661
        },
        {
          "X": 426,
          "Y": 661
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":7}}"
    },
    {
      "DetectedText": "? 6(",
      "Confidence": 58,
      "Polygon": [
        {
          "X": 295,
          "Y": 705
        },
        {
          "X": 368,
          "Y": 705
        },
        {
          "X": 368,
          "Y": 753
        },
        {
          "X": 295,
          "Y": 753
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "No failures to",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1746,
          "Y": 714
        },
        {
          "X": 1968,
          "Y": 714
        },
        {
          "X": 1968,
          "Y": 758
        },
        {
          "X": 1746,
          "Y": 758
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "20",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1395,
          "Y": 751
        },
        {
          "X": 1436,
          "Y": 751
        },
        {
          "X": 1436,
          "Y": 791
        },
        {
          "X": 1395,
          "Y": 791
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":13}}"
    },
    {
      "DetectedText": "date for both",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1748,
          "Y": 771
        },
        {
          "X": 1966,
          "Y": 771
        },
        {
          "X": 1966,
          "Y": 808
        },
        {
          "X": 1748,
          "Y": 808
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "SACX and",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1763,
          "Y": 815
        },
        {
          "X": 1951,
          "Y": 815
        },
        {
          "X": 1951,
          "Y": 854
        },
        {
          "X": 1763,
          "Y": 854
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "SAC305",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1785,
          "Y": 862
        },
        {
          "X": 1926,
          "Y": 862
        },
        {
          "X": 1926,
          "Y": 903
        },
        {
          "X": 1785,
          "Y": 903
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "4500",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1577,
          "Y": 929
        },
        {
          "X": 1619,
          "Y": 929
        },
        {
          "X": 1619,
          "Y": 954
        },
        {
          "X": 1577,
          "Y": 954
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "5000",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1717,
          "Y": 933
        },
        {
          "X": 1783,
          "Y": 933
        },
        {
          "X": 1783,
          "Y": 956
        },
        {
          "X": 1717,
          "Y": 956
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":16}}"
    },
    {
      "DetectedText": "●1Ag",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 935,
          "Y": 942
        },
        {
          "X": 1034,
          "Y": 942
        },
        {
          "X": 1034,
          "Y": 985
        },
        {
          "X": 935,
          "Y": 985
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "Cycles",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1730,
          "Y": 955
        },
        {
          "X": 1803,
          "Y": 955
        },
        {
          "X": 1803,
          "Y": 984
        },
        {
          "X": 1730,
          "Y": 984
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "20",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 319,
          "Y": 975
        },
        {
          "X": 368,
          "Y": 975
        },
        {
          "X": 368,
          "Y": 1018
        },
        {
          "X": 319,
          "Y": 1018
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
    },
    {
      "DetectedText": "园2Ag",
      "Confidence": 90,
      "Polygon": [
        {
          "X": 932,
          "Y": 985
        },
        {
          "X": 1035,
          "Y": 985
        },
        {
          "X": 1035,
          "Y": 1027
        },
        {
          "X": 932,
          "Y": 1027
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "◆3Ag",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 933,
          "Y": 1029
        },
        {
          "X": 1033,
          "Y": 1029
        },
        {
          "X": 1033,
          "Y": 1068
        },
        {
          "X": 933,
          "Y": 1068
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "Figure 18: Temperature cycling test of SAC",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1017
        },
        {
          "X": 2300,
          "Y": 1017
        },
        {
          "X": 2300,
          "Y": 1064
        },
        {
          "X": 1313,
          "Y": 1064
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "▼4Ag",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 938,
          "Y": 1067
        },
        {
          "X": 1031,
          "Y": 1067
        },
        {
          "X": 1031,
          "Y": 1108
        },
        {
          "X": 938,
          "Y": 1108
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "alloys. All common low-Ag SAC alloys fail",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1312,
          "Y": 1075
        },
        {
          "X": 2292,
          "Y": 1075
        },
        {
          "X": 2292,
          "Y": 1119
        },
        {
          "X": 1312,
          "Y": 1119
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "200",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 537,
          "Y": 1147
        },
        {
          "X": 594,
          "Y": 1147
        },
        {
          "X": 594,
          "Y": 1185
        },
        {
          "X": 537,
          "Y": 1185
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "400",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 679,
          "Y": 1150
        },
        {
          "X": 760,
          "Y": 1150
        },
        {
          "X": 760,
          "Y": 1188
        },
        {
          "X": 679,
          "Y": 1188
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "600 .",
      "Confidence": 67,
      "Polygon": [
        {
          "X": 839,
          "Y": 1152
        },
        {
          "X": 925,
          "Y": 1152
        },
        {
          "X": 925,
          "Y": 1193
        },
        {
          "X": 839,
          "Y": 1193
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "800",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1033,
          "Y": 1152
        },
        {
          "X": 1117,
          "Y": 1152
        },
        {
          "X": 1117,
          "Y": 1188
        },
        {
          "X": 1033,
          "Y": 1188
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "around 4,000 cycles. However, SACX and",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1310,
          "Y": 1133
        },
        {
          "X": 2297,
          "Y": 1133
        },
        {
          "X": 2297,
          "Y": 1176
        },
        {
          "X": 1310,
          "Y": 1176
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "SAC305 show no failure up to 6, 500 cycles.",
      "Confidence": 80,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1188
        },
        {
          "X": 2244,
          "Y": 1188
        },
        {
          "X": 2244,
          "Y": 1232
        },
        {
          "X": 1313,
          "Y": 1232
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "Thermal Cycle, N (Cycle)",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 561,
          "Y": 1214
        },
        {
          "X": 955,
          "Y": 1214
        },
        {
          "X": 955,
          "Y": 1258
        },
        {
          "X": 561,
          "Y": 1258
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "Figure 17: Temperature cycling test data",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 217,
          "Y": 1270
        },
        {
          "X": 1202,
          "Y": 1270
        },
        {
          "X": 1202,
          "Y": 1316
        },
        {
          "X": 217,
          "Y": 1316
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":10}}"
    },
    {
      "DetectedText": "In addition to exhibiting exceptional",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1475,
          "Y": 1306
        },
        {
          "X": 2295,
          "Y": 1306
        },
        {
          "X": 2295,
          "Y": 1350
        },
        {
          "X": 1475,
          "Y": 1350
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "from Terashima et al [9] showing the direct",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 215,
          "Y": 1328
        },
        {
          "X": 1204,
          "Y": 1328
        },
        {
          "X": 1204,
          "Y": 1374
        },
        {
          "X": 215,
          "Y": 1374
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":10}}"
    },
    {
      "DetectedText": "relationship between Ag content and thermal",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 219,
          "Y": 1383
        },
        {
          "X": 1202,
          "Y": 1383
        },
        {
          "X": 1202,
          "Y": 1427
        },
        {
          "X": 219,
          "Y": 1427
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":10}}"
    },
    {
      "DetectedText": "temperature cycling performance, drop-shock",
      "Confidence": 92,
      "Polygon": [
        {
          "X": 1312,
          "Y": 1364
        },
        {
          "X": 2298,
          "Y": 1364
        },
        {
          "X": 2298,
          "Y": 1407
        },
        {
          "X": 1312,
          "Y": 1407
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "results of the SACX alloy have also been",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 1310,
          "Y": 1416
        },
        {
          "X": 2301,
          "Y": 1416
        },
        {
          "X": 2301,
          "Y": 1460
        },
        {
          "X": 1310,
          "Y": 1460
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "fatigue life.",
      "Confidence": 92,
      "Polygon": [
        {
          "X": 220,
          "Y": 1438
        },
        {
          "X": 448,
          "Y": 1438
        },
        {
          "X": 448,
          "Y": 1484
        },
        {
          "X": 220,
          "Y": 1484
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":10}}"
    },
    {
      "DetectedText": "confirmed.",
      "Confidence": 95,
      "Polygon": [
        {
          "X": 1314,
          "Y": 1473
        },
        {
          "X": 1529,
          "Y": 1473
        },
        {
          "X": 1529,
          "Y": 1513
        },
        {
          "X": 1314,
          "Y": 1513
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "n our internal testing we started",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 384,
          "Y": 1552
        },
        {
          "X": 1204,
          "Y": 1552
        },
        {
          "X": 1204,
          "Y": 1593
        },
        {
          "X": 384,
          "Y": 1593
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":11}}"
    },
    {
      "DetectedText": "To understand how alloy additives",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1439,
          "Y": 1585
        },
        {
          "X": 2299,
          "Y": 1585
        },
        {
          "X": 2299,
          "Y": 1629
        },
        {
          "X": 1439,
          "Y": 1629
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "temperature cycling test on selected low Ag",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 216,
          "Y": 1606
        },
        {
          "X": 1203,
          "Y": 1606
        },
        {
          "X": 1203,
          "Y": 1654
        },
        {
          "X": 216,
          "Y": 1654
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "affect drop shock and temperature cycling",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1315,
          "Y": 1640
        },
        {
          "X": 2301,
          "Y": 1640
        },
        {
          "X": 2301,
          "Y": 1686
        },
        {
          "X": 1315,
          "Y": 1686
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "alloys. Test was run a six layer boards, each",
      "Confidence": 80,
      "Polygon": [
        {
          "X": 217,
          "Y": 1664
        },
        {
          "X": 1203,
          "Y": 1664
        },
        {
          "X": 1203,
          "Y": 1706
        },
        {
          "X": 217,
          "Y": 1706
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "performance, it is important understand their",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1309,
          "Y": 1692
        },
        {
          "X": 2299,
          "Y": 1692
        },
        {
          "X": 2299,
          "Y": 1741
        },
        {
          "X": 1309,
          "Y": 1741
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "vith 15 daisy chained dummy BGA84",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 238,
          "Y": 1714
        },
        {
          "X": 1207,
          "Y": 1714
        },
        {
          "X": 1207,
          "Y": 1762
        },
        {
          "X": 238,
          "Y": 1762
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "effect on bulk alloy properties. Comparing",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1751
        },
        {
          "X": 2297,
          "Y": 1751
        },
        {
          "X": 2297,
          "Y": 1795
        },
        {
          "X": 1313,
          "Y": 1795
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "components.",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 216,
          "Y": 1771
        },
        {
          "X": 487,
          "Y": 1771
        },
        {
          "X": 487,
          "Y": 1818
        },
        {
          "X": 216,
          "Y": 1818
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "Components have NiAu",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 609,
          "Y": 1768
        },
        {
          "X": 1196,
          "Y": 1768
        },
        {
          "X": 1196,
          "Y": 1820
        },
        {
          "X": 609,
          "Y": 1820
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "surface finish and each was assembled with",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 218,
          "Y": 1829
        },
        {
          "X": 1205,
          "Y": 1829
        },
        {
          "X": 1205,
          "Y": 1873
        },
        {
          "X": 218,
          "Y": 1873
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "the alloy microstructure [5-7] is one tool to",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1317,
          "Y": 1808
        },
        {
          "X": 2300,
          "Y": 1808
        },
        {
          "X": 2300,
          "Y": 1853
        },
        {
          "X": 1317,
          "Y": 1853
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "12mil spheres with a water soluble BGA flux",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 217,
          "Y": 1884
        },
        {
          "X": 1206,
          "Y": 1884
        },
        {
          "X": 1206,
          "Y": 1933
        },
        {
          "X": 217,
          "Y": 1933
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "understand how these alloys will behave in",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1311,
          "Y": 1866
        },
        {
          "X": 2298,
          "Y": 1866
        },
        {
          "X": 2298,
          "Y": 1910
        },
        {
          "X": 1311,
          "Y": 1910
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "actual performance tests.",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 1312,
          "Y": 1922
        },
        {
          "X": 1891,
          "Y": 1922
        },
        {
          "X": 1891,
          "Y": 1968
        },
        {
          "X": 1312,
          "Y": 1968
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "Representative",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1972,
          "Y": 1921
        },
        {
          "X": 2300,
          "Y": 1921
        },
        {
          "X": 2300,
          "Y": 1970
        },
        {
          "X": 1972,
          "Y": 1970
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "WSX. Surface finish on board side was Cu-",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 219,
          "Y": 1939
        },
        {
          "X": 1205,
          "Y": 1939
        },
        {
          "X": 1205,
          "Y": 1987
        },
        {
          "X": 219,
          "Y": 1987
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "OSP. Since the intent was to understand the",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 218,
          "Y": 1995
        },
        {
          "X": 1205,
          "Y": 1995
        },
        {
          "X": 1205,
          "Y": 2042
        },
        {
          "X": 218,
          "Y": 2042
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "alloy samples were micro-sectioned and SEM",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1312,
          "Y": 1974
        },
        {
          "X": 2299,
          "Y": 1974
        },
        {
          "X": 2299,
          "Y": 2020
        },
        {
          "X": 1312,
          "Y": 2020
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "alloy behavior, we used the same water",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 228,
          "Y": 2050
        },
        {
          "X": 1198,
          "Y": 2050
        },
        {
          "X": 1198,
          "Y": 2097
        },
        {
          "X": 228,
          "Y": 2097
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "images recorded. In some cases, EDAX was",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2033
        },
        {
          "X": 2295,
          "Y": 2033
        },
        {
          "X": 2295,
          "Y": 2076
        },
        {
          "X": 1313,
          "Y": 2076
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "soluble BGA flux to assemble the boards as",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 218,
          "Y": 2111
        },
        {
          "X": 1197,
          "Y": 2111
        },
        {
          "X": 1197,
          "Y": 2154
        },
        {
          "X": 218,
          "Y": 2154
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "used to map the element distribution.",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1311,
          "Y": 2088
        },
        {
          "X": 2127,
          "Y": 2088
        },
        {
          "X": 2127,
          "Y": 2133
        },
        {
          "X": 1311,
          "Y": 2133
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "well instead of using a solder paste. Alloys",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 217,
          "Y": 2166
        },
        {
          "X": 1205,
          "Y": 2166
        },
        {
          "X": 1205,
          "Y": 2213
        },
        {
          "X": 217,
          "Y": 2213
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "included in this test were SAC305 (control),",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 217,
          "Y": 2222
        },
        {
          "X": 1202,
          "Y": 2222
        },
        {
          "X": 1202,
          "Y": 2267
        },
        {
          "X": 217,
          "Y": 2267
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "SAC105,",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 221,
          "Y": 2277
        },
        {
          "X": 401,
          "Y": 2277
        },
        {
          "X": 401,
          "Y": 2323
        },
        {
          "X": 221,
          "Y": 2323
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "SAC0307,",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 488,
          "Y": 2275
        },
        {
          "X": 707,
          "Y": 2275
        },
        {
          "X": 707,
          "Y": 2321
        },
        {
          "X": 488,
          "Y": 2321
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "SAC105+Ni",
      "Confidence": 96,
      "Polygon": [
        {
          "X": 790,
          "Y": 2270
        },
        {
          "X": 1046,
          "Y": 2270
        },
        {
          "X": 1046,
          "Y": 2321
        },
        {
          "X": 790,
          "Y": 2321
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "and",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1127,
          "Y": 2281
        },
        {
          "X": 1207,
          "Y": 2281
        },
        {
          "X": 1207,
          "Y": 2321
        },
        {
          "X": 1127,
          "Y": 2321
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "SAC0307+Bi",
      "Confidence": 96,
      "Polygon": [
        {
          "X": 1433,
          "Y": 2263
        },
        {
          "X": 1601,
          "Y": 2263
        },
        {
          "X": 1601,
          "Y": 2290
        },
        {
          "X": 1433,
          "Y": 2290
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":24}}"
    },
    {
      "DetectedText": "SAC105+Bi",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1744,
          "Y": 2266
        },
        {
          "X": 1890,
          "Y": 2266
        },
        {
          "X": 1890,
          "Y": 2295
        },
        {
          "X": 1744,
          "Y": 2295
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":25}}"
    },
    {
      "DetectedText": "SACX0307 (SAC0307+0.1Bi). The test",
      "Confidence": 90,
      "Polygon": [
        {
          "X": 218,
          "Y": 2328
        },
        {
          "X": 1205,
          "Y": 2328
        },
        {
          "X": 1205,
          "Y": 2376
        },
        {
          "X": 218,
          "Y": 2376
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "results to date are shown in figure 18. Most of",
      "Confidence": 79,
      "Polygon": [
        {
          "X": 217,
          "Y": 2392
        },
        {
          "X": 1205,
          "Y": 2392
        },
        {
          "X": 1205,
          "Y": 2434
        },
        {
          "X": 217,
          "Y": 2434
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "the low-Ag alloys such as SAC0307 and",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 218,
          "Y": 2446
        },
        {
          "X": 1204,
          "Y": 2446
        },
        {
          "X": 1204,
          "Y": 2491
        },
        {
          "X": 218,
          "Y": 2491
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "SAC105 fail around 4,000 cycles. However,",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 219,
          "Y": 2498
        },
        {
          "X": 1196,
          "Y": 2498
        },
        {
          "X": 1196,
          "Y": 2549
        },
        {
          "X": 219,
          "Y": 2549
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "high silver alloys (SAC305) used as control",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 219,
          "Y": 2555
        },
        {
          "X": 1202,
          "Y": 2555
        },
        {
          "X": 1202,
          "Y": 2604
        },
        {
          "X": 219,
          "Y": 2604
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "SAC0307",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 1449,
          "Y": 2554
        },
        {
          "X": 1577,
          "Y": 2554
        },
        {
          "X": 1577,
          "Y": 2585
        },
        {
          "X": 1449,
          "Y": 2585
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":26}}"
    },
    {
      "DetectedText": "SAC105",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1752,
          "Y": 2549
        },
        {
          "X": 1868,
          "Y": 2549
        },
        {
          "X": 1868,
          "Y": 2583
        },
        {
          "X": 1752,
          "Y": 2583
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":27}}"
    },
    {
      "DetectedText": "SAC305",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 2064,
          "Y": 2553
        },
        {
          "X": 2177,
          "Y": 2553
        },
        {
          "X": 2177,
          "Y": 2583
        },
        {
          "X": 2064,
          "Y": 2583
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":28}}"
    },
    {
      "DetectedText": "has shown no failure until 6, 500 cycles. Also",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 216,
          "Y": 2610
        },
        {
          "X": 1184,
          "Y": 2610
        },
        {
          "X": 1184,
          "Y": 2656
        },
        {
          "X": 216,
          "Y": 2656
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "the SACX alloy (Cookson Electronics' Bi-",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 199,
          "Y": 2667
        },
        {
          "X": 1194,
          "Y": 2667
        },
        {
          "X": 1194,
          "Y": 2713
        },
        {
          "X": 199,
          "Y": 2713
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "containing SAC0307 alloy) has not shown",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 216,
          "Y": 2725
        },
        {
          "X": 1202,
          "Y": 2725
        },
        {
          "X": 1202,
          "Y": 2770
        },
        {
          "X": 216,
          "Y": 2770
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "any failure so far. SAC0307 without Bi has",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 218,
          "Y": 2780
        },
        {
          "X": 1205,
          "Y": 2780
        },
        {
          "X": 1205,
          "Y": 2825
        },
        {
          "X": 218,
          "Y": 2825
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "failed around 4,000 cycles just like all other",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 216,
          "Y": 2836
        },
        {
          "X": 1202,
          "Y": 2836
        },
        {
          "X": 1202,
          "Y": 2887
        },
        {
          "X": 216,
          "Y": 2887
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "Figure 19: Microstructure of SAC alloys,",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1373,
          "Y": 2834
        },
        {
          "X": 2292,
          "Y": 2834
        },
        {
          "X": 2292,
          "Y": 2879
        },
        {
          "X": 1373,
          "Y": 2879
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":29}}"
    },
    {
      "DetectedText": "low-Ag SAC alloys.",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 218,
          "Y": 2893
        },
        {
          "X": 624,
          "Y": 2893
        },
        {
          "X": 624,
          "Y": 2937
        },
        {
          "X": 218,
          "Y": 2937
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "with and without Bi addition.",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1368,
          "Y": 2888
        },
        {
          "X": 1964,
          "Y": 2888
        },
        {
          "X": 1964,
          "Y": 2932
        },
        {
          "X": 1368,
          "Y": 2932
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":31}}"
    }
  ],
  "Language": "zh",
  "RequestId": "af61e098-e1db-4221-84fe-b012c4b2aea5"
}

data=shuru["TextDetections"]




'''
下面写主要的算法.
'''

# 看到用任何的ocr都会出现,因为句子里面短语之间间隔过大,而出现把一个段落中的话跟话之间拆开的现象

#所以我们用并查集来做这个处理.

# ocr之后得到一堆box,,  假设box1,.......boxn.


# 如果box之间贴的比较近.这个比较近需要给出几何上的刻画.那么就说他们是相同门派的.
# 然后用56565.py里面给出的并查集算法.得到所有的门派分类.    其实门派也就是我们问题中的
#     段落的概念.


# 下面我们就给出box之间接近的刻画函即可!


#还是要先算出平均的字高和平均的段落水平间隔.

zigao=None
duanluoshuiping=None




test=data[0]





save=[]
for i in data:
     y2=(i['Polygon'][2]['Y']+i['Polygon'][3]['Y'])/2
     y1=(i['Polygon'][1]['Y']+i['Polygon'][0]['Y'])/2
     save.append(y2-y1)

zigao=sum(save)/len(save)
print(zigao)



# 如果两个box 水平差别不大, 在正负  zigao/5 以内就判定为同一条直线上的文字.这样取他们横间隔
# 作为段落的间隔即可! 下面实现一下看看跟真实图片的差别大不.




# 注意下面i或者j 只计算一遍.因为同一行 如果分成3个部分,那么没必要算第一个部分和第三个部分的间隔.



# 其中rate 表示pdf 行之间没有对其的比例:

rate=0.4
jilu666=[]
jiange=[]
left=[]
right=[]
for i in range(len(data)):
  for j in range(i+1,len(data)):
     if j==i:
       continue
     tmp1=data[i]['Polygon']
     tmp2=data[j]['Polygon']


     y2=(tmp1[2]['Y']+tmp1[3]['Y'])/2
     y1=(tmp1[1]['Y']+tmp1[0]['Y'])/2
     ypingjun1=((y2+y1)/2)

     y2 = (tmp2[2]['Y'] + tmp2[3]['Y']) / 2
     y1 = (tmp2[1]['Y'] + tmp2[0]['Y']) / 2
     ypingjun2 = ((y2 + y1) / 2)

     tmp=[]
     if ypingjun1-ypingjun2  > -zigao*rate and ypingjun1-ypingjun2  < zigao*rate:
        if i in left or j in right:
          continue

        left.append(i)
        right.append(j)
        tmp.append((tmp1[0]['X']+tmp1[3]['X'])/2)
        tmp.append((tmp1[1]['X']+tmp1[2]['X'])/2)
        tmp.append((tmp2[0]['X']+tmp2[3]['X'])/2)
        tmp.append((tmp2[1]['X']+tmp2[2]['X'])/2)
        tmp=sorted(tmp)
        jiange.append(tmp[2]-tmp[1])
        jilu666.append((i,j))


def checkBoxtonghang(i,j):
  tmp1 = data[i]['Polygon']
  tmp2 = data[j]['Polygon']

  y2 = (tmp1[2]['Y'] + tmp1[3]['Y']) / 2
  y1 = (tmp1[1]['Y'] + tmp1[0]['Y']) / 2
  ypingjun1 = ((y2 + y1) / 2)

  y2 = (tmp2[2]['Y'] + tmp2[3]['Y']) / 2
  y1 = (tmp2[1]['Y'] + tmp2[0]['Y']) / 2
  ypingjun2 = ((y2 + y1) / 2)

  tmp = []
  if ypingjun1 - ypingjun2 > -zigao * rate and ypingjun1 - ypingjun2 < zigao * rate:
        return True
  return False







print("处理前间隔表",jiange)
print("间隔表对应的data中index对",jilu666)

# 去掉过大的百分之20. 过大时因为图片中的文本也识别出来了.还有图片的附带文字这2个导致.


print("处理后间隔表")
jiange=sorted(jiange)
jiange=jiange[int(len(jiange)*0.2):int(len(jiange)*0.8)]

print(jiange)
duanluojiange=None

# 经过实践,duanluojiange 尽量算小一点.这样效果更好. 因为更严格了.


duanluojiange=sum(jiange)/len(jiange)
duanluojiange*=jiangexishu

# 看看如何用图像方法,得到中见空白区域的宽度,这里面先用zigao*1.5来近似用.
duanluojiange=zigao*1.5





#下面这个指标就作为段落横间隔.


# 用上面2个指标来给出box之间是否在同一个段落的指标函数.


# 两个box ,如果横坐标间隔比  duanluojiange 小,并且在同一个水平线上,那么他们就是同一个门派

def panding(box1,box2):
    #为了统一,,
# box 是[{'X': 219, 'Y': 449}, {'X': 530, 'Y': 449}, {'X': 530, 'Y': 496}, {'X': 219, 'Y': 496}]    是一个数组.
    tmp1=box1
    tmp2=box2
    y2 = (tmp1[2]['Y'] + tmp1[3]['Y']) / 2
    y1 = (tmp1[1]['Y'] + tmp1[0]['Y']) / 2
    ypingjun1 = ((y2 + y1) / 2)

    y2 = (tmp2[2]['Y'] + tmp2[3]['Y']) / 2
    y1 = (tmp2[1]['Y'] + tmp2[0]['Y']) / 2
    ypingjun2 = ((y2 + y1) / 2)

    #如果box1, box2 在同一行,同一个段落.
    if ypingjun1 - ypingjun2 > -zigao * rate and ypingjun1 - ypingjun2 < zigao * rate:
      tmp=[]

      tmp.append((tmp1[0]['X'] + tmp1[3]['X']) / 2)
      tmp.append((tmp1[1]['X'] + tmp1[2]['X']) / 2)
      tmp.append((tmp2[0]['X'] + tmp2[3]['X']) / 2)
      tmp.append((tmp2[1]['X'] + tmp2[2]['X']) / 2)
      tmp = sorted(tmp)
      a=tmp[2] - tmp[1]
      if a<=duanluojiange:
        return True



    # 如果box1, box2 是上下行.
    # 第一个box 的上下线.
    y2 = (tmp1[2]['Y'] + tmp1[3]['Y']) / 2    # 下线
    y1 = (tmp1[1]['Y'] + tmp1[0]['Y']) / 2  # 上线


    y22 = (tmp2[2]['Y'] + tmp2[3]['Y']) / 2   #下线
    y11 = (tmp2[1]['Y'] + tmp2[0]['Y']) / 2  #上线
    tmp34=[]
    tmp34.append(y2)
    tmp34.append(y1)
    tmp34.append(y22)
    tmp34.append(y11)
    tmp34=sorted(tmp34)
    if tmp34[2]-tmp34[1]<zigao*0.5:
      tmp=[]

      a1=((tmp1[0]['X'] + tmp1[3]['X']) / 2)
      a2=((tmp1[1]['X'] + tmp1[2]['X']) / 2)
      a3=((tmp2[0]['X'] + tmp2[3]['X']) / 2)
      a4=((tmp2[1]['X'] + tmp2[2]['X']) / 2)
      # 让2个线有重合部分. 求线 a1 到a2   和线 a3到a4 的重合部分.
      t= min(a2,a4) -max(a1,a3)
      if t>zigao*0.5:
        return True









    return False



# 下面直接写入并查集数据结构中.
import  bingcha
tmp=bingcha.DIS_JOIN()
tmp.clear(len(data))
for i in range(len(data)):
  for j in range(len(data)):

     if i==j:
       continue
     tmp1=data[i]['Polygon']
     tmp2=data[j]['Polygon']

     if panding(tmp1,tmp2):
       tmp.join(i,j)

tmp=tmp.get_set()





'''
[array([ 0,  1,  3,  5,  7,  8, 10, 12, 13, 15, 17, 19, 21, 23, 24, 26, 28,
       29, 30, 31, 32, 36, 40, 41, 42, 43, 44]), array([ 2,  4,  6,  9, 11, 14, 16, 18, 20, 22, 25, 27]), array([33, 37]), array([34, 38]), array([35, 39]), array([45]), array([46]), array([47]), array([48]), array([49]), array([50, 51, 52, 54]), array([53]), array([55, 56, 57, 59, 61, 63, 65, 66, 68, 70, 72, 74, 76, 77, 79, 82, 86,
       89, 91, 93]), array([58, 60, 62, 64]), array([67, 69, 71, 73, 75, 78, 80, 81, 83, 84, 85, 87, 88, 90, 92])]
       
       
       这个结果基本实现了聚类.
'''


# 下面进行可视化,看聚类结果.




import cv2
import matplotlib.pyplot as plt
import numpy




# 当一个门派里面的字符太少的时候就删除这个门派!



menpaistr=''
savetmp=[]
for i in tmp:
  menpaistr = ''

  # 目前想到的方法是对当前门派里面box, 找最左边2个box,他们起始文字是figure,那么就不要这个门派.
  tmp888 = []
  for j in i:


     tmp888.append((data[j]['Polygon'][0]['X'],j))
     # paixu
  tmp888=sorted(tmp888,key=lambda x:x[0])
  # print(tmp888,99999999999999999)






  for j in i:
    menpaistr+=data[j]['DetectedText']



  if len(menpaistr)>50 and menpaistr[:6]!="Figure":  # 这个地方还需要精细判断!!!!!!!!!!!!



    # 目前想到的方法是对当前门派里面box, 找最左边2个box,他们起始文字是figure,那么就不要这个门派.
    savetmp.append(i)




savetmp2=[]
for i in savetmp:


  # 目前想到的方法是对当前门派里面box, 找最左边2个box,他们起始文字是figure,那么就不要这个门派.
  tmp888 = []
  for j in i:


     tmp888.append((data[j]['Polygon'][0]['X'],j))
     # paixu
  tmp888=sorted(tmp888,key=lambda x:x[0])
  # print(tmp888,99999999999999999)




  def check(tmp888):
        if len(tmp888) == 2:

          if data[tmp888[0][1]]['DetectedText'][:6] != "Figure" and data[tmp888[1][1]]['DetectedText'][:6] != "Figure":
            return True        # 表示是一个好的段落.
        if len(tmp888) < 2:
          if data[tmp888[0][1]]['DetectedText'][:6] != "Figure":
            return True


        # 如果是注释,那么他一定会在前几个字符上写上Figure,并且是一行的头.
    # 也就是与带figure同行的没有比他x坐标小的.
        def check2(biaohao,tmp888):
          genbiaohaotonghangde=[]
          for j in tmp888:
            biaohao2=j[1]
            if checkBoxtonghang(biaohao,biaohao2):
              genbiaohaotonghangde.append(biaohao2)
          hang = []
          for biaohao2 in genbiaohaotonghangde:
            if biaohao==biaohao2:
              continue

            hang.append(data[biaohao2]['Polygon'][0]['X'])
          if hang!=[]:
           minhang=min(hang)
          else:
            minhang=99999



          if  data[biaohao]['Polygon'][0]['X']<minhang:
                 return False  # 说明bu是门派
          return True




        for i in tmp888:
          biaohao=i[1]
          if data[biaohao]['DetectedText'][:6]=="Figure":
            if check2(biaohao,tmp888)==False:
              return False

        return True



  if check(tmp888):
    savetmp2.append(i)



print(savetmp2,9999999999999999)
savetmp=savetmp2


im = cv2.imread('77.Jpeg')
print("处理之后的切片,分块信息")
print("段落细节",savetmp)
print("段落总数",len(savetmp))
print(duanluojiange,"段落间隔值")
for i in savetmp[0]:

  cv2.rectangle(im, (data[i]['Polygon'][0]['X'], data[i]['Polygon'][0]['Y']), (data[i]['Polygon'][2]['X'], data[i]['Polygon'][2]['Y']), (1,1,1), 5)

cv2.imwrite("88888.png",im)










'''
下面在图片中删除这6块即可.

当然想直接把里面各个图片抽出来,但是图片如果紧贴文档的边缘,那么就不好知道应该切的范围了.
'''

# 找到能把门派全包含的矩形.



##
for tmp in savetmp:

  xmin,xmax,ymin,ymax=9999,0,9999,0
  for i in tmp:
    a=data[i]['Polygon']
    for j in range(4):
       xmin=min(xmin,a[j]['X'])
       ymin=min(ymin,a[j]['Y'])
       xmax=max(xmax,a[j]['X'])
       ymax=max(ymax,a[j]['Y'])
  #稍微括一点,因为腾讯ocr框不准.
  xmin-=zigao*0.1
  ymin-=zigao*0.1
  xmax+=zigao*0.1
  ymax+=zigao*0.1
  xmin=int(xmin)
  ymin=int(ymin)
  xmax=int(xmax)
  ymax=int(ymax)

  cv2.rectangle(im,(xmin,ymin),(xmax,ymax),(255,255,255),-1)#-1表示的是填充矩形的意思
































cv2.imwrite("new.png",im)


