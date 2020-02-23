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
      "DetectedText": "standard operating temperatures and don't ",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 215,
          "Y": 451
        },
        {
          "X": 1206,
          "Y": 451
        },
        {
          "X": 1206,
          "Y": 497
        },
        {
          "X": 215,
          "Y": 497
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "SAC305 T=260C",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 1627,
          "Y": 483
        },
        {
          "X": 1861,
          "Y": 483
        },
        {
          "X": 1861,
          "Y": 516
        },
        {
          "X": 1627,
          "Y": 516
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "wet as well. An optimized balance of Ag and",
      "Confidence": 80,
      "Polygon": [
        {
          "X": 218,
          "Y": 508
        },
        {
          "X": 1203,
          "Y": 508
        },
        {
          "X": 1203,
          "Y": 552
        },
        {
          "X": 218,
          "Y": 552
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "other additives helps to lower the surface",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 219,
          "Y": 563
        },
        {
          "X": 1203,
          "Y": 563
        },
        {
          "X": 1203,
          "Y": 606
        },
        {
          "X": 219,
          "Y": 606
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "0.3",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 1359,
          "Y": 589
        },
        {
          "X": 1434,
          "Y": 589
        },
        {
          "X": 1434,
          "Y": 626
        },
        {
          "X": 1359,
          "Y": 626
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
    },
    {
      "DetectedText": "tension of solder alloys at standard Pb-free",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 217,
          "Y": 615
        },
        {
          "X": 1201,
          "Y": 615
        },
        {
          "X": 1201,
          "Y": 661
        },
        {
          "X": 217,
          "Y": 661
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "operating temperatures. This lower surface",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 219,
          "Y": 672
        },
        {
          "X": 1204,
          "Y": 672
        },
        {
          "X": 1204,
          "Y": 716
        },
        {
          "X": 219,
          "Y": 716
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "tension results in faster wetting contributing",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 216,
          "Y": 731
        },
        {
          "X": 1201,
          "Y": 731
        },
        {
          "X": 1201,
          "Y": 775
        },
        {
          "X": 216,
          "Y": 775
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "0.1",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1359,
          "Y": 720
        },
        {
          "X": 1431,
          "Y": 720
        },
        {
          "X": 1431,
          "Y": 751
        },
        {
          "X": 1359,
          "Y": 751
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "to better hole fill and SMD soldering at lower",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 219,
          "Y": 784
        },
        {
          "X": 1200,
          "Y": 784
        },
        {
          "X": 1200,
          "Y": 829
        },
        {
          "X": 219,
          "Y": 829
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "contact times.",
      "Confidence": 92,
      "Polygon": [
        {
          "X": 219,
          "Y": 842
        },
        {
          "X": 511,
          "Y": 842
        },
        {
          "X": 511,
          "Y": 886
        },
        {
          "X": 219,
          "Y": 886
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":5}}"
    },
    {
      "DetectedText": "-0.1",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 1388,
          "Y": 849
        },
        {
          "X": 1476,
          "Y": 849
        },
        {
          "X": 1476,
          "Y": 883
        },
        {
          "X": 1388,
          "Y": 883
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":6}}"
    },
    {
      "DetectedText": "12345678910",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1528,
          "Y": 834
        },
        {
          "X": 2153,
          "Y": 834
        },
        {
          "X": 2153,
          "Y": 870
        },
        {
          "X": 1528,
          "Y": 870
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":6}}"
    },
    {
      "DetectedText": "- IF2010F",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1883,
          "Y": 895
        },
        {
          "X": 2012,
          "Y": 895
        },
        {
          "X": 2012,
          "Y": 932
        },
        {
          "X": 1883,
          "Y": 932
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":26}}"
    },
    {
      "DetectedText": "|出_0.2",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1319,
          "Y": 914
        },
        {
          "X": 1438,
          "Y": 914
        },
        {
          "X": 1438,
          "Y": 946
        },
        {
          "X": 1319,
          "Y": 946
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "L2Z02",
      "Confidence": 63,
      "Polygon": [
        {
          "X": 1895,
          "Y": 955
        },
        {
          "X": 2004,
          "Y": 955
        },
        {
          "X": 2004,
          "Y": 991
        },
        {
          "X": 1895,
          "Y": 991
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":27}}"
    },
    {
      "DetectedText": ".5[",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 315,
          "Y": 973
        },
        {
          "X": 357,
          "Y": 973
        },
        {
          "X": 357,
          "Y": 1005
        },
        {
          "X": 315,
          "Y": 1005
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":7}}"
    },
    {
      "DetectedText": "Sn0.7Cu T=260C",
      "Confidence": 92,
      "Polygon": [
        {
          "X": 548,
          "Y": 976
        },
        {
          "X": 783,
          "Y": 976
        },
        {
          "X": 783,
          "Y": 1006
        },
        {
          "X": 548,
          "Y": 1006
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "” EF3215",
      "Confidence": 78,
      "Polygon": [
        {
          "X": 1895,
          "Y": 990
        },
        {
          "X": 2005,
          "Y": 990
        },
        {
          "X": 2005,
          "Y": 1023
        },
        {
          "X": 1895,
          "Y": 1023
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":27}}"
    },
    {
      "DetectedText": ").4|",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 313,
          "Y": 1031
        },
        {
          "X": 357,
          "Y": 1031
        },
        {
          "X": 357,
          "Y": 1067
        },
        {
          "X": 313,
          "Y": 1067
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":7}}"
    },
    {
      "DetectedText": "● EF4102",
      "Confidence": 78,
      "Polygon": [
        {
          "X": 1896,
          "Y": 1026
        },
        {
          "X": 2001,
          "Y": 1026
        },
        {
          "X": 2001,
          "Y": 1056
        },
        {
          "X": 1896,
          "Y": 1056
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":27}}"
    },
    {
      "DetectedText": "-0",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 1359,
          "Y": 1048
        },
        {
          "X": 1409,
          "Y": 1048
        },
        {
          "X": 1409,
          "Y": 1084
        },
        {
          "X": 1359,
          "Y": 1084
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "-0.5",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 1359,
          "Y": 1102
        },
        {
          "X": 1437,
          "Y": 1102
        },
        {
          "X": 1437,
          "Y": 1139
        },
        {
          "X": 1359,
          "Y": 1139
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "0.2-",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 309,
          "Y": 1154
        },
        {
          "X": 357,
          "Y": 1154
        },
        {
          "X": 357,
          "Y": 1196
        },
        {
          "X": 309,
          "Y": 1196
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "Wetting Time, sec",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1676,
          "Y": 1155
        },
        {
          "X": 1925,
          "Y": 1155
        },
        {
          "X": 1925,
          "Y": 1192
        },
        {
          "X": 1676,
          "Y": 1192
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":28}}"
    },
    {
      "DetectedText": "0.1",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 287,
          "Y": 1224
        },
        {
          "X": 357,
          "Y": 1224
        },
        {
          "X": 357,
          "Y": 1263
        },
        {
          "X": 287,
          "Y": 1263
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "0.5",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1359,
          "Y": 1241
        },
        {
          "X": 1432,
          "Y": 1241
        },
        {
          "X": 1432,
          "Y": 1278
        },
        {
          "X": 1359,
          "Y": 1278
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":24}}"
    },
    {
      "DetectedText": "SAC405 T=260C",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 1678,
          "Y": 1254
        },
        {
          "X": 1912,
          "Y": 1254
        },
        {
          "X": 1912,
          "Y": 1289
        },
        {
          "X": 1678,
          "Y": 1289
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":28}}"
    },
    {
      "DetectedText": "0.",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 1359,
          "Y": 1303
        },
        {
          "X": 1414,
          "Y": 1303
        },
        {
          "X": 1414,
          "Y": 1337
        },
        {
          "X": 1359,
          "Y": 1337
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":24}}"
    },
    {
      "DetectedText": "p_0.1",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 269,
          "Y": 1351
        },
        {
          "X": 357,
          "Y": 1351
        },
        {
          "X": 357,
          "Y": 1383
        },
        {
          "X": 269,
          "Y": 1383
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "?3..45678910",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 510,
          "Y": 1335
        },
        {
          "X": 1063,
          "Y": 1335
        },
        {
          "X": 1063,
          "Y": 1374
        },
        {
          "X": 510,
          "Y": 1374
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":16}}"
    },
    {
      "DetectedText": "- IF2010F",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 808,
          "Y": 1391
        },
        {
          "X": 925,
          "Y": 1391
        },
        {
          "X": 925,
          "Y": 1429
        },
        {
          "X": 808,
          "Y": 1429
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "EF2202",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 814,
          "Y": 1435
        },
        {
          "X": 917,
          "Y": 1435
        },
        {
          "X": 917,
          "Y": 1479
        },
        {
          "X": 814,
          "Y": 1479
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": ").3 t",
      "Confidence": 74,
      "Polygon": [
        {
          "X": 309,
          "Y": 1483
        },
        {
          "X": 357,
          "Y": 1483
        },
        {
          "X": 357,
          "Y": 1518
        },
        {
          "X": 309,
          "Y": 1518
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":11}}"
    },
    {
      "DetectedText": "; EF3215",
      "Confidence": 79,
      "Polygon": [
        {
          "X": 815,
          "Y": 1474
        },
        {
          "X": 916,
          "Y": 1474
        },
        {
          "X": 916,
          "Y": 1514
        },
        {
          "X": 815,
          "Y": 1514
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "EF4102",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 811,
          "Y": 1513
        },
        {
          "X": 916,
          "Y": 1513
        },
        {
          "X": 916,
          "Y": 1552
        },
        {
          "X": 811,
          "Y": 1552
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "0.4",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 307,
          "Y": 1551
        },
        {
          "X": 357,
          "Y": 1551
        },
        {
          "X": 357,
          "Y": 1583
        },
        {
          "X": 307,
          "Y": 1583
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":11}}"
    },
    {
      "DetectedText": "●RF80",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 810,
          "Y": 1561
        },
        {
          "X": 883,
          "Y": 1561
        },
        {
          "X": 883,
          "Y": 1591
        },
        {
          "X": 810,
          "Y": 1591
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": ").5",
      "Confidence": 96,
      "Polygon": [
        {
          "X": 309,
          "Y": 1618
        },
        {
          "X": 357,
          "Y": 1618
        },
        {
          "X": 357,
          "Y": 1653
        },
        {
          "X": 309,
          "Y": 1653
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":13}}"
    },
    {
      "DetectedText": "Wetting Time, sec",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 578,
          "Y": 1652
        },
        {
          "X": 824,
          "Y": 1652
        },
        {
          "X": 824,
          "Y": 1684
        },
        {
          "X": 578,
          "Y": 1684
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "”IF2010F",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 1893,
          "Y": 1682
        },
        {
          "X": 2006,
          "Y": 1682
        },
        {
          "X": 2006,
          "Y": 1714
        },
        {
          "X": 1893,
          "Y": 1714
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":29}}"
    },
    {
      "DetectedText": "EF2202",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1898,
          "Y": 1716
        },
        {
          "X": 2005,
          "Y": 1716
        },
        {
          "X": 2005,
          "Y": 1750
        },
        {
          "X": 1898,
          "Y": 1750
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":29}}"
    },
    {
      "DetectedText": "Sn0.7Cu0.3Ag T=260C",
      "Confidence": 93,
      "Polygon": [
        {
          "X": 488,
          "Y": 1745
        },
        {
          "X": 808,
          "Y": 1745
        },
        {
          "X": 808,
          "Y": 1779
        },
        {
          "X": 488,
          "Y": 1779
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "-0.3",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1359,
          "Y": 1744
        },
        {
          "X": 1428,
          "Y": 1744
        },
        {
          "X": 1428,
          "Y": 1778
        },
        {
          "X": 1359,
          "Y": 1778
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":25}}"
    },
    {
      "DetectedText": "EF3215",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1897,
          "Y": 1747
        },
        {
          "X": 2001,
          "Y": 1747
        },
        {
          "X": 2001,
          "Y": 1782
        },
        {
          "X": 1897,
          "Y": 1782
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":29}}"
    },
    {
      "DetectedText": "0.4",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 239,
          "Y": 1793
        },
        {
          "X": 306,
          "Y": 1793
        },
        {
          "X": 306,
          "Y": 1828
        },
        {
          "X": 239,
          "Y": 1828
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":10}}"
    },
    {
      "DetectedText": "EF4102",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 1895,
          "Y": 1784
        },
        {
          "X": 2001,
          "Y": 1784
        },
        {
          "X": 2001,
          "Y": 1814
        },
        {
          "X": 1895,
          "Y": 1814
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":29}}"
    },
    {
      "DetectedText": "-0.5",
      "Confidence": 96,
      "Polygon": [
        {
          "X": 1359,
          "Y": 1868
        },
        {
          "X": 1437,
          "Y": 1868
        },
        {
          "X": 1437,
          "Y": 1904
        },
        {
          "X": 1359,
          "Y": 1904
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":35}}"
    },
    {
      "DetectedText": "目0.2",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 256,
          "Y": 1923
        },
        {
          "X": 310,
          "Y": 1923
        },
        {
          "X": 310,
          "Y": 1959
        },
        {
          "X": 256,
          "Y": 1959
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "Wetting Time, sec",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1677,
          "Y": 1922
        },
        {
          "X": 1925,
          "Y": 1922
        },
        {
          "X": 1925,
          "Y": 1954
        },
        {
          "X": 1677,
          "Y": 1954
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":36}}"
    },
    {
      "DetectedText": "E0.1",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 257,
          "Y": 1989
        },
        {
          "X": 308,
          "Y": 1989
        },
        {
          "X": 308,
          "Y": 2031
        },
        {
          "X": 257,
          "Y": 2031
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "Figure 9: Wetting comparison of SAC305",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1312,
          "Y": 1980
        },
        {
          "X": 2226,
          "Y": 1980
        },
        {
          "X": 2226,
          "Y": 2032
        },
        {
          "X": 1312,
          "Y": 2032
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":37}}"
    },
    {
      "DetectedText": "and SAC405",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 1310,
          "Y": 2035
        },
        {
          "X": 1586,
          "Y": 2035
        },
        {
          "X": 1586,
          "Y": 2086
        },
        {
          "X": 1310,
          "Y": 2086
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":37}}"
    },
    {
      "DetectedText": "-0.1 9",
      "Confidence": 71,
      "Polygon": [
        {
          "X": 275,
          "Y": 2113
        },
        {
          "X": 357,
          "Y": 2113
        },
        {
          "X": 357,
          "Y": 2157
        },
        {
          "X": 275,
          "Y": 2157
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "IF2010F",
      "Confidence": 97,
      "Polygon": [
        {
          "X": 848,
          "Y": 2175
        },
        {
          "X": 966,
          "Y": 2175
        },
        {
          "X": 966,
          "Y": 2212
        },
        {
          "X": 848,
          "Y": 2212
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":32}}"
    },
    {
      "DetectedText": "EF2202",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 853,
          "Y": 2215
        },
        {
          "X": 960,
          "Y": 2215
        },
        {
          "X": 960,
          "Y": 2256
        },
        {
          "X": 853,
          "Y": 2256
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":32}}"
    },
    {
      "DetectedText": "~0",
      "Confidence": 73,
      "Polygon": [
        {
          "X": 239,
          "Y": 2250
        },
        {
          "X": 287,
          "Y": 2250
        },
        {
          "X": 287,
          "Y": 2289
        },
        {
          "X": 239,
          "Y": 2289
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":30}}"
    },
    {
      "DetectedText": "EF3215",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 852,
          "Y": 2259
        },
        {
          "X": 957,
          "Y": 2259
        },
        {
          "X": 957,
          "Y": 2294
        },
        {
          "X": 852,
          "Y": 2294
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":32}}"
    },
    {
      "DetectedText": "-0.4",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 239,
          "Y": 2313
        },
        {
          "X": 311,
          "Y": 2313
        },
        {
          "X": 311,
          "Y": 2354
        },
        {
          "X": 239,
          "Y": 2354
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":31}}"
    },
    {
      "DetectedText": "EF4102",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 855,
          "Y": 2307
        },
        {
          "X": 957,
          "Y": 2307
        },
        {
          "X": 957,
          "Y": 2338
        },
        {
          "X": 855,
          "Y": 2338
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":32}}"
    },
    {
      "DetectedText": ", RF800",
      "Confidence": 79,
      "Polygon": [
        {
          "X": 851,
          "Y": 2350
        },
        {
          "X": 938,
          "Y": 2350
        },
        {
          "X": 938,
          "Y": 2379
        },
        {
          "X": 851,
          "Y": 2379
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":32}}"
    },
    {
      "DetectedText": "-0.5",
      "Confidence": 90,
      "Polygon": [
        {
          "X": 239,
          "Y": 2384
        },
        {
          "X": 316,
          "Y": 2384
        },
        {
          "X": 316,
          "Y": 2415
        },
        {
          "X": 239,
          "Y": 2415
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":31}}"
    },
    {
      "DetectedText": "W etting Time, sec",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 570,
          "Y": 2420
        },
        {
          "X": 813,
          "Y": 2420
        },
        {
          "X": 813,
          "Y": 2450
        },
        {
          "X": 570,
          "Y": 2450
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":33}}"
    },
    {
      "DetectedText": "Figure 8: Wetting comparison of Sn0.7Cu",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 217,
          "Y": 2477
        },
        {
          "X": 1137,
          "Y": 2477
        },
        {
          "X": 1137,
          "Y": 2528
        },
        {
          "X": 217,
          "Y": 2528
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":34}}"
    },
    {
      "DetectedText": "and Sn0.3Ag0.7Cu",
      "Confidence": 92,
      "Polygon": [
        {
          "X": 221,
          "Y": 2537
        },
        {
          "X": 632,
          "Y": 2537
        },
        {
          "X": 632,
          "Y": 2581
        },
        {
          "X": 221,
          "Y": 2581
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":34}}"
    }
  ],
  "Language": "zh",
  "RequestId": "010d72e7-a432-4b13-9afb-14259b23ba55"
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


im = cv2.imread('88.Jpeg')
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


