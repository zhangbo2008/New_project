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




#下面是解析后的大字典.

shuru={
  "TextDetections": [
    {
      "DetectedText": "that different.",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 219,
          "Y": 449
        },
        {
          "X": 530,
          "Y": 449
        },
        {
          "X": 530,
          "Y": 496
        },
        {
          "X": 219,
          "Y": 496
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Figure 4 show shows",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 638,
          "Y": 448
        },
        {
          "X": 1203,
          "Y": 448
        },
        {
          "X": 1203,
          "Y": 495
        },
        {
          "X": 638,
          "Y": 495
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "and Sn2.5Ag0.9Cu. All the solder joints were",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1312,
          "Y": 450
        },
        {
          "X": 2298,
          "Y": 450
        },
        {
          "X": 2298,
          "Y": 497
        },
        {
          "X": 1312,
          "Y": 497
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "microstructures of a) Sn3.0Ag0.5Cu， b)",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 218,
          "Y": 506
        },
        {
          "X": 1198,
          "Y": 506
        },
        {
          "X": 1198,
          "Y": 551
        },
        {
          "X": 218,
          "Y": 551
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "reflowed up to 2409C peak temperature.",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1312,
          "Y": 506
        },
        {
          "X": 2289,
          "Y": 506
        },
        {
          "X": 2289,
          "Y": 552
        },
        {
          "X": 1312,
          "Y": 552
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "Sn3.9Ag0.6Cu，c) Sn3.7Ag0.9Cu， and d)",
      "Confidence": 90,
      "Polygon": [
        {
          "X": 219,
          "Y": 558
        },
        {
          "X": 1196,
          "Y": 558
        },
        {
          "X": 1196,
          "Y": 607
        },
        {
          "X": 219,
          "Y": 607
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Three different cooling rates were studies,",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1315,
          "Y": 561
        },
        {
          "X": 2290,
          "Y": 561
        },
        {
          "X": 2290,
          "Y": 608
        },
        {
          "X": 1315,
          "Y": 608
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "Sn3.6Ag1.0Cu.",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 217,
          "Y": 614
        },
        {
          "X": 542,
          "Y": 614
        },
        {
          "X": 542,
          "Y": 660
        },
        {
          "X": 217,
          "Y": 660
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Coarse Sn dendrites fc",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 618,
          "Y": 614
        },
        {
          "X": 1167,
          "Y": 614
        },
        {
          "X": 1167,
          "Y": 659
        },
        {
          "X": 618,
          "Y": 659
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "0.2°C/min，1.2°C/min and 3.0°C/min. It can",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1313,
          "Y": 614
        },
        {
          "X": 2296,
          "Y": 614
        },
        {
          "X": 2296,
          "Y": 660
        },
        {
          "X": 1313,
          "Y": 660
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "SAC305 are quite different from extremely",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 217,
          "Y": 672
        },
        {
          "X": 1205,
          "Y": 672
        },
        {
          "X": 1205,
          "Y": 717
        },
        {
          "X": 217,
          "Y": 717
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "be clearly seen that a combination of high",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1315,
          "Y": 672
        },
        {
          "X": 2297,
          "Y": 672
        },
        {
          "X": 2297,
          "Y": 719
        },
        {
          "X": 1315,
          "Y": 719
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "fine Sn",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 221,
          "Y": 725
        },
        {
          "X": 424,
          "Y": 725
        },
        {
          "X": 424,
          "Y": 774
        },
        {
          "X": 221,
          "Y": 774
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "dendrites for Sn3.9Ag0.6Cu.",
      "Confidence": 92,
      "Polygon": [
        {
          "X": 487,
          "Y": 730
        },
        {
          "X": 1199,
          "Y": 730
        },
        {
          "X": 1199,
          "Y": 776
        },
        {
          "X": 487,
          "Y": 776
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "silver content and slow cooling rate results",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1333,
          "Y": 732
        },
        {
          "X": 2299,
          "Y": 732
        },
        {
          "X": 2299,
          "Y": 776
        },
        {
          "X": 1333,
          "Y": 776
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "Sn3.7Ag0.9Cu shows Sn dendrite pattern",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 218,
          "Y": 784
        },
        {
          "X": 1205,
          "Y": 784
        },
        {
          "X": 1205,
          "Y": 831
        },
        {
          "X": 218,
          "Y": 831
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "growth of large size Ag3Sn platelets. Ag3Sn",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1310,
          "Y": 787
        },
        {
          "X": 2301,
          "Y": 787
        },
        {
          "X": 2301,
          "Y": 831
        },
        {
          "X": 1310,
          "Y": 831
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "similar to SnAg eutectic whileSn3.6Ag1.0Cu",
      "Confidence": 90,
      "Polygon": [
        {
          "X": 219,
          "Y": 839
        },
        {
          "X": 1202,
          "Y": 839
        },
        {
          "X": 1202,
          "Y": 887
        },
        {
          "X": 219,
          "Y": 887
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "in itself has a higher melting temperature,",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1315,
          "Y": 840
        },
        {
          "X": 2293,
          "Y": 840
        },
        {
          "X": 2293,
          "Y": 888
        },
        {
          "X": 1315,
          "Y": 888
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "microstructure doesn't appear dendritic at all.",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 216,
          "Y": 894
        },
        {
          "X": 1187,
          "Y": 894
        },
        {
          "X": 1187,
          "Y": 940
        },
        {
          "X": 216,
          "Y": 940
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "thus these platelets start precipitating and",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1279,
          "Y": 895
        },
        {
          "X": 2290,
          "Y": 895
        },
        {
          "X": 2290,
          "Y": 940
        },
        {
          "X": 1279,
          "Y": 940
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "Also, noticeable is the large Ag3Sn needle",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 218,
          "Y": 951
        },
        {
          "X": 1202,
          "Y": 951
        },
        {
          "X": 1202,
          "Y": 998
        },
        {
          "X": 218,
          "Y": 998
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "growing while solder is still in the liquid state.",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1313,
          "Y": 955
        },
        {
          "X": 2290,
          "Y": 955
        },
        {
          "X": 2290,
          "Y": 999
        },
        {
          "X": 1313,
          "Y": 999
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "present in",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 215,
          "Y": 1008
        },
        {
          "X": 456,
          "Y": 1008
        },
        {
          "X": 456,
          "Y": 1054
        },
        {
          "X": 215,
          "Y": 1054
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Figure 4(b)， Sn3.9Ag0.6Cu.",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 524,
          "Y": 1009
        },
        {
          "X": 1193,
          "Y": 1009
        },
        {
          "X": 1193,
          "Y": 1057
        },
        {
          "X": 524,
          "Y": 1057
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "Higher Ag level enhances precipitation while",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1316,
          "Y": 1012
        },
        {
          "X": 2298,
          "Y": 1012
        },
        {
          "X": 2298,
          "Y": 1056
        },
        {
          "X": 1316,
          "Y": 1056
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "Considering most manufacturers tolerances,",
      "Confidence": 92,
      "Polygon": [
        {
          "X": 218,
          "Y": 1067
        },
        {
          "X": 1199,
          "Y": 1067
        },
        {
          "X": 1199,
          "Y": 1110
        },
        {
          "X": 218,
          "Y": 1110
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "longer cooling time means longer growth time.",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1316,
          "Y": 1067
        },
        {
          "X": 2303,
          "Y": 1067
        },
        {
          "X": 2303,
          "Y": 1111
        },
        {
          "X": 1316,
          "Y": 1111
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "composition",
      "Confidence": 95,
      "Polygon": [
        {
          "X": 363,
          "Y": 1121
        },
        {
          "X": 617,
          "Y": 1121
        },
        {
          "X": 617,
          "Y": 1165
        },
        {
          "X": 363,
          "Y": 1165
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
    },
    {
      "DetectedText": "may",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 688,
          "Y": 1123
        },
        {
          "X": 762,
          "Y": 1123
        },
        {
          "X": 762,
          "Y": 1164
        },
        {
          "X": 688,
          "Y": 1164
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
    },
    {
      "DetectedText": "e",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 872,
          "Y": 1121
        },
        {
          "X": 917,
          "Y": 1121
        },
        {
          "X": 917,
          "Y": 1162
        },
        {
          "X": 872,
          "Y": 1162
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
    },
    {
      "DetectedText": "considered",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 967,
          "Y": 1123
        },
        {
          "X": 1204,
          "Y": 1123
        },
        {
          "X": 1204,
          "Y": 1166
        },
        {
          "X": 967,
          "Y": 1166
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
    },
    {
      "DetectedText": "SAC405.A slight change in composition may",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 218,
          "Y": 1172
        },
        {
          "X": 1202,
          "Y": 1172
        },
        {
          "X": 1202,
          "Y": 1219
        },
        {
          "X": 218,
          "Y": 1219
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "0.2C/min",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 1430,
          "Y": 1187
        },
        {
          "X": 1574,
          "Y": 1187
        },
        {
          "X": 1574,
          "Y": 1213
        },
        {
          "X": 1430,
          "Y": 1213
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":5}}"
    },
    {
      "DetectedText": "1.20C/min",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 1736,
          "Y": 1184
        },
        {
          "X": 1879,
          "Y": 1184
        },
        {
          "X": 1879,
          "Y": 1216
        },
        {
          "X": 1736,
          "Y": 1216
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":6}}"
    },
    {
      "DetectedText": "3.0C/min",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 2038,
          "Y": 1184
        },
        {
          "X": 2184,
          "Y": 1184
        },
        {
          "X": 2184,
          "Y": 1213
        },
        {
          "X": 2038,
          "Y": 1213
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":7}}"
    },
    {
      "DetectedText": "results in a significant difference in solder",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 218,
          "Y": 1235
        },
        {
          "X": 1205,
          "Y": 1235
        },
        {
          "X": 1205,
          "Y": 1278
        },
        {
          "X": 218,
          "Y": 1278
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "127 jm",
      "Confidence": 78,
      "Polygon": [
        {
          "X": 1368,
          "Y": 1225
        },
        {
          "X": 1454,
          "Y": 1225
        },
        {
          "X": 1454,
          "Y": 1262
        },
        {
          "X": 1368,
          "Y": 1262
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "127 pum",
      "Confidence": 74,
      "Polygon": [
        {
          "X": 1686,
          "Y": 1228
        },
        {
          "X": 1763,
          "Y": 1228
        },
        {
          "X": 1763,
          "Y": 1256
        },
        {
          "X": 1686,
          "Y": 1256
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "127 pm",
      "Confidence": 69,
      "Polygon": [
        {
          "X": 1996,
          "Y": 1226
        },
        {
          "X": 2074,
          "Y": 1226
        },
        {
          "X": 2074,
          "Y": 1259
        },
        {
          "X": 1996,
          "Y": 1259
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":10}}"
    },
    {
      "DetectedText": "performance. That is not a good news for",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 216,
          "Y": 1291
        },
        {
          "X": 1196,
          "Y": 1291
        },
        {
          "X": 1196,
          "Y": 1334
        },
        {
          "X": 216,
          "Y": 1334
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "electronics manufacturers.",
      "Confidence": 96,
      "Polygon": [
        {
          "X": 217,
          "Y": 1345
        },
        {
          "X": 817,
          "Y": 1345
        },
        {
          "X": 817,
          "Y": 1391
        },
        {
          "X": 217,
          "Y": 1391
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "Good news",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 925,
          "Y": 1347
        },
        {
          "X": 1202,
          "Y": 1347
        },
        {
          "X": 1202,
          "Y": 1392
        },
        {
          "X": 925,
          "Y": 1392
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "though is that this kind of large variations can",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 218,
          "Y": 1401
        },
        {
          "X": 1199,
          "Y": 1401
        },
        {
          "X": 1199,
          "Y": 1449
        },
        {
          "X": 218,
          "Y": 1449
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "be expected only near the eutectic point.",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 217,
          "Y": 1454
        },
        {
          "X": 1092,
          "Y": 1454
        },
        {
          "X": 1092,
          "Y": 1501
        },
        {
          "X": 217,
          "Y": 1501
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "127 jum",
      "Confidence": 73,
      "Polygon": [
        {
          "X": 1391,
          "Y": 1453
        },
        {
          "X": 1458,
          "Y": 1453
        },
        {
          "X": 1458,
          "Y": 1484
        },
        {
          "X": 1391,
          "Y": 1484
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":11}}"
    },
    {
      "DetectedText": "127um",
      "Confidence": 95,
      "Polygon": [
        {
          "X": 1684,
          "Y": 1454
        },
        {
          "X": 1773,
          "Y": 1454
        },
        {
          "X": 1773,
          "Y": 1485
        },
        {
          "X": 1684,
          "Y": 1485
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "127 jum",
      "Confidence": 73,
      "Polygon": [
        {
          "X": 1988,
          "Y": 1451
        },
        {
          "X": 2079,
          "Y": 1451
        },
        {
          "X": 2079,
          "Y": 1482
        },
        {
          "X": 1988,
          "Y": 1482
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":13}}"
    },
    {
      "DetectedText": "sopmb)",
      "Confidence": 74,
      "Polygon": [
        {
          "X": 505,
          "Y": 1625
        },
        {
          "X": 677,
          "Y": 1625
        },
        {
          "X": 677,
          "Y": 1659
        },
        {
          "X": 505,
          "Y": 1659
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "50km",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 934,
          "Y": 1644
        },
        {
          "X": 997,
          "Y": 1644
        },
        {
          "X": 997,
          "Y": 1669
        },
        {
          "X": 934,
          "Y": 1669
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "Figure 5: As soldered solder joints x-section.",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1316,
          "Y": 1686
        },
        {
          "X": 2287,
          "Y": 1686
        },
        {
          "X": 2287,
          "Y": 1734
        },
        {
          "X": 1316,
          "Y": 1734
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "High Ag level and slow cooling rate increases",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1314,
          "Y": 1741
        },
        {
          "X": 2288,
          "Y": 1741
        },
        {
          "X": 2288,
          "Y": 1789
        },
        {
          "X": 1314,
          "Y": 1789
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "probability of Ag3Sn platelet formation. From",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1315,
          "Y": 1797
        },
        {
          "X": 2279,
          "Y": 1797
        },
        {
          "X": 2279,
          "Y": 1843
        },
        {
          "X": 1315,
          "Y": 1843
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "S0ym ",
      "Confidence": 62,
      "Polygon": [
        {
          "X": 926,
          "Y": 1882
        },
        {
          "X": 1009,
          "Y": 1882
        },
        {
          "X": 1009,
          "Y": 1908
        },
        {
          "X": 926,
          "Y": 1908
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":16}}"
    },
    {
      "DetectedText": "[4]",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1315,
          "Y": 1850
        },
        {
          "X": 1396,
          "Y": 1850
        },
        {
          "X": 1396,
          "Y": 1903
        },
        {
          "X": 1315,
          "Y": 1903
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "Ag3Sn in itself has a higher melting",
      "Confidence": 77,
      "Polygon": [
        {
          "X": 1455,
          "Y": 1965
        },
        {
          "X": 2298,
          "Y": 1965
        },
        {
          "X": 2298,
          "Y": 2013
        },
        {
          "X": 1455,
          "Y": 2013
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "temperature, thus these platelets start",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2023
        },
        {
          "X": 2299,
          "Y": 2023
        },
        {
          "X": 2299,
          "Y": 2067
        },
        {
          "X": 1313,
          "Y": 2067
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "precipitating and growing while solder is still",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1317,
          "Y": 2076
        },
        {
          "X": 2297,
          "Y": 2076
        },
        {
          "X": 2297,
          "Y": 2123
        },
        {
          "X": 1317,
          "Y": 2123
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "Figure 4: Microstructure of as soldered",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 219,
          "Y": 2138
        },
        {
          "X": 1077,
          "Y": 2138
        },
        {
          "X": 1077,
          "Y": 2188
        },
        {
          "X": 219,
          "Y": 2188
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "in the liquid state. Higher Ag level enhances",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2130
        },
        {
          "X": 2299,
          "Y": 2130
        },
        {
          "X": 2299,
          "Y": 2177
        },
        {
          "X": 1313,
          "Y": 2177
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "joints of (a) Sn3.0Ag0. 5Cu, (b)",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 219,
          "Y": 2189
        },
        {
          "X": 874,
          "Y": 2189
        },
        {
          "X": 874,
          "Y": 2243
        },
        {
          "X": 219,
          "Y": 2243
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "Ag3Sn precipitation rate while longer cooling",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2188
        },
        {
          "X": 2295,
          "Y": 2188
        },
        {
          "X": 2295,
          "Y": 2234
        },
        {
          "X": 1313,
          "Y": 2234
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "Sn3.9Ag0.6Cu, (c) Sn3.7Ag0.9Cu, and (d)",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 218,
          "Y": 2247
        },
        {
          "X": 1129,
          "Y": 2247
        },
        {
          "X": 1129,
          "Y": 2297
        },
        {
          "X": 218,
          "Y": 2297
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "time means longer growth time. Sometimes",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2249
        },
        {
          "X": 2298,
          "Y": 2249
        },
        {
          "X": 2298,
          "Y": 2292
        },
        {
          "X": 1312,
          "Y": 2292
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "Sn3.6Ag1.0Cu.",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 219,
          "Y": 2305
        },
        {
          "X": 543,
          "Y": 2305
        },
        {
          "X": 543,
          "Y": 2351
        },
        {
          "X": 219,
          "Y": 2351
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "the Ag3Sn platelets can grow so large in the",
      "Confidence": 80,
      "Polygon": [
        {
          "X": 1311,
          "Y": 2301
        },
        {
          "X": 2297,
          "Y": 2301
        },
        {
          "X": 2297,
          "Y": 2349
        },
        {
          "X": 1311,
          "Y": 2349
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "liquid stage that when solder shrinks during",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2357
        },
        {
          "X": 2299,
          "Y": 2357
        },
        {
          "X": 2299,
          "Y": 2403
        },
        {
          "X": 1312,
          "Y": 2403
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "The long thin Ag3Sn plate seen is seen",
      "Confidence": 80,
      "Polygon": [
        {
          "X": 369,
          "Y": 2423
        },
        {
          "X": 1204,
          "Y": 2423
        },
        {
          "X": 1204,
          "Y": 2466
        },
        {
          "X": 369,
          "Y": 2466
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "freezing，the Ag3Sn platelet protrudes",
      "Confidence": 90,
      "Polygon": [
        {
          "X": 1307,
          "Y": 2412
        },
        {
          "X": 2299,
          "Y": 2412
        },
        {
          "X": 2299,
          "Y": 2457
        },
        {
          "X": 1307,
          "Y": 2457
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "in figure 4(b) only. This alloy, Sn3.9Ag0.6Cu,",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 219,
          "Y": 2472
        },
        {
          "X": 1199,
          "Y": 2472
        },
        {
          "X": 1199,
          "Y": 2522
        },
        {
          "X": 219,
          "Y": 2522
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "outwards severely deforming the solder",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 1314,
          "Y": 2470
        },
        {
          "X": 2298,
          "Y": 2470
        },
        {
          "X": 2298,
          "Y": 2513
        },
        {
          "X": 1314,
          "Y": 2513
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "is the only alloy shown in this picture that is",
      "Confidence": 80,
      "Polygon": [
        {
          "X": 220,
          "Y": 2529
        },
        {
          "X": 1199,
          "Y": 2529
        },
        {
          "X": 1199,
          "Y": 2575
        },
        {
          "X": 220,
          "Y": 2575
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "interconnection. Figure 6 shows a SAC405",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1314,
          "Y": 2522
        },
        {
          "X": 2299,
          "Y": 2522
        },
        {
          "X": 2299,
          "Y": 2572
        },
        {
          "X": 1314,
          "Y": 2572
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "on the Ag-rich side of the eutectic.",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 199,
          "Y": 2585
        },
        {
          "X": 1198,
          "Y": 2585
        },
        {
          "X": 1198,
          "Y": 2630
        },
        {
          "X": 199,
          "Y": 2630
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "solder sphere reflowed under a reflow profile",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2583
        },
        {
          "X": 2302,
          "Y": 2583
        },
        {
          "X": 2302,
          "Y": 2626
        },
        {
          "X": 1312,
          "Y": 2626
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "Probability of Ag3Sn precipitation increases",
      "Confidence": 90,
      "Polygon": [
        {
          "X": 216,
          "Y": 2646
        },
        {
          "X": 1202,
          "Y": 2646
        },
        {
          "X": 1202,
          "Y": 2691
        },
        {
          "X": 216,
          "Y": 2691
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "with very slow cooling rate",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2637
        },
        {
          "X": 1897,
          "Y": 2637
        },
        {
          "X": 1897,
          "Y": 2681
        },
        {
          "X": 1312,
          "Y": 2681
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "A large Ag3Sn",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 1975,
          "Y": 2635
        },
        {
          "X": 2301,
          "Y": 2635
        },
        {
          "X": 2301,
          "Y": 2687
        },
        {
          "X": 1975,
          "Y": 2687
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "dramatically on that side of the eutectic as",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 217,
          "Y": 2703
        },
        {
          "X": 1201,
          "Y": 2703
        },
        {
          "X": 1201,
          "Y": 2745
        },
        {
          "X": 217,
          "Y": 2745
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "platelet appears at the surface of the sphere.",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2696
        },
        {
          "X": 2298,
          "Y": 2696
        },
        {
          "X": 2298,
          "Y": 2738
        },
        {
          "X": 1312,
          "Y": 2738
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "one would expect.",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 229,
          "Y": 2758
        },
        {
          "X": 644,
          "Y": 2758
        },
        {
          "X": 644,
          "Y": 2801
        },
        {
          "X": 229,
          "Y": 2801
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "Henderson et al [4]",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 725,
          "Y": 2754
        },
        {
          "X": 1204,
          "Y": 2754
        },
        {
          "X": 1204,
          "Y": 2801
        },
        {
          "X": 725,
          "Y": 2801
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "Therefore, even though most of the OEM's",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1315,
          "Y": 2748
        },
        {
          "X": 2299,
          "Y": 2748
        },
        {
          "X": 2299,
          "Y": 2797
        },
        {
          "X": 1315,
          "Y": 2797
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "studied this",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 217,
          "Y": 2809
        },
        {
          "X": 517,
          "Y": 2809
        },
        {
          "X": 517,
          "Y": 2854
        },
        {
          "X": 217,
          "Y": 2854
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "Ag3Sn",
      "Confidence": 95,
      "Polygon": [
        {
          "X": 576,
          "Y": 2807
        },
        {
          "X": 719,
          "Y": 2807
        },
        {
          "X": 719,
          "Y": 2857
        },
        {
          "X": 576,
          "Y": 2857
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "platelet formation",
      "Confidence": 94,
      "Polygon": [
        {
          "X": 775,
          "Y": 2808
        },
        {
          "X": 1202,
          "Y": 2808
        },
        {
          "X": 1202,
          "Y": 2855
        },
        {
          "X": 775,
          "Y": 2855
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "would treat SAC305 and SAC405 alloys near",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1315,
          "Y": 2805
        },
        {
          "X": 2299,
          "Y": 2805
        },
        {
          "X": 2299,
          "Y": 2850
        },
        {
          "X": 1315,
          "Y": 2850
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "phenomenon in detail.",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 220,
          "Y": 2868
        },
        {
          "X": 741,
          "Y": 2868
        },
        {
          "X": 741,
          "Y": 2913
        },
        {
          "X": 220,
          "Y": 2913
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "Figure 5 shows",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 822,
          "Y": 2867
        },
        {
          "X": 1205,
          "Y": 2867
        },
        {
          "X": 1205,
          "Y": 2913
        },
        {
          "X": 822,
          "Y": 2913
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "eutectic and tend to use same reflow profile,",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2863
        },
        {
          "X": 2297,
          "Y": 2863
        },
        {
          "X": 2297,
          "Y": 2906
        },
        {
          "X": 1313,
          "Y": 2906
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "micrographs of cross-sectioned solder joints",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 216,
          "Y": 2925
        },
        {
          "X": 1204,
          "Y": 2925
        },
        {
          "X": 1204,
          "Y": 2969
        },
        {
          "X": 216,
          "Y": 2969
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "these results show that more care must be",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 1311,
          "Y": 2918
        },
        {
          "X": 2299,
          "Y": 2918
        },
        {
          "X": 2299,
          "Y": 2965
        },
        {
          "X": 1311,
          "Y": 2965
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "formed with two SAC alloys, Sn3 .8Ag0.7Cu",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 218,
          "Y": 2977
        },
        {
          "X": 1201,
          "Y": 2977
        },
        {
          "X": 1201,
          "Y": 3024
        },
        {
          "X": 218,
          "Y": 3024
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "taken with SAC405. Apart from deforming",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2973
        },
        {
          "X": 2298,
          "Y": 2973
        },
        {
          "X": 2298,
          "Y": 3018
        },
        {
          "X": 1313,
          "Y": 3018
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    }
  ],
  "Language": "zh",
  "RequestId": "f2a2d125-220b-4c69-b493-38baa4e4a7ec"
}

data=shuru["TextDetections"]


print(data)

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




print("        ")
print("        ")
print("        ")
print("        ")
print(data[0])



test=data[0]

print(test['Polygon'])



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
print("                ")
print("                ")
print("                ")
print("                ")
print("                ")
print("                ")
print("                ")
print("                ")
print("                ")
print(jiange)


# 去掉过大的百分之20. 过大时因为图片中的文本也识别出来了.还有图片的附带文字这2个导致.



jiange=sorted(jiange)
jiange=jiange[int(len(jiange)*0.2):int(len(jiange)*0.8)]

print(jiange)
duanluojiange=None

# 经过实践,duanluojiange 尽量算小一点.这样效果更好. 因为更严格了.


duanluojiange=sum(jiange)/len(jiange)
duanluojiange*=0.7








#下面这个指标就作为段落横间隔.
print(duanluojiange)

print(zigao)

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
print(tmp)
print(len(tmp))


print("22222222")

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

im = cv2.imread('tmp.jpg')

'''
这个部分是画框看着,比较的.实际代码不用跑哦的.
t232=tmp[0]
for i in t232:

  cv2.rectangle(im, (data[i]['Polygon'][0]['X'], data[i]['Polygon'][0]['Y']), (data[i]['Polygon'][2]['X'], data[i]['Polygon'][2]['Y']), (1,1,1), 5)


t232=tmp[1]
for i in t232:

  cv2.rectangle(im, (data[i]['Polygon'][0]['X'], data[i]['Polygon'][0]['Y']), (data[i]['Polygon'][2]['X'], data[i]['Polygon'][2]['Y']), (50,100,50), 5)


t232=tmp[-1]
for i in t232:

  cv2.rectangle(im, (data[i]['Polygon'][0]['X'], data[i]['Polygon'][0]['Y']), (data[i]['Polygon'][2]['X'], data[i]['Polygon'][2]['Y']), (100,100,100), 5)

t232=tmp[-3]
for i in t232:

  cv2.rectangle(im, (data[i]['Polygon'][0]['X'], data[i]['Polygon'][0]['Y']), (data[i]['Polygon'][2]['X'], data[i]['Polygon'][2]['Y']), (200,0,200), 5)




t232=tmp[-2]
for i in t232:

  cv2.rectangle(im, (data[i]['Polygon'][0]['X'], data[i]['Polygon'][0]['Y']), (data[i]['Polygon'][2]['X'], data[i]['Polygon'][2]['Y']), (200,0,200), 5)



t232=tmp[-5]
for i in t232:

  cv2.rectangle(im, (data[i]['Polygon'][0]['X'], data[i]['Polygon'][0]['Y']), (data[i]['Polygon'][2]['X'], data[i]['Polygon'][2]['Y']), (200,0,200), 5)


t232=tmp[-6]
for i in t232:

  cv2.rectangle(im, (data[i]['Polygon'][0]['X'], data[i]['Polygon'][0]['Y']), (data[i]['Polygon'][2]['X'], data[i]['Polygon'][2]['Y']), (200,0,200), 5)
'''








#看看聚类的效果








'''
下面进行剔除那些图片中的文字.

继续操作tmp

'''


# 当一个门派里面的字符太少的时候就删除这个门派!



menpaistr=''
savetmp=[]
for i in tmp:
  menpaistr = ''
  for j in i:
    menpaistr+=data[j]['DetectedText']

  print(menpaistr)
  print(3)

  if len(menpaistr)>50:
    savetmp.append(i)
print(savetmp)

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


