###############################################################################
#
# Tests for XlsxWriter.
#
# SPDX-License-Identifier: BSD-2-Clause
# Copyright (c), 2013-2024, John McNamara, jmcnamara@cpan.org
#

import unittest
from datetime import datetime
from ...worksheet import Worksheet


class TestConvertDateTime(unittest.TestCase):
    """
    Test the Worksheet _convert_date_time() method against dates extracted
    from Excel.

    """

    def setUp(self):
        self.worksheet = Worksheet()

    def test_convert_date_time(self):
        """Test the _convert_date_time() method."""

        # Dates and corresponding numbers from an Excel file.
        excel_dates = [
            ("1899-12-31T00:00:00.000", 0),
            ("1982-08-25T00:15:20.213", 30188.010650613425),
            ("2065-04-19T00:16:48.290", 60376.011670023145),
            ("2147-12-15T00:55:25.446", 90565.038488958337),
            ("2230-08-10T01:02:46.891", 120753.04359827546),
            ("2313-04-06T01:04:15.597", 150942.04462496529),
            ("2395-11-30T01:09:40.889", 181130.04838991899),
            ("2478-07-25T01:11:32.560", 211318.04968240741),
            ("2561-03-21T01:30:19.169", 241507.06272186342),
            ("2643-11-15T01:48:25.580", 271695.07529606484),
            ("2726-07-12T02:03:31.919", 301884.08578609955),
            ("2809-03-06T02:11:11.986", 332072.09111094906),
            ("2891-10-31T02:24:37.095", 362261.10042934027),
            ("2974-06-26T02:35:07.220", 392449.10772245371),
            ("3057-02-19T02:45:12.109", 422637.1147234838),
            ("3139-10-17T03:06:39.990", 452826.12962951389),
            ("3222-06-11T03:08:08.251", 483014.13065105322),
            ("3305-02-05T03:19:12.576", 513203.13834),
            ("3387-10-01T03:29:42.574", 543391.14563164348),
            ("3470-05-27T03:37:30.813", 573579.15105107636),
            ("3553-01-21T04:14:38.231", 603768.17683137732),
            ("3635-09-16T04:16:28.559", 633956.17810832174),
            ("3718-05-13T04:17:58.222", 664145.17914608796),
            ("3801-01-06T04:21:41.794", 694333.18173372687),
            ("3883-09-02T04:56:35.792", 724522.20596981479),
            ("3966-04-28T05:25:14.885", 754710.2258667245),
            ("4048-12-21T05:26:05.724", 784898.22645513888),
            ("4131-08-18T05:46:44.068", 815087.24078782403),
            ("4214-04-13T05:48:01.141", 845275.24167987274),
            ("4296-12-07T05:53:52.315", 875464.24574438657),
            ("4379-08-03T06:14:48.580", 905652.26028449077),
            ("4462-03-28T06:46:15.738", 935840.28212659725),
            ("4544-11-22T07:31:20.407", 966029.31343063654),
            ("4627-07-19T07:58:33.754", 996217.33233511576),
            ("4710-03-15T08:07:43.130", 1026406.3386936343),
            ("4792-11-07T08:29:11.091", 1056594.3536005903),
            ("4875-07-04T09:08:15.328", 1086783.3807329629),
            ("4958-02-27T09:30:41.781", 1116971.3963169097),
            ("5040-10-23T09:34:04.462", 1147159.3986627546),
            ("5123-06-20T09:37:23.945", 1177348.4009715857),
            ("5206-02-12T09:37:56.655", 1207536.4013501736),
            ("5288-10-08T09:45:12.230", 1237725.406391551),
            ("5371-06-04T09:54:14.782", 1267913.412671088),
            ("5454-01-28T09:54:22.108", 1298101.4127558796),
            ("5536-09-24T10:01:36.151", 1328290.4177795255),
            ("5619-05-20T12:09:48.602", 1358478.5068125231),
            ("5702-01-14T12:34:08.549", 1388667.5237100578),
            ("5784-09-08T12:56:06.495", 1418855.5389640625),
            ("5867-05-06T12:58:58.217", 1449044.5409515856),
            ("5949-12-30T12:59:54.263", 1479232.5416002662),
            ("6032-08-24T13:34:41.331", 1509420.5657561459),
            ("6115-04-21T13:58:28.601", 1539609.5822754744),
            ("6197-12-14T14:02:16.899", 1569797.5849178126),
            ("6280-08-10T14:36:17.444", 1599986.6085352316),
            ("6363-04-06T14:37:57.451", 1630174.60969272),
            ("6445-11-30T14:57:42.757", 1660363.6234115392),
            ("6528-07-26T15:10:48.307", 1690551.6325035533),
            ("6611-03-22T15:14:39.890", 1720739.635183912),
            ("6693-11-15T15:19:47.988", 1750928.6387498612),
            ("6776-07-11T16:04:24.344", 1781116.6697262037),
            ("6859-03-07T16:22:23.952", 1811305.6822216667),
            ("6941-10-31T16:29:55.999", 1841493.6874536921),
            ("7024-06-26T16:58:20.259", 1871681.7071789235),
            ("7107-02-21T17:04:02.415", 1901870.7111390624),
            ("7189-10-16T17:18:29.630", 1932058.7211762732),
            ("7272-06-11T17:47:21.323", 1962247.7412190163),
            ("7355-02-05T17:53:29.866", 1992435.7454845603),
            ("7437-10-02T17:53:41.076", 2022624.7456143056),
            ("7520-05-28T17:55:06.044", 2052812.7465977315),
            ("7603-01-21T18:14:49.151", 2083000.7602910995),
            ("7685-09-16T18:17:45.738", 2113189.7623349307),
            ("7768-05-12T18:29:59.700", 2143377.7708298611),
            ("7851-01-07T18:33:21.233", 2173566.773162419),
            ("7933-09-02T19:14:24.673", 2203754.8016744559),
            ("8016-04-27T19:17:12.816", 2233942.8036205554),
            ("8098-12-22T19:23:36.418", 2264131.8080603937),
            ("8181-08-17T19:46:25.908", 2294319.8239109721),
            ("8264-04-13T20:07:47.314", 2324508.8387420601),
            ("8346-12-08T20:31:37.603", 2354696.855296331),
            ("8429-08-03T20:39:57.770", 2384885.8610853008),
            ("8512-03-29T20:50:17.067", 2415073.8682530904),
            ("8594-11-22T21:02:57.827", 2445261.8770581828),
            ("8677-07-19T21:23:05.519", 2475450.8910360998),
            ("8760-03-14T21:34:49.572", 2505638.8991848612),
            ("8842-11-08T21:39:05.944", 2535827.9021521294),
            ("8925-07-04T21:39:18.426", 2566015.9022965971),
            ("9008-02-28T21:46:07.769", 2596203.9070343636),
            ("9090-10-24T21:57:55.662", 2626392.9152275696),
            ("9173-06-19T22:19:11.732", 2656580.9299968979),
            ("9256-02-13T22:23:51.376", 2686769.9332335186),
            ("9338-10-09T22:27:58.771", 2716957.9360968866),
            ("9421-06-05T22:43:30.392", 2747146.9468795368),
            ("9504-01-30T22:48:25.834", 2777334.9502990046),
            ("9586-09-24T22:53:51.727", 2807522.9540709145),
            ("9669-05-20T23:12:56.536", 2837711.9673210187),
            ("9752-01-14T23:15:54.109", 2867899.9693762613),
            ("9834-09-10T23:17:12.632", 2898088.9702850925),
            ("9999-12-31T23:59:59.000", 2958465.999988426),
        ]

        for excel_date in excel_dates:
            date = datetime.strptime(excel_date[0], "%Y-%m-%dT%H:%M:%S.%f")

            got = self.worksheet._convert_date_time(date)
            exp = excel_date[1]
            self.assertEqual(got, exp)
