'''
SCTE35 DTMF Descriptor Example

Usage:
    pypy3 Dtmf_Descriptor.py

'''


from threefive import decode

dtmf =b'/DAsAAAAAAAAAP/wDwUAAABef0/+zPACTQAAAAAADAEKQ1VFSbGfMTIxIxGolm3/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'

decode(dtmf)
