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
tupiandizhi='test2.jpg'               # 这个是图片地址
shuru={
  "TextDetections": [
    {
      "DetectedText": "corresponds to high silver and medium",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 216,
          "Y": 452
        },
        {
          "X": 1202,
          "Y": 452
        },
        {
          "X": 1202,
          "Y": 495
        },
        {
          "X": 216,
          "Y": 495
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": ". SAC305",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1952,
          "Y": 493
        },
        {
          "X": 2038,
          "Y": 493
        },
        {
          "X": 2038,
          "Y": 519
        },
        {
          "X": 1952,
          "Y": 519
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "copper level SAC alloys and consists of liquid",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 216,
          "Y": 507
        },
        {
          "X": 1204,
          "Y": 507
        },
        {
          "X": 1204,
          "Y": 552
        },
        {
          "X": 216,
          "Y": 552
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "o-",
      "Confidence": 74,
      "Polygon": [
        {
          "X": 1387,
          "Y": 516
        },
        {
          "X": 1436,
          "Y": 516
        },
        {
          "X": 1436,
          "Y": 548
        },
        {
          "X": 1387,
          "Y": 548
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
    },
    {
      "DetectedText": "SAC105",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1953,
          "Y": 526
        },
        {
          "X": 2047,
          "Y": 526
        },
        {
          "X": 2047,
          "Y": 552
        },
        {
          "X": 1953,
          "Y": 552
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "SAC0307",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1954,
          "Y": 555
        },
        {
          "X": 2055,
          "Y": 555
        },
        {
          "X": 2055,
          "Y": 581
        },
        {
          "X": 1954,
          "Y": 581
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "phase along with Ag3Sn intermetallic solid",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 219,
          "Y": 562
        },
        {
          "X": 1204,
          "Y": 562
        },
        {
          "X": 1204,
          "Y": 608
        },
        {
          "X": 219,
          "Y": 608
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "phase.",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 217,
          "Y": 617
        },
        {
          "X": 355,
          "Y": 617
        },
        {
          "X": 355,
          "Y": 659
        },
        {
          "X": 217,
          "Y": 659
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Shaded section to the right",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 465,
          "Y": 615
        },
        {
          "X": 1206,
          "Y": 615
        },
        {
          "X": 1206,
          "Y": 659
        },
        {
          "X": 465,
          "Y": 659
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "corresponds to medium range Ag and high",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 218,
          "Y": 673
        },
        {
          "X": 1207,
          "Y": 673
        },
        {
          "X": 1207,
          "Y": 720
        },
        {
          "X": 218,
          "Y": 720
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Cu level and consists of liquid and CusSn5",
      "Confidence": 80,
      "Polygon": [
        {
          "X": 216,
          "Y": 730
        },
        {
          "X": 1206,
          "Y": 730
        },
        {
          "X": 1206,
          "Y": 779
        },
        {
          "X": 216,
          "Y": 779
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "intermetallic. Triangular are in the center is",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 218,
          "Y": 787
        },
        {
          "X": 1200,
          "Y": 787
        },
        {
          "X": 1200,
          "Y": 830
        },
        {
          "X": 218,
          "Y": 830
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "all liquid for all practical purposes. In reality",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 221,
          "Y": 843
        },
        {
          "X": 1206,
          "Y": 843
        },
        {
          "X": 1206,
          "Y": 886
        },
        {
          "X": 221,
          "Y": 886
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "true liquidus is usually higher. As reported by",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 217,
          "Y": 894
        },
        {
          "X": 1200,
          "Y": 894
        },
        {
          "X": 1200,
          "Y": 940
        },
        {
          "X": 217,
          "Y": 940
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "200 210 220 230 240 250",
      "Confidence": 75,
      "Polygon": [
        {
          "X": 1359,
          "Y": 924
        },
        {
          "X": 2039,
          "Y": 924
        },
        {
          "X": 2039,
          "Y": 956
        },
        {
          "X": 1359,
          "Y": 956
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "Moon et al [2]， a tiny peak is seen in the",
      "Confidence": 74,
      "Polygon": [
        {
          "X": 216,
          "Y": 950
        },
        {
          "X": 1204,
          "Y": 950
        },
        {
          "X": 1204,
          "Y": 998
        },
        {
          "X": 216,
          "Y": 998
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Temperature (°C)",
      "Confidence": 92,
      "Polygon": [
        {
          "X": 1643,
          "Y": 974
        },
        {
          "X": 1845,
          "Y": 974
        },
        {
          "X": 1845,
          "Y": 1005
        },
        {
          "X": 1643,
          "Y": 1005
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":5}}"
    },
    {
      "DetectedText": "DSC/DTA plots corresponding to the melting",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 218,
          "Y": 1010
        },
        {
          "X": 1199,
          "Y": 1010
        },
        {
          "X": 1199,
          "Y": 1057
        },
        {
          "X": 218,
          "Y": 1057
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Figure 2: Melting behavior of SAC305,",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1315,
          "Y": 1026
        },
        {
          "X": 2158,
          "Y": 1026
        },
        {
          "X": 2158,
          "Y": 1075
        },
        {
          "X": 1315,
          "Y": 1075
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":6}}"
    },
    {
      "DetectedText": ")f the primary intermetallic phase high",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 245,
          "Y": 1068
        },
        {
          "X": 1203,
          "Y": 1068
        },
        {
          "X": 1203,
          "Y": 1110
        },
        {
          "X": 245,
          "Y": 1110
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "SAC105 and SAC0307. SAC305 is close to",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1079
        },
        {
          "X": 2263,
          "Y": 1079
        },
        {
          "X": 2263,
          "Y": 1128
        },
        {
          "X": 1313,
          "Y": 1128
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":7}}"
    },
    {
      "DetectedText": "temperature. That temperature will be the",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 218,
          "Y": 1120
        },
        {
          "X": 1205,
          "Y": 1120
        },
        {
          "X": 1205,
          "Y": 1167
        },
        {
          "X": 218,
          "Y": 1167
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "eutectic but the low silver alloys show two",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 1309,
          "Y": 1141
        },
        {
          "X": 2209,
          "Y": 1141
        },
        {
          "X": 2209,
          "Y": 1182
        },
        {
          "X": 1309,
          "Y": 1182
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":7}}"
    },
    {
      "DetectedText": "true liquidus temperature. But since the",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 217,
          "Y": 1174
        },
        {
          "X": 1200,
          "Y": 1174
        },
        {
          "X": 1200,
          "Y": 1219
        },
        {
          "X": 217,
          "Y": 1219
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "distinct peaks corresponding to SnAg eutectic",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1198
        },
        {
          "X": 2298,
          "Y": 1198
        },
        {
          "X": 2298,
          "Y": 1242
        },
        {
          "X": 1313,
          "Y": 1242
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "fraction of this intermetallic phase very small,",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 218,
          "Y": 1235
        },
        {
          "X": 1200,
          "Y": 1235
        },
        {
          "X": 1200,
          "Y": 1280
        },
        {
          "X": 218,
          "Y": 1280
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "phase and SnCu eutectic.",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1311,
          "Y": 1253
        },
        {
          "X": 1863,
          "Y": 1253
        },
        {
          "X": 1863,
          "Y": 1297
        },
        {
          "X": 1311,
          "Y": 1297
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "for all practical purposes the",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 228,
          "Y": 1287
        },
        {
          "X": 983,
          "Y": 1287
        },
        {
          "X": 983,
          "Y": 1333
        },
        {
          "X": 228,
          "Y": 1333
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "liquidus",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1039,
          "Y": 1290
        },
        {
          "X": 1206,
          "Y": 1290
        },
        {
          "X": 1206,
          "Y": 1333
        },
        {
          "X": 1039,
          "Y": 1333
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "temperature is where rest of the phases have",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 218,
          "Y": 1346
        },
        {
          "X": 1202,
          "Y": 1346
        },
        {
          "X": 1202,
          "Y": 1391
        },
        {
          "X": 218,
          "Y": 1391
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "completely melted.",
      "Confidence": 94,
      "Polygon": [
        {
          "X": 219,
          "Y": 1400
        },
        {
          "X": 618,
          "Y": 1400
        },
        {
          "X": 618,
          "Y": 1446
        },
        {
          "X": 219,
          "Y": 1446
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "223 °C",
      "Confidence": 73,
      "Polygon": [
        {
          "X": 1450,
          "Y": 1424
        },
        {
          "X": 1599,
          "Y": 1424
        },
        {
          "X": 1599,
          "Y": 1470
        },
        {
          "X": 1450,
          "Y": 1470
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "8",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 1359,
          "Y": 1470
        },
        {
          "X": 1409,
          "Y": 1470
        },
        {
          "X": 1409,
          "Y": 1509
        },
        {
          "X": 1359,
          "Y": 1509
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "t290",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 272,
          "Y": 1580
        },
        {
          "X": 317,
          "Y": 1580
        },
        {
          "X": 317,
          "Y": 1619
        },
        {
          "X": 272,
          "Y": 1619
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":11}}"
    },
    {
      "DetectedText": "80",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 454,
          "Y": 1609
        },
        {
          "X": 517,
          "Y": 1609
        },
        {
          "X": 517,
          "Y": 1646
        },
        {
          "X": 454,
          "Y": 1646
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":11}}"
    },
    {
      "DetectedText": "270",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 675,
          "Y": 1615
        },
        {
          "X": 757,
          "Y": 1615
        },
        {
          "X": 757,
          "Y": 1660
        },
        {
          "X": 675,
          "Y": 1660
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "260",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 613,
          "Y": 1683
        },
        {
          "X": 668,
          "Y": 1683
        },
        {
          "X": 668,
          "Y": 1724
        },
        {
          "X": 613,
          "Y": 1724
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "Ag3Sn",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 400,
          "Y": 1715
        },
        {
          "X": 487,
          "Y": 1715
        },
        {
          "X": 487,
          "Y": 1760
        },
        {
          "X": 400,
          "Y": 1760
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "250",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 519,
          "Y": 1744
        },
        {
          "X": 606,
          "Y": 1744
        },
        {
          "X": 606,
          "Y": 1787
        },
        {
          "X": 519,
          "Y": 1787
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":13}}"
    },
    {
      "DetectedText": "25-4+ AgSm",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 1341,
          "Y": 1736
        },
        {
          "X": 1684,
          "Y": 1736
        },
        {
          "X": 1684,
          "Y": 1791
        },
        {
          "X": 1341,
          "Y": 1791
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "240",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 439,
          "Y": 1794
        },
        {
          "X": 514,
          "Y": 1794
        },
        {
          "X": 514,
          "Y": 1849
        },
        {
          "X": 439,
          "Y": 1849
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "84",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 208,
          "Y": 1879
        },
        {
          "X": 261,
          "Y": 1879
        },
        {
          "X": 261,
          "Y": 1928
        },
        {
          "X": 208,
          "Y": 1928
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":10}}"
    },
    {
      "DetectedText": "[5/",
      "Confidence": 61,
      "Polygon": [
        {
          "X": 730,
          "Y": 1864
        },
        {
          "X": 790,
          "Y": 1864
        },
        {
          "X": 790,
          "Y": 1920
        },
        {
          "X": 730,
          "Y": 1920
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "高/",
      "Confidence": 64,
      "Polygon": [
        {
          "X": 722,
          "Y": 1890
        },
        {
          "X": 785,
          "Y": 1890
        },
        {
          "X": 785,
          "Y": 1964
        },
        {
          "X": 722,
          "Y": 1964
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "3-",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1402,
          "Y": 1902
        },
        {
          "X": 1476,
          "Y": 1902
        },
        {
          "X": 1476,
          "Y": 1954
        },
        {
          "X": 1402,
          "Y": 1954
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "L",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1559,
          "Y": 1904
        },
        {
          "X": 1629,
          "Y": 1904
        },
        {
          "X": 1629,
          "Y": 1961
        },
        {
          "X": 1559,
          "Y": 1961
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "33",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 211,
          "Y": 1958
        },
        {
          "X": 263,
          "Y": 1958
        },
        {
          "X": 263,
          "Y": 2004
        },
        {
          "X": 211,
          "Y": 2004
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":10}}"
    },
    {
      "DetectedText": "2-",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1359,
          "Y": 1986
        },
        {
          "X": 1432,
          "Y": 1986
        },
        {
          "X": 1432,
          "Y": 2033
        },
        {
          "X": 1359,
          "Y": 2033
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "~",
      "Confidence": 60,
      "Polygon": [
        {
          "X": 377,
          "Y": 2017
        },
        {
          "X": 477,
          "Y": 2017
        },
        {
          "X": 477,
          "Y": 2065
        },
        {
          "X": 377,
          "Y": 2065
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":16}}"
    },
    {
      "DetectedText": "| Sm",
      "Confidence": 52,
      "Polygon": [
        {
          "X": 1426,
          "Y": 2054
        },
        {
          "X": 1565,
          "Y": 2054
        },
        {
          "X": 1565,
          "Y": 2110
        },
        {
          "X": 1426,
          "Y": 2110
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":24}}"
    },
    {
      "DetectedText": "!↑",
      "Confidence": 76,
      "Polygon": [
        {
          "X": 270,
          "Y": 2139
        },
        {
          "X": 397,
          "Y": 2139
        },
        {
          "X": 397,
          "Y": 2193
        },
        {
          "X": 270,
          "Y": 2193
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "[副昂哥司",
      "Confidence": 71,
      "Polygon": [
        {
          "X": 655,
          "Y": 2169
        },
        {
          "X": 879,
          "Y": 2169
        },
        {
          "X": 879,
          "Y": 2236
        },
        {
          "X": 655,
          "Y": 2236
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "%00.40.81.21.62.02.4 2.8",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 1407,
          "Y": 2187
        },
        {
          "X": 2172,
          "Y": 2187
        },
        {
          "X": 2172,
          "Y": 2248
        },
        {
          "X": 1407,
          "Y": 2248
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":25}}"
    },
    {
      "DetectedText": "0.4 0.8 1.2 1.6 2.0 2.4 2.",
      "Confidence": 75,
      "Polygon": [
        {
          "X": 356,
          "Y": 2241
        },
        {
          "X": 928,
          "Y": 2241
        },
        {
          "X": 928,
          "Y": 2286
        },
        {
          "X": 356,
          "Y": 2286
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "Sn",
      "Confidence": 65,
      "Polygon": [
        {
          "X": 266,
          "Y": 2281
        },
        {
          "X": 317,
          "Y": 2281
        },
        {
          "X": 317,
          "Y": 2320
        },
        {
          "X": 266,
          "Y": 2320
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "wt.% Cu",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 550,
          "Y": 2287
        },
        {
          "X": 691,
          "Y": 2287
        },
        {
          "X": 691,
          "Y": 2326
        },
        {
          "X": 550,
          "Y": 2326
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "(Sn)",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1345,
          "Y": 2257
        },
        {
          "X": 1434,
          "Y": 2257
        },
        {
          "X": 1434,
          "Y": 2304
        },
        {
          "X": 1345,
          "Y": 2304
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":26}}"
    },
    {
      "DetectedText": "wt.% Cu",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1718,
          "Y": 2262
        },
        {
          "X": 1901,
          "Y": 2262
        },
        {
          "X": 1901,
          "Y": 2312
        },
        {
          "X": 1718,
          "Y": 2312
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":27}}"
    },
    {
      "DetectedText": "Figure 3: Calculated isothermal sections for",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1315,
          "Y": 2327
        },
        {
          "X": 2275,
          "Y": 2327
        },
        {
          "X": 2275,
          "Y": 2371
        },
        {
          "X": 1315,
          "Y": 2371
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":28}}"
    },
    {
      "DetectedText": "Figure 1: Calculated liquidus surfaces for",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 217,
          "Y": 2342
        },
        {
          "X": 1125,
          "Y": 2342
        },
        {
          "X": 1125,
          "Y": 2394
        },
        {
          "X": 217,
          "Y": 2394
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "SgAgCu at 223°C. [2]",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1315,
          "Y": 2379
        },
        {
          "X": 1792,
          "Y": 2379
        },
        {
          "X": 1792,
          "Y": 2430
        },
        {
          "X": 1315,
          "Y": 2430
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":28}}"
    },
    {
      "DetectedText": "SnAgCu alloys [2]",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 216,
          "Y": 2399
        },
        {
          "X": 605,
          "Y": 2399
        },
        {
          "X": 605,
          "Y": 2451
        },
        {
          "X": 216,
          "Y": 2451
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "Knowing melting and freezing points is",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1456,
          "Y": 2489
        },
        {
          "X": 2299,
          "Y": 2489
        },
        {
          "X": 2299,
          "Y": 2538
        },
        {
          "X": 1456,
          "Y": 2538
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":29}}"
    },
    {
      "DetectedText": "only part of the information. For in-depth",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2549
        },
        {
          "X": 2299,
          "Y": 2549
        },
        {
          "X": 2299,
          "Y": 2593
        },
        {
          "X": 1313,
          "Y": 2593
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "understanding of the solder joint formation",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2607
        },
        {
          "X": 2299,
          "Y": 2607
        },
        {
          "X": 2299,
          "Y": 2650
        },
        {
          "X": 1312,
          "Y": 2650
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "and its reliability one has to understand the",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1311,
          "Y": 2663
        },
        {
          "X": 2298,
          "Y": 2663
        },
        {
          "X": 2298,
          "Y": 2705
        },
        {
          "X": 1311,
          "Y": 2705
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "solidification",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2716
        },
        {
          "X": 1581,
          "Y": 2716
        },
        {
          "X": 1581,
          "Y": 2761
        },
        {
          "X": 1313,
          "Y": 2761
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "behavior",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1643,
          "Y": 2714
        },
        {
          "X": 1833,
          "Y": 2714
        },
        {
          "X": 1833,
          "Y": 2762
        },
        {
          "X": 1643,
          "Y": 2762
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "n more",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 1914,
          "Y": 2712
        },
        {
          "X": 2109,
          "Y": 2712
        },
        {
          "X": 2109,
          "Y": 2763
        },
        {
          "X": 1914,
          "Y": 2763
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "detail.",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 2167,
          "Y": 2712
        },
        {
          "X": 2297,
          "Y": 2712
        },
        {
          "X": 2297,
          "Y": 2763
        },
        {
          "X": 2167,
          "Y": 2763
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "Anderson [3] reported a detailed study of the",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1307,
          "Y": 2771
        },
        {
          "X": 2299,
          "Y": 2771
        },
        {
          "X": 2299,
          "Y": 2817
        },
        {
          "X": 1307,
          "Y": 2817
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "solidification behavior of several near eutectic",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2831
        },
        {
          "X": 2297,
          "Y": 2831
        },
        {
          "X": 2297,
          "Y": 2874
        },
        {
          "X": 1312,
          "Y": 2874
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "SAC",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2880
        },
        {
          "X": 1415,
          "Y": 2880
        },
        {
          "X": 1415,
          "Y": 2926
        },
        {
          "X": 1313,
          "Y": 2926
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":31}}"
    },
    {
      "DetectedText": "alloys",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1486,
          "Y": 2887
        },
        {
          "X": 1608,
          "Y": 2887
        },
        {
          "X": 1608,
          "Y": 2929
        },
        {
          "X": 1486,
          "Y": 2929
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":31}}"
    },
    {
      "DetectedText": "showed",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1842,
          "Y": 2888
        },
        {
          "X": 2004,
          "Y": 2888
        },
        {
          "X": 2004,
          "Y": 2929
        },
        {
          "X": 1842,
          "Y": 2929
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":32}}"
    },
    {
      "DetectedText": "significant",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 2083,
          "Y": 2888
        },
        {
          "X": 2299,
          "Y": 2888
        },
        {
          "X": 2299,
          "Y": 2930
        },
        {
          "X": 2083,
          "Y": 2930
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":32}}"
    },
    {
      "DetectedText": "differences in microstructure of as soldered",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1311,
          "Y": 2941
        },
        {
          "X": 2297,
          "Y": 2941
        },
        {
          "X": 2297,
          "Y": 2987
        },
        {
          "X": 1311,
          "Y": 2987
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":33}}"
    },
    {
      "DetectedText": "joints even though alloy compositions are not",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1310,
          "Y": 3000
        },
        {
          "X": 2299,
          "Y": 3000
        },
        {
          "X": 2299,
          "Y": 3047
        },
        {
          "X": 1310,
          "Y": 3047
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":33}}"
    }
  ],
  "Language": "zh",
  "RequestId": "c47aa95e-ed61-4aac-98e0-118414fd2c4e"
}                    #这个是图片的ocr结果.











#下面是解析后的大字典.



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
              tmp34=[]
              biaohaolie=data[biaohao]['Polygon'][0]['Y']
              for j in tmp888:
                liebiao=data[j[1]]['Polygon'][0]['Y']
                if liebiao<biaohaolie:
                  tmp34.append(j[1])
              wenben=''
              for i in tmp34:
                wenben+=data[i]['DetectedText']
              if len(wenben)<50:

                   #  看 biaohao上面的文字有多少.
                   return False  # 说明bu是门派

            # 看figure上面的文本有多少.
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


im = cv2.imread(tupiandizhi)
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


