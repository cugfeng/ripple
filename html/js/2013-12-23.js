var rate_array = [
['Time', 'Buy', 'Sell'],
['00:00', 0.1334, 0.1310],
['00:11', 0.1334, 0.1335],
['00:13', 0.1334, 0.1335],
['00:19', 0.1334, 0.1310],
['00:22', 0.1334, 0.1303],
['00:34', 0.1334, 0.1298],
['00:35', 0.1300, 0.1298],
['01:08', 0.1300, 0.1294],
['01:30', 0.1300, 0.1300],
['01:31', 0.1300, 0.1294],
['01:40', 0.1310, 0.1294],
['07:02', 0.1310, 0.1310],
['07:03', 0.1310, 0.1310],
['07:44', 0.1310, 0.1310],
['07:58', 0.1320, 0.1310],
['07:59', 0.1330, 0.1310],
['08:00', 0.1330, 0.1310],
['08:01', 0.1330, 0.1310],
['08:02', 0.1330, 0.1310],
['08:09', 0.1346, 0.1310],
['08:13', 0.1346, 0.1330],
['08:32', 0.1346, 0.1340],
['08:52', 0.1346, 0.1332],
['08:57', 0.1346, 0.1332],
['09:14', 0.1350, 0.1332],
['09:33', 0.1340, 0.1332],
['09:35', 0.1340, 0.1330],
['10:24', 0.1330, 0.1330],
['10:27', 0.1320, 0.1330],
['10:28', 0.1320, 0.1330],
['10:30', 0.1318, 0.1330],
['10:31', 0.1318, 0.1330],
['10:42', 0.1330, 0.1321],
['10:43', 0.1337, 0.1321],
['10:44', 0.1340, 0.1321],
['10:45', 0.1340, 0.1321],
['10:47', 0.1340, 0.1321],
['10:48', 0.1340, 0.1321],
['10:56', 0.1340, 0.1321],
['10:57', 0.1340, 0.1322],
['11:02', 0.1340, 0.1340],
['11:03', 0.1340, 0.1340],
['11:09', 0.1329, 0.1321],
['11:11', 0.1329, 0.1321],
['11:12', 0.1329, 0.1320],
['11:39', 0.1329, 0.1310],
['11:52', 0.1325, 0.1310],
['12:11', 0.1325, 0.1310],
['12:12', 0.1310, 0.1310],
['12:14', 0.1320, 0.1310],
['12:16', 0.1323, 0.1310],
['12:24', 0.1323, 0.1310],
['12:30', 0.1320, 0.1310],
['12:35', 0.1326, 0.1310],
['12:38', 0.1326, 0.1310],
['13:02', 0.1327, 0.1310],
['13:50', 0.1313, 0.1310],
['13:55', 0.1313, 0.1313],
['14:08', 0.1313, 0.1320],
['14:16', 0.1313, 0.1322],
['14:19', 0.1313, 0.1321],
['14:22', 0.1320, 0.1321],
['14:24', 0.1320, 0.1321],
['14:29', 0.1320, 0.1320],
['14:32', 0.1335, 0.1320],
['14:38', 0.1335, 0.1299],
['14:39', 0.1335, 0.1300],
['14:40', 0.1335, 0.1296],
['14:41', 0.1335, 0.1296],
['14:45', 0.1335, 0.1296],
['14:49', 0.1335, 0.1296],
['14:54', 0.1296, 0.1296],
['15:17', 0.1296, 0.1296],
['15:20', 0.1309, 0.1290],
['15:36', 0.1309, 0.1301],
['15:37', 0.1309, 0.1300],
['15:51', 0.1290, 0.1300],
['15:53', 0.1290, 0.1300],
['15:55', 0.1290, 0.1290],
['15:56', 0.1290, 0.1290],
['16:00', 0.1290, 0.1284],
['16:01', 0.1290, 0.1284],
['16:03', 0.1290, 0.1285],
['16:06', 0.1290, 0.1285],
['16:10', 0.1290, 0.1283],
['16:11', 0.1290, 0.1283],
['16:12', 0.1290, 0.1282],
['16:16', 0.1290, 0.1282],
['16:18', 0.1283, 0.1282],
['16:20', 0.1283, 0.1280],
['16:24', 0.1300, 0.1309],
['16:34', 0.1300, 0.1309],
['16:35', 0.1309, 0.1280],
['16:36', 0.1300, 0.1280],
['16:37', 0.1300, 0.1280],
['16:46', 0.1300, 0.1282],
['16:47', 0.1300, 0.1282],
['16:55', 0.1300, 0.1282],
['16:56', 0.1300, 0.1282],
['17:04', 0.1300, 0.1285],
['17:05', 0.1300, 0.1285],
['17:44', 0.1300, 0.1285],
['17:46', 0.1300, 0.1285],
['18:01', 0.1300, 0.1282],
['18:10', 0.1282, 0.1282],
['18:13', 0.1282, 0.1282],
['18:19', 0.1282, 0.1282],
['18:21', 0.1282, 0.1282],
['18:25', 0.1282, 0.1280],
['18:27', 0.1282, 0.1280],
['18:36', 0.1282, 0.1280],
['18:37', 0.1282, 0.1280],
['18:42', 0.1282, 0.1280],
['18:45', 0.1282, 0.1281],
['18:50', 0.1282, 0.1281],
['18:51', 0.1282, 0.1281],
['19:01', 0.1280, 0.1280],
['19:02', 0.1280, 0.1280],
['19:03', 0.1280, 0.1280],
['19:07', 0.1280, 0.1280],
['19:08', 0.1280, 0.1280],
['19:10', 0.1280, 0.1280],
['19:11', 0.1280, 0.1282],
['19:12', 0.1282, 0.1282],
['19:13', 0.1282, 0.1282],
['19:28', 0.1282, 0.1280],
['19:35', 0.1282, 0.1270],
['19:36', 0.1270, 0.1270],
['19:37', 0.1270, 0.1270],
['19:48', 0.1270, 0.1270],
['20:04', 0.1270, 0.1278],
['20:09', 0.1270, 0.1278],
['20:12', 0.1270, 0.1280],
['20:15', 0.1287, 0.1280],
['20:17', 0.1287, 0.1290],
['20:21', 0.1287, 0.1280],
['20:22', 0.1287, 0.1290],
['20:26', 0.1280, 0.1290],
['20:27', 0.1280, 0.1290],
['20:28', 0.1280, 0.1290],
['20:32', 0.1280, 0.1290],
['20:37', 0.1280, 0.1290],
['20:38', 0.1280, 0.1274],
['20:39', 0.1280, 0.1274],
['20:41', 0.1274, 0.1274],
['20:42', 0.1274, 0.1274],
['20:46', 0.1274, 0.1274],
['20:49', 0.1274, 0.1274],
['20:50', 0.1274, 0.1274],
['20:52', 0.1274, 0.1273],
['20:53', 0.1274, 0.1270],
['20:54', 0.1274, 0.1270],
['20:55', 0.1274, 0.1270],
['20:56', 0.1274, 0.1270],
['20:57', 0.1274, 0.1270],
['20:58', 0.1267, 0.1261],
['20:59', 0.1263, 0.1261],
['21:00', 0.1262, 0.1261],
['21:01', 0.1262, 0.1261],
['21:03', 0.1261, 0.1260],
['21:04', 0.1259, 0.1260],
['21:05', 0.1259, 0.1260],
['21:06', 0.1259, 0.1260],
['21:07', 0.1260, 0.1260],
['21:13', 0.1267, 0.1260],
['21:15', 0.1287, 0.1287],
['21:16', 0.1285, 0.1287],
['21:18', 0.1287, 0.1285],
['21:19', 0.1287, 0.1285],
['21:28', 0.1287, 0.1270],
['21:35', 0.1285, 0.1270],
['21:59', 0.1262, 0.1270],
['22:00', 0.1262, 0.1270],
['22:03', 0.1262, 0.1260],
['22:04', 0.1262, 0.1260],
['22:05', 0.1262, 0.1261],
['22:07', 0.1262, 0.1261],
['22:10', 0.1267, 0.1261],
['22:16', 0.1270, 0.1261],
['22:19', 0.1270, 0.1268],
['22:23', 0.1270, 0.1268],
['22:25', 0.1280, 0.1268],
['22:31', 0.1287, 0.1268],
['22:47', 0.1287, 0.1268],
['22:49', 0.1287, 0.1268],
['22:50', 0.1287, 0.1268],
['22:52', 0.1287, 0.1268],
['23:09', 0.1286, 0.1268],
['23:10', 0.1286, 0.1268],
['23:17', 0.1286, 0.1272],
['23:22', 0.1286, 0.1272],
['23:23', 0.1286, 0.1272],
['23:25', 0.1286, 0.1272],
['23:27', 0.1286, 0.1272],
['23:29', 0.1286, 0.1272],
['23:30', 0.1286, 0.1272],
['23:31', 0.1286, 0.1272],
['23:32', 0.1286, 0.1272],
['23:34', 0.1286, 0.1272],
['23:35', 0.1286, 0.1272],
['23:36', 0.1286, 0.1272],
['23:37', 0.1286, 0.1286],
['23:48', 0.1286, 0.1298]
]
var volume_array = [
['Time', 'Buy', 'Sell'],
['00:00', 500.1, 359.4],
['01:00', 18.5, 1763.4],
['02:00', 0.0, 0.0],
['03:00', 0.0, 0.0],
['04:00', 0.0, 0.0],
['05:00', 0.0, 0.0],
['06:00', 0.0, 0.0],
['07:00', 1615.9, 260.6],
['08:00', 2931.5, 155.3],
['09:00', 37003.2, 6.7],
['10:00', 16354.9, 4277.3],
['11:00', 2651.2, 357.4],
['12:00', 2328.7, 196.4],
['13:00', 3142.2, 65.0],
['14:00', 11250.4, 8672.4],
['15:00', 161.1, 1017.8],
['16:00', 4417.6, 1156.1],
['17:00', 1077.9, 205.4],
['18:00', 2109.2, 1229.3],
['19:00', 2349.4, 1670.1],
['20:00', 7754.7, 8227.8],
['21:00', 13061.6, 1646.6],
['22:00', 378.4, 814.0],
['23:00', 35443.9, 120.0]
]