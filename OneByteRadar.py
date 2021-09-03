from pymem         import Pymem
from pymem.process import module_from_name

from re import search

pm = Pymem('csgo.exe')
client = module_from_name(pm.process_handle, 'client.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll,\
                             client.SizeOfImage)
address = search(rb'\x80\xB9.{5}\x74\x12\x8B\x41\x08',\
                 clientModule)
address = address.start()
address = client.lpBaseOfDll + address + 6

pm.write_uchar(address, 2)
pm.close_process()
