"""
LJM library error codes.

"""

# Success
NOERROR = 0

# Warnings:
WARNINGS_BEGIN = 200
WARNINGS_END = 399
FRAMES_OMITTED_DUE_TO_PACKET_SIZE = 201

LOG_FAILURE = 202

# Modbus Errors:
MODBUS_ERRORS_BEGIN = 1200
MODBUS_ERRORS_END = 1216
MBE1_ILLEGAL_FUNCTION = 1201
MBE2_ILLEGAL_DATA_ADDRESS = 1202
MBE3_ILLEGAL_DATA_VALUE = 1203
MBE4_SLAVE_DEVICE_FAILURE = 1204
MBE5_ACKNOWLEDGE = 1205
MBE6_SLAVE_DEVICE_BUSY = 1206
MBE8_MEMORY_PARITY_ERROR = 1208
MBE10_GATEWAY_PATH_UNAVAILABLE = 1210
MBE11_GATEWAY_TARGET_NO_RESPONSE = 1211

# Library Errors:
LIBRARY_ERRORS_BEGIN = 1220
LIBRARY_ERRORS_END = 1399

UNKNOWN_ERROR = 1221
INVALID_DEVICE_TYPE = 1222
INVALID_HANDLE = 1223
DEVICE_NOT_OPEN = 1224
STREAM_NOT_INITIALIZED = 1225
DEVICE_NOT_FOUND = 1227
DEVICE_ALREADY_OPEN = 1229
COULD_NOT_CLAIM_DEVICE = 1230
CANNOT_CONNECT = 1231
SOCKET_LEVEL_ERROR = 1233
CANNOT_OPEN_DEVICE = 1236
CANNOT_DISCONNECT = 1237
WINSOCK_FAILURE = 1238
DEVICE_RECONNECT_FAILED = 1239

INVALID_ADDRESS = 1250
INVALID_CONNECTION_TYPE = 1251
INVALID_DIRECTION = 1252
INVALID_FUNCTION = 1253

INVALID_NUM_REGISTERS = 1254
INVALID_PARAMETER = 1255
INVALID_PROTOCOL_ID = 1256
INVALID_TRANSACTION_ID = 1257
INVALID_VALUE_TYPE = 1259
MEMORY_ALLOCATION_FAILURE = 1260

NO_COMMAND_BYTES_SENT = 1261

INCORRECT_NUM_COMMAND_BYTES_SENT = 1262

NO_RESPONSE_BYTES_RECEIVED = 1263

INCORRECT_NUM_RESPONSE_BYTES_RECEIVED = 1264

MIXED_FORMAT_IP_ADDRESS = 1265

UNKNOWN_IDENTIFIER = 1266
NOT_IMPLEMENTED = 1267
INVALID_INDEX = 1268

INVALID_LENGTH = 1269
ERROR_BIT_SET = 1270

INVALID_MAXBYTESPERMBFB = 1271

NULL_POINTER = 1272

NULL_OBJ = 1273

RESERVED_NAME = 1274

UNPARSABLE_DEVICE_TYPE = 1275

UNPARSABLE_CONNECTION_TYPE = 1276

UNPARSABLE_IDENTIFIER = 1277

PACKET_SIZE_TOO_LARGE = 1278

TRANSACTION_ID_ERR = 1279
PROTOCOL_ID_ERR = 1280
LENGTH_ERR = 1281
UNIT_ID_ERR = 1282
FUNCTION_ERR = 1283
STARTING_REG_ERR = 1284
NUM_REGS_ERR = 1285
NUM_BYTES_ERR = 1286
INVALID_NUM_VALUES = 1291
MODBUS_CONSTANTS_FILE_NOT_FOUND = 1292
INVALID_MODBUS_CONSTANTS_FILE = 1293
INVALID_NAME = 1294
OVERSPECIFIED_PORT = 1296
INTENT_NOT_READY = 1297
ATTR_LOAD_COMM_FAILURE = 1298
INVALID_CONFIG_NAME = 1299

ERROR_RETRIEVAL_FAILURE = 1300
LJM_BUFFER_FULL = 1301
COULD_NOT_START_STREAM = 1302
STREAM_NOT_RUNNING = 1303
UNABLE_TO_STOP_STREAM = 1304