"""
Identity on streams
BotIn : bytes stream
BotOut : bytes stream
UsrIn : text stream
UsrOut : text stream
SysIn : Nothing : Empty State (rely on python interpreter + OS)
SysOut : Nothing : Unchanged state (rely on python interpreter + OS)
This is a basic building block of Python Hexagonal Architecture
It can be seen as a filter on stream,
"""
import asyncio

import aioconsole


def usr_id(d):
    return d

def bot_id(d):
    return d


### HANDLING SYSTEM SIGNAL IS INTEGRATED IN LANGUAGE since we are doing python...
import signal, os

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# # Set the signal handler and a 5-second alarm
# signal.signal(signal.SIGALRM, handler)
# signal.alarm(5)
#
# # This open() may hang indefinitely
# fd = os.open('/dev/ttyS0', os.O_RDWR)
#
# signal.alarm(0)          # Disable the alarm


async def usrIO(stdin, stdout):
    line = await stdin.readline()
    message = line.decode()

    stdout.write(usr_id(message))
    yield line


async def usr():
    stdin, stdout = await aioconsole.get_standard_streams()
    while True:  # TODO : signal handling -> system interaction
        async for l in usrIO(stdin, stdout):
            # do something for each line
            pass


# async def botIO(reader, writer):
#     data = await reader.read(100)
#     message = data.decode()
#     addr = writer.get_extra_info('peername')
#
#     print(f"Received {message!r} from {addr!r}")
#
#     print(f"Send: {message!r}")
#     writer.write(bot_id(data))
#     await writer.drain()
#
#     print("Close the connection")
#     writer.close()
#
#
# async def bot():
#     server = await asyncio.start_server(
#         botIO, '127.0.0.1', 8888)
#
#     addr = server.sockets[0].getsockname()
#     print(f'Serving on {addr}')
#
#     async with server:
#         await server.serve_forever()

#asyncio.run(asyncio.gather(bot(), usr()))
asyncio.run(usr())