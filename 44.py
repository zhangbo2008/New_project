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
      "DetectedText": "the solder spheres (or interconnections ir",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 199,
          "Y": 451
        },
        {
          "X": 1179,
          "Y": 451
        },
        {
          "X": 1179,
          "Y": 494
        },
        {
          "X": 199,
          "Y": 494
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
    },
    {
      "DetectedText": "general), such large size Ag3Sn platelets lead",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 217,
          "Y": 508
        },
        {
          "X": 1199,
          "Y": 508
        },
        {
          "X": 1199,
          "Y": 551
        },
        {
          "X": 217,
          "Y": 551
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
    },
    {
      "DetectedText": "F",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 1503,
          "Y": 497
        },
        {
          "X": 1556,
          "Y": 497
        },
        {
          "X": 1556,
          "Y": 549
        },
        {
          "X": 1503,
          "Y": 549
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
    },
    {
      "DetectedText": "stress build up around them and results in",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 218,
          "Y": 562
        },
        {
          "X": 1237,
          "Y": 562
        },
        {
          "X": 1237,
          "Y": 606
        },
        {
          "X": 218,
          "Y": 606
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}"
    },
    {
      "DetectedText": "crack initiation in thermally or mechanically",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 216,
          "Y": 615
        },
        {
          "X": 1203,
          "Y": 615
        },
        {
          "X": 1203,
          "Y": 663
        },
        {
          "X": 216,
          "Y": 663
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":5}}"
    },
    {
      "DetectedText": "stressed solder joints.",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 217,
          "Y": 671
        },
        {
          "X": 683,
          "Y": 671
        },
        {
          "X": 683,
          "Y": 714
        },
        {
          "X": 217,
          "Y": 714
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":6}}"
    },
    {
      "DetectedText": "tz",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 1630,
          "Y": 838
        },
        {
          "X": 1676,
          "Y": 838
        },
        {
          "X": 1676,
          "Y": 896
        },
        {
          "X": 1630,
          "Y": 896
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":7}}"
    },
    {
      "DetectedText": "Wetting time, sec",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 1736,
          "Y": 1013
        },
        {
          "X": 1990,
          "Y": 1013
        },
        {
          "X": 1990,
          "Y": 1053
        },
        {
          "X": 1736,
          "Y": 1053
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":8}}"
    },
    {
      "DetectedText": "Figure 6: SEM and optical images of a",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 219,
          "Y": 1116
        },
        {
          "X": 1056,
          "Y": 1116
        },
        {
          "X": 1056,
          "Y": 1161
        },
        {
          "X": 219,
          "Y": 1161
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "severely deformed SAC405 solder sphere.",
      "Confidence": 88,
      "Polygon": [
        {
          "X": 216,
          "Y": 1169
        },
        {
          "X": 1127,
          "Y": 1169
        },
        {
          "X": 1127,
          "Y": 1217
        },
        {
          "X": 216,
          "Y": 1217
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "Figure 7: A typical wetting balance curve.",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1161
        },
        {
          "X": 2205,
          "Y": 1161
        },
        {
          "X": 2205,
          "Y": 1216
        },
        {
          "X": 1313,
          "Y": 1216
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":16}}"
    },
    {
      "DetectedText": "Effect of silver on wetting",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 219,
          "Y": 1278
        },
        {
          "X": 1002,
          "Y": 1278
        },
        {
          "X": 1002,
          "Y": 1339
        },
        {
          "X": 219,
          "Y": 1339
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":9}}"
    },
    {
      "DetectedText": "Solderability tests of lead free alloys of",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1460,
          "Y": 1273
        },
        {
          "X": 2301,
          "Y": 1273
        },
        {
          "X": 2301,
          "Y": 1322
        },
        {
          "X": 1460,
          "Y": 1322
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":17}}"
    },
    {
      "DetectedText": "interest had been carried out by the wetting",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1310,
          "Y": 1332
        },
        {
          "X": 2296,
          "Y": 1332
        },
        {
          "X": 2296,
          "Y": 1375
        },
        {
          "X": 1310,
          "Y": 1375
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "behavior of SnAgCu alloys",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 218,
          "Y": 1351
        },
        {
          "X": 1043,
          "Y": 1351
        },
        {
          "X": 1043,
          "Y": 1411
        },
        {
          "X": 218,
          "Y": 1411
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":10}}"
    },
    {
      "DetectedText": "balance method.",
      "Confidence": 91,
      "Polygon": [
        {
          "X": 1314,
          "Y": 1388
        },
        {
          "X": 1721,
          "Y": 1388
        },
        {
          "X": 1721,
          "Y": 1431
        },
        {
          "X": 1314,
          "Y": 1431
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "A Minisco ST50",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1847,
          "Y": 1389
        },
        {
          "X": 2298,
          "Y": 1389
        },
        {
          "X": 2298,
          "Y": 1432
        },
        {
          "X": 1847,
          "Y": 1432
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "solderability tester was used for wetting",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1312,
          "Y": 1447
        },
        {
          "X": 2297,
          "Y": 1447
        },
        {
          "X": 2297,
          "Y": 1493
        },
        {
          "X": 1312,
          "Y": 1493
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "Intrinsic wetting ability of solder alloys",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 363,
          "Y": 1492
        },
        {
          "X": 1199,
          "Y": 1492
        },
        {
          "X": 1199,
          "Y": 1536
        },
        {
          "X": 363,
          "Y": 1536
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":11}}"
    },
    {
      "DetectedText": "balance testing. Copper test coupons that",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1503
        },
        {
          "X": 2298,
          "Y": 1503
        },
        {
          "X": 2298,
          "Y": 1545
        },
        {
          "X": 1313,
          "Y": 1545
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "is an important performance property, which",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 219,
          "Y": 1549
        },
        {
          "X": 1205,
          "Y": 1549
        },
        {
          "X": 1205,
          "Y": 1594
        },
        {
          "X": 219,
          "Y": 1594
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "were 25. 5mm X 12.78mm X 0.28mm were",
      "Confidence": 80,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1556
        },
        {
          "X": 2298,
          "Y": 1556
        },
        {
          "X": 2298,
          "Y": 1605
        },
        {
          "X": 1313,
          "Y": 1605
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "directly affects the integrity of solder",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 217,
          "Y": 1604
        },
        {
          "X": 1207,
          "Y": 1604
        },
        {
          "X": 1207,
          "Y": 1651
        },
        {
          "X": 217,
          "Y": 1651
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "cleaned in isopropyl alcohol and then dipped",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1310,
          "Y": 1612
        },
        {
          "X": 2294,
          "Y": 1612
        },
        {
          "X": 2294,
          "Y": 1656
        },
        {
          "X": 1310,
          "Y": 1656
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "interconnections. This intrinsic wetting abiity",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 218,
          "Y": 1663
        },
        {
          "X": 1201,
          "Y": 1663
        },
        {
          "X": 1201,
          "Y": 1705
        },
        {
          "X": 218,
          "Y": 1705
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "in 10% flouroboric acid solution, rinsed with",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1668
        },
        {
          "X": 2297,
          "Y": 1668
        },
        {
          "X": 2297,
          "Y": 1715
        },
        {
          "X": 1313,
          "Y": 1715
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "also",
      "Confidence": 98,
      "Polygon": [
        {
          "X": 233,
          "Y": 1721
        },
        {
          "X": 304,
          "Y": 1721
        },
        {
          "X": 304,
          "Y": 1762
        },
        {
          "X": 233,
          "Y": 1762
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "controls the production yield and",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 361,
          "Y": 1717
        },
        {
          "X": 1198,
          "Y": 1717
        },
        {
          "X": 1198,
          "Y": 1762
        },
        {
          "X": 361,
          "Y": 1762
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "tap water, flushed with DI water, and then",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 1312,
          "Y": 1725
        },
        {
          "X": 2299,
          "Y": 1725
        },
        {
          "X": 2299,
          "Y": 1771
        },
        {
          "X": 1312,
          "Y": 1771
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "throughput when using a dynamic soldering",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 217,
          "Y": 1771
        },
        {
          "X": 1199,
          "Y": 1771
        },
        {
          "X": 1199,
          "Y": 1817
        },
        {
          "X": 217,
          "Y": 1817
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "dried. The solder pot was heated to 2609C.",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 1309,
          "Y": 1781
        },
        {
          "X": 2297,
          "Y": 1781
        },
        {
          "X": 2297,
          "Y": 1826
        },
        {
          "X": 1309,
          "Y": 1826
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":18}}"
    },
    {
      "DetectedText": "process, such as wave or reflow soldering.",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 218,
          "Y": 1829
        },
        {
          "X": 1126,
          "Y": 1829
        },
        {
          "X": 1126,
          "Y": 1871
        },
        {
          "X": 218,
          "Y": 1871
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":12}}"
    },
    {
      "DetectedText": "copper",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1448,
          "Y": 1841
        },
        {
          "X": 1598,
          "Y": 1841
        },
        {
          "X": 1598,
          "Y": 1884
        },
        {
          "X": 1448,
          "Y": 1884
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "coupons",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1652,
          "Y": 1838
        },
        {
          "X": 1839,
          "Y": 1838
        },
        {
          "X": 1839,
          "Y": 1883
        },
        {
          "X": 1652,
          "Y": 1883
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "were",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1887,
          "Y": 1838
        },
        {
          "X": 1992,
          "Y": 1838
        },
        {
          "X": 1992,
          "Y": 1882
        },
        {
          "X": 1887,
          "Y": 1882
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "dipped for",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 2040,
          "Y": 1834
        },
        {
          "X": 2316,
          "Y": 1834
        },
        {
          "X": 2316,
          "Y": 1883
        },
        {
          "X": 2040,
          "Y": 1883
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":19}}"
    },
    {
      "DetectedText": "approximately 5 seconds to a depth of 10mm",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1309,
          "Y": 1890
        },
        {
          "X": 2297,
          "Y": 1890
        },
        {
          "X": 2297,
          "Y": 1938
        },
        {
          "X": 1309,
          "Y": 1938
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "The wetting balance test is a method",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 371,
          "Y": 1943
        },
        {
          "X": 1205,
          "Y": 1943
        },
        {
          "X": 1205,
          "Y": 1986
        },
        {
          "X": 371,
          "Y": 1986
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":13}}"
    },
    {
      "DetectedText": "in a flux. Excess flux was removed by",
      "Confidence": 80,
      "Polygon": [
        {
          "X": 1313,
          "Y": 1947
        },
        {
          "X": 2316,
          "Y": 1947
        },
        {
          "X": 2316,
          "Y": 1992
        },
        {
          "X": 1313,
          "Y": 1992
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "used by some industry segments to test",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 219,
          "Y": 2001
        },
        {
          "X": 1204,
          "Y": 2001
        },
        {
          "X": 1204,
          "Y": 2042
        },
        {
          "X": 219,
          "Y": 2042
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "touching the end of the coupon to clean filter",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2006
        },
        {
          "X": 2301,
          "Y": 2006
        },
        {
          "X": 2301,
          "Y": 2053
        },
        {
          "X": 1313,
          "Y": 2053
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "wettability of components.",
      "Confidence": 89,
      "Polygon": [
        {
          "X": 216,
          "Y": 2050
        },
        {
          "X": 857,
          "Y": 2050
        },
        {
          "X": 857,
          "Y": 2097
        },
        {
          "X": 216,
          "Y": 2097
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "This test",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 976,
          "Y": 2051
        },
        {
          "X": 1202,
          "Y": 2051
        },
        {
          "X": 1202,
          "Y": 2095
        },
        {
          "X": 976,
          "Y": 2095
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "paper.\" The coupon was then positioned in",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1314,
          "Y": 2065
        },
        {
          "X": 2300,
          "Y": 2065
        },
        {
          "X": 2300,
          "Y": 2106
        },
        {
          "X": 1314,
          "Y": 2106
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "measures the forces imposed by the molten",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 217,
          "Y": 2108
        },
        {
          "X": 1204,
          "Y": 2108
        },
        {
          "X": 1204,
          "Y": 2154
        },
        {
          "X": 217,
          "Y": 2154
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "the machine. The coupon was immersed in",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2117
        },
        {
          "X": 2302,
          "Y": 2117
        },
        {
          "X": 2302,
          "Y": 2163
        },
        {
          "X": 1313,
          "Y": 2163
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "solder upon the test specimen",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 216,
          "Y": 2166
        },
        {
          "X": 994,
          "Y": 2166
        },
        {
          "X": 994,
          "Y": 2209
        },
        {
          "X": 216,
          "Y": 2209
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":14}}"
    },
    {
      "DetectedText": "the solder to a depth of 5mm for 10 seconds",
      "Confidence": 79,
      "Polygon": [
        {
          "X": 1309,
          "Y": 2170
        },
        {
          "X": 2298,
          "Y": 2170
        },
        {
          "X": 2298,
          "Y": 2216
        },
        {
          "X": 1309,
          "Y": 2216
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "specimen is dipped into and held in the",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 217,
          "Y": 2224
        },
        {
          "X": 1203,
          "Y": 2224
        },
        {
          "X": 1203,
          "Y": 2265
        },
        {
          "X": 217,
          "Y": 2265
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "at a dip rate of approximately 21mm/s. The",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2227
        },
        {
          "X": 2297,
          "Y": 2227
        },
        {
          "X": 2297,
          "Y": 2271
        },
        {
          "X": 1312,
          "Y": 2271
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "solder bath. This wetting force is measured",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 218,
          "Y": 2276
        },
        {
          "X": 1203,
          "Y": 2276
        },
        {
          "X": 1203,
          "Y": 2324
        },
        {
          "X": 218,
          "Y": 2324
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "machine automatically corrects for buoyancy",
      "Confidence": 90,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2288
        },
        {
          "X": 2297,
          "Y": 2288
        },
        {
          "X": 2297,
          "Y": 2332
        },
        {
          "X": 1312,
          "Y": 2332
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "as a function of time and automatically",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 217,
          "Y": 2330
        },
        {
          "X": 1200,
          "Y": 2330
        },
        {
          "X": 1200,
          "Y": 2376
        },
        {
          "X": 217,
          "Y": 2376
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "and calculates wetting force at every 1/8th",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2342
        },
        {
          "X": 2298,
          "Y": 2342
        },
        {
          "X": 2298,
          "Y": 2383
        },
        {
          "X": 1313,
          "Y": 2383
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "recorded. A typical wetting balance curve is",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 220,
          "Y": 2389
        },
        {
          "X": 1205,
          "Y": 2389
        },
        {
          "X": 1205,
          "Y": 2433
        },
        {
          "X": 220,
          "Y": 2433
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "second.",
      "Confidence": 95,
      "Polygon": [
        {
          "X": 1314,
          "Y": 2401
        },
        {
          "X": 1475,
          "Y": 2401
        },
        {
          "X": 1475,
          "Y": 2442
        },
        {
          "X": 1314,
          "Y": 2442
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":20}}"
    },
    {
      "DetectedText": "shown in Figure 7",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 216,
          "Y": 2444
        },
        {
          "X": 662,
          "Y": 2444
        },
        {
          "X": 662,
          "Y": 2489
        },
        {
          "X": 216,
          "Y": 2489
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "The commonly used",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 719,
          "Y": 2447
        },
        {
          "X": 1206,
          "Y": 2447
        },
        {
          "X": 1206,
          "Y": 2491
        },
        {
          "X": 719,
          "Y": 2491
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "performance measure is the time to cross the",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 218,
          "Y": 2502
        },
        {
          "X": 1203,
          "Y": 2502
        },
        {
          "X": 1203,
          "Y": 2546
        },
        {
          "X": 218,
          "Y": 2546
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "In this study, wetting time (tz) and",
      "Confidence": 81,
      "Polygon": [
        {
          "X": 1468,
          "Y": 2507
        },
        {
          "X": 2297,
          "Y": 2507
        },
        {
          "X": 2297,
          "Y": 2552
        },
        {
          "X": 1468,
          "Y": 2552
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":21}}"
    },
    {
      "DetectedText": "zero axis of wetting force. Maximum wetting",
      "Confidence": 84,
      "Polygon": [
        {
          "X": 217,
          "Y": 2556
        },
        {
          "X": 1200,
          "Y": 2556
        },
        {
          "X": 1200,
          "Y": 2605
        },
        {
          "X": 217,
          "Y": 2605
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "maximum wetting",
      "Confidence": 93,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2569
        },
        {
          "X": 1729,
          "Y": 2569
        },
        {
          "X": 1729,
          "Y": 2610
        },
        {
          "X": 1312,
          "Y": 2610
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "force",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1801,
          "Y": 2567
        },
        {
          "X": 1907,
          "Y": 2567
        },
        {
          "X": 1907,
          "Y": 2608
        },
        {
          "X": 1801,
          "Y": 2608
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "(Fmax)， were",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1971,
          "Y": 2567
        },
        {
          "X": 2297,
          "Y": 2567
        },
        {
          "X": 2297,
          "Y": 2611
        },
        {
          "X": 1971,
          "Y": 2611
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "force Fmax is the measured force between",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 217,
          "Y": 2610
        },
        {
          "X": 1201,
          "Y": 2610
        },
        {
          "X": 1201,
          "Y": 2656
        },
        {
          "X": 217,
          "Y": 2656
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "measured for SAC305， Sn0.7Cu and",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1311,
          "Y": 2620
        },
        {
          "X": 2291,
          "Y": 2620
        },
        {
          "X": 2291,
          "Y": 2667
        },
        {
          "X": 1311,
          "Y": 2667
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "specimen surface and the molten solder.",
      "Confidence": 87,
      "Polygon": [
        {
          "X": 218,
          "Y": 2671
        },
        {
          "X": 1085,
          "Y": 2671
        },
        {
          "X": 1085,
          "Y": 2713
        },
        {
          "X": 218,
          "Y": 2713
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":15}}"
    },
    {
      "DetectedText": "SAC0307 alloys. Five No Clean fluxes were",
      "Confidence": 83,
      "Polygon": [
        {
          "X": 1313,
          "Y": 2674
        },
        {
          "X": 2298,
          "Y": 2674
        },
        {
          "X": 2298,
          "Y": 2723
        },
        {
          "X": 1313,
          "Y": 2723
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "used to study wetting characteristics of these",
      "Confidence": 86,
      "Polygon": [
        {
          "X": 1311,
          "Y": 2730
        },
        {
          "X": 2299,
          "Y": 2730
        },
        {
          "X": 2299,
          "Y": 2775
        },
        {
          "X": 1311,
          "Y": 2775
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "alloys.",
      "Confidence": 99,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2785
        },
        {
          "X": 1444,
          "Y": 2785
        },
        {
          "X": 1444,
          "Y": 2832
        },
        {
          "X": 1312,
          "Y": 2832
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":22}}"
    },
    {
      "DetectedText": "This is one of the major differences",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 1460,
          "Y": 2901
        },
        {
          "X": 2298,
          "Y": 2901
        },
        {
          "X": 2298,
          "Y": 2948
        },
        {
          "X": 1460,
          "Y": 2948
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":23}}"
    },
    {
      "DetectedText": "between Ag bearing and Ag free alloys. Ag",
      "Confidence": 82,
      "Polygon": [
        {
          "X": 1312,
          "Y": 2955
        },
        {
          "X": 2298,
          "Y": 2955
        },
        {
          "X": 2298,
          "Y": 3007
        },
        {
          "X": 1312,
          "Y": 3007
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":24}}"
    },
    {
      "DetectedText": "free alloys have higher surface tension at",
      "Confidence": 85,
      "Polygon": [
        {
          "X": 1310,
          "Y": 3014
        },
        {
          "X": 2300,
          "Y": 3014
        },
        {
          "X": 2300,
          "Y": 3056
        },
        {
          "X": 1310,
          "Y": 3056
        }
      ],
      "AdvancedInfo": "{\"Parag\":{\"ParagNo\":24}}"
    }
  ],
  "Language": "zh",
  "RequestId": "4b754d44-0cf8-4c2a-8645-0fb97375a80d"
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


im = cv2.imread('55.Jpeg')
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


